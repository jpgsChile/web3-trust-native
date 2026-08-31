---
name: book-migration
description: Playbook para migrar un Libro DOCX→BOOK.md con revisión humana. Usar cuando el usuario pida migrar L0–L8 o L3-DA.
---

# Skill — Migración de Libro

## Pasos

1. Confirmar Libro y estado actual (`README` + `manifest` + `BOOK`).
2. Leer DOCX histórico solo como fuente; no modificarlo.
3. Migrar a `BOOK.md` con fidelidad; marcar huecos explícitamente.
4. Actualizar README + manifest (`pending-human-review`).
5. Listar divergencias y riesgos.
6. Esperar revisión humana antes de `official` o commit.

## Checklist de calidad

- [ ]  Artículos no inventados
- [ ]  Cadenas/diagramas en fences
- [ ]  Estilo según EDITORIAL-CANON
- [ ]  dependsOn coherente
- [ ]  original/ intacto
