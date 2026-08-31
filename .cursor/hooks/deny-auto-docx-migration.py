#!/usr/bin/env python3
"""Impide pipelines de conversión automática masiva DOCX→Markdown."""
from __future__ import annotations

import json
import re
import sys

PATTERNS = [
    r"pandoc\s+.*\.docx",
    r"docx2md",
    r"mammoth",
    r"python-docx.*BOOK\.md",
    r"for\s+\w+\s+in\s+.*\.docx",
    r"find\s+.*\.docx.*-exec",
    r"libreoffice\s+--headless.*docx",
]


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        print(json.dumps({"permission": "allow"}))
        return

    command = str(data.get("command") or data.get("cmd") or "")
    blob = command or json.dumps(data)
    for pat in PATTERNS:
        if re.search(pat, blob, flags=re.I):
            print(
                json.dumps(
                    {
                        "permission": "deny",
                        "user_message": "Conversión automática DOCX→Markdown bloqueada por política constitucional.",
                        "agent_message": "Migración prohibida como acto automático. Usa el comando migrate-book y deja pending-human-review.",
                    },
                    ensure_ascii=False,
                )
            )
            return

    print(json.dumps({"permission": "allow"}))


if __name__ == "__main__":
    main()
