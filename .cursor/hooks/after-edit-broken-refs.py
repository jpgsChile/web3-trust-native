#!/usr/bin/env python3
"""Detecta referencias rotas a Libros/paths en Markdown editado."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOK_RE = re.compile(r"\b(L3-DA|L[0-8])\b")
PATH_RE = re.compile(r"constitution/(L3-DA|L[0-8])(/[^\s)`\"]+)?")


def existing_books() -> set[str]:
    const = ROOT / "constitution"
    if not const.is_dir():
        return set()
    return {p.name for p in const.iterdir() if p.is_dir()}


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        print("{}")
        return

    path = str(data.get("file") or data.get("path") or data.get("filePath") or "")
    if not path.endswith(".md"):
        print("{}")
        return

    p = Path(path)
    if not p.is_file():
        p = ROOT / path
    if not p.is_file():
        print("{}")
        return

    text = p.read_text(encoding="utf-8", errors="replace")
    books = existing_books()
    broken = []

    for m in PATH_RE.finditer(text):
        book = m.group(1)
        if book not in books:
            broken.append(m.group(0))
        else:
            rel = m.group(0)
            # if path includes more than book, check file existence lightly
            full = ROOT / rel.split("#")[0]
            if full.suffix and not full.exists():
                broken.append(rel)

    # L9+ false friends
    for m in re.finditer(r"\bL([9]|[1-9][0-9])\b", text):
        broken.append(m.group(0))

    if broken:
        uniq = sorted(set(broken))[:20]
        print(
            json.dumps(
                {
                    "agent_message": "Posibles referencias rotas: " + ", ".join(uniq),
                },
                ensure_ascii=False,
            )
        )
        return

    print("{}")


if __name__ == "__main__":
    main()
