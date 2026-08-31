#!/usr/bin/env python3
"""Bloquea escrituras destructivas solo si el PATH destino es historico binario."""
from __future__ import annotations

import json
import sys


def extract_paths(data: dict) -> list[str]:
    paths: list[str] = []
    for key in ("file_path", "filePath", "path", "file", "target", "uri"):
        val = data.get(key)
        if isinstance(val, str):
            paths.append(val)
    for key in ("args", "input", "tool_input", "arguments"):
        nested = data.get(key)
        if isinstance(nested, dict):
            paths.extend(extract_paths(nested))
    return paths


def is_protected_historical(path: str) -> bool:
    """True solo para paths bajo constitution/<libro>/original/*.docx."""
    norm = path.replace("\\", "/")
    if "/constitution/" not in norm:
        return False
    if "/original/" not in norm:
        return False
    return norm.lower().endswith(".docx")


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        print(json.dumps({"permission": "allow"}))
        return

    tool = str(data.get("tool_name") or data.get("tool") or data.get("toolName") or "")
    paths = extract_paths(data)
    command = str(data.get("command") or "")

    if tool in {"Read", "Grep", "Glob"}:
        print(json.dumps({"permission": "allow"}))
        return

    if any(is_protected_historical(p) for p in paths) and tool in {
        "Write",
        "Delete",
        "StrReplace",
        "EditNotebook",
    }:
        print(
            json.dumps(
                {
                    "permission": "deny",
                    "user_message": "Operacion bloqueada sobre fuente historica binaria de un Libro.",
                    "agent_message": (
                        "No modificar ni eliminar fuentes historicas binarias. "
                        "La migracion escribe BOOK.md, nunca reescribe el historico."
                    ),
                },
                ensure_ascii=False,
            )
        )
        return

    if command:
        norm_cmd = command.replace("\\", "/")
        targets = (
            "/constitution/" in norm_cmd
            and "/original/" in norm_cmd
            and ".docx" in norm_cmd.lower()
        )
        destructive = any(tok in command for tok in ("rm ", "mv ", "unlink", "truncate", "sed -i"))
        if targets and destructive:
            print(
                json.dumps(
                    {
                        "permission": "deny",
                        "user_message": "Comando shell bloqueado sobre fuente historica binaria.",
                        "agent_message": "Las fuentes historicas binarias son inmutables.",
                    },
                    ensure_ascii=False,
                )
            )
            return

    print(json.dumps({"permission": "allow"}))


if __name__ == "__main__":
    main()
