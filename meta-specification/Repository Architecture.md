# Repository Architecture

## Arquitectura del Repositorio Web3 Trust-Native

**Versión:** 0.1.0 Draft

**Estado:** Draft (metaspecificación · no Official · no publicación 1.0.0)

**Rol (CDR-001 / CDR-005):** metaspecificación del árbol. Explica; **no** enmienda la Constitución.  
`.cursor/` es tooling operativo; **no** es autoridad constitucional.  
**Git (estado operativo):** repositorio presente; remote `https://github.com/jpgsChile/web3-trust-native`; rama `master`; snapshot GitHub presente. LICENSE = MIT / CODE_ONLY. Git preserva; no crea autoridad ni Official/Published.  
**Histórico (L3-RELEASE2):** `.git` local **sin** remote ni commits; la licencia pendiente bloqueaba el push público.

---

# Propósito

El presente documento establece la arquitectura del repositorio de la Constitución **Web3 Trust-Native**, definiendo la organización, jerarquía, responsabilidades y relaciones entre los artefactos del estándar **según el árbol físico real** y clasificando lo previsto pero aún no materializado.

El propósito de esta arquitectura no consiste únicamente en organizar archivos.

Su propósito consiste en preservar la integridad constitucional del conocimiento institucional, garantizando que toda representación física del estándar permanezca coherente con la arquitectura normativa definida por la Constitución (`constitution/`).

El repositorio constituye una **materialización organizada del conocimiento constitucional**.

No constituye la Constitución misma.

La autoridad reside exclusivamente en el conocimiento constitucional (árbol `constitution/`) y no en la estructura del repositorio, ni en `CONSTITUTION.md` (resumen de entrada), ni en `STANDARD.md` (gobernanza subordinada), ni en `.cursor/`.

---

# Principios Arquitectónicos

Toda evolución del repositorio deberá respetar simultáneamente los siguientes principios.

## 1. Primacía Constitucional

La Constitución (`constitution/`, con L0 en `constitution/L0/BOOK.md`) constituye la autoridad normativa del ecosistema.

Toda carpeta, archivo, herramienta o representación derivada —incluida esta metaspecificación— deberá permanecer subordinada a ella.

---

## 2. Separación entre Autoridad y Representación

La autoridad normativa pertenece exclusivamente a la Constitución.

El repositorio constituye únicamente su representación organizada.

Modificar la estructura del repositorio nunca implica modificar la Constitución.

---

## 3. Separación entre Normativo y No Normativo

Todo artefacto deberá clasificarse explícitamente como:

- Normativo
- Metaespecificación
- Derivado
- Auxiliar
- Ejemplo
- Investigación

Nunca deberán mezclarse dentro de una misma estructura.

---

## 4. Independencia Tecnológica

La organización del repositorio no dependerá de tecnologías específicas.

Podrá evolucionar independientemente de:

- Git
- GitHub
- GitLab
- IDEs
- Lenguajes
- Frameworks
- Plataformas Cloud

---

## 5. Materialización Controlada

Todo archivo constituye una materialización del conocimiento.

La materialización podrá cambiar.

El conocimiento deberá permanecer.

---

## 6. Evolución Compatible

Toda modificación del repositorio deberá preservar:

- continuidad constitucional;
- trazabilidad;
- compatibilidad;
- versionado;
- referencias cruzadas.

---

# Clasificación de Artefactos

Todo elemento del repositorio pertenece exactamente a una de las siguientes categorías.

## Artefactos Normativos

Definen el estándar.

Poseen autoridad constitucional según su estado de migración/publicación (CDR-001).

Ejemplos **existentes:**

- Libros bajo `constitution/L0`…`L8` y `L3-DA` (`BOOK.md`, `original/*.docx`, manifests)
- `CONSTITUTION.md` es **entrada/resumen**, no norma paralela

---

## Artefactos de Gobernanza

Definen procesos, CDR y evolución del estándar.

**Subordinados** a la Constitución.

Ejemplos **existentes (parcial):** `STANDARD.md`, `standard/cdr/` (CDR Accepted).

Carpetas `standard/governance|lifecycle|publication|versioning|standard/` — **RESERVADAS** (vacías en disco; Git no versiona directorios vacíos). `standard/process/` está **parcialmente materializado** (`L1-HR-CLOSE.md`).

---

## Artefactos de Metaespecificación

Explican el estándar.

No modifican la Constitución.

Ejemplos **existentes:** este documento, `Readme.md`.

Ejemplos **NO MATERIALIZADOS:** MANIFEST.md, INDEX.md, GLOSSARY.md, VERSION.md, CHANGELOG.md.

---

## Artefactos Ontológicos / de Conocimiento / Schemas / Conformance / Compilador / IA

Previstos en la arquitectura a largo plazo.

Estado actual: **RESERVADOS / NO MATERIALIZADOS** (no existen como carpetas canónicas en el árbol).

No sustituyen la Constitución.

---

## Artefactos Derivados

Son generados automáticamente (cuando existan generadores).

Nunca constituyen la fuente oficial.

---

## Artefactos Auxiliares / Tooling operativo

Facilitan edición y custodia.

No poseen autoridad normativa.

Ejemplo **existente:** `.cursor/`, `AGENTS.md`.

---

## Artefactos de Referencia

Documentan interoperabilidad con otros estándares.

`reference model/` — **RESERVADO** (vacío).

No alteran la Constitución.

---

# Jerarquía Arquitectónica

Toda interpretación del repositorio deberá respetar el siguiente orden de **precedencia conceptual** (las capas inferiores no modifican el significado de las superiores):

```
Constitución (constitution/)     [EXISTENTE]

↓

Gobernanza / STANDARD / CDR      [EXISTENTE parcial]

↓

Metaespecificación               [EXISTENTE parcial]

↓

Tooling operativo (.cursor/)     [EXISTENTE · no normativo]

↓

Capas futuras derivadas          [RESERVADAS / NO MATERIALIZADAS]
(ontology, knowledge, schemas, conformance, ai, compiler, examples, guides, …)
```

Las capas inferiores nunca podrán modificar el significado de las superiores.

---

# Fuente Única de Verdad

La única fuente normativa del estándar es la Constitución en `constitution/`.

Todo lo demás constituye representación, gobernanza, metaspecificación o tooling derivado.

En consecuencia, cuando existan:

- Ontologías derivarán de la Constitución.
- Grafos derivarán de la Constitución.
- Schemas derivarán de la Constitución.
- Reglas para IA derivarán de la Constitución.
- Compiladores derivarán de la Constitución.

Nunca ocurrirá el proceso inverso.

Hoy esas capas derivadas están **no materializadas**.

---

# Organización del Repositorio

El repositorio se estructura mediante dominios de responsabilidad claramente separados.

Cada carpeta posee un único propósito.

Ninguna carpeta podrá asumir responsabilidades pertenecientes a otra.

## Árbol EXISTENTE (físico)

```text
web3-trust-native/

Readme.md
CONSTITUTION.md          # entrada/resumen (subordinado a L0)
STANDARD.md              # gobernanza subordinada
AGENTS.md
.gitignore

constitution/            # único árbol con autoridad constitucional estructural
  L0/ … L8/
  L3-DA/

meta-specification/
  Repository Architecture.md

standard/
  cdr/                   # EXISTENTE (CDR-001 … CDR-007 ACCEPTED)
  process/               # EXISTENTE parcial (`L1-HR-CLOSE.md`)
  governance/            # RESERVADO (vacío en disco; Git no versiona directorios vacíos)
  lifecycle/             # RESERVADO (vacío en disco; Git no versiona directorios vacíos)
  publication/           # RESERVADO (vacío en disco; Git no versiona directorios vacíos)
  versioning/            # RESERVADO (vacío en disco; Git no versiona directorios vacíos)
  standard/              # RESERVADO (vacío en disco; Git no versiona directorios vacíos)

reference model/         # RESERVADO (vacío en disco; Git no versiona directorios vacíos)

.cursor/                 # tooling operativo (no autoridad constitucional)
```

## Capas RESERVADAS / NO MATERIALIZADAS

No declararlas como existentes. No crearlas por este documento:

`ontology/`, `knowledge/`, `schemas/`, `profiles/`, `ai/`, `conformance/`, `compiler/`, `guides/`, `examples/`, `whitepapers/`, `prompts/`, `VERSION.md`, `CHANGELOG.md`, `releases/`. (Remote GitHub: configurado; no es capa reservada ni autoridad constitucional.)

---

# Responsabilidad de las Carpetas

## constitution/ — EXISTENTE

Contiene exclusivamente el conocimiento normativo por Libros.

Es la única carpeta con autoridad constitucional estructural.

L0: migración `human-reviewed` (manifest; Draft `0.1.0`; no Official; no Published). L1 y L2: `human-reviewed`. L3: `official` (cierre de migración del Libro; no Official de ecosistema; no Published; no L3-COMPLETE). L3-DA y L4–L8: `historical-only` (stub). Identidad canónica L7 = Materialización Institucional; L8 = Agentes Institucionales (CDR-002); la reconciliación textual de títulos L7/L8 en L0 BOOK permanece como `DIVERGENCIA PENDIENTE DE RECONCILIACIÓN HUMANA` (no auto-editar L0).

---

## meta-specification/ — EXISTENTE (parcial)

Contiene los documentos que describen el estándar.

No modifica el estándar.

Lo explica.

---

## standard/ — EXISTENTE (parcial)

Gobierna la evolución del propio estándar (CDR, procesos previstos).

Subordinado a la Constitución.

---

## .cursor/ / AGENTS.md — EXISTENTE (operativo)

Custodia editorial del Agent.

No legisla.

---

## ontology/, knowledge/, schemas/, profiles/, ai/, conformance/, compiler/, guides/, examples/, whitepapers/ — NO MATERIALIZADAS

Reservadas para materialización futura bajo mandato humano.

No inventar su contenido desde esta metaspecificación.

---

# Reglas de Evolución

Toda incorporación de nuevos artefactos deberá responder previamente las siguientes preguntas:

1. ¿Pertenece a la Constitución?

2. ¿Pertenece a la Metaespecificación?

3. ¿Es una representación derivada?

4. ¿Es únicamente documentación?

5. ¿Es una implementación?

6. ¿Es una herramienta?

Sólo después podrá definirse su ubicación.

---

# Compatibilidad

Toda evolución del repositorio deberá preservar:

- enlaces permanentes;
- referencias cruzadas;
- trazabilidad histórica;
- identificadores constitucionales;
- compatibilidad con versiones anteriores.

---

# Consideraciones para Agentes de Inteligencia Artificial

Los **Agentes Institucionales** (Libro L8; la IA es especialización posible — CDR-002) deberán interpretar la arquitectura del repositorio como una representación estructurada del conocimiento constitucional y nunca como la fuente de autoridad del estándar.

Durante procesos de generación, análisis, validación o evolución deberán respetar la jerarquía arquitectónica definida en este documento, preservando la separación entre conocimiento normativo, gobernanza, metaspecificación, tooling operativo y capas futuras no materializadas.

Ningún agente podrá inferir autoridad normativa a partir de la ubicación física de un archivo, ni tratar `.cursor/` como Constitución.

La autoridad proviene exclusivamente de la Constitución en `constitution/`.

Toda generación automática deberá mantener trazabilidad hacia los artículos constitucionales que la originan.

---

# Declaración Final

La arquitectura del repositorio constituye el mecanismo mediante el cual el conocimiento constitucional puede organizarse, evolucionar y materializarse sin comprometer su integridad.

Así como la Constitución gobierna a la institución, la presente Arquitectura **describe** el repositorio que preserva dicha Constitución — sin autoridad normativa propia y en estado **0.1.0 Draft**.

En consecuencia, el repositorio deja de presentarse como colección indiferenciada de archivos y se reconoce como infraestructura de preservación y evolución del conocimiento institucional **Web3 Trust-Native**, con capas futuras explícitamente **no materializadas** hasta mandato humano.