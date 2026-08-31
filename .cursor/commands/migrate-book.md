# Migrar Libro

Asiste la migración de un Libro constitucional desde su fuente histórica hacia `BOOK.md`.

## Entrada requerida

- Identificador del Libro (`L0`…`L8` o `L3-DA`)

## Protocolo

1. Leer `.cursor/references/MIGRATION-STATES.md` y `.cursor/references/FORBIDDEN-ACTIONS.md`.
2. Confirmar que existe la carpeta `constitution/<LIBRO>/` con su subcarpeta histórica.
3. No modificar archivos históricos binarios del Libro.
4. Producir o actualizar `BOOK.md` como **borrador** fiel a la fuente.
5. Actualizar `README.md` y `manifest.json` con `source.migration: "pending-human-review"`.
6. No inventar artículos ausentes.
7. Entregar resumen de riesgos de fidelidad para revisión humana.
8. **No** marcar `official` ni hacer commit salvo mandato explícito.

## Salida

- Diff de `BOOK.md` / README / manifest
- Lista de advertencias
- Estado resultante: `draft-migrated`
