# Ficha técnica de calidad — Ingeniería Analítica

**Caso:** Click&Buy Latam — E-Commerce y Retail

## Resultados
- Filas iniciales: **2040**
- Filas finales: **2000**
- Columnas originales: **12**
- Duplicados por clave primaria eliminados: **40**
- Categorías imputadas: **80**
- Descuentos imputados a 0 con comprobación: **100**
- Fechas inválidas: **0**
- Montos inconsistentes: **0**
- Cantidades negativas conservadas: **26**
- Nulos finales: **0**

## Criterios
**Deduplicación:** por clave `ID_Transaccion`. Los repetidos fueron revisados; si el script detecta IDs repetidos con contenido conflictivo, se detiene para revisión manual.

**Categorías:** imputadas con relación Producto-Categoría observada en los registros completos.

**Descuento:** se imputó 0 únicamente cuando el monto informado coincide con Precio × Cantidad (tolerancia USD 0,01).

**Precio:** símbolo `$` removido y conversión a numérico.

**Fecha:** formatos mixtos convertidos a `YYYY-MM-DD`.

**Strings:** espacios exteriores eliminados y cadenas vacías convertidas en nulos.

**Cantidades negativas:** conservadas y señalizadas; no se asume que todas sean devoluciones.

**Outliers:** flags IQR (1.5×IQR) y Z-score (|z|>3). No se eliminan automáticamente.

## Validaciones
Clave única, nulos por variable, monto reportado vs calculado y flags de negativos/outliers.
Consultar `auditoria_resumen.csv` y `matriz_auditoria_calidad.csv`.
