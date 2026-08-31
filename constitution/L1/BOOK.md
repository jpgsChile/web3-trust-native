# L1 — Reglas de Arquitectura Web3 Trust-Native

> **Libro:** L1  
> **Versión vigente (repositorio):** 0.1.0  
> **Estado vigente (repositorio):** Draft  
> **Fuente histórica:** `original/L1-001-Reglas-de-Arquitectura.docx`  
> **Bloque materializado:** B0 (front-matter histórico + preámbulo)  
> **Estado de migración:** Materialización parcial controlada — artículos I–LXXX, declaración final, versionado histórico, relación con niveles y `FIN` permanecen en la fuente histórica hasta lotes posteriores  
> **Autoridad efectiva (CDR-001):** `BOOK.md` es el path canónico previsto (`source.official`); mientras la migración no esté cerrada, el cuerpo no materializado conserva su norma de hecho en el DOCX histórico. Este archivo **no** es Official, **no** es Published y **no** es `human-reviewed`  
> **Regla:** nunca conversión automática DOCX → Markdown  
> **Expediente de proceso (NO NORMATIVO):** `../../standard/process/L1-HR-CLOSE.md`  
> **HR-L1-02:** los valores históricos del DOCX (`Versión 0.1`, `Línea Base Arquitectónica`) se preservan abajo como contexto histórico y **no** sustituyen el estado vigente `0.1.0` / Draft

---

## Front-matter histórico (DOCX)

### Versión 0.1 — Especificación Normativa para Razonamiento Arquitectónico

| Campo histórico | Valor histórico (DOCX) |
|-----------------|------------------------|
| Versión | 0.1 |
| Estado | Línea Base Arquitectónica |
| Nivel | L1 — Reglas de Arquitectura |
| Idioma canónico prioritario | Español |
| Dependencia normativa | L0 — Constitución Web3 Trust-Native v0.1 |
| Ámbito | Arquitecturas, protocolos, sistemas y agentes de inteligencia artificial Web3 Trust-Native |
| Precedencia | Inferior a L0 y superior a L2–L8 |

---

## PREÁMBULO

L0 — Constitución Web3 Trust-Native establece los principios fundamentales de confianza, autoridad, evidencia y soberanía.

L1 convierte esos principios en:

**reglas obligatorias de razonamiento arquitectónico.**

L1 no prescribe una blockchain.

No prescribe EVM.

No prescribe Solidity.

No prescribe Layer 1 o Layer 2.

No prescribe una topología universal.

No prescribe un stack tecnológico.

Su función consiste en determinar **cómo debe derivarse una arquitectura a partir del dominio y de sus requerimientos de confianza y soberanía.**

La secuencia normativa fundamental será:

```text
CONSTITUCIÓN
      ↓
DOMINIO
      ↓
CONFIANZA
      ↓
AUTORIDAD
      ↓
EVIDENCIA
      ↓
SOBERANÍA
      ↓
ARQUITECTURA
      ↓
INFRAESTRUCTURA
      ↓
IMPLEMENTACIÓN
```

Por tanto:

**La arquitectura no selecciona primero tecnología.**

**La arquitectura determina primero garantías.**

## ARTÍCULO I — MANDATO ARQUITECTÓNICO

Toda arquitectura Web3 Trust-Native deberá demostrar cómo satisface los principios establecidos por L0.

Ningún componente tecnológico podrá incorporarse simplemente porque:

- sea popular;
- sea conocido por el equipo;
- forme parte de un stack habitual;
- facilite el desarrollo;
- haya sido utilizado en otro proyecto;
- sea recomendado por defecto por un agente de IA.


Toda decisión deberá responder:

**¿Qué garantía del modelo de confianza satisface este componente?**

Si no existe una respuesta verificable, el componente no deberá considerarse arquitectónicamente necesario.

## ARTÍCULO II — PRECEDENCIA CONSTITUCIONAL

L1 no podrá reinterpretar ni contradecir L0.

La jerarquía será:

```text
L0 — CONSTITUCIÓN
        >
L1 — ARQUITECTURA
        >
L2 — PROTOCOLO
        >
L3 — DOMINIO
        >
L4–L8 — IMPLEMENTACIÓN Y OPERACIÓN
```


Ante cualquier conflicto:

**prevalece la regla de nivel superior.**

## ARTÍCULO III — CADENA DE DERIVACIÓN

Toda arquitectura deberá derivarse mediante:

```text
DOMINIO
   ↓
ACTORES
   ↓
CONFIANZA
   ↓
AUTORIDAD
   ↓
CLAIMS
   ↓
ATTESTATIONS
   ↓
PROOFS
   ↓
SOBERANÍA
   ↓
ESTADO
   ↓
PROTOCOLO
   ↓
ARQUITECTURA
   ↓
INFRAESTRUCTURA
```


Se prohíbe invertir esta secuencia.

Por tanto, queda rechazado:

```text
BLOCKCHAIN
   ↓
STACK
   ↓
SMART CONTRACTS
   ↓
BASE DE DATOS
   ↓
API
   ↓
“ADAPTAR EL NEGOCIO”
```


## ARTÍCULO IV — PUERTA DE ENTRADA ARQUITECTÓNICA

Antes de diseñar componentes tecnológicos deberán existir respuestas suficientes para:

### DOMINIO

¿Qué realidad se intenta representar?

### ACTORES

¿Quiénes participan?

### RELACIONES

¿Cómo se relacionan?

### CONFIANZA

¿Quién necesita confiar en quién?

### AUTORIDAD

¿Quién puede declarar qué?

### OBSERVADORES AUTORIZADOS

¿Quién puede observar legítimamente hechos externos?

### CLAIMS

¿Qué afirmaciones relevantes existen?

### ATTESTATIONS

¿Quién puede respaldarlas?

### PROOFS

¿Qué debe poder demostrarse?

### PROPIEDAD

¿Quién posee qué?

### CONSENTIMIENTO

¿Quién puede autorizar acceso o uso?

### PRIVACIDAD

¿Qué información no debe ser públicamente visible?

### SOBERANÍA

¿Qué autoridad no puede entregarse a un intermediario?

### GOBERNANZA

¿Quién puede modificar las reglas?

Si estas preguntas no están suficientemente resueltas:

**la arquitectura tecnológica no deberá considerarse madura para aprobación.**

## ARTÍCULO V — MODELO DE ACTORES

Toda arquitectura deberá construir explícitamente un Modelo de Actores.

Para cada Actor deberá identificarse:

```text
Actor
├── Identidad
├── Rol
├── Autoridad
├── Capacidades
├── Relaciones
├── Propiedad
├── Consentimientos
├── Delegaciones
├── Claims
├── Attestations
└── Proofs
```


Una dirección EVM no deberá considerarse por sí sola modelo de identidad suficiente.

```text
Actor ≠ Wallet ≠ Address
```


Una misma entidad podrá controlar múltiples cuentas.

Una cuenta podrá cambiar.

La identidad del dominio deberá sobrevivir, cuando corresponda, a la rotación de claves.

## ARTÍCULO VI — MATRIZ DE AUTORIDAD

Toda arquitectura deberá construir una Matriz de Autoridad.

Como mínimo:

```text
ACTOR
RECURSO
ACCIÓN
AUTORIDAD
ORIGEN DE AUTORIDAD
ALCANCE
DURACIÓN
DELEGABLE
REVOCABLE
```


La pregunta principal será:

**¿Por qué este Actor puede realizar esta acción?**

“Porque es administrador” no constituye justificación suficiente.

## ARTÍCULO VII — AUTORIDAD CONTEXTUAL

Toda autoridad deberá estar limitada al contexto en el cual resulta legítima.

Formalmente:

```text
Authority =
f(
 Actor,
 Capability,
 Resource,
 Context,
 Purpose,
 Scope,
 Time,
 Jurisdiction
)
```


No deberá existir autoridad universal salvo que el dominio demuestre una necesidad excepcional y constitucionalmente compatible.

## ARTÍCULO VIII — MODELO DE CONFIANZA

Toda arquitectura deberá producir un Modelo de Confianza.

Deberá identificar:

```text
Actor A
   │
   │ relación
   ▼
Actor B
   │
   │ autoridad
   ▼
Claim
   │
   │ Attestation
   ▼
Proof
```


La arquitectura deberá determinar qué relaciones:

- requieren confianza humana;
- requieren autoridad institucional;
- pueden verificarse criptográficamente;
- pueden delegarse;
- pueden revocarse;
- requieren consenso;
- requieren privacidad.


## ARTÍCULO IX — GRAFO DE CONFIANZA

Cuando el dominio lo permita deberá construirse:

```text
G = (A, R)
```


donde:

```text
A = Actores
R = Relaciones verificables
```


Cada relación deberá poseer semántica explícita.

Ejemplos:

```text
EMITE
ACREDITA
POSEE
AUTORIZA
DELEGA
REVOCA
CREA
PARTICIPA
CERTIFICA
VERIFICA
CONSiente
```


No deberán crearse relaciones genéricas cuando exista una semántica de dominio más precisa.

## ARTÍCULO X — FRONTERA ENTRE REALIDAD Y PROTOCOLO

Cuando el protocolo represente hechos externos deberá existir una Frontera de Realidad.

```text
REALIDAD
   ↓
OBSERVADOR AUTORIZADO
   ↓
CLAIM
   ↓
ATTESTATION
   ↓
PROOF
   ↓
ESTADO
```


Blockchain no deberá asumir como verdad automática aquello que provenga del mundo exterior.

## ARTÍCULO XI — OBSERVADORES AUTORIZADOS

Todo Observador Autorizado deberá poseer:

```text
IDENTIDAD
AUTORIDAD
ALCANCE
CONTEXTO
VIGENCIA
MECANISMO DE VERIFICACIÓN
MECANISMO DE REVOCACIÓN
```


Un oracle técnico no deberá confundirse con autoridad del dominio.

El oracle puede transportar información.

La autoridad proviene del Actor o mecanismo legitimado por el dominio.

## ARTÍCULO XII — MODELO DE ESTADO

Toda arquitectura deberá clasificar explícitamente el estado.

Como mínimo:

```text
ESTADO AUTORITATIVO
ESTADO DERIVADO
ESTADO PRIVADO
ESTADO TEMPORAL
ESTADO INDEXADO
ARTEFACTO EXTERNO
PRUEBA
```


Esta clasificación deberá realizarse antes de decidir almacenamiento.

## ARTÍCULO XIII — ESTADO AUTORITATIVO

Se considera Estado Autoritativo aquel cuya modificación altera la verdad fundamental del protocolo.

Ejemplos posibles:

- ownership;
- permisos;
- Claims;
- Attestations;
- revocaciones;
- capabilities;
- consentimientos;
- relaciones fundamentales;
- balances;
- governance state.


Cuando el dominio requiera verificabilidad independiente:

**el Estado Autoritativo no deberá depender exclusivamente de una base de datos privada.**

## ARTÍCULO XIV — ESTADO DERIVADO

Estado Derivado es aquel que puede reconstruirse desde información autoritativa.

Ejemplos:

- estadísticas;
- rankings;
- dashboards;
- búsquedas;
- vistas;
- agregaciones;
- métricas;
- recomendaciones.


Podrá almacenarse en infraestructura centralizada cuando:

**su pérdida no modifique la verdad del protocolo.**

## ARTÍCULO XV — ESTADO INDEXADO

Los indexadores podrán mantener representaciones optimizadas del estado.

```text
PROTOCOL STATE
      ↓
    EVENTS
      ↓
   INDEXER
      ↓
QUERY MODEL
```


El indexador:

**no deberá convertirse en fuente de verdad.**

Si desaparece deberá poder reconstruirse.

## ARTÍCULO XVI — MATRIZ DE ESTADO

Toda arquitectura deberá generar una Matriz de Estado:

```text
DATO / RECURSO
CLASIFICACIÓN
AUTORIDAD
LECTURA
ESCRITURA
PERSISTENCIA
PRIVACIDAD
RECONSTRUIBLE
REVOCABLE
UBICACIÓN PROPUESTA
JUSTIFICACIÓN
```


Ninguna decisión on-chain / off-chain deberá tomarse sin esta clasificación.

## ARTÍCULO XVII — CRITERIO ON-CHAIN

Un estado deberá considerarse candidato a on-chain cuando requiera una o más de las siguientes garantías:

- consenso compartido;
- ownership verificable;
- ejecución determinista;
- resistencia a manipulación;
- portabilidad;
- auditabilidad;
- interoperabilidad;
- disponibilidad independiente;
- gobernanza verificable.


No todo dato que pueda almacenarse on-chain deberá almacenarse allí.

## ARTÍCULO XVIII — CRITERIO OFF-CHAIN

Un recurso podrá permanecer off-chain cuando:

- sea demasiado grande;
- requiera privacidad;
- sea reconstruible;
- no constituya verdad fundamental;
- su disponibilidad pueda garantizarse por otros mecanismos;
- posea una referencia criptográfica suficiente;
- exista una estrategia de persistencia compatible con soberanía.


off-chain no significa automáticamente centralizado.

## ARTÍCULO XIX — INFORMACIÓN PRIVADA

La información privada deberá diseñarse bajo:

**privacidad desde la arquitectura.**

No deberá publicarse información sensible simplemente porque blockchain lo permita.

Deberán evaluarse según el dominio:

```text
Encryption
Commitments
Selective Disclosure
Zero-Knowledge Proofs
Verifiable Credentials
Decentralized Identifiers
Encrypted Decentralized Storage
Threshold Cryptography
```


La arquitectura deberá intentar demostrar propiedades sin revelar información innecesaria.

## ARTÍCULO XX — MINIMIZACIÓN DE INFORMACIÓN

Todo protocolo deberá aplicar:

**mínima información necesaria.**

Si una decisión puede demostrarse mediante:

```text
Proof(condition == true)
```


no deberá exigirse necesariamente la exposición del conjunto completo de datos que produjo dicha condición.

## ARTÍCULO XXI — ARQUITECTURA DE PROPIEDAD

Todo recurso deberá identificar:

```text
CREADOR
SUJETO
PROPIETARIO
CUSTODIO
EMISOR
CONTROLADOR
BENEFICIARIO
```


cuando dichos roles sean aplicables.

La arquitectura no deberá inferir:

```text
CREATOR == OWNER
```


ni:

```text
CUSTODIAN == OWNER
```


sin fundamento del dominio.

## ARTÍCULO XXII — ARQUITECTURA DE CONSENTIMIENTO

El consentimiento deberá modelarse como una relación verificable.

Conceptualmente:

```text
Consent {
    grantor
    grantee
    resource
    capability
    purpose
    scope
    issuedAt
    expiresAt
    revocable
}
```


El consentimiento deberá poder ser:

- explícito;
- limitado;
- verificable;
- temporal;
- revocable;


cuando el dominio así lo requiera.

## ARTÍCULO XXIII — ARQUITECTURA DE CAPACIDADES

La autorización deberá favorecer capacidades explícitas.

Ejemplo:

```text
Actor
   │
   └── HAS_CAPABILITY
             │
             ▼
         CAN_ATTEST
```


Las capacidades deberán poder derivarse de:

- ownership;
- credenciales;
- Attestations;
- roles;
- delegaciones;
- consentimiento;
- governance;
- reglas del protocolo.


## ARTÍCULO XXIV — CLAIM → ATTESTATION → PROOF

Toda arquitectura que represente afirmaciones deberá distinguir:

### CLAIM

Lo que un Actor afirma.

### ATTESTATION

Quién respalda esa afirmación y con qué autoridad.

### PROOF

Qué puede demostrarse criptográficamente.

La cadena será:

```text
AUTHORIZED OBSERVER
        ↓
      CLAIM
        ↓
   ATTESTATION
        ↓
      PROOF
```


Estas entidades no deberán colapsarse en un único booleano de base de datos.

## ARTÍCULO XXV — ARQUITECTURA DE IDENTIDAD

La identidad deberá diseñarse independientemente de una plataforma específica.

Deberá evaluarse:

- identidad criptográfica;
- rotación de claves;
- recuperación;
- delegación;
- identidad institucional;
- múltiples wallets;
- smart accounts;
- Decentralized Identifiers;
- Verifiable Credentials;


según requerimientos del dominio.

La wallet deberá entenderse como mecanismo de control criptográfico, no necesariamente como identidad completa.

## ARTÍCULO XXVI — RECUPERACIÓN

La soberanía no deberá convertir la pérdida de una clave en pérdida inevitable de identidad, derechos o historia cuando el dominio permita mecanismos de recuperación.

Podrán evaluarse:

- social recovery;
- guardian models;
- smart accounts;
- multisig;
- institutional recovery;
- threshold schemes.


La recuperación no deberá introducir un administrador universal oculto.

## ARTÍCULO XXVII — ARQUITECTURA DE INTEROPERABILIDAD

La interoperabilidad deberá construirse alrededor de:

```text
IDENTIDAD
CLAIMS
ATTESTATIONS
PROOFS
CAPABILITIES
STANDARDS
```


y no simplemente mediante APIs entre aplicaciones.

Una API puede facilitar interoperabilidad.

No deberá ser su única garantía.

## ARTÍCULO XXVIII — INTEROPERABILIDAD SIN TRANSFERENCIA DE SOBERANÍA

Un protocolo deberá poder verificar información proveniente de otro dominio sin necesariamente:

- copiarla;
- apropiarse de ella;
- almacenarla permanentemente;
- obtener acceso al origen completo.


Preferir:

```text
VERIFY(PROOF)
```


sobre:

```text
IMPORT(ALL_DATA)
```


cuando el dominio lo permita.

## ARTÍCULO XXIX — ARQUITECTURA DE GOBERNANZA

Toda arquitectura deberá identificar:

```text
QUIÉN PROPONE
QUIÉN APRUEBA
QUIÉN EJECUTA
QUIÉN PUEDE VETAR
QUIÉN PUEDE REVOCAR
QUIÉN PUEDE ACTUALIZAR
QUIÉN PUEDE EMERGENCY-PAUSE
```


cuando corresponda.

Gobernanza no deberá equivaler automáticamente a token voting.

## ARTÍCULO XXX — SOBERANÍA DE GOBERNANZA

La gobernanza deberá reflejar la legitimidad del dominio.

Cuando existan múltiples autoridades deberá evaluarse gobernanza distribuida.

La existencia de una organización promotora no le concede autoridad permanente sobre el protocolo.

## ARTÍCULO XXXI — SELECCIÓN DEL NIVEL DE SOBERANÍA

Toda arquitectura deberá clasificar su requerimiento predominante:

### S0 — SOBERANÍA DE APLICACIÓN

La aplicación puede depender ampliamente de infraestructura externa.

### S1 — SOBERANÍA DE PROTOCOLO

El protocolo requiere reglas propias verificables sobre infraestructura compartida.

### S2 — SOBERANÍA DE EJECUCIÓN

El dominio requiere control significativo sobre ejecución, configuración o economía.

### S3 — SOBERANÍA DE RED

El dominio requiere control sobre participación, gobernanza, validadores, reglas de red o consenso.

## ARTÍCULO XXXII — REGLA DE SELECCIÓN DE RED

La selección deberá derivarse:

```text
TRUST REQUIREMENTS
        ↓
SOVEREIGNTY REQUIREMENTS
        ↓
ARCHITECTURAL REQUIREMENTS
        ↓
NETWORK REQUIREMENTS
        ↓
INFRASTRUCTURE CANDIDATES
```


Nunca:

```text
FAVORITE BLOCKCHAIN
        ↓
PROJECT ARCHITECTURE
```


## ARTÍCULO XXXIII — CRITERIOS PARA INFRAESTRUCTURA COMPARTIDA

Una red existente, Layer 2 o infraestructura compartida deberá favorecerse cuando:

- sus garantías sean suficientes;
- no exista necesidad legítima de controlar validadores;
- no exista necesidad de consenso especializado;
- el dominio pueda heredar seguridad;
- el protocolo mantenga soberanía suficiente;
- exista portabilidad razonable;
- la dependencia no introduzca autoridad incompatible.


## ARTÍCULO XXXIV — CRITERIOS PARA SOBERANÍA DE RED

Una Layer 1, appchain o red soberana sólo deberá proponerse cuando existan requerimientos demostrables relacionados con:

- gobernanza propia;
- conjunto de validadores;
- participación permissioned;
- jurisdicción;
- privacidad;
- reglas de consenso;
- ejecución especializada;
- disponibilidad;
- economía propia;
- independencia operacional;
- soberanía pública o institucional.


**“Queremos nuestra propia blockchain” no constituye requerimiento arquitectónico suficiente.**

## ARTÍCULO XXXV — COMPATIBILIDAD EVM

EVM deberá considerarse una decisión de compatibilidad y ejecución.

No un principio constitucional.

Podrá seleccionarse cuando aporte:

- interoperabilidad;
- tooling maduro;
- portabilidad de smart contracts;
- ecosistema;
- seguridad operacional;
- acceso a desarrolladores;
- compatibilidad entre redes.


La selección deberá justificarse.

## ARTÍCULO XXXVI — BASES DE DATOS

Una base de datos tradicional podrá utilizarse cuando actúe como:

- índice;
- caché;
- almacenamiento temporal;
- analytics store;
- search engine;
- read model;
- materialized view;
- cola operacional;
- almacenamiento reconstruible.


No deberá convertirse en fuente maestra de:

- ownership;
- autoridad;
- permisos fundamentales;
- identidad soberana;
- balances protocolarios;
- Claims autoritativos;
- Attestations;
- governance state.


## ARTÍCULO XXXVII — PRUEBA DE ELIMINACIÓN DE BASE DE DATOS

Toda arquitectura que incluya una base de datos deberá responder:

**¿Qué ocurre si eliminamos completamente esta base?**

Si puede reconstruirse:

```text
PROTOCOLO
   +
EVENTOS
   +
ARTEFACTOS
   ↓
DATABASE REBUILD
```


su uso puede resultar compatible.

Si eliminarla destruye la verdad fundamental:

**se requiere Excepción Arquitectónica.**

## ARTÍCULO XXXVIII — BACKEND

El backend deberá considerarse infraestructura auxiliar.

Podrá:

- construir transacciones;
- enviar notificaciones;
- indexar;
- agregar información;
- gestionar sesiones no autoritativas;
- facilitar UX;
- ejecutar relayers;
- proporcionar APIs de consulta.


No deberá ser la única entidad capaz de reconstruir o interpretar la verdad del protocolo.

## ARTÍCULO XXXIX — REGLAS DE NEGOCIO

Las reglas que determinen:

- ownership;
- transferencia;
- autoridad;
- consentimiento;
- emisión;
- revocación;
- distribución;
- governance;
- derechos protocolarios;


deberán ubicarse donde puedan ser verificadas y ejecutadas con las garantías requeridas.

No deberán ocultarse exclusivamente en un backend privado cuando constituyan reglas fundamentales del protocolo.

## ARTÍCULO XL — INDEXADORES

Todo indexador deberá tratarse como:

**proyección reconstruible del protocolo.**

Deberá documentarse:

```text
SOURCE
EVENTS
REBUILD STRATEGY
CONSISTENCY MODEL
FAILURE MODE
ALTERNATIVE INDEXER
```


## ARTÍCULO XLI — ALMACENAMIENTO DE ARTEFACTOS

Cuando existan documentos, multimedia, metadata u otros artefactos grandes deberá distinguirse:

```text
CONTENT
CONTENT HASH
OWNERSHIP
ACCESS POLICY
ENCRYPTION
AVAILABILITY
LOCATION
```


El hash no reemplaza automáticamente una estrategia de disponibilidad.

IPFS no garantiza por sí solo persistencia eterna.

La arquitectura deberá definir quién garantiza disponibilidad y bajo qué incentivos.

## ARTÍCULO XLII — RPC

Los proveedores RPC deberán considerarse puntos de acceso reemplazables.

La arquitectura deberá evitar dependencia absoluta de un único proveedor.

Deberán contemplarse:

- múltiples endpoints;
- fallback;
- posibilidad de self-hosting cuando corresponda;
- portabilidad de proveedor.

Un RPC no deberá convertirse en autoridad.

## ARTÍCULO XLIII — ORACLES

Todo oracle deberá analizarse mediante:

```text
SOURCE
OBSERVER
AUTHORITY
TRANSPORT
VERIFICATION
INCENTIVE
FAILURE
DISPUTE
REVOCATION
```


La arquitectura deberá distinguir:

**fuente de información**

de:

**autoridad para afirmar la información.**

## ARTÍCULO XLIV — BRIDGES

Los bridges introducen nuevas dependencias de confianza.

Toda utilización deberá documentar:

- modelo de seguridad;
- custodios;
- validadores;
- contratos;
- mecanismo de verificación;
- riesgo de liquidez;
- riesgo de congelamiento;
- estrategia ante falla.

La interoperabilidad cross-chain no deberá asumirse gratuita en términos de confianza.

## ARTÍCULO XLV — DEPENDENCIAS

Toda dependencia deberá clasificarse:

```text
CRÍTICA
REEMPLAZABLE
RECONSTRUIBLE
CENTRALIZADA
DESCENTRALIZADA
EXTERNA
CONTROLADA
```


Y deberá responder:

**¿Qué ocurre si desaparece?**

## ARTÍCULO XLVI — DEUDA DE SOBERANÍA

Se denomina Deuda de Soberanía a toda dependencia que:

- limita salida;
- concentra autoridad;
- impide portabilidad;
- dificulta reconstrucción;
- introduce vendor lock-in;
- requiere confianza no prevista;
- sin una estrategia razonable de eliminación o sustitución.

Toda Deuda de Soberanía deberá registrarse explícitamente.

## ARTÍCULO XLVII — DESCENTRALIZACIÓN PROGRESIVA

Se permitirá evolución progresiva cuando exista una arquitectura objetivo explícita.

```text
MVP
↓
PROTOCOLO
↓
DESCENTRALIZACIÓN
↓
SOBERANÍA OBJETIVO
```


Un MVP podrá contener simplificaciones.

No podrá convertir dichas simplificaciones en fundamentos irreversibles.

## ARTÍCULO XLVIII — TRAICIÓN ARQUITECTÓNICA

Se considerará Traición Arquitectónica cuando una decisión temporal:

- redefine ownership;
- centraliza identidad;
- convierte una base en fuente maestra;
- impide portabilidad;
- introduce custodia irreversible;
- impide migración;
- destruye soberanía futura.

Una simplificación de MVP no justifica traicionar el modelo objetivo.

## ARTÍCULO XLIX — PRUEBA DE DESAPARICIÓN

Antes de aprobar una arquitectura deberá simularse:

```text
DELETE COMPANY
DELETE FRONTEND
DELETE BACKEND
DELETE DATABASE
DELETE PRIMARY RPC
DELETE PRIMARY INDEXER
```


y evaluar:

```text
¿SOBREVIVE LA VERDAD?
¿SOBREVIVE LA PROPIEDAD?
¿SOBREVIVEN LOS PROOFS?
¿SOBREVIVEN LOS DERECHOS?
¿PUEDE CONSTRUIRSE OTRO CLIENTE?
```


## ARTÍCULO L — PRUEBA DE SALIDA

Todo Actor deberá evaluarse frente a:

**¿Puede abandonar el proveedor sin perder aquello que legítimamente controla?**

La prueba deberá incluir:

- identidad;
- activos;
- Claims;
- Attestations;
- Proofs;
- credenciales;
- historial;
- relaciones;
- reputación portable.


## ARTÍCULO LI — PRUEBA DE RECONSTRUCCIÓN

La arquitectura deberá determinar qué puede reconstruirse a partir de:

```text
STATE
+
EVENTS
+
PROOFS
+
DECENTRALIZED ARTIFACTS
```


Todo componente reconstruible deberá considerarse infraestructura auxiliar y no fuente primaria de verdad.

## ARTÍCULO LII — MATRIZ DE SOBERANÍA

Toda propuesta arquitectónica deberá incluir:

```text
DIMENSIÓN
ACTOR SOBERANO
AUTORIDAD
INFRAESTRUCTURA
DEPENDENCIA
RIESGO
MECANISMO DE SALIDA
```


Como mínimo para:

```text
IDENTIDAD
DATOS
PROPIEDAD
CONSENTIMIENTO
EJECUCIÓN
GOBERNANZA
ALMACENAMIENTO
INTEROPERABILIDAD
```


## ARTÍCULO LIII — REGISTRO DE DECISIONES ARQUITECTÓNICAS

Las decisiones relevantes deberán documentarse mediante ADR o mecanismo equivalente.

Cada decisión deberá registrar:

```text
CONTEXTO
REQUERIMIENTO DE CONFIANZA
REQUERIMIENTO DE SOBERANÍA
ALTERNATIVAS
DECISIÓN
JUSTIFICACIÓN
TRADE-OFFS
RIESGOS
REVERSIBILIDAD
ESTRATEGIA DE SALIDA
```


La elección tecnológica sin contexto no constituye decisión arquitectónica suficiente.

## ARTÍCULO LIV — EXCEPCIÓN ARQUITECTÓNICA

Cuando resulte necesaria una decisión incompatible con la preferencia descentralizada deberá generarse:

```text
EXCEPCIÓN ARQUITECTÓNICA
Principio afectado:
Restricción:
Justificación:
Evidencia:
Centralización introducida:
Autoridad concentrada:
Impacto sobre soberanía:
Impacto sobre confianza:
Alternativas evaluadas:
Mitigación:
Duración esperada:
Condición de eliminación:
Estrategia de salida:
Aprobación humana:
```


## ARTÍCULO LV — CONTROL DE CONTAMINACIÓN WEB2.5

Toda arquitectura deberá comprobar:

```text
[ ] Base de datos como fuente maestra
[ ] Backend como autoridad
[ ] Identidad controlada por plataforma
[ ] Permisos privados no verificables
[ ] Custodia central innecesaria
[ ] Administrador universal
[ ] API como única interoperabilidad
[ ] Reputación no portable
[ ] Ownership dependiente de empresa
[ ] Blockchain utilizada sólo como timestamp/hash
[ ] Reglas fundamentales fuera del protocolo
[ ] Dependencia de proveedor sin salida
```


La existencia de cualquiera de estos elementos no implica rechazo automático.

Implica:

**revisión, justificación o eliminación.**

## ARTÍCULO LVI — PUNTUACIÓN DE DESCENTRALIZACIÓN

La arquitectura deberá poder evaluarse al menos en:

```text
D1 — Identidad
D2 — Propiedad
D3 — Autoridad
D4 — Estado
D5 — Ejecución
D6 — Almacenamiento
D7 — Gobernanza
D8 — Interoperabilidad
D9 — Portabilidad
D10 — Recuperabilidad
```


No deberá utilizarse una puntuación única como sustituto del análisis.

El objetivo es identificar dónde persisten dependencias de confianza.

## ARTÍCULO LVII — PUERTA DE APROBACIÓN ARQUITECTÓNICA

Una arquitectura sólo podrá declararse:

**WEB3 TRUST-NATIVE ARCHITECTURE READY**

cuando exista evidencia suficiente de:

```text
[✓] Domain Model
[✓] Actor Model
[✓] Trust Model
[✓] Authority Matrix
[✓] Authorized Observer Model
[✓] Claim Model
[✓] Attestation Model
[✓] Proof Model
[✓] State Matrix
[✓] Sovereignty Matrix
[✓] Privacy Model
[✓] Governance Model
[✓] Dependency Analysis
[✓] Exit Strategy
[✓] Reconstruction Strategy
[✓] Web2.5 Contamination Review
```


La ausencia de elementos deberá declararse explícitamente.

## ARTÍCULO LVIII — ESTADOS DE MADUREZ ARQUITECTÓNICA

Toda propuesta podrá encontrarse en uno de los siguientes estados:

### A0 — DESCUBRIMIENTO

Dominio todavía insuficientemente comprendido.

### A1 — CONFIANZA MODELADA

Actores, relaciones, autoridad y confianza identificados.

### A2 — SOBERANÍA MODELADA

Propiedad, consentimiento, gobernanza y límites de autoridad identificados.

### A3 — PROTOCOLO DERIVADO

Claims, Attestations, Proofs, estado y reglas fundamentales definidos.

### A4 — ARQUITECTURA DERIVADA

Componentes arquitectónicos definidos desde requerimientos.

### A5 — INFRAESTRUCTURA SELECCIONADA

Tecnologías concretas justificadas.

### A6 — ARQUITECTURA APROBADA

Todas las puertas normativas superadas.

## ARTÍCULO LIX — PROHIBICIÓN DE SALTOS DE MADUREZ

Un agente no deberá saltar directamente:

```text
A0
↓
A5
```


Ejemplo prohibido:

“Necesitamos una plataforma de certificaciones. Utilicemos Next.js, PostgreSQL, NestJS, Solidity y Avalanche.”

La respuesta correcta deberá comenzar por A0–A2.

## ARTÍCULO LX — OBLIGACIÓN DE JUSTIFICACIÓN TECNOLÓGICA

Toda tecnología propuesta deberá registrar:

```text
TECNOLOGÍA
ROL
GARANTÍA APORTADA
REQUERIMIENTO QUE SATISFACE
AUTORIDAD QUE INTRODUCE
DEPENDENCIA QUE INTRODUCE
ALTERNATIVAS
REVERSIBILIDAD
ESTRATEGIA DE SALIDA
```


Ejemplo:

```text
Technology: Base
Role: Shared EVM execution
Guarantee: public settlement + interoperability
Requirement: S1 Protocol Sovereignty
Introduced dependency: Base / Ethereum ecosystem
Exit strategy: portable EVM contracts + state migration plan
```


## ARTÍCULO LXI — CHAIN NEUTRALITY

Hasta alcanzar A4:

**la arquitectura deberá permanecer chain-neutral siempre que sea posible.**

La selección concreta de blockchain pertenece a la fase de infraestructura.

Esto evita que preferencias tecnológicas contaminen el modelo del dominio.

## ARTÍCULO LXII — EXCEPCIÓN A CHAIN NEUTRALITY

Una blockchain podrá formar parte temprana del requerimiento únicamente cuando el dominio ya dependa legítimamente de ella.

Ejemplos posibles:

- protocolo que extiende activos existentes de una red;
- interoperabilidad obligatoria con contratos existentes;
- dependencia económica protocolaria preexistente.

La excepción deberá documentarse.

## ARTÍCULO LXIII — COMPARACIÓN DE INFRAESTRUCTURAS

Cuando existan múltiples candidatas deberán compararse utilizando requerimientos derivados.

Como mínimo:

```text
SEGURIDAD
SOBERANÍA
FINALIDAD
GOBERNANZA
PRIVACIDAD
INTEROPERABILIDAD
EVM / VM
COSTO
ESCALABILIDAD
VALIDADORES
DATA AVAILABILITY
PORTABILIDAD
DEPENDENCIAS
MADUREZ
EXIT STRATEGY
```


No deberá seleccionarse infraestructura únicamente por TPS, fees o popularidad.

## ARTÍCULO LXIV — ARQUITECTURA MULTICADENA

La arquitectura multichain sólo deberá utilizarse cuando múltiples redes aporten garantías necesarias.

No deberá adoptarse por moda.

Cada red adicional introduce:

```text
COMPLEJIDAD
BRIDGE RISK
LIQUIDITY FRAGMENTATION
STATE SYNCHRONIZATION
OPERATIONAL DEPENDENCY
SECURITY ASSUMPTIONS
```


La carga de justificar multichain corresponde a quien la propone.

## ARTÍCULO LXV — ARQUITECTURA DE EVENTOS

Los eventos deberán diseñarse como parte de la historia verificable.

Deberán permitir, cuando corresponda:

- auditoría;
- reconstrucción;
- indexación;
- trazabilidad;
- interoperabilidad.

Los eventos no deberán utilizarse como sustituto indiscriminado del estado.

## ARTÍCULO LXVI — ACTUALIZABILIDAD

Todo mecanismo upgradeable deberá declarar:

```text
QUIÉN ACTUALIZA
QUÉ PUEDE CAMBIAR
QUÉ NO PUEDE CAMBIAR
TIEMPO DE ESPERA
MECANISMO DE APROBACIÓN
EMERGENCY PATH
EXIT PATH
```


Upgradeable no deberá significar:

**control administrativo ilimitado.**

## ARTÍCULO LXVII — INMUTABILIDAD SELECTIVA

No todo deberá ser mutable.

No todo deberá ser immutable.

La arquitectura deberá determinar explícitamente:

```text
INVARIANTES
ESTADO MUTABLE
ESTADO REVOCABLE
ESTADO EXPIRABLE
ESTADO HISTÓRICO
```


La inmutabilidad deberá utilizarse donde represente una garantía del dominio.

## ARTÍCULO LXVIII — EMERGENCIAS

Los mecanismos de emergencia deberán limitarse por:

- propósito;
- duración;
- autoridad;
- alcance;
- transparencia;
- auditoría.

Un pause() no deberá convertirse en mecanismo permanente de control central.

## ARTÍCULO LXIX — MODELO DE FALLA

Toda arquitectura deberá responder:

**¿Cómo falla el sistema?**

Deberán analizarse:

```text
CHAIN FAILURE
RPC FAILURE
INDEXER FAILURE
STORAGE FAILURE
ORACLE FAILURE
KEY LOSS
GOVERNANCE CAPTURE
SMART CONTRACT FAILURE
BRIDGE FAILURE
OPERATOR FAILURE
```


La resiliencia deberá diseñarse antes de producción.

## ARTÍCULO LXX — MODELO DE AMENAZA DE CONFIANZA

Además del threat model de seguridad deberá existir un:

**Modelo de Amenaza de Confianza.**

Deberá analizar:

- autoridad abusiva;
- colusión;
- falsa Attestation;
- Observador Autorizado comprometido;
- captura de governance;
- censura;
- pérdida de soberanía;
- concentración progresiva;
- dependencia operacional.


## ARTÍCULO LXXI — NO CONFUNDIR DESCENTRALIZACIÓN CON AUSENCIA DE GOBIERNO

Un protocolo descentralizado puede requerir:

- normas;
- autoridades;
- responsabilidades;
- mecanismos de disputa;
- gobernanza;
- supervisión legítima.

Descentralización significa distribuir autoridad conforme al dominio.

No eliminar toda autoridad.

## ARTÍCULO LXXII — ARQUITECTURA PÚBLICO-PRIVADA

Cuando un dominio combine Estado, empresas y personas:

**ninguno deberá convertirse automáticamente en autoridad universal.**

La arquitectura deberá separar:

```text
REGULACIÓN
GOBERNANZA
PROPIEDAD
CUSTODIA
OPERACIÓN
VERIFICACIÓN
CONSENTIMIENTO
```


Esto permite modelos públicos y privados sostenibles sin sacrificar soberanía.

## ARTÍCULO LXXIII — MODELO DE INCENTIVOS

Cuando exista necesidad de incentivar:

- validación;
- almacenamiento;
- disponibilidad;
- participación;
- seguridad;
- observación;
- coordinación;

la arquitectura deberá modelar incentivos explícitamente.

No deberá suponerse que un token es la solución automática.

## ARTÍCULO LXXIV — SOSTENIBILIDAD

La descentralización deberá ser operacionalmente sostenible.

Toda arquitectura deberá considerar:

- quién opera infraestructura;
- quién paga;
- quién mantiene;
- quién actualiza;
- qué incentivos existen;
- qué ocurre si desaparecen subsidios iniciales.

Un sistema técnicamente descentralizado pero económicamente inviable no constituye arquitectura sostenible.

## ARTÍCULO LXXV — REGLA PARA AGENTES DE INTELIGENCIA ARTIFICIAL

Todo agente gobernado por L1 deberá razonar en este orden:

```text
1. Comprender dominio
2. Identificar actores
3. Construir modelo de confianza
4. Determinar autoridad
5. Identificar Observadores Autorizados
6. Modelar Claims
7. Modelar Attestations
8. Determinar Proofs
9. Modelar propiedad
10. Modelar consentimiento
11. Determinar privacidad
12. Derivar soberanía
13. Clasificar estado
14. Diseñar protocolo
15. Derivar arquitectura
16. Evaluar infraestructura
17. Seleccionar tecnologías
18. Diseñar implementación
```


## ARTÍCULO LXXVI — CONFLICTO ARQUITECTÓNICO

Cuando una solicitud contradiga L0 o L1, el agente deberá responder:

```text
CONFLICTO ARQUITECTÓNICO WEB3 TRUST-NATIVE
Regla afectada:
Solicitud conflictiva:
Dependencia de confianza introducida:
Impacto sobre soberanía:
Alternativa propuesta:
Trade-offs:
¿Requiere excepción humana?: Sí / No
```


El agente no deberá ignorar silenciosamente el conflicto.

## ARTÍCULO LXXVII — PROHIBICIÓN DE DEFAULTS WEB2

Un agente no deberá introducir automáticamente:

```text
PostgreSQL
MySQL
MongoDB
Firebase
Supabase
Redis
REST API
GraphQL
central auth
admin dashboard
```


simplemente porque formen parte de patrones habituales.

Cada componente deberá justificar su existencia.

Esto no significa que estén prohibidos.

Significa:

**No Default Authority.**

## ARTÍCULO LXXVIII — SALIDA ESPERADA DEL RAZONAMIENTO ARQUITECTÓNICO

Antes de producir código, el agente deberá ser capaz de entregar:

```text
1. Resumen del dominio
2. Modelo de Actores
3. Grafo de Confianza
4. Matriz de Autoridad
5. Modelo de Observadores Autorizados
6. Catálogo de Claims
7. Catálogo de Attestations
8. Catálogo de Proofs
9. Matriz de Estado
10. Modelo de Propiedad
11. Modelo de Consentimiento
12. Modelo de Privacidad
13. Matriz de Soberanía
14. Modelo de Gobernanza
15. Nivel de Soberanía S0–S3
16. Arquitectura propuesta
17. Dependencias
18. Deuda de Soberanía
19. Excepciones
20. Infraestructura candidata
21. Justificación tecnológica
22. Estrategia de salida
```


## ARTÍCULO LXXIX — PRINCIPIO DE ARQUITECTURA DEMOSTRABLE

Una arquitectura Web3 Trust-Native no deberá defenderse diciendo:

“Está descentralizada.”

Deberá poder demostrar:

```text
QUÉ está descentralizado
POR QUÉ debe estar descentralizado
ENTRE QUIÉNES se distribuye autoridad
QUÉ permanece centralizado
POR QUÉ puede permanecer centralizado
QUÉ dependencias existen
CÓMO pueden eliminarse
QUÉ ocurre si el operador desaparece
```


## ARTÍCULO LXXX — REGLA DE CIERRE

Toda arquitectura deberá poder trazarse hacia atrás:

```text
TECNOLOGÍA
↑
INFRAESTRUCTURA
↑
ARQUITECTURA
↑
SOBERANÍA
↑
CONFIANZA
↑
DOMINIO
```


Si una tecnología no puede trazarse hasta un requerimiento legítimo del dominio:

**deberá considerarse accidental, innecesaria o pendiente de justificación.**

La arquitectura correcta no comienza preguntando:

**“¿Qué blockchain utilizaremos?”**

Comienza preguntando:

**“¿Qué relaciones de confianza debemos transformar en relaciones verificables y qué soberanía debemos preservar?”**


## DECLARACIÓN ARQUITECTÓNICA FINAL

L1 — Reglas de Arquitectura Web3 Trust-Native transforma la Constitución en un sistema normativo de decisión.

Su propósito no consiste en producir arquitecturas idénticas.

Su propósito consiste en garantizar que arquitecturas diferentes deriven correctamente de sus respectivos dominios.

Por ello:

```text
HealthProof
≠
Music On Chain
≠
CertProof
≠
Future Futbol
≠
TIM
```


aunque todos puedan compartir:

```text
TRUST-NATIVE PRINCIPLES
+
VERIFIABLE RELATIONSHIPS
+
SOVEREIGNTY DERIVATION
+
PROTOCOL-FIRST ARCHITECTURE
```


HealthProof podrá derivar hacia S3.

Music On Chain podrá derivar hacia S1.

CertProof podrá derivar hacia S1 o S2.

Future Futbol podrá derivar hacia S1 o S2.

TIM podrá evolucionar conforme sus requerimientos institucionales e industriales determinen su soberanía.

Estas conclusiones no deberán imponerse.

Deberán ser:

**derivadas, justificadas y demostrables.**

Por tanto, la regla arquitectónica fundamental de Web3 Trust-Native será:

**La Confianza determina la Soberanía.**

**La Soberanía condiciona la Arquitectura.**

**La Arquitectura selecciona la Infraestructura.**

Y la infraestructura:

**nunca deberá redefinir el dominio que debía servir.**

## VERSIONADO

Esta versión queda establecida como:

**L1 — Reglas de Arquitectura Web3 Trust-Native v0.1**

### CORRECCIÓN

v0.1.x

Aclaraciones sin modificación del modelo arquitectónico.

### EVOLUCIÓN MENOR

v0.x

Nuevas reglas compatibles.

### EVOLUCIÓN MAYOR

v1.x+

Modificaciones de principios arquitectónicos fundamentales.

Toda evolución deberá mantener compatibilidad con L0 o declarar explícitamente el conflicto constitucional.

## RELACIÓN CON LOS SIGUIENTES NIVELES

```text
L0 — CONSTITUCIÓN
│
▼
L1 — REGLAS DE ARQUITECTURA
│
▼
L2 — REGLAS DE PROTOCOLO
│
▼
L3 — CANON DE DOMINIO
│
▼
L4 — SMART CONTRACTS
│
▼
L5 — SEGURIDAD Y PRIVACIDAD
│
▼
L6 — INFRAESTRUCTURA
│
▼
L7 — APLICACIÓN Y EXPERIENCIA DE USUARIO
│
▼
L8 — AGENTES DE INTELIGENCIA ARTIFICIAL Y CURSOR
```


L1 determina **cómo pensar la arquitectura**.

L2 deberá determinar **cómo convertir esa arquitectura en reglas de protocolo**.

L3 deberá determinar **cómo especializar esas reglas para cada dominio**.

L4–L7 deberán determinar **cómo implementarlas**.

L8 deberá garantizar que los agentes de inteligencia artificial respeten toda la jerarquía.

## FIN — L1 REGLAS DE ARQUITECTURA WEB3 TRUST-NATIVE v0.1

