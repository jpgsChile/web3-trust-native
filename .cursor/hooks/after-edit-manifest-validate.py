#!/usr/bin/env python3
"""Valida manifests tras edición."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = {"book", "title", "version", "status", "levels", "articles", "dependsOn", "source"}
SOURCE_REQUIRED = {"official", "historical"}


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        print("{}")
        return

    path = str(data.get("file") or data.get("path") or data.get("filePath") or "")
    if not path.endswith("manifest.json") or "constitution/" not in path.replace("\\", "/"):
        print("{}")
        return

    p = Path(path)
    if not p.is_file():
        # relative to repo
        root = Path(__file__).resolve().parents[2]
        p = root / path
    if not p.is_file():
        print(
            json.dumps(
                {
                    "agent_message": f"manifest editado pero no encontrado en disco: {path}",
                },
                ensure_ascii=False,
            )
        )
        return

    try:
        manifest = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(
            json.dumps(
                {
                    "agent_message": f"manifest.json inválido ({p}): {e}",
                },
                ensure_ascii=False,
            )
        )
        return

    missing = sorted(REQUIRED - set(manifest))
    src = manifest.get("source") if isinstance(manifest.get("source"), dict) else {}
    missing_src = sorted(SOURCE_REQUIRED - set(src))
    msgs = []
    if missing:
        msgs.append("faltan campos: " + ", ".join(missing))
    if missing_src:
        msgs.append("source incompleto: " + ", ".join(missing_src))
    if not isinstance(manifest.get("dependsOn"), list):
        msgs.append("dependsOn debe ser lista")
    if msgs:
        print(
            json.dumps(
                {
                    "agent_message": "Validación manifest: " + "; ".join(msgs),
                },
                ensure_ascii=False,
            )
        )
        return

    print(
        json.dumps(
            {
                "agent_message": f"manifest OK: {manifest.get('book')} v{manifest.get('version')}",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
