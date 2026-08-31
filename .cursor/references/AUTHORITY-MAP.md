# AUTHORITY-MAP — Mapa de Autoridad del Repositorio

> Operativo para agentes. Decisiones: [`standard/cdr/CDR-001.md`](../../standard/cdr/CDR-001.md), [`CDR-002.md`](../../standard/cdr/CDR-002.md), [`CDR-003.md`](../../standard/cdr/CDR-003.md).

## Principio

```text
CONSTITUTION (Libros en constitution/)  = autoridad normativa
STANDARD.md                             = autoridad procesal/organizativa subordinada
AGENTS.md / .cursor/                    = materialización operativa (nunca normativa)
```

Ningún archivo fuera de `constitution/**` puede crear, alterar o reinterpretar norma constitucional.

## Autoridad estructural vs efectiva (CDR-001)

| Concepto | Significado |
|----------|-------------|
| **Estructural** | `constitution/` es el único **árbol normativo canónico**. |
| **Efectiva/publicada** | La fuerza vinculante de un Libro depende de su **estado de migración y publicación**. |

La existencia de `constitution/Lx/BOOK.md` **no** implica por sí sola que el Libro sea norma publicada.

## Superficies

| Artefacto | Rol | Autoridad |
|-----------|-----|-----------|
| `constitution/` | Árbol normativo canónico | Estructural |
| `constitution/L0/BOOK.md` | Norma L0 (artículos) | Migración **`human-reviewed`** (manifest); Draft `0.1.0`; **no** Official; **no** Published. Norma efectiva revisada (CDR-001). No es publicación de ecosistema. |
| `constitution/L1/BOOK.md` | Reglas de Arquitectura; cuerpo MD materializado | Migración **`human-reviewed`**; Draft `0.1.0`; **no** Official; **no** Published. |
| `constitution/L2/BOOK.md` | Reglas de Protocolo; cuerpo MD materializado B0–B14 | Migración **`human-reviewed`**; Draft `0.1.0`; **no** Official; **no** Published. |
| `constitution/L3/BOOK.md` | Canon de Dominio; cuerpo MD materializado B0–B12 (DOCX 0–`FIN`) | Migración **`official`** (L3-PROM1; cierre del Libro); revisión humana aceptada; Draft `0.1.0`; **no** Official de ecosistema; **no** Published; **no** L3-COMPLETE. Norma efectiva del Libro (CDR-001). Migración ≠ publicación. |
| `constitution/L3/original/L3-001-Canon-de-Dominio.docx` | Fuente histórica inmutable de L3 | Ancla de fidelidad; DOCX intacto. No se sustituye por BOOK como publicación. |
| `constitution/L4`–`L8`, `L3-DA` `BOOK.md` | Entrada canónica futura | Stubs — **no** norma publicada en MD; cuerpo en `original/*.docx`; campo `source.migration` ausente (`historical-only`) |
| `constitution/*/original/*.docx` | Fuente histórica inmutable | De facto cuando BOOK es stub; ancla de fidelidad si BOOK está pendiente de review |
| `CONSTITUTION.md` | **Carta Constitucional** (declarativa) | Orientadora; **no** sustituye artículos de L0 |
| `STANDARD.md` | Gobernanza / procesos / CDR / versionado / publicación | Procesal subordinada — **no** normativa superior |
| `meta-specification/**` | Explica el estándar | Metaespecificación |
| `constitution/*/README.md`, `manifest.json` | Contexto / metadatos | Auxiliar |
| `AGENTS.md`, `.cursor/**` | Custodia del editor/agent | Operativa |
| `standard/cdr/*.md` | Decisiones de gobernanza Accepted | Procesal (no son artículos) |

## Precedencia entre Libros

```
L0 > L1 > L2 > L3 > L3-DA > L4 > L5 > L6 > L7 > L8
```

## Precedencia entre tipos de superficie

1. Norma de Libro efectiva/publicada  
2. BOOK con autoridad de trabajo (`pending-human-review`) — sujeta a fidelidad  
3. DOCX histórico  
4. Carta (`CONSTITUTION.md`)  
5. `STANDARD.md`  
6. Metaespecificación  
7. Operativo (`AGENTS.md`, `.cursor`, manifests)

Conflicto STANDARD vs Constitución → gana la **Constitución** (Libros).

## Identidad canónica L7 / L8 (CDR-002)

| Libro | Título canónico |
|-------|-----------------|
| **L7** | Reglas de **Materialización Institucional** |
| **L8** | Reglas de los **Agentes Institucionales** |

| Concepto | Relación |
|----------|----------|
| Aplicación / UX | Subdominio / forma de **Materialización** — **no** título de L7 |
| Agentes de IA | Especialización de **Agentes Institucionales** — **no** título de L8 |

### Divergencia pendiente (no auto-corregir)

En `constitution/L0/BOOK.md` (jerarquía final) aún aparecen títulos Versión B:

- `L7 — REGLAS DE APLICACIÓN Y EXPERIENCIA DE USUARIO`
- `L8 — REGLAS PARA AGENTES DE INTELIGENCIA ARTIFICIAL`

**Estado:** `DIVERGENCIA PENDIENTE DE RECONCILIACIÓN HUMANA`  
Tratar como candidato a **MIGRATION FIDELITY CONFLICT** (CDR-001). **No editar L0 automáticamente.**

## Versionado (CDR-003) — operativo

- Distinguir **VERSIÓN** (semver por plano) de **ESTADO** (migración / publicación / decisión).  
- `bookVersion` actual de Libros: **0.1.0** + Draft.  
- `standardVersion` actual: **0.1.0** + Draft.  
- El `1.0.0` en Carta/Readme/Architecture **no** es publicación constitucional oficial.  
- **No inventar** `VERSION.md`, `CHANGELOG.md`, release o tag si no existen.  
- **Git local (L3-RELEASE2):** existe `.git`; **sin** remote; **sin** commits; **sin** push; **sin** GitHub. No afirmar `authority: git` como autoridad normativa ni como publicación. La licencia pendiente bloquea el push público (RELEASE4).

## Conducta del Agent

1. Clasificar la superficie antes de aplicar norma.  
2. Respetar estados de migración.  
3. Ante divergencia BOOK pendiente ↔ DOCX → protocolo en `MIGRATION-STATES.md`.  
4. Ante títulos L7/L8 Versión B en L0 → reportar divergencia; no “arreglar”.  
5. Ante duda constitucional → **HUMAN REVIEW REQUIRED**.  
6. Promoción `human-reviewed` → `official`: **no** ejecutar sin mandato PROM explícito. HR1 **no** basta. L3: ejecutado por **L3-PROM1** (`source.migration = official`; Draft; **no** Official de ecosistema; **no** Published). Otros Libros: procedimiento y gates en `MIGRATION-STATES.md`. Migración de Libro **≠** Official/Published de ecosistema (CDR-003).
