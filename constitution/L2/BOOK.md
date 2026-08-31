# L2 — Reglas de Protocolo Web3 Trust-Native

> **Libro:** L2  
> **Versión vigente (repositorio):** 0.1.0  
> **Estado vigente (repositorio):** Draft  
> **Fuente histórica:** `original/L2-001-Reglas-de-Protocolo.docx`  
> **Bloque materializado:** B0–B14 (front-matter histórico, preámbulo, artículos I–C, declaración final, principio canónico, relación con la jerarquía, regla lingüística, versionado histórico, estado canónico y `FIN`)  
> **Estado de migración:** `human-reviewed` — DOCX completamente materializado en BOOK  
> **Autoridad efectiva (CDR-001):** `BOOK.md` es el path canónico previsto (`source.official`); fidelidad de la materialización B0–B14 aceptada por revisión humana. Este archivo **no** es Official y **no** es Published  
> **Regla:** nunca conversión automática DOCX → Markdown  
> **Separación versión/estado:** los valores históricos del DOCX (`Versión 0.1`, `Versión canónica inicial`) se preservan abajo como contexto histórico y **no** sustituyen el estado vigente `0.1.0` / Draft

---

## Front-matter histórico (DOCX)

### Versión 0.1 — Especificación Normativa para el Diseño de Protocolos Verificables

| Campo histórico | Valor histórico (DOCX) |
|-----------------|------------------------|
| Versión | 0.1 |
| Estado | Versión canónica inicial |
| Nivel | L2 — Reglas de Protocolo |
| Idioma canónico prioritario | Español |
| Dependencias normativas | L0 — Constitución Web3 Trust-Native v0.1; L1 — Reglas de Arquitectura Web3 Trust-Native v0.1 |
| Ámbito | Protocolos Web3 Trust-Native y su especialización posterior por dominio |
| Precedencia | Inferior a L0 y L1; superior a L3–L8 |

---

## PREÁMBULO

L0 establece los principios que deben preservarse.

L1 establece cómo debe razonarse y derivarse una arquitectura.

L2 establece:

cómo transformar relaciones humanas, institucionales, económicas y digitales en un protocolo verificable.

Un protocolo Web3 Trust-Native no es simplemente un conjunto de smart contracts.

No es una API descentralizada.

No es una colección de tokens.

No es una base de datos trasladada a blockchain.

No es una aplicación tradicional que utiliza una wallet.

Un protocolo Web3 Trust-Native es:

un sistema formal de Actores, Autoridades, Capacidades, Relaciones, Afirmaciones, Atestaciones, Pruebas, Consentimientos, Delegaciones, Estados y Transiciones que permite representar confianza verificable sin depender innecesariamente de una autoridad central.

La gramática protocolaria fundamental será:

```text
ACTOR
  ↓
AUTORIDAD
  ↓
CAPACIDAD
  ↓
ACCIÓN
  ↓
AFIRMACIÓN
  ↓
ATESTACIÓN
  ↓
PRUEBA
  ↓
TRANSICIÓN DE ESTADO
  ↓
ESTADO VERIFICABLE
```

No todo flujo requerirá necesariamente todos estos elementos.

Sin embargo, toda transición protocolaria relevante deberá poder responder:

Quién actuó, con qué autoridad, mediante qué capacidad, sobre qué recurso, dentro de qué contexto, sustentado por qué evidencia, y qué consecuencia verificable produjo.

---

> **Límite B0.** La materialización de este archivo termina aquí. `ARTÍCULO I` … `ARTÍCULO C` y los bloques posteriores al artículo C permanecen en `original/L2-001-Reglas-de-Protocolo.docx`.

## ARTÍCULO I — MANDATO DEL PROTOCOLO

Todo protocolo deberá convertir las relaciones fundamentales del dominio en reglas verificables.

Deberá determinar como mínimo:

```text
QUIÉN
PUEDE HACER QUÉ
SOBRE QUÉ
CON QUÉ AUTORIDAD
MEDIANTE QUÉ CAPACIDAD
EN QUÉ CONTEXTO
CON QUÉ EVIDENCIA
BAJO QUÉ CONDICIONES
CON QUÉ CONSECUENCIA
```

Estas reglas deberán pertenecer conceptualmente al protocolo.

La aplicación no deberá convertirse en su fuente de autoridad.

## ARTÍCULO II — PROTOCOLO NO ES IMPLEMENTACIÓN

Deberá preservarse:

```text
DOMINIO
   ↓
PROTOCOLO
   ↓
ARQUITECTURA
   ↓
IMPLEMENTACIÓN DEL PROTOCOLO
   ↓
SMART CONTRACTS / COMPONENTES
   ↓
CLIENTES Y APLICACIONES
```

El protocolo define significado, reglas e invariantes.

Los smart contracts constituyen una posible implementación ejecutable.

Por tanto:

**PROTOCOLO ≠ SMART CONTRACT**

El protocolo deberá poder sobrevivir conceptualmente a una evolución tecnológica de su implementación.

## ARTÍCULO III — VOCABULARIO PROTOCOLARIO FUNDAMENTAL

Todo protocolo deberá evaluar explícitamente las siguientes primitivas conceptuales:

```text
Actor
Identidad
Autoridad
Capacidad
Recurso
Relación
Afirmación
Atestación
Prueba
Evidencia
Consentimiento
Delegación
Revocación
Propiedad
Custodia
Procedencia
Estado
Evento
Gobernanza
```

No todas deberán convertirse en estructuras independientes.

Sin embargo:

ninguna primitiva relevante podrá desaparecer por conveniencia tecnológica.

## ARTÍCULO IV — ACTOR

Un Actor representa una entidad reconocible dentro del dominio y capaz de participar en relaciones protocolarias.

Conceptualmente:

```text
Actor {
    identificador
    referenciasDeIdentidad
    tipo
    estado
}
```

Un Actor podrá representar:

```text
PERSONA
ORGANIZACIÓN
INSTITUCIÓN
AUTORIDAD
DISPOSITIVO
PROTOCOLO
AGENTE AUTÓNOMO
```

Un Actor no deberá confundirse con la cuenta utilizada para operar.

**ACTOR ≠ WALLET ≠ ADDRESS**

## ARTÍCULO V — IDENTIDAD

La Identidad deberá permitir determinar:

qué entidad está actuando o siendo referenciada.

Podrá apoyarse, según el dominio, en:

- wallet;
- smart account;
- DID;
- Verifiable Credential;
- claves criptográficas;
- identidad institucional;
- mecanismos de identidad delegada.

La identidad protocolaria deberá diferenciarse de autenticación, autorización y dirección blockchain.

## ARTÍCULO VI — CONTINUIDAD DE IDENTIDAD

Cuando el dominio lo requiera, la identidad deberá poder sobrevivir a:

- rotación de claves;
- cambio de wallet;
- recuperación;
- sustitución de proveedor;
- actualización tecnológica.

La pérdida de una cuenta no deberá implicar necesariamente la desaparición de la identidad soberana.

## ARTÍCULO VII — AUTORIDAD

Autoridad representa la legitimidad de un Actor para realizar determinada acción dentro de un contexto.

Conceptualmente:

```text
Autoridad {
    actor
    capacidad
    recurso
    contexto
    alcance
    válidaDesde
    válidaHasta
    revocable
}
```

La autoridad no deberá inferirse únicamente desde:

msg.sender

La pregunta protocolaria será:

**¿Por qué msg.sender posee autoridad para realizar esta acción?**

## ARTÍCULO VIII — ORIGEN DE LA AUTORIDAD

Toda Autoridad deberá derivarse de una fuente verificable.

Podrá provenir de:

```text
PROPIEDAD
ATESTACIÓN
CREDENCIAL
CONSENTIMIENTO
DELEGACIÓN
GOBERNANZA
REGLA DEL PROTOCOLO
AUTORIDAD INSTITUCIONAL
AUTORIDAD LEGAL O REGULATORIA
```

No deberá existir autoridad protocolaria sin procedencia identificable.

## ARTÍCULO IX — AUTORIDAD CONTEXTUAL

La Autoridad deberá estar delimitada.

Conceptualmente:

```text
Autoridad =
f(
    Actor,
    Capacidad,
    Recurso,
    Contexto,
    Propósito,
    Alcance,
    Tiempo,
    Jurisdicción
)
```

```text
Autoridad en un contexto:
≠

autoridad universal.
```

## ARTÍCULO X — CAPACIDAD

Una Capacidad representa una acción específica que un Actor está legitimado para realizar.

Ejemplos:

```text
PUEDE_CREAR
PUEDE_EMITIR
PUEDE_ATESTAR
PUEDE_VERIFICAR
PUEDE_LEER
PUEDE_INCORPORAR
PUEDE_TRANSFERIR
PUEDE_DELEGAR
PUEDE_REVOCAR
PUEDE_LICENCIAR
PUEDE_CERTIFICAR
PUEDE_GOBERNAR
```

Las capacidades deberán expresar semántica de dominio.

Deberá evitarse una abstracción como:

ADMINISTRADOR

cuando pueda expresarse con precisión:

PUEDE_ATESTAR_AFIRMACIÓN_CLÍNICA

o:

PUEDE_CERTIFICAR_CAPACIDAD_MINERA

## ARTÍCULO XI — PRINCIPIO DE MÍNIMA CAPACIDAD

Todo Actor deberá recibir únicamente las capacidades necesarias.

```text
CAPACIDAD OTORGADA
        ≤
CAPACIDAD NECESARIA
```

Una capacidad específica deberá preferirse a una autoridad general cuando ambas puedan satisfacer el requerimiento.

## ARTÍCULO XII — RECURSO

Un Recurso representa un objeto del dominio sobre el cual pueden existir derechos, relaciones, autoridad o acciones.

Ejemplos:

```text
Ficha Clínica
Obra Creativa
Credencial
Certificación
Partido
Perfil Deportivo
Capacidad Minera
Consentimiento
Licencia
Atestación
```

Los Recursos deberán poseer semántica propia del dominio.

## ARTÍCULO XIII — IDENTIDAD DEL RECURSO

Todo Recurso protocolariamente relevante deberá poseer una identidad estable.

Su identidad no deberá depender necesariamente de:

- una URL;
- una clave primaria SQL;
- un nombre de archivo;
- una ruta del frontend;
- un proveedor específico.

El identificador deberá permitir reconocer el Recurso a través del tiempo y de implementaciones compatibles cuando el dominio lo requiera.

## ARTÍCULO XIV — RELACIÓN

Una Relación expresa un vínculo semántico entre Actores, Recursos u otras entidades protocolarias.

Ejemplos:

```text
Actor ──POSEE──────────> Recurso

Actor ──EMITE──────────> Afirmación

Actor ──ATESTA─────────> Afirmación

Actor ──AUTORIZA───────> Actor

Actor ──DELEGA─────────> Capacidad

Artista ──CREA─────────> Obra

Liga ──ORGANIZA────────> Partido

Médico ──ATIENDE───────> Paciente

Trabajador ──POSEE─────> Capacidad
```

Una relación relevante constituye información protocolaria.

## ARTÍCULO XV — SEMÁNTICA DE LA RELACIÓN

Toda Relación deberá poder expresar:

```text
ORIGEN
PREDICADO
DESTINO
AUTORIDAD
CONTEXTO
VIGENCIA
PROCEDENCIA
```

Conceptualmente:

```text
Relación =
(origen, predicado, destino, contexto)
```

Deberá favorecerse precisión semántica sobre relaciones genéricas.

## ARTÍCULO XVI — AFIRMACIÓN

Una Afirmación es una declaración atribuible realizada por un Actor respecto de un sujeto, recurso, propiedad o hecho.

Conceptualmente:

```text
Afirmación {
    identificador
    emisor
    sujeto
    predicado
    objeto
    contexto
    evidencia
    emitidaEn
}
```

El protocolo deberá diferenciar:

```text
existencia de una Afirmación
de:
validez de una Afirmación.
```

## ARTÍCULO XVII — AFIRMACIÓN NO ES VERDAD

La existencia de:

```text
AFIRMACIÓN(X)

no implica:
VERDAD(X)

Implica:
ACTOR A AFIRMA X
```

Ésta constituye una regla fundamental.

Blockchain puede demostrar que una afirmación fue realizada.

No puede determinar automáticamente que la afirmación corresponde a la realidad física.

## ARTÍCULO XVIII — SUJETO DE LA AFIRMACIÓN

Toda Afirmación deberá identificar su sujeto cuando corresponda.

Ejemplos:

```text
Afirmación sobre Paciente
Afirmación sobre Artista
Afirmación sobre Obra
Afirmación sobre Trabajador
Afirmación sobre Partido
Afirmación sobre Credencial
```

El emisor de una Afirmación no deberá confundirse con su sujeto.

## ARTÍCULO XIX — EMISOR DE LA AFIRMACIÓN

Toda Afirmación deberá ser atribuible a un emisor.

Cuando corresponda deberá poder demostrarse:

```text
EMISOR
+
AUTORIDAD
+
FIRMA
+
CONTEXTO
```

La procedencia forma parte de la semántica de la Afirmación.

## ARTÍCULO XX — EVIDENCIA

Una Afirmación podrá referenciar Evidencia.

La Evidencia podrá provenir de:

```text
DOCUMENTO
FIRMA
HASH
SENSOR
REGISTRO EXTERNO
VERIFIABLE CREDENTIAL
PRUEBA PREVIA
EVENTO DEL PROTOCOLO
ATESTACIÓN
```

La existencia de Evidencia no convierte automáticamente una Afirmación en verdad.

## ARTÍCULO XXI — OBSERVADOR AUTORIZADO

Cuando una Afirmación se origine en el mundo físico o institucional deberá determinarse si existe un Observador Autorizado.

Un Observador Autorizado es:

un Actor cuya autoridad para observar, declarar o certificar determinado hecho puede ser verificada dentro del contexto correspondiente.

Deberá poder identificarse:

```text
IDENTIDAD
AUTORIDAD
ALCANCE
CONTEXTO
VIGENCIA
MÉTODO DE VERIFICACIÓN
REVOCACIÓN
```

## ARTÍCULO XXII — FRONTERA ENTRE REALIDAD Y PROTOCOLO

Los hechos externos deberán atravesar conceptualmente:

```text
REALIDAD
   ↓
OBSERVADOR AUTORIZADO
   ↓
AFIRMACIÓN
   ↓
ATESTACIÓN
   ↓
PRUEBA
   ↓
ESTADO DEL PROTOCOLO
```

El protocolo no deberá ocultar esta frontera.

## ARTÍCULO XXIII — ATESTACIÓN

Una Atestación constituye respaldo verificable de una Afirmación.

Conceptualmente:

```text
Atestación {
    identificador
    atestador
    afirmación
    autoridad
    contexto
    emitidaEn
    expiraEn
    estado
}
```

Una Atestación deberá ser atribuible a un Actor identificable.

## ARTÍCULO XXIV — ATESTADOR

El Atestador deberá poseer Autoridad verificable para respaldar la Afirmación.

Por tanto:

```text
ATESTACIÓN VÁLIDA
        ⇔
ATESTADOR AUTORIZADO

dentro del contexto correspondiente.
```

## ARTÍCULO XXV — ATESTACIÓN CONTEXTUAL

Toda Atestación deberá interpretarse dentro de su contexto.

Por ejemplo:

```text
HOSPITAL
   ↓ ATESTA
MÉDICO
   ↓ PARA
PRÁCTICA CLÍNICA

no implica:
MÉDICO
   ↓ AUTORIZADO PARA
CERTIFICACIÓN MINERA
```

La autoridad no deberá propagarse fuera de su dominio legítimo.

## ARTÍCULO XXVI — CADENA DE ATESTACIONES

Cuando el dominio lo requiera podrán existir cadenas verificables:

```text
AUTORIDAD
   ↓
INSTITUCIÓN
   ↓
PROFESIONAL
   ↓
AFIRMACIÓN
```

Cada nivel deberá poder demostrar la autoridad que posee y, cuando corresponda, la autoridad que delega o atesta.

## ARTÍCULO XXVII — RUTA DE CONFIANZA

Se denominará Ruta de Confianza a una cadena verificable mediante la cual puede establecerse la procedencia de determinada autoridad.

Conceptualmente:

```text
AUTORIDAD RAÍZ
      ↓
AUTORIDAD DELEGADA
      ↓
ACTOR AUTORIZADO
      ↓
AFIRMACIÓN
      ↓
ATESTACIÓN
      ↓
PRUEBA
```

El protocolo deberá poder evaluar la Ruta de Confianza cuando ésta sea necesaria para determinar legitimidad.

## ARTÍCULO XXVIII — PRUEBA

Una Prueba constituye evidencia verificable de una propiedad o afirmación.

Podrá demostrar, entre otras:

```text
POSEE_CAPACIDAD
POSEE_RECURSO
POSEE_CREDENCIAL_VÁLIDA
ESTÁ_AUTORIZADO
POSEE_CONSENTIMIENTO
CREÓ_OBRA
PARTICIPÓ_EN_EVENTO
```

Una Prueba deberá poder ser evaluada mediante un mecanismo de verificación definido.

## ARTÍCULO XXIX — PRUEBA Y VERIFICADOR

Toda Prueba deberá definir:

```text
QUÉ DEMUESTRA
SOBRE QUÉ SUJETO
MEDIANTE QUÉ EVIDENCIA
CÓMO SE VERIFICA
BAJO QUÉ CONTEXTO
CUÁNDO ES VÁLIDA
```

El Verificador no deberá depender necesariamente de confiar en:

- la aplicación;
- el backend;
- la empresa creadora;
- una base de datos privada.

El ideal protocolario será:

```text
VERIFICAR(PRUEBA)

en lugar de:
CONFIAR(BASE_DE_DATOS_DE_LA_EMPRESA)
```

## ARTÍCULO XXX — MINIMIZACIÓN DE PRUEBA

Una Prueba deberá revelar únicamente la información necesaria cuando el dominio y la tecnología lo permitan.

Preferir:

```text
PRUEBA(condición == verdadera)
```

sobre la revelación del conjunto completo de información utilizado para producirla.

Cuando corresponda podrán evaluarse Zero-Knowledge Proofs, divulgación selectiva u otros mecanismos criptográficos.

## ARTÍCULO XXXI — COMPOSICIÓN DE PRUEBAS

Las Pruebas podrán componerse cuando el dominio lo permita.

```text
PRUEBA DE IDENTIDAD
        +
PRUEBA DE CREDENCIAL
        +
PRUEBA DE AUTORIDAD
        ↓
PRUEBA DE CAPACIDAD PROFESIONAL
```

La composición deberá respetar propósito, privacidad, vigencia y contexto.

## ARTÍCULO XXXII — CONSENTIMIENTO

El Consentimiento constituye autorización otorgada por un Actor legitimado.

Conceptualmente:

```text
Consentimiento {
    otorgante
    receptor
    recurso
    capacidad
    propósito
    alcance
    emitidoEn
    expiraEn
    estado
}
```

El Consentimiento deberá ser verificable cuando determine derechos protocolarios.

## ARTÍCULO XXXIII — CONSENTIMIENTO LIMITADO

Consentir una acción no deberá implicar consentimiento universal.

```text
CONSENTIMIENTO(A)
≠
CONSENTIMIENTO(TODO)
```

El Consentimiento deberá poder limitarse por:

```text
RECURSO
PROPÓSITO
CAPACIDAD
ALCANCE
TIEMPO
CONTEXTO
```

## ARTÍCULO XXXIV — DELEGACIÓN

La Delegación representa transferencia limitada de una Capacidad.

```text
ACTOR A
   │
   └── DELEGA
          ↓
      CAPACIDAD
          ↓
       ACTOR B
```

Delegar una Capacidad:

```text
≠

transferir Propiedad.
```

## ARTÍCULO XXXV — REDELEGACIÓN

Toda Delegación deberá establecer si permite una delegación posterior.

```text
PUEDE_REDELEGAR = SÍ / NO
```

La redelegación no deberá asumirse por defecto.

## ARTÍCULO XXXVI — REVOCACIÓN

Toda relación revocable deberá poseer un mecanismo explícito.

Podrán ser revocables según el dominio:

```text
CAPACIDAD
CONSENTIMIENTO
DELEGACIÓN
CREDENCIAL
ATESTACIÓN
AUTORIZACIÓN
```

La Revocación deberá producir un estado verificable.

## ARTÍCULO XXXVII — REVOCACIÓN NO ES BORRADO

Deberá preservarse:

```text
REVOCADO
≠
NUNCA EXISTIÓ
```

Cuando corresponda, el protocolo deberá conservar la existencia histórica de una relación mientras modifica su vigencia actual.

Esto permite:

```text
HISTORIA INMUTABLE
+
VIGENCIA MUTABLE
```

sin confundir ambas propiedades.

## ARTÍCULO XXXVIII — PROPIEDAD

Propiedad representa control legítimo sobre un Recurso.

No deberá inferirse automáticamente desde:

```text
CREADOR
EMISOR
CUSTODIO
OPERADOR
PROPIETARIO DE BASE DE DATOS
CREADOR DEL PROTOCOLO
```

La Propiedad deberá definirse según la semántica del dominio.

## ARTÍCULO XXXIX — CUSTODIA

Custodia y Propiedad deberán mantenerse separadas.

**CUSTODIA ≠ PROPIEDAD**

Un Actor podrá custodiar un Recurso sin ser su propietario.

Una institución podrá mantener información sin adquirir soberanía sobre ella.

## ARTÍCULO XL — PROCEDENCIA

Todo Recurso o afirmación relevante deberá poder preservar su procedencia cuando ésta constituya una garantía del dominio.

Conceptualmente:

```text
ORIGEN
  ↓
CREACIÓN
  ↓
AFIRMACIONES
  ↓
ATESTACIONES
  ↓
TRANSFORMACIONES
  ↓
ESTADO ACTUAL
```

La procedencia deberá permitir responder:

**¿De dónde proviene aquello que estoy verificando?**

## ARTÍCULO XLI — ESTADO

Estado representa aquello que el protocolo considera vigente en un momento determinado.

Todo Estado deberá derivarse de transiciones válidas.

```text
ESTADO(n)
   +
TRANSICIÓN VÁLIDA
      ↓
ESTADO(n+1)
```

## ARTÍCULO XLII — TRANSICIÓN DE ESTADO

Toda Transición de Estado relevante deberá satisfacer:

```text
TRANSICIÓN VÁLIDA
        ⇔
ACTOR VÁLIDO
+
AUTORIDAD VÁLIDA
+
CAPACIDAD VÁLIDA
+
ENTRADA VÁLIDA
+
CONTEXTO VÁLIDO
+
REGLAS DEL PROTOCOLO
```

La transición deberá ser explicable independientemente de su implementación.

## ARTÍCULO XLIII — PRECONDICIONES

Toda transición deberá definir las condiciones necesarias para ejecutarse.

Ejemplo:

```text
EMITIR_ATESTACIÓN

requiere:

- Actor existente
- Capacidad vigente
- Afirmación existente
- Autoridad vigente
- Contexto válido
```

Las precondiciones deberán derivarse del protocolo.

## ARTÍCULO XLIV — POSTCONDICIONES

Toda transición deberá definir sus consecuencias.

Ejemplo:

```text
REVOCAR_ATESTACIÓN
        ↓
ESTADO = REVOCADA
        +
EVENTO_DE_REVOCACIÓN
```

Una transición deberá dejar consecuencias determinables.

## ARTÍCULO XLV — INVARIANTES

Todo protocolo deberá identificar sus Invariantes.

Un Invariante es una condición que nunca deberá romperse mientras el protocolo sea válido.

Ejemplos:

Ningún Actor sin autoridad puede emitir una Atestación.

Ninguna Propiedad puede transferirse sin autoridad válida.

Una Capacidad revocada no puede autorizar acciones futuras.

Un Consentimiento expirado no concede acceso.

Una Atestación no puede otorgar más autoridad que la que posee su emisor.

Los Invariantes deberán existir antes del diseño de smart contracts.

## ARTÍCULO XLVI — EVENTO

Toda transición relevante deberá considerar la generación de un Evento protocolario.

Conceptualmente:

```text
Evento {
    actor
    acción
    recurso
    contexto
    tiempo
}
```

Los Eventos deberán facilitar, cuando corresponda:

- auditoría;
- reconstrucción;
- trazabilidad;
- indexación;
- interoperabilidad.

## ARTÍCULO XLVII — HISTORIA VERIFICABLE

La historia protocolaria deberá derivarse de:

```text
ESTADO
+
EVENTOS
+
PRUEBAS
```

y, cuando corresponda:

```text
+
ARTEFACTOS VERIFICABLES
```

La historia fundamental no deberá depender exclusivamente de registros privados del operador.

## ARTÍCULO XLVIII — MÁQUINA DE ESTADOS

Cuando corresponda, un Recurso deberá modelarse mediante una máquina de estados.

Ejemplo:

```text
CREADA
  ↓
EMITIDA
  ↓
VIGENTE
  ↓
REVOCADA
```

o:

```text
BORRADOR
   ↓
AFIRMADA
   ↓
ATESTADA
   ↓
VERIFICADA
   ↓
EXPIRADA
```

Los estados deberán poseer significado de dominio.

## ARTÍCULO XLIX — TRANSICIONES PERMITIDAS

Toda máquina de estados deberá definir:

```text
DESDE
ACCIÓN
ACTOR
AUTORIDAD
CAPACIDAD
PRECONDICIONES
HACIA
EVENTO
```

No deberá permitirse una transición simplemente porque técnicamente pueda programarse.

## ARTÍCULO L — ESTADOS TERMINALES

Los estados terminales deberán declararse.

Ejemplos:

```text
REVOCADO
CANCELADO
QUEMADO
ARCHIVADO
```

Cuando puedan revertirse deberá definirse explícitamente quién posee autoridad para hacerlo.

## ARTÍCULO LI — TEMPORALIDAD

El protocolo deberá diferenciar, cuando corresponda:

```text
emitidoEn
válidoDesde
vigenteHasta
expiraEn
revocadoEn
efectivoDesde
```

Estos conceptos no deberán utilizarse como equivalentes.

## ARTÍCULO LII — CONFIANZA TEMPORAL

La confianza puede variar con el tiempo.

```text
VÁLIDO EN t1
≠
VÁLIDO EN t2
```

Autoridades, Capacidades, Atestaciones, Credenciales, Consentimientos y Delegaciones podrán poseer vigencia temporal.

## ARTÍCULO LIII — CONTRADICCIÓN

El protocolo deberá admitir que pueden existir Afirmaciones contradictorias.

```text
AFIRMACIÓN A
      ↘
    CONFLICTO
      ↗
AFIRMACIÓN B
```

La existencia de blockchain no elimina desacuerdos del mundo real.

## ARTÍCULO LIV — DISPUTA

Cuando el dominio requiera resolver contradicciones deberá definirse un mecanismo de Disputa.

Podrá considerar:

- autoridad resolutoria;
- arbitraje;
- nueva evidencia;
- múltiples Atestaciones;
- gobernanza;
- resolución institucional;
- coexistencia de versiones.

El mecanismo deberá ser legítimo para el dominio.

## ARTÍCULO LV — EL PROTOCOLO NO ES JUEZ UNIVERSAL

Un protocolo no deberá inventar autoridad sobre hechos que no puede determinar.

Cuando exista una disputa humana, institucional, clínica, industrial o jurídica:

el protocolo deberá representar el mecanismo legítimo de resolución, no sustituirlo arbitrariamente.

## ARTÍCULO LVI — ACCIONES DE GOBERNANZA

Toda acción de Gobernanza deberá representarse como una acción protocolaria explícita.

Ejemplos:

```text
MODIFICAR_PARÁMETRO
INCORPORAR_AUTORIDAD
REVOCAR_AUTORIDAD
PAUSAR
ACTUALIZAR
MODIFICAR_REGLA
```

Cada acción deberá poseer autoridad, alcance y trazabilidad.

## ARTÍCULO LVII — PARÁMETROS E INVARIANTES

Deberá diferenciarse:

```text
PARÁMETRO MODIFICABLE
≠
INVARIANTE
```

La Gobernanza podrá modificar parámetros dentro de sus capacidades.

No deberá poder destruir silenciosamente garantías fundamentales del protocolo.

## ARTÍCULO LVIII — VERSIONADO DEL PROTOCOLO

Todo protocolo deberá poseer una versión identificable.

Una evolución deberá poder determinar:

```text
REGLAS ANTERIORES
REGLAS NUEVAS
AUTORIDAD DE CAMBIO
MIGRACIÓN
COMPATIBILIDAD
EFECTOS SOBRE DERECHOS EXISTENTES
```

## ARTÍCULO LIX — ACTUALIZACIONES

Toda actualización deberá evaluar su impacto sobre:

- Propiedad;
- derechos;
- Autoridad;
- Consentimiento;
- Atestaciones;
- Pruebas;
- Procedencia;
- historia;
- privacidad;
- soberanía.

Una actualización técnica no deberá convertirse en mecanismo de expropiación o apropiación protocolaria.

## ARTÍCULO LX — COMPOSICIÓN

Los protocolos deberán favorecer mecanismos verificables de composición.

Preferentemente mediante:

```text
PRUEBAS
ATESTACIONES
CAPACIDADES
CREDENCIALES
INTERFACES ESTANDARIZADAS
```

antes que dependencia absoluta de APIs privadas.

## ARTÍCULO LXI — CONFIANZA ENTRE PROTOCOLOS

Un protocolo podrá reconocer una Prueba proveniente de otro protocolo cuando pueda establecerse:

```text
PROTOCOLO ORIGEN RECONOCIDO
+
PRUEBA VÁLIDA
+
AUTORIDAD VÁLIDA
+
CONTEXTO COMPATIBLE
+
PROPÓSITO COMPATIBLE
```

La confianza entre protocolos deberá ser explícita y contextual.

## ARTÍCULO LXII — PORTABILIDAD DE CONFIANZA

Las relaciones verificables deberán aspirar a ser portables cuando el dominio lo permita.

Ejemplo conceptual:

```text
CERTPROOF
   │
   └── PRUEBA DE CAPACIDAD
             │
             ▼
            TIM
```

TIM podrá verificar una capacidad acreditada sin apropiarse del historial completo de CertProof.

Esto constituye:

Portabilidad de Confianza.

## ARTÍCULO LXIII — FRONTERA DEL DOMINIO

Todo protocolo deberá declarar:

```text
QUÉ CONOCE
QUÉ NO CONOCE
QUÉ CONTROLA
QUÉ NO CONTROLA
QUÉ PUEDE VERIFICAR
QUÉ NO PUEDE VERIFICAR
```

Un protocolo no deberá atribuirse autoridad sobre un dominio externo sin legitimidad.

## ARTÍCULO LXIV — DEPENDENCIAS EXTERNAS

Toda dependencia externa que pueda afectar una transición protocolaria deberá declararse.

Ejemplos:

```text
oracle
bridge
protocolo externo
registro institucional
proveedor de identidad
red externa
```

La dependencia deberá formar parte del Modelo de Confianza.

## ARTÍCULO LXV — FALLO DEL PROTOCOLO

El protocolo deberá definir comportamiento ante:

```text
PRUEBA INVÁLIDA
AUTORIDAD EXPIRADA
CAPACIDAD REVOCADA
ATESTACIÓN AUSENTE
ORACLE NO DISPONIBLE
AFIRMACIONES CONTRADICTORIAS
RECURSO NO DISPONIBLE
DEPENDENCIA EXTERNA NO DISPONIBLE
```

Los modos de fallo deberán estar especificados.

## ARTÍCULO LXVI — FALLO CERRADO Y FALLO ABIERTO

Para toda operación crítica deberá determinarse si el comportamiento esperado es:

```text
FALLO CERRADO
```

o:

```text
FALLO ABIERTO
```

En operaciones que afecten autoridad, propiedad, consentimiento, privacidad o derechos deberá favorecerse el fallo cerrado, salvo justificación explícita del dominio.

## ARTÍCULO LXVII — MINIMALISMO PROTOCOLARIO

El protocolo deberá contener aquello que requiera garantías protocolarias.

No deberá absorber innecesariamente:

- presentación;
- preferencias visuales;
- analítica;
- búsqueda;
- caché;
- recomendaciones;
- lógica exclusivamente de interfaz.

El protocolo no deberá convertirse en aplicación.

## ARTÍCULO LXVIII — MINIMALISMO SEMÁNTICO

La generalización no deberá destruir el significado del dominio.

Deberá evitarse:

```text
EntidadGenérica
AcciónGenérica
DatoGenérico
```

cuando puedan existir conceptos como:

```text
AfirmaciónClínica
ObraCreativa
CapacidadMinera
AtestaciónDeportiva
Credencial
```

El objetivo será:

reutilización semántica sin pérdida de significado.

## ARTÍCULO LXIX — NO EXISTE CONTRATO UNIVERSAL

Web3 Trust-Native no exige construir un smart contract universal para todos los dominios.

Podrá existir vocabulario compartido.

Pero:

```text
SEMÁNTICA COMPARTIDA
        ↓
PROTOCOLO DE DOMINIO
        ↓
IMPLEMENTACIÓN DE DOMINIO
```

Cada dominio deberá preservar sus reglas legítimas.

## ARTÍCULO LXX — MÓDULOS DEL PROTOCOLO

Cuando resulte apropiado, un protocolo podrá organizarse conceptualmente en módulos:

```text
IDENTIDAD
AUTORIDAD
AFIRMACIONES
ATESTACIONES
PRUEBAS
CONSENTIMIENTO
DELEGACIÓN
PROPIEDAD
GOBERNANZA
```

La modularidad deberá representar límites semánticos reales.

No deberá utilizarse como fragmentación artificial.

## ARTÍCULO LXXI — NÚCLEO DEL PROTOCOLO

Cuando múltiples módulos compartan reglas fundamentales podrá existir conceptualmente un Núcleo del Protocolo.

Su responsabilidad deberá limitarse a:

- invariantes fundamentales;
- coordinación;
- validaciones compartidas;
- referencias protocolarias esenciales.

No deberá convertirse en un God Contract.

## ARTÍCULO LXXII — PUERTA DE ACCESO AL PROTOCOLO

Podrá existir una capa de acceso al protocolo para simplificar la interacción de clientes y aplicaciones.

Esta capa:

- podrá construir operaciones;
- coordinar llamadas;
- abstraer complejidad;
- facilitar integración.

No deberá convertirse en autoridad central ni fuente exclusiva de verdad.

## ARTÍCULO LXXIII — TOKEN

Un token sólo deberá formar parte del protocolo cuando represente una función legítima.

Podrá representar:

```text
VALOR
DERECHO
ACCESO
INCENTIVO
GOBERNANZA
LIQUIDACIÓN
RECURSO
```

según el dominio.

La existencia de blockchain no constituye justificación suficiente para tokenizar.

## ARTÍCULO LXXIV — ACTIVOS NO TRANSFERIBLES

Cuando un activo represente:

- identidad;
- capacidad;
- credencial;
- reputación;
- mérito;
- participación personal;

deberá analizarse si permitir su transferencia destruye su significado.

Cuando corresponda podrá utilizarse un modelo Soulbound u otro mecanismo no transferible.

## ARTÍCULO LXXV — ECONOMÍA DEL PROTOCOLO

Cuando exista una economía protocolaria deberá responderse:

```text
QUIÉN PAGA
QUIÉN RECIBE
POR QUÉ
POR QUÉ SERVICIO
BAJO QUÉ REGLA
QUIÉN PUEDE MODIFICARLA
```

Los flujos económicos fundamentales deberán ser verificables.

## ARTÍCULO LXXVI — COMISIONES

Toda comisión protocolaria deberá poseer:

```text
PROPÓSITO
BENEFICIARIO
CÁLCULO
AUTORIDAD DE MODIFICACIÓN
LÍMITES
TRAZABILIDAD
```

Las comisiones no deberán quedar ocultas en infraestructura auxiliar cuando formen parte de la economía fundamental.

## ARTÍCULO LXXVII — INCENTIVOS

Los incentivos deberán alinearse con el comportamiento deseado.

El protocolo deberá analizar si algún Actor puede obtener beneficio mediante:

- Afirmaciones falsas;
- Atestaciones fraudulentas;
- censura;
- colusión;
- captura de Gobernanza;
- creación masiva de identidades;
- manipulación de Pruebas;
- retención de información.

La economía forma parte del modelo de confianza.

## ARTÍCULO LXXVIII — RESISTENCIA SYBIL

Cuando una regla dependa de personas o entidades únicas deberá analizarse el problema Sybil.

```text
1 WALLET
≠
1 PERSONA
```

La identidad criptográfica no deberá confundirse con unicidad humana.

## ARTÍCULO LXXIX — FRONTERA DE PRIVACIDAD

Todo protocolo deberá clasificar información según:

```text
PÚBLICA
VERIFICABLE
PRIVADA
CIFRADA
DIVULGABLE
NO DIVULGABLE
```

La información verificable no necesita ser necesariamente pública.

```text
VERIFICABILIDAD
≠
VISIBILIDAD UNIVERSAL
```

## ARTÍCULO LXXX — PRIVACIDAD DE METADATOS

La privacidad deberá considerar no sólo el contenido.

También deberá analizar:

- relaciones;
- frecuencia;
- timestamps;
- contrapartes;
- patrones de actividad;
- vínculos institucionales.

Los metadatos pueden revelar información sensible aun cuando el contenido esté cifrado.

## ARTÍCULO LXXXI — MINIMIZACIÓN DE DATOS

El protocolo deberá evitar capturar o conservar información que no necesite para proporcionar sus garantías.

Especialmente:

no deberá almacenarse información personal on-chain simplemente porque sea técnicamente posible.

## ARTÍCULO LXXXII — HASH NO ES PRIVACIDAD

Un hash de información sensible no garantiza privacidad.

La arquitectura y el protocolo deberán evaluar, cuando corresponda:

```text
salt
commitment
encryption
Zero-Knowledge Proof
selective disclosure
```

El hash deberá utilizarse según sus propiedades reales y no como sustituto genérico de privacidad.

## ARTÍCULO LXXXIII — PRUEBA DE NECESIDAD PROTOCOLARIA

Toda primitiva incorporada deberá responder:

**¿Qué garantía desaparece si eliminamos este elemento?**

Si la respuesta es:

ninguna,

el elemento podrá pertenecer a la aplicación o infraestructura y no necesariamente al protocolo.

## ARTÍCULO LXXXIV — PRUEBA DE AUTORIDAD

Para toda acción fundamental deberá responderse:

**¿Qué evidencia demuestra que este Actor posee autoridad para realizarla?**

Si la respuesta depende únicamente de:

- una fila privada;
- una variable del backend;
- un administrador;
- una lista cerrada controlada unilateralmente;

deberá revisarse el modelo de autoridad.

## ARTÍCULO LXXXV — PRUEBA DE INDEPENDENCIA DEL OPERADOR

Toda regla fundamental deberá evaluarse preguntando:

**¿Puede otro cliente verificar esta regla sin depender exclusivamente del operador original?**

Cuando la respuesta sea negativa deberá identificarse la dependencia de confianza introducida.

## ARTÍCULO LXXXVI — CATÁLOGO PROTOCOLARIO OBLIGATORIO

Antes del diseño de smart contracts deberá existir, según aplicabilidad:

```text
1. Catálogo de Actores
2. Catálogo de Identidades
3. Catálogo de Recursos
4. Catálogo de Relaciones
5. Catálogo de Autoridades
6. Catálogo de Capacidades
7. Catálogo de Observadores Autorizados
8. Catálogo de Afirmaciones
9. Catálogo de Evidencias
10. Catálogo de Atestaciones
11. Catálogo de Pruebas
12. Modelo de Consentimiento
13. Modelo de Delegación
14. Modelo de Revocación
15. Modelo de Propiedad
16. Modelo de Custodia
17. Modelo de Procedencia
18. Máquinas de Estado
19. Catálogo de Invariantes
20. Catálogo de Eventos
21. Acciones de Gobernanza
22. Rutas de Confianza
23. Dependencias Externas
24. Modelo de Fallo
25. Frontera de Privacidad
26. Modelo de Disputas
27. Modelo Económico, cuando corresponda
```

La ausencia de un catálogo aplicable deberá justificarse.

## ARTÍCULO LXXXVII — PUERTA DE APROBACIÓN DEL PROTOCOLO

Un protocolo sólo podrá declararse:

```text
PROTOCOLO WEB3 TRUST-NATIVE APTO
```

cuando pueda responder satisfactoriamente:

```text
[✓] ¿Quiénes son los Actores?
[✓] ¿Cómo se establece su Identidad?
[✓] ¿Qué Recursos existen?
[✓] ¿Qué Relaciones existen?
[✓] ¿Quién posee Autoridad?
[✓] ¿De dónde deriva esa Autoridad?
[✓] ¿Qué Capacidades existen?
[✓] ¿Quién puede otorgarlas?
[✓] ¿Quién puede revocarlas?
[✓] ¿Qué Afirmaciones pueden realizarse?
[✓] ¿Quién puede realizarlas?
[✓] ¿Qué Observadores Autorizados existen?
[✓] ¿Quién puede Atestar?
[✓] ¿Qué Pruebas pueden construirse?
[✓] ¿Qué requiere Consentimiento?
[✓] ¿Qué puede Delegarse?
[✓] ¿Qué puede Revocarse?
[✓] ¿Qué significa Propiedad?
[✓] ¿Qué significa Custodia?
[✓] ¿Cómo se preserva Procedencia?
[✓] ¿Cuáles son las máquinas de Estado?
[✓] ¿Cuáles son los Invariantes?
[✓] ¿Qué Eventos deben emitirse?
[✓] ¿Cómo funciona la Gobernanza?
[✓] ¿Cómo se resuelven Disputas?
[✓] ¿Cómo falla el protocolo?
[✓] ¿Qué información debe permanecer privada?
[✓] ¿Qué puede verificar un tercero independiente?
```

## ARTÍCULO LXXXVIII — ESTADOS DE MADUREZ DEL PROTOCOLO

Se establecen los siguientes estados:

```text
P0 — DESCUBRIMIENTO
El dominio todavía está siendo comprendido.
P1 — SEMÁNTICA
Actores, Recursos y Relaciones definidos.
P2 — AUTORIDAD
Autoridades, Capacidades, Consentimientos y Delegaciones definidos.
P3 — EVIDENCIA
Observadores Autorizados, Afirmaciones, Evidencias, Atestaciones y Pruebas definidos.
P4 — ESTADO
Máquinas de Estado, Transiciones, Eventos e Invariantes definidos.
P5 — GOBERNANZA Y RESILIENCIA
Gobernanza, actualizaciones, disputas, dependencias y fallos definidos.
P6 — PROTOCOLO APROBADO
Todas las puertas normativas aplicables han sido superadas.
```

## ARTÍCULO LXXXIX — PROHIBICIÓN DE SALTO A IMPLEMENTACIÓN

No deberá realizarse:

```text
P0
 ↓
SOLIDITY
```

como proceso normal de diseño.

La secuencia será:

```text
P0
 ↓
P1
 ↓
P2
 ↓
P3
 ↓
P4
 ↓
P5
 ↓
P6
 ↓
L4 — REGLAS DE SMART CONTRACTS
```

Podrán existir prototipos exploratorios.

No deberán confundirse con protocolo aprobado.

## ARTÍCULO XC — TRAZABILIDAD PROTOCOLARIA

Todo componente fundamental implementado deberá poder trazarse hacia su origen:

```text
CÓDIGO
  ↑
REGLA DEL SMART CONTRACT
  ↑
REGLA DEL PROTOCOLO
  ↑
AUTORIDAD / ESTADO / PRUEBA
  ↑
REQUERIMIENTO DE CONFIANZA
  ↑
DOMINIO
```

Código sin trazabilidad protocolaria deberá considerarse candidato a eliminación o revisión.

## ARTÍCULO XCI — CONFLICTO DE PROTOCOLO

Cuando una propuesta contradiga L0, L1 o L2 deberá declararse:

```text
CONFLICTO DE PROTOCOLO WEB3 TRUST-NATIVE

Regla afectada:
Propuesta conflictiva:
Dependencia introducida:
Impacto sobre confianza:
Impacto sobre autoridad:
Impacto sobre soberanía:
Alternativa propuesta:
Compromisos:
¿Requiere excepción humana?: SÍ / NO
```

El conflicto no deberá resolverse silenciosamente.

## ARTÍCULO XCII — REGLA PARA AGENTES DE INTELIGENCIA ARTIFICIAL

Antes de generar smart contracts, un agente deberá razonar:

```text
ACTORES
   ↓
IDENTIDADES
   ↓
RECURSOS
   ↓
RELACIONES
   ↓
AUTORIDADES
   ↓
CAPACIDADES
   ↓
OBSERVADORES AUTORIZADOS
   ↓
AFIRMACIONES
   ↓
ATESTACIONES
   ↓
PRUEBAS
   ↓
CONSENTIMIENTOS
   ↓
DELEGACIONES
   ↓
REVOCACIONES
   ↓
PROPIEDAD Y CUSTODIA
   ↓
MÁQUINAS DE ESTADO
   ↓
INVARIANTES
   ↓
EVENTOS
   ↓
GOBERNANZA
   ↓
DISEÑO DE SMART CONTRACTS
```

Si faltan elementos fundamentales, el agente deberá identificarlos antes de inventarlos.

## ARTÍCULO XCIII — PROHIBICIÓN DEL MODELO CRUD

No deberá traducirse automáticamente:

```text
CREATE
READ
UPDATE
DELETE
```

en funciones de smart contracts.

Las funciones deberán representar intención del dominio.

Ejemplos:

```text
emitirAfirmación()
atestarAfirmación()
otorgarConsentimiento()
delegarCapacidad()
revocarAtestación()
registrarObra()
certificarCapacidad()
transferirPropiedad()
```

El lenguaje del protocolo deberá expresar significado, no operaciones de base de datos.

## ARTÍCULO XCIV — LENGUAJE DEL PROTOCOLO

Toda regla deberá poder explicarse sin mostrar Solidity.

Primero deberá existir:

```text
REGLA
```

Luego:

```text
ESPECIFICACIÓN
```

Después:

```text
IMPLEMENTACIÓN
```

Si una regla sólo puede comprenderse observando código:

la especificación protocolaria todavía es insuficiente.

## ARTÍCULO XCV — REGLA DE SUFICIENCIA CRIPTOGRÁFICA

No toda información deberá almacenarse on-chain.

Sin embargo, toda afirmación crítica deberá poseer suficiente evidencia para determinar, cuando corresponda:

```text
ORIGEN
EMISOR
SUJETO
AUTORIDAD
INTEGRIDAD
VIGENCIA
PROCEDENCIA
REVOCACIÓN
CONSENTIMIENTO
```

El objetivo será:

verdad protocolaria criptográficamente suficiente, no almacenamiento indiscriminado.

## ARTÍCULO XCVI — GRAFO DE CONFIANZA PROTOCOLARIO

Cuando resulte apropiado, el protocolo deberá poder representarse como:

```text
G = (A, R, E)
```

donde:

```text
A = Actores
R = Relaciones verificables
E = Evidencias y Pruebas asociadas
```

Esto permite interpretar el protocolo no como una colección de registros, sino como:

un grafo verificable de relaciones de confianza.

## ARTÍCULO XCVII — GRAMÁTICA PROTOCOLARIA CANÓNICA

Web3 Trust-Native establece como gramática protocolaria de referencia:

```text
ACTOR
  ↓
AUTORIDAD
  ↓
CAPACIDAD
  ↓
ACCIÓN
  ↓
AFIRMACIÓN
  ↓
ATESTACIÓN
  ↓
PRUEBA
  ↓
TRANSICIÓN DE ESTADO
  ↓
ESTADO VERIFICABLE
```

Esta gramática no implica que toda acción requiera necesariamente una Afirmación o Atestación.

Establece las categorías mediante las cuales deberán razonarse las relaciones de confianza.

## ARTÍCULO XCVIII — GRAMÁTICA DE REALIDAD

Para hechos provenientes del mundo exterior se establece:

```text
REALIDAD
   ↓
OBSERVADOR AUTORIZADO
   ↓
AFIRMACIÓN
   ↓
EVIDENCIA
   ↓
ATESTACIÓN
   ↓
PRUEBA
   ↓
REGLA DEL PROTOCOLO
   ↓
TRANSICIÓN DE ESTADO
```

Esta cadena constituye la frontera formal entre:

```text
lo que ocurrió en el mundo
y
lo que el protocolo puede demostrar.
```

## ARTÍCULO XCIX — REGLA FUNDAMENTAL DE TRANSICIÓN

Toda transición fundamental deberá responder:

```text
¿QUIÉN?
   ↓
¿CON QUÉ IDENTIDAD?
   ↓
¿BAJO QUÉ AUTORIDAD?
   ↓
¿MEDIANTE QUÉ CAPACIDAD?
   ↓
¿SOBRE QUÉ RECURSO?
   ↓
¿EN QUÉ CONTEXTO?
   ↓
¿CON QUÉ EVIDENCIA?
   ↓
¿QUÉ REGLA LO PERMITE?
   ↓
¿QUÉ ESTADO CAMBIA?
   ↓
¿QUÉ EVENTO QUEDA?
   ↓
¿QUÉ PRUEBA PUEDE VERIFICARSE?
```

Si una transición fundamental no puede responder estas preguntas aplicables:

todavía no está suficientemente especificada.

## ARTÍCULO C — PRINCIPIO DE PRUEBA SOBRE PROMESA

Todo protocolo Web3 Trust-Native deberá aspirar a transformar:

```text
“LA PLATAFORMA DICE QUE X”
```

en:

```text
“UN ACTOR AFIRMA X”
        ↓
“POSEE AUTORIDAD PARA AFIRMAR X”
        ↓
“EXISTE EVIDENCIA”
        ↓
“EXISTE ATESTACIÓN CUANDO CORRESPONDE”
        ↓
“EXISTE UNA PRUEBA VERIFICABLE”
```

El protocolo deberá reducir la necesidad de:

“Confía en nosotros.”

y reemplazarla, donde sea posible, por:

“Verifica la evidencia.”

## DECLARACIÓN FINAL DEL PROTOCOLO

Web3 Trust-Native define un protocolo como:

una máquina verificable de relaciones de confianza, autoridad, evidencia y estado.

Los Actores representan participantes.

La Identidad permite reconocerlos.

La Autoridad establece legitimidad.

Las Capacidades delimitan acciones.

Los Recursos representan objetos del dominio.

Las Relaciones conectan Actores y Recursos.

Las Afirmaciones permiten declarar.

La Evidencia permite sustentar.

Los Observadores Autorizados conectan la realidad con el protocolo.

Las Atestaciones permiten respaldar.

Las Pruebas permiten demostrar.

El Consentimiento permite autorizar.

La Delegación permite distribuir autoridad.

La Revocación permite retirar vigencia.

La Propiedad establece control legítimo.

La Custodia establece responsabilidad sin apropiación automática.

La Procedencia conserva origen e historia.

El Estado representa aquello que está vigente.

Las Transiciones modifican ese Estado bajo reglas verificables.

Los Eventos preservan trazabilidad.

Los Invariantes protegen las garantías fundamentales.

La Gobernanza permite evolución legítima.

Por tanto:

```text
DOMINIO
   ↓
RELACIONES DE CONFIANZA
   ↓
AUTORIDAD
   ↓
CAPACIDADES
   ↓
AFIRMACIONES
   ↓
ATESTACIONES
   ↓
PRUEBAS
   ↓
TRANSICIONES
   ↓
ESTADO VERIFICABLE
   ↓
PROTOCOLO
```

L2 no determina todavía qué blockchain deberá utilizarse.

L2 no determina todavía cómo deberán escribirse los smart contracts.

L2 no determina todavía la arquitectura específica de HealthProof, Music On Chain, CertProof, Future Futbol o TIM.

L2 determina:

qué debe significar un protocolo Web3 Trust-Native antes de decidir cómo implementarlo.

## PRINCIPIO CANÓNICO DE L2

La pregunta fundamental no será:

**¿Qué datos debemos guardar?**

Será:

**¿Qué relaciones de confianza debemos poder demostrar?**

No será:

**¿Quién puede modificar este registro?**

Será:

**¿Qué Actor posee autoridad, de dónde proviene esa autoridad y qué Capacidad le permite producir esta transición?**

No será:

**¿Qué dice nuestra base de datos?**

Será:

**¿Qué puede verificar independientemente un tercero a partir del protocolo y de la evidencia legítima?**

## RELACIÓN CON LA JERARQUÍA WEB3 TRUST-NATIVE

```text
L0 — CONSTITUCIÓN
 │
 │ establece principios
 ▼
L1 — REGLAS DE ARQUITECTURA
 │
 │ establece razonamiento arquitectónico
 ▼
L2 — REGLAS DE PROTOCOLO
 │
 │ formaliza relaciones verificables
 ▼
L3 — CANON DE DOMINIO
 │
 │ especializa el modelo
 ▼
L4 — REGLAS DE SMART CONTRACTS
 │
 │ formaliza implementación ejecutable
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

L0 responde:

**¿Qué principios son irrenunciables?**

L1 responde:

**¿Cómo debe derivarse la arquitectura?**

L2 responde:

**¿Cómo se formaliza la confianza en reglas verificables?**

L3 responderá:

**¿Cómo se manifiestan esas reglas dentro de un dominio concreto?**

## REGLA LINGÜÍSTICA CANÓNICA

La documentación canónica española Web3 Trust-Native deberá redactarse en español.

Se conservarán en inglés términos cuando:

- constituyan palabras reservadas de un lenguaje;
- correspondan a nombres oficiales de tecnologías o estándares;
- sean expresiones técnicas cuya traducción pueda alterar su significado;
- formen parte de código, interfaces o especificaciones externas.

Ejemplos:

```text
EVM
Solidity
smart contract
struct
mapping
msg.sender
wallet
smart account
RPC
oracle
bridge
Layer 1
Layer 2
rollup
appchain
IPFS
DID
Verifiable Credential
Zero-Knowledge Proof
Soulbound
```

Los conceptos propios del marco deberán expresarse prioritariamente en español:

```text
Actor
Autoridad
Capacidad
Recurso
Relación
Afirmación
Atestación
Prueba
Evidencia
Consentimiento
Delegación
Revocación
Propiedad
Custodia
Procedencia
Estado
Transición
Evento
Gobernanza
Observador Autorizado
Ruta de Confianza
Portabilidad de Confianza
```

## VERSIONADO

Esta versión queda establecida como:

**L2 — Reglas de Protocolo Web3 Trust-Native v0.1**

y reemplaza cualquier borrador previo de L2 v0.1.

### CORRECCIÓN

v0.1.x

Aclaraciones sin modificación de la semántica protocolaria.

### EVOLUCIÓN MENOR

v0.x

Nuevas reglas o primitivas compatibles.

### EVOLUCIÓN MAYOR

v1.x+

Cambios en principios protocolarios fundamentales.

Toda modificación deberá preservar compatibilidad con L0 y L1 o declarar formalmente el conflicto.

## ESTADO CANÓNICO

```text
WEB3 TRUST-NATIVE
L2 — REGLAS DE PROTOCOLO
VERSIÓN 0.1

ESTADO:
CANÓNICA

IDIOMA:
ESPAÑOL

PRECEDENCIA:
L0 > L1 > L2 > L3 > L4 > L5 > L6 > L7 > L8

FIN — L2 REGLAS DE PROTOCOLO WEB3 TRUST-NATIVE v0.1
```

---

> **Límite B14.** La materialización del cuerpo del DOCX termina en `FIN — L2 REGLAS DE PROTOCOLO WEB3 TRUST-NATIVE v0.1`. No queda Heading1 posterior en la fuente histórica.
