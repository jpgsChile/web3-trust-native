#!/usr/bin/env python3
"""sessionStart — contexto constitucional mínimo para la sesión."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONST = ROOT / "constitution"


def book_state(book_dir: Path) -> str:
    book = book_dir / "BOOK.md"
    manifest = book_dir / "manifest.json"
    if not book.exists():
        return "missing"
    text = book.read_text(encoding="utf-8", errors="replace")
    if "pendiente de migración oficial" in text.lower():
        return "historical-only"
    migration = None
    if manifest.exists():
        try:
            migration = json.loads(manifest.read_text(encoding="utf-8")).get("source", {}).get("migration")
        except json.JSONDecodeError:
            migration = "invalid-manifest"
    if migration:
        return migration
    if "ARTÍCULO" in text or "## Preámbulo" in text:
        return "draft-migrated"
    return "unknown"


def main() -> None:
    _ = sys.stdin.read()
    lines = []
    if CONST.is_dir():
        for d in sorted(CONST.iterdir()):
            if d.is_dir() and (d.name.startswith("L") or d.name == "L3-DA"):
                lines.append(f"- {d.name}: {book_state(d)}")
    summary = "Web3 Trust-Native — sesión de custodia constitucional.\nEstados de Libros:\n" + "\n".join(lines)
    summary += "\nAutoridad: ver .cursor/references/AUTHORITY-MAP.md. No inventar conceptos. No migrar DOCX→oficial sin revisión humana."
    print(json.dumps({"additional_context": summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
