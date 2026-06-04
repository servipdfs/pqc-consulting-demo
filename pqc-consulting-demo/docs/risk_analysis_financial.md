# Análisis de riesgos cuánticos (SNDL)

| Activo | Algoritmo | Vida útil | Riesgo | Prioridad | Acción |
|--------|-----------|-----------|--------|-----------|--------|
| SWIFT | RSA-2048 | 7 años | Medio-Alto | Alta | Migrar a ML-DSA híbrido |
| Backups | RSA-wrapped AES | >30 años | **Crítico** | Crítica | Envolver KEK con ML-KEM |
| Firmas software | RSA-3072 | perpetuo | Alto | Alta | SLH-DSA |

Priorización según QSFF + FS-ISAC.