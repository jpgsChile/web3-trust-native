# FORBIDDEN-ACTIONS — Acciones Prohibidas al Agent

> Operativo. Decisiones: [`standard/cdr/CDR-001.md`](../../standard/cdr/CDR-001.md), [`CDR-002.md`](../../standard/cdr/CDR-002.md), [`CDR-003.md`](../../standard/cdr/CDR-003.md).

## Autoridad

1. Inventar artículos, libros, niveles o primitivos constitucionales.  
2. Contradecir L0 u otro Libro superior.  
3. Tratar el repositorio, README, `STANDARD.md` o `.cursor` como fuente **normativa** superior a los Libros.  
4. Usar `STANDARD.md` para redefinir conceptos, alterar artículos, cambiar la jerarquía L0–L8, invalidar norma o crear excepciones constitucionales.  
5. Reinterpretar la Constitución para “modernizarla” sin enmienda / CDR.  
6. Tratar todo `BOOK.md` bajo `constitution/` como norma **publicada** solo por existir.

## Estructura

7. Crear carpetas de capas futuras (`ontology/`, `knowledge/`, `schemas/`, `ai/`, `compiler/`, etc.) sin mandato explícito del custodio humano.  
8. Mezclar normativo y no normativo en la misma carpeta.  
9. Romper el patrón `BOOK.md` + `README.md` + `manifest.json` + `original/`.

## Migración y fidelidad

10. Convertir DOCX → Markdown de forma automática y darlo por oficial.  
11. Modificar, renombrar destructivamente o eliminar `original/*.docx`.  
12. Saltar estados de migración (`historical-only` → `official`).  
13. **Corregir silenciosamente** divergencias entre `BOOK.md` (`pending-human-review`) y `original/*.docx`.  
14. Elegir automáticamente una fuente en **MIGRATION FIDELITY CONFLICT**.  
15. Auto-reconciliar títulos L7/L8 en L0 sin revisión humana (`DIVERGENCIA PENDIENTE DE RECONCILIACIÓN HUMANA`).

## Léxico e identidad de Libros (CDR-002)

16. Introducir términos no definidos en el canon sin marcarlos como *propuesta*.  
17. Usar como **título canónico de Libro**:  
    - L7 = “Aplicación y Experiencia de Usuario”  
    - L8 = “Agentes de Inteligencia Artificial”  
18. Ignorar identidad canónica:  
    - L7 = **Materialización Institucional**  
    - L8 = **Agentes Institucionales**  
19. Generar ontología, KG o schemas que inventen significado.

## Versionado y publicación (CDR-003)

20. Afirmar `constitutionalVersion` / publicación **1.0.0 Official** sin release y mandato humano.  
21. Mezclar **versión** (semver) con **estado** (Draft, pending-human-review, Official).  
22. Inventar o afirmar existencia de `VERSION.md`, `CHANGELOG.md`, release o tag si no existen.  
23. Afirmar `authority: git` como preservación efectiva mientras **Git esté ausente**.  
24. Inicializar Git o crear tags sin mandato explícito de implementación.

## Operación

25. Ejecutar pipelines masivos de “completar la Constitución”.  
26. Afirmar conformidad Trust-Native sin trazabilidad a artículos.  
27. Resolver contradicciones constitucionales “en silencio”; marcar **HUMAN REVIEW REQUIRED**.
