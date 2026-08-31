# L1-HR-CLOSE — Cierre de decisiones humanas para migración L1

| Campo | Valor |
|-------|--------|
| ID | L1-HR-CLOSE |
| Tipo | **Expediente de proceso** · **NO NORMATIVO** |
| Estado | **CLOSED** (decisiones humanas registradas) |
| Fecha | 2026-08-25 |
| Autoridad | Custodio humano del estándar Web3 Trust-Native |
| Contrato marco | [`standard/cdr/CDR-007.md`](../cdr/CDR-007.md) (**ACCEPTED**) |
| Origen | L1-A0 · L1-A1 (`HUMAN DECISION REQUIRED`) |

---

## Aviso de autoridad (obligatorio)

Este archivo es **gobernanza / proceso**.

- **No** es un CDR.
- **No** enmienda la Constitución.
- **No** modifica L0, L1 BOOK, manifests, DOCX ni CDR-001…007.
- **No** crea doctrina normativa nueva.
- **No** autoriza por sí solo la materialización B0–B9.
- Opera **dentro** del contrato de CDR-007 (puertas HR-L1-01…05).

Precedencia: Constitución (`constitution/`) > CDR Accepted > este expediente.

---

## 1. Decisiones cerradas

| ID | Decisión del custodio | Estado |
|----|----------------------|--------|
| **HR-L1-01** | Patrón **P2** (ver §2) | **CLOSED** |
| **HR-L1-02** | Front-matter histórico ≠ estado vigente del repo (ver §3) | **CLOSED** |
| **HR-L1-03** | Texto histórico + aclaración **fuera** del cuerpo normativo (ver §4) | **CLOSED** |
| **HR-L1-04** | Revisión humana por bloques B0–B9 (ver §5) | **CLOSED** (método) |
| **HR-L1-05** | `source.migration` en manifest L1 | **DIFERIDO** (sin cambio) |

---

## 2. HR-L1-01 — Patrón P2 (L4 / L7 / L8)

### Decisión registrada (custodio)

> Preservar **literalmente** las referencias históricas L4/L7/L8 contenidas en el DOCX de L1 y documentar su correspondencia con las identidades canónicas actuales mediante una **aclaración no normativa**, sin alterar el cuerpo constitucional histórico y sin reabrir L0/CDR-002.

### Reglas de aplicación futura (materialización)

1. En el futuro `constitution/L1/BOOK.md`, el texto histórico del DOCX relativo a L4/L7/L8 se **copia con fidelidad** (incluida la sección de relación con niveles y la agrupación del Art. II).
2. La correspondencia con identidades canónicas se documenta **solo** como aclaración **no normativa** (p. ej. esta tabla, anexo de expediente, o nota explícitamente marcada no normativa).
3. **Prohibido** sustituir en silencio los rótulos históricos por títulos canónicos dentro del cuerpo normativo.
4. **Prohibido** reabrir L0 o CDR-002.
5. Las referencias históricas **no** redefinen la identidad formal de los Libros.

### Tabla de correspondencia (no normativa)

| Texto histórico en DOCX L1 | Tratamiento | Identidad canónica vigente (no reabrir) |
|----------------------------|-------------|----------------------------------------|
| `L4 — SMART CONTRACTS` | Referencia histórica / conceptual del documento L1 | L4 según artefactos vigentes: **Unidad Normativa de Ejecución (UNE)** |
| `L7 — APLICACIÓN Y EXPERIENCIA DE USUARIO` | Referencia histórica / conceptual del documento L1 | **L7 — REGLAS DE MATERIALIZACIÓN INSTITUCIONAL** (CDR-002) |
| `L8 — AGENTES DE INTELIGENCIA ARTIFICIAL Y CURSOR` | Referencia histórica / conceptual del documento L1 | **L8 — REGLAS DE LOS AGENTES INSTITUCIONALES** (CDR-002) |
| `L4–L8 — IMPLEMENTACIÓN Y OPERACIÓN` (Art. II) | Agrupación histórica de precedencia en L1 | No sustituye títulos formales de L4…L8 |

**UX / Aplicación** = subdominio/forma de Materialización (CDR-002) — **no** título de L7.  
**Agentes de IA / Cursor** (en rótulos históricos de L1) = especialización/contexto — **no** título de L8.

---

## 3. HR-L1-02 — Front-matter

Regla de materialización futura (sin editar BOOK ni DOCX en este lote):

| Elemento | Tratamiento |
|----------|-------------|
| `Versión 0.1` / “Línea Base Arquitectónica” (DOCX) | Conservar como **contexto histórico** cuando corresponda en la migración |
| Estado vigente del repositorio | **`0.1.0` / `Draft`** (manifest L1) |
| Interpretar “Línea Base Arquitectónica” como Official / Published / 1.0.0 | **Prohibido** |
| Restaurar “Canon Constitucional Fundacional” como estado vigente | **Prohibido** |
| Convertir `0.1` histórico → `1.0.0` | **Prohibido** (CDR-003 / CDR-007) |

Este lote **no** modifica `constitution/L1/BOOK.md` ni `manifest.json`.

---

## 4. HR-L1-03 — UX / IA / Cursor

Política fijada por el custodio:

1. Si una referencia histórica de L1 puede confundirse con la identidad canónica de otro Libro: **conservar el texto histórico** y colocar la aclaración **fuera** del cuerpo normativo (metadata, expediente o nota explícitamente no normativa).
2. `"APLICACIÓN Y EXPERIENCIA DE USUARIO"` **no** redefine L7.
3. `"AGENTES DE INTELIGENCIA ARTIFICIAL Y CURSOR"` **no** redefine L8.
4. Artículos de L1 sobre agentes de IA (p. ej. LXXV–LXXVI) **permanecen en L1**.
5. **No** mover contenido a L8.
6. **No** modificar L0.

Alineado a HR-L1-01 (P2) y CDR-002 / CDR-007.

---

## 5. HR-L1-04 — Método de revisión humana

| Regla | Valor |
|-------|--------|
| Método | Revisión por bloques **B0–B9** |
| Auditoría | Cada bloque tiene su propia auditoría de fidelidad |
| `human-reviewed` en L1 | **No** declarar hasta completar la revisión humana correspondiente |
| Materialización | Controlada; **no** automática DOCX→Markdown |

---

## 6. Fuera de alcance de este expediente

- Iniciar B0–B9.
- Editar `constitution/L1/BOOK.md`.
- Editar `constitution/L1/manifest.json` (incl. `version`, `status`, `source.migration`).
- Modificar DOCX, L0, otros Libros, CDR-001…007, `.cursor/`.
- Crear CDR-008.
- Declarar Official / Published.
- Crear Git o capas futuras.

---

## 7. Efecto sobre planificación

Con HR-L1-01, HR-L1-02 y HR-L1-03 **CLOSED** bajo CDR-007:

- Queda cerrado el gate decisional identificado en L1-A1 para esas tres HR.
- La materialización B0 **sigue requiriendo mandato explícito** de lote posterior.
- Este archivo **no** equivale a `READY FOR MATERIALIZATION` ni autoriza B0.

---

## 8. Historial

| Fecha | Evento |
|-------|--------|
| 2026-08-25 | Custodio acepta HR-L1-01 = **P2**; fija HR-L1-02, HR-L1-03 y método HR-L1-04. |
| 2026-08-25 | Materialización de este expediente no normativo en `standard/process/`. |
