# EDITORIAL-CANON — Canon Editorial Mínimo

> Operativo. Decisiones: [`standard/cdr/CDR-001.md`](../../standard/cdr/CDR-001.md), [`CDR-002.md`](../../standard/cdr/CDR-002.md), [`CDR-003.md`](../../standard/cdr/CDR-003.md).

## Identidad del estándar

- Nombre oficial: **Web3 Trust-Native**  
- No describirlo como framework, plataforma, blockchain o colección de documentos sueltos.  
- Es una **Constitución / estándar constitucional** para instituciones gobernadas por conocimiento.  
- `CONSTITUTION.md` = **Carta** (declarativa). La norma articulada vive en los **Libros** bajo `constitution/`.  
- `STANDARD.md` = gobernanza procesal; **no** redactar como si legislara artículos.

## Títulos canónicos de Libros (CDR-002)

| Libro | Usar (canónico) | No usar como título de Libro |
|-------|-----------------|------------------------------|
| L7 | **Materialización Institucional** | “Aplicación y Experiencia de Usuario” |
| L8 | **Agentes Institucionales** | “Agentes de Inteligencia Artificial” |

| Concepto permitido | Cómo usarlo |
|--------------------|-------------|
| Aplicación / UX | Etapa de derivación o **subdominio/forma** de Materialización |
| Agentes de IA | **Especialización** de Agentes Institucionales (p. ej. Art. L de L0) |

Si L0 u otro texto aún muestra títulos Versión B para L7/L8:

```text
DIVERGENCIA PENDIENTE DE RECONCILIACIÓN HUMANA
```

No “corregir” L0 en lotes operativos. Reportar; pedir revisión humana.

## Términos preferidos

| Usar | Evitar como sustituto |
|------|------------------------|
| Constitución | “spec técnica” / “docs del producto” |
| Libro (L0–L8) | “módulo”, “paquete”, “capítulo de software” |
| Canon de Dominio | “modelo de negocio” como autoridad |
| UNE | “microservicio” como equivalente |
| Materialización | “frontend” como equivalente constitucional del Libro L7 |
| Agente Institucional | “bot” / “usuario del sistema” como equivalente del Libro L8 |
| Evidencia / Prueba | “confianza ciega” |
| Fuente histórica (DOCX) | “legacy inútil” |
| Carta (`CONSTITUTION.md`) | “la Constitución completa con artículos” |
| Standard (procesal) | “norma superior a la Constitución” |

## Estilo

1. Español como idioma canónico prioritario.  
2. Oraciones claras; una idea normativa por párrafo cuando sea posible.  
3. Principios en **negrita** cuando sean axiomas.  
4. Cadenas de derivación en bloques de código Markdown.  
5. Listas para enumeraciones normativas cortas.  
6. No emojis en texto constitucional.  
7. No tono de marketing de producto software.

## Versionado editorial (CDR-003)

- Distinguir **versión** (número por plano) de **estado** (Draft, pending-human-review, Official, etc.).  
- Versión de Libro en `manifest.json` y cabecera de `BOOK.md` deben coincidir entre sí.  
- Estado actual honesto de Libros / Standard: **0.1.0** + **Draft** (salvo evidencia histórica distinta en el propio archivo).  
- **No** elevar a `1.0.0` / `Official` constitucional sin mandato humano y publicación real.  
- **No** inventar ni citar como existentes: `VERSION.md`, `CHANGELOG.md`, release, tag, si ausentes.  
- Git ausente ⇒ no redactar como si la preservación Git ya fuera efectiva.
