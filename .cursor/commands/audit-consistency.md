# Auditoría de Consistencia Constitucional

Detecta contradicciones y desalineaciones entre Libros, manifests y metaespecificación.

## Protocolo

1. Cargar manifests de todos los Libros.
2. Verificar cadena `dependsOn` vs jerarquía canónica.
3. Comparar títulos `manifest.title` vs menciones en L0/README/metaspec.
4. Listar divergencias conocidas (p. ej. naming L7/L8).
5. Separar hallazgos en: **contradicción normativa**, **deriva editorial**, **mapa repo vs realidad**.

## Salida

Tabla de hallazgos con severidad y archivo citado. Sin correcciones automáticas destructivas.
