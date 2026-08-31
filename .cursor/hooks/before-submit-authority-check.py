#!/usr/bin/env python3
"""beforeSubmitPrompt — alerta si el prompt pide invención o contradicción."""
from __future__ import annotations

import json
import re
import sys

FLAGS = [
    (re.compile(r"invent[ae]|inventa(r|ción)?", re.I), "posible pedido de invención"),
    (re.compile(r"ignor[ae].*constituci|bypass.*l0|omite.*l0", re.I), "posible pedido de omitir Constitución"),
    (re.compile(r"convierte?\s+todos\s+los\s+docx|auto(mática|matica)?\s+migr", re.I), "posible migración automática masiva"),
    (re.compile(r"crea(r)?\s+ontology|genera(r)?\s+owl|knowledge\s+graph\s+completo", re.I), "posible creación prematura de capas"),
    (re.compile(r"reescribe\s+l0|reemplaza\s+la\s+constituci", re.I), "posible reescritura de L0"),
]


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        print("{}")
        return

    prompt = str(
        data.get("prompt")
        or data.get("user_prompt")
        or data.get("message")
        or data.get("content")
        or ""
    )
    if not prompt:
        prompt = json.dumps(data, ensure_ascii=False)

    hits = [msg for rx, msg in FLAGS if rx.search(prompt)]
    if hits:
        print(
            json.dumps(
                {
                    "agent_message": (
                        "Custodia constitucional: el prompt parece solicitar acciones de riesgo ("
                        + "; ".join(hits)
                        + "). Aplicar non-invention, authority y forbidden-actions. "
                        "No inventar conceptos ni marcar migraciones como oficiales."
                    ),
                },
                ensure_ascii=False,
            )
        )
        return

    print("{}")


if __name__ == "__main__":
    main()
