---
name: reference-audit
description: Playbook de auditoría de referencias rotas, manifests y trazabilidad. Usar en auditorías de integridad del repo.
---

# Skill — Auditoría de Referencias

## Pasos

1. Aplicar CROSSREF-POLICY.
2. Inventariar Libros existentes bajo `constitution/`.
3. Escanear Markdown/JSON por paths e IDs inválidos.
4. Validar campos mínimos de cada `manifest.json`.
5. Contrastar títulos entre manifests y menciones en L0/metaspec.
6. Emitir informe por severidad sin reescrituras masivas.

## Severidades

- **P0** contradicción de autoridad / L0
- **P1** referencia rota o manifest inválido
- **P2** deriva editorial / naming
- **P3** mejora cosmética
