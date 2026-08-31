# MIGRATION-STATES — Estados Oficiales de Migración de Libros

> Operativo. Decisiones: [`standard/cdr/CDR-001.md`](../../standard/cdr/CDR-001.md), [`CDR-003.md`](../../standard/cdr/CDR-003.md).

## Cadena obligatoria

```
Google Docs / DOCX
    ↓
original/*.docx          (histórico inmutable)
    ↓
Cursor (asistencia)
    ↓
BOOK.md                  (borrador / autoridad de trabajo)
    ↓
Revisión humana
    ↓
Commit Git (preservación; no crea norma por sí solo)
    ↓
published / official (según política de publicación — CDR-003)
```

## Estados de migración

| Estado | Significado | `BOOK.md` | `manifest.source.migration` | Autoridad efectiva (CDR-001) |
|--------|-------------|-----------|------------------------------|------------------------------|
| `historical-only` | Solo existe DOCX | Stub | ausente o `historical-only` | BOOK **no** es norma efectiva; DOCX = representación completa |
| `draft-migrated` | MD borrador asistido | Contenido migrado | `pending-human-review` | **Autoridad de trabajo**; no publicación cerrada |
| `human-reviewed` | Humano aprobó fidelidad | Contenido aprobado | `human-reviewed` | Norma efectiva revisada; candidata a publicación |
| `official` / publicada | Cerrada como fuente normativa del Libro | Fuente oficial del Libro | `official` | Norma efectiva/publicada del Libro |

**Versión ≠ estado:** el número `bookVersion` (p. ej. `0.1.0`) no implica publicación (CDR-003).

## Autoridad estructural vs efectiva

- **Estructural:** el Libro vive bajo `constitution/Lx/`.  
- **Efectiva:** depende del estado de esta tabla.  
- Existir `BOOK.md` **no** = norma publicada.

## Protocolo: MIGRATION FIDELITY CONFLICT (CDR-001)

Si un `BOOK.md` en estado `pending-human-review` (o borrador migrado equivalente) **difiere** de su `original/*.docx`:

1. **NO** corregir silenciosamente.  
2. **NO** elegir automáticamente una fuente.  
3. Identificar **ambas** fuentes (rutas exactas).  
4. Describir la divergencia (qué diverge).  
5. Marcar explícitamente:

```text
MIGRATION FIDELITY CONFLICT
```

6. Requerir **revisión humana**.  
7. **NO** declarar el BOOK `official` mientras el conflicto esté abierto.

### Caso conocido (no auto-editar)

En `constitution/L0/BOOK.md`, la jerarquía final etiqueta L7/L8 con títulos distintos a la identidad canónica (CDR-002) y a los DOCX L7/L8.

```text
DIVERGENCIA PENDIENTE DE RECONCILIACIÓN HUMANA
```

Tratar como conflicto de fidelidad / naming pendiente. **No modificar L0 en lotes operativos.**

## Prohibiciones

- Conversión automática DOCX → Markdown como acto definitivo  
- Marcar `official` sin revisión humana  
- Borrar `original/` tras migrar  
- Editar DOCX “para sincronizar” con Markdown  
- Resolver MIGRATION FIDELITY CONFLICT sin humano  

## Git

Git **está presente localmente**: `.git` inicializado por **L3-RELEASE2**.  
No hay remote. No hay commits. No hay push. No hay operaciones GitHub.  
Git **preserva**, no crea autoridad (CDR-003).  
No afirmar `authority: git` como autoridad normativa.  
Primer commit: **pendiente** (este mandato es control pre-commit; no ejecuta el commit).  
Licencia pendiente (H3-C): bloquea el push público (RELEASE4) hasta resolución humana.

## Estado actual observado

Valores de `manifest.source.migration` (o ausencia del campo) frente al filesystem. No equivalen a Official/Published de ecosistema.

| Libro | Estado de migración |
|-------|---------------------|
| L0 | `human-reviewed` (manifest; Draft `0.1.0`; **no** Official; **no** Published) |
| L1 | `human-reviewed` (BOOK materializado; Draft `0.1.0`; **no** Official; **no** Published) |
| L2 | `human-reviewed` (BOOK materializado B0–B14; Draft `0.1.0`; **no** Official; **no** Published) |
| L3 | `official` (L3-PROM1; B0–B12; HR1 ACCEPTED; GOV7 GLOBAL A; `source.migration = official`; Draft `0.1.0`; Git **no** requerido para esta migración (C2); CDR **no** requerido; **no** Official de ecosistema; **no** Published; **no** L3-COMPLETE) |
| L3-DA, L4–L8 | `historical-only` (BOOK stub; cuerpo en `original/*.docx`; campo `source.migration` **ausente**) |

## Procedimiento de promoción de migración (no ejecución)

> Formalizado en **L3-GOV6**. Este apartado **no** ejecuta promoción, **no** crea un quinto estado, **no** sustituye CDR-001/CDR-003 y **no** autoriza `Official` / `Published` / `1.0.0`.

Aplica a un Libro cuyo `source.migration` vigente sea `human-reviewed`. **L3** fue promovido a `official` por **L3-PROM1** (registro abajo). Un Agent **no** transita otros Libros sin mandato PROM **explícito**.

### Separación de planos (DEFINED)

```text
MIGRATION_OFFICIAL ≠ ECOSYSTEM_OFFICIAL
```

Respaldado por CDR-003 §6.B (`migration-official` = nombre interno del cierre del Libro; no confundir con release del ecosistema) y CDR-003 §6.C / §11 (publicación / `publicationStatus`).

`source.migration = official` **no** equivale por sí solo a:

- `Official = YES` (ecosistema / `publicationStatus = OFFICIAL`)
- `Published = YES`
- `constitutionalVersion` publicada
- `L3-COMPLETE`

`source.official = BOOK.md` sigue siendo **ruta** canónica prevista, no estado Official.

### Promotion target (DECISION_REQUIRED)

Tras `human-reviewed` la taxonomía existente solo admite estas dos lecturas del **mismo** cierre de Libro (no hay tercera):

| Lectura | Dónde | ¿Valor de `manifest.source.migration`? |
|---------|--------|----------------------------------------|
| `official` | Esta tabla, columna de campo; CDR-001 §6.1 | **Sí** (valor tabulado) |
| `migration-official` | CDR-003 §6.B | **No** — etiqueta interna. **INTERNAL_LABEL_ONLY**. No escribirlo en `manifest.json` salvo unificación futura de taxonomía (exigiría mandato/CDR; **no** se hace aquí). |

```text
PROMOTION_TARGET     = DECISION_REQUIRED
STATE_STRING_POLICY  = DECISION_REQUIRED
```

Ningún manifest del repositorio usa hoy `migration-official`. Precedentes de campo: `human-reviewed` (L0, L1, L2); `official` (L3, L3-PROM1).

### Git (DECISION_REQUIRED)

No se resuelve C1 vs C2 en este apartado.

- **C1:** la «Cadena obligatoria» de este archivo coloca Commit Git **antes** de `published / official`.
- **C2:** § Git de este archivo y CDR-003 §12: esa cadena es **política futura**; Git **preserva**, no crea autoridad; primer commit = Draft honesto, no Constitución `1.0.0` Official.

```text
GIT_POLICY      = DECISION_REQUIRED
GIT_EXCEPTION   = UNDEFINED_IN_REPOSITORY
```

Sin `.git` no hay excepción documentada `NO_GIT → official`. **No** inicializar Git desde un lote de migración.

**Hecho posterior (L3-RELEASE2):** `.git` existe por mandato de *preservación* (no es lote PROM). No altera C2 ni el PROM1 ya ejecutado. No es publicación.

### Autoridad (DEFINED)

```text
HUMAN_REVIEW_AUTHORITY  →  PROMOTION_AUTHORITY  →  PUBLICATION_AUTHORITY
```

- `HR1 ≠ PROMOTION_AUTHORITY` (CDR-006/007: review ≠ Official/Published).
- `PROMOTION_AUTHORITY ≠ PUBLICATION_AUTHORITY` (CDR-003: migración de Libro ≠ release de ecosistema).
- Quién ordena PROM: **custodio humano**, mediante mandato de promoción explícito. Hoy: `PROMOTION_AUTHORITY = NOT_YET_GRANTED`.

No aceptan como autorización de promoción: «ok», «continúa», «hazlo», «adelante».

### Versionado (UNDEFINED_IN_REPOSITORY para el bump)

Versión ≠ estado (CDR-003). Este procedimiento **no** cambia `0.1.0` ni implica `1.0.0`.

```text
VERSION_POLICY = UNDEFINED_IN_REPOSITORY
```

respecto de si un PROM futuro debe alterar `manifest.version`. D2 (L3): histórico `0.1` / operativo `0.1.0` se **preserva**.

### L3-COMPLETE (UNDEFINED_IN_REPOSITORY)

No es estado de esta tabla. No hay relación formal `migration state → L3-COMPLETE`.

```text
L3_COMPLETE_POLICY = UNDEFINED_IN_REPOSITORY
```

### CDR (UNDEFINED_IN_REPOSITORY)

```text
CDR_REQUIRED_FOR_PROCEDURE = NO   (este apartado documenta procedimiento operativo)
CDR_REQUIRED_FOR_EXECUTION = UNDEFINED_IN_REPOSITORY
```

Este archivo **no** crea ni modifica CDR.

### Gates (obligatorios antes de cualquier PROM)

Una promoción **no** puede ejecutarse si algún gate está `UNRESOLVED` / `DECISION_REQUIRED` / `UNDEFINED_IN_REPOSITORY` sin resolución expresa en el mandato PROM.

| Gate | Contenido | Estado actual (L3-GOV6) |
|------|-----------|-------------------------|
| 1 SOURCE INTEGRITY | BOOK/DOCX/hashes | PASS (no se reabre aquí) |
| 2 HUMAN REVIEW | HR1/HR2 `human-reviewed` | PASS |
| 3 CUSTODIAN AUTHORITY | mandato PROM explícito | **UNRESOLVED** |
| 4 TARGET DEFINITION | `official` vs etiqueta interna | **DECISION_REQUIRED** |
| 5 VERSION POLICY | ¿cambia `0.1.0`? | **UNDEFINED_IN_REPOSITORY** |
| 6 GIT POLICY | C1 vs C2 | **DECISION_REQUIRED** |
| 7 MIGRATION/PUBLICATION | planos separados | DEFINED; PROM no publica |
| 8 CDR REQUIREMENT | ¿CDR para ejecutar? | **UNDEFINED_IN_REPOSITORY** |
| 9 TRACEABILITY | registro mínimo (abajo) | DEFINED como requisito; registro **no** creado |
| 10 EXPLICIT PROMOTION MANDATE | mandato PROM con campos mínimos | **UNRESOLVED** |

### Trazabilidad mínima (futuro registro; no crear ahora)

El mandato PROM deberá dejar reconstruible: estado previo; custodio; mandato; target; SHA PRE; archivos modificados; SHA POST; estado posterior; fecha/hora; Git si corresponde; publicación si corresponde (`NOT_APPLICABLE` si el PROM es solo migración).

### Campos mínimos de un mandato PROM futuro

`PROMOTION_TARGET` · `STATE_FROM` · `STATE_TO` · `CUSTODIAN_AUTHORIZATION` · `GIT_REQUIREMENT` · `VERSION_POLICY` · `PUBLICATION_SCOPE` · `CDR_REQUIREMENT` · `TRACEABILITY_REQUIREMENTS` · `PROTECTED_FILES`

`STATE_FROM` esperado mientras no haya PROM: `human-reviewed`.  
`PUBLICATION_SCOPE` de un PROM de **solo migración**: `none` (no Official, no Published, no release/tag).

### Superficies protegidas en un PROM de migración (salvo mandato que las abra)

`BOOK.md` · `original/*.docx` · D2–D6 / E1 wrapper B0 · CDR existentes · Git (salvo mandato de implementación Git) · `version` / `status` Draft salvo política explícita.

### Matriz (sin inferir)

| Estado actual | Acción | Estado siguiente | Autoridad | Git | Publicación |
|---------------|--------|------------------|-----------|-----|-------------|
| `human-reviewed` | conservación | `human-reviewed` | — | — | no |
| `human-reviewed` | migration promotion | **DECISION_REQUIRED** | custodio + mandato PROM | **DECISION_REQUIRED** | no |
| migration target | publicación | **DECISION_REQUIRED** | `PUBLICATION_AUTHORITY` | **DECISION_REQUIRED** | **DECISION_REQUIRED** |
| Published/Official | release | **DECISION_REQUIRED** | `PUBLICATION_AUTHORITY` | **DECISION_REQUIRED** | sí |

## Registro L3-PROM1

Ejecución de promoción de **migración** (no publicación). Mandato: `L3-PROM1`.

```text
MANDATE_ID                 = L3-PROM1
STATE_FROM                 = human-reviewed
STATE_TO                   = official
PROMOTION_TARGET           = official
CUSTODIAN_AUTHORIZATION    = GOV7 GLOBAL A / D4 = 4A
VERSION                    = 0.1.0
GIT_STATE                  = NO_GIT
PUBLICATION_STATE          = NOT_EXECUTED
DATE/TIME                  = 2026-08-30T18:52:29-04:00
FILES_MODIFIED             = constitution/L3/manifest.json
                             constitution/L3/README.md
                             .cursor/references/AUTHORITY-MAP.md
                             .cursor/references/MIGRATION-STATES.md
```

SHA_PRE:

```text
BOOK             = 6060a16e632da1179a2e81826efdd2bf1cb96e8d9b396ad8775f30677b595d58
DOCX             = 571b65dee9ff7237bbf61f747a84c69c1e1122ed8a3cb1012df9281a7c503dc1
manifest         = 15604d6dd90ede04f881e22d65ad0da87a3653ab71be5b4b845fe58756d64f04
README           = bc97abf658ab94061ca1cb48f570ccf63ceb87e7559b072f10432ea7da899af5
AUTHORITY-MAP    = 6c4977ed065df0dd14e4789a8679a467b523607ec1ef9d28ac3da5afaea03f23
MIGRATION-STATES = 9df6d6f6ef0eefea9d7f03ef32c0a012c2844e6e4eb3834679bd408354f0b70e
```

SHA_POST (BOOK/DOCX idénticos; auxiliares tras L3-PROM1; este archivo = hash posterior a este registro, en el informe PROM1):

```text
BOOK          = 6060a16e632da1179a2e81826efdd2bf1cb96e8d9b396ad8775f30677b595d58
DOCX          = 571b65dee9ff7237bbf61f747a84c69c1e1122ed8a3cb1012df9281a7c503dc1
manifest      = 59d09e7186775ab885a82ca40e9f42e99c3d7c4fa3001cdec40539fb7e4ff5f9
README        = d232c924a6de52687bbdba544451d22cc94d08b1bb9c59e2850719eb15553d1f
AUTHORITY-MAP = 7d8f7dd2e12a9865490b9a0abfc8c0ed17a599eb2f6a2572bd864358f52b7578
```

Política GOV7 aplicada: D1=1A; D2=2A (`migration-official` = INTERNAL_LABEL_ONLY); D3=3B; D4=4A; D5=5A; D6=6A; D7=7A; D8=8A; D9=CONFIRM.

## Registro L3-RELEASE2

Inicialización Git de **preservación** y alineación documental H1. No es publicación. No es push. No crea LICENSE. No modifica BOOK/DOCX/L3/CDR.

```text
MANDATE_ID                 = L3-RELEASE2
H1                         = B (alinear superficies antes de git init)
H2                         = A (.gitignore mínimo antes del primer commit)
H3                         = C (licencia pendiente; bloquea RELEASE4)
H4                         = A (sin .gitkeep / placeholders)
GLOBAL                     = ACEPTADA
GIT_INIT                   = YES
GIT_REMOTE                 = NONE
COMMIT_EXECUTED            = NO
PUSH_EXECUTED              = NO
GITHUB_OPERATIONS          = 0
DEFAULT_BRANCH             = master (default de git init; no se cambió config)
LICENSE                    = PENDING
DATE/TIME                  = 2026-08-30T20:06:41-04:00
FILES_MODIFIED             = Readme.md
                             CONSTITUTION.md
                             meta-specification/Repository Architecture.md
                             .cursor/references/AUTHORITY-MAP.md
                             .cursor/references/MIGRATION-STATES.md
                             .gitignore (creado)
FILES_NOT_MODIFIED         = constitution/L3/BOOK.md
                             constitution/L3/original/*.docx
                             constitution/L3/manifest.json
                             constitution/L3/README.md
                             constitution/L0–L8 BOOK.md y DOCX (salvo L3 ya listado)
                             standard/cdr/*
```

SHA (protegidos L3 idénticos a CLOSE1/PROM1; auxiliares tras alineación H1 + Git local):

```text
BOOK             = 6060a16e632da1179a2e81826efdd2bf1cb96e8d9b396ad8775f30677b595d58
DOCX             = 571b65dee9ff7237bbf61f747a84c69c1e1122ed8a3cb1012df9281a7c503dc1
manifest         = 59d09e7186775ab885a82ca40e9f42e99c3d7c4fa3001cdec40539fb7e4ff5f9
README_L3        = d232c924a6de52687bbdba544451d22cc94d08b1bb9c59e2850719eb15553d1f
AUTHORITY-MAP    = c6c881a3b3d6105584598d2b4b0e5004b335b18f92e71606b81c8003e0288fb2
Readme.md        = f17d3d7ed021be76f0064234d727b9edd070802273f751d80db20e7235f8c20e
CONSTITUTION.md  = e0ec25322c3758e2f22943b9bf3d4b9c8ed20f89ad8cb0aef70178deb2f8b553
Architecture     = a891ef0b52b95f2d9caa6f8b5884f50d506185124c632b1ca1d7913d969c2787
.gitignore       = f98ff7923e05d6ea238b5257c21f3f22196ea9cc475a95674157bb838de1e269
```

MIGRATION-STATES SHA = hash de este archivo **después** de este registro (informe RELEASE2).
