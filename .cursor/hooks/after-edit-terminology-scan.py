#!/usr/bin/env python3
"""Escaneo ligero de terminología sospechosa / anti-canon."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SUSPECT = [
    (re.compile(r"\bframework\b", re.I), "evitar describir WTN como framework"),
    (re.compile(r"\bsaas\b", re.I), "evitar productizar como SaaS"),
    (re.compile(r"\bTrustScore\b"), "término no canónico detectado"),
    (re.compile(r"\bL9\b"), "Libro L9 no existe"),
    (re.compile(r"fuente maestra.*postgres|postgres.*fuente maestra", re.I), "posible conflicto Web2.5 / L0"),
]


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        print("{}")
        return

    path = str(data.get("file") or data.get("path") or data.get("filePath") or "")
    if not (path.endswith(".md") or path.endswith(".json")):
        print("{}")
        return
    # No escanear el propio EDITORIAL/FORBIDDEN como falsos positivos fuertes en references
    norm = path.replace("\\", "/")
    if "/.cursor/references/" in norm or "/.cursor/rules/" in norm:
        print("{}")
        return

    p = Path(path)
    if not p.is_file():
        p = ROOT / path
    if not p.is_file():
        print("{}")
        return

    text = p.read_text(encoding="utf-8", errors="replace")
    hits = []
    for rx, msg in SUSPECT:
        if rx.search(text):
            hits.append(msg)

    if hits:
        print(
            json.dumps(
                {
                    "agent_message": "Alerta terminológica/editorial: " + "; ".join(hits),
                },
                ensure_ascii=False,
            )
        )
        return

    print("{}")


if __name__ == "__main__":
    main()
