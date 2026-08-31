# CROSSREF-POLICY — Política de Referencias Cruzadas

> Operativo. Decisiones: [`standard/cdr/CDR-001.md`](../../standard/cdr/CDR-001.md), [`CDR-002.md`](../../standard/cdr/CDR-002.md), [`CDR-003.md`](../../standard/cdr/CDR-003.md).

## Formas canónicas

| Tipo | Forma |
|------|-------|
| Libro | `L0`, `L1`, … `L8`, `L3-DA` |
| Título L7 | **Materialización Institucional** (no “Aplicación y UX” como título de Libro) |
| Título L8 | **Agentes Institucionales** (no “Agentes de IA” como título de Libro) |
| Artículo romano (L0–L3 típico) | `L0 Art. VII` o `ARTÍCULO VII` dentro del Libro |
| Artículo numerado | `L7-001`, `L4-050`, `L3DA-001` |
| Archivo de Libro | `constitution/L7/BOOK.md` |
| Manifest | `constitution/L7/manifest.json` |
| Fuente histórica | `constitution/L7/original/L7-001-….docx` |
| CDR | `standard/cdr/CDR-001.md` (etc.) |

## Reglas

1. Toda afirmación normativa debe poder trazarse a Libro + artículo (o declarar que aún no está migrado / que el cuerpo está en DOCX).  
2. Las dependencias de un Libro viven en `manifest.json` → `dependsOn`.  
3. No citar paths inventados (`VERSION.md`, `releases/`, etc. si no existen).  
4. No citar artículos inexistentes en el `BOOK.md` vigente o en el DOCX histórico.  
5. Al mover un artículo a `articles/NNN.md`, actualizar referencias en el mismo cambio o dejar TODO explícito.  
6. Citar el **título canónico** del Libro (CDR-002). Si una fuente usa título Versión B para L7/L8, señalar:

```text
DIVERGENCIA PENDIENTE DE RECONCILIACIÓN HUMANA
```

7. Distinguir cita de **concepto** (“Aplicación”, “Agente de IA”) de cita de **identidad de Libro**.  
8. Distinguir **versión** (`0.1.0`) de **estado** (`Draft`, `pending-human-review`) (CDR-003).

## Detección de referencia rota o conflictiva

Se considera problemática si:

- apunta a un Libro/path inexistente;  
- apunta a un artículo no presente en el Libro citado (MD o DOCX según estado);  
- usa un título de Libro distinto del canónico (CDR-002 / `manifest.json`) **sin** nota de divergencia;  
- afirma publicación Official / `1.0.0` constitucional sin base (CDR-003);  
- asume Git/`authority: git` efectivo sin `.git`.

Ante conflicto de fidelidad BOOK↔DOCX → `MIGRATION-STATES.md` (MIGRATION FIDELITY CONFLICT).
