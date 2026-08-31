# Auditoría de Referencias Rotas

## Protocolo

1. Aplicar `.cursor/references/CROSSREF-POLICY.md`.
2. Escanear `constitution/**/*.md`, `meta-specification/**/*.md`, raíz `*.md`.
3. Detectar:
   - paths `constitution/...` inexistentes
   - Libros `L9+` u otros IDs inválidos
   - artículos citados no presentes (cuando el Libro esté migrado)
4. Reportar lista accionable por archivo.

## Restricciones

- No inventar archivos destino para “arreglar” refs.
- Solo proponer correcciones trazables.
