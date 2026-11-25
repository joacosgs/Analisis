# Entrega a Business Intelligence

## Click&Buy Latam — E-Commerce y Retail

**Grupo:** 1  
**Rol:** Analista / Científico de Datos  
**Responsables:** Mariano Torres Mari y Santiago Juárez  
**Destinatarios:** Joaquín y Leonel  

## 1. Dataset utilizado

data/processed/dataset_limpio.csv

El dataset contiene 2.000 transacciones y 23 columnas,
sin valores nulos ni identificadores duplicados.

## 2. Criterios comerciales

Para calcular el rendimiento comercial y el ticket
promedio se consideran únicamente las operaciones que
cumplen las siguientes condiciones:

- Estado_Pedido = Entregado.
- Cantidad mayor que cero.
- Monto_Total_USD mayor que cero.

Los pedidos cancelados, devueltos y en tránsito
se analizan por separado.

Los ingresos calculados representan ventas positivas
entregadas y no ingresos netos contables confirmados.

## 3. Indicadores principales

| Indicador | Resultado |
|---|---:|
| Transacciones totales | 2.000 |
| Ventas positivas entregadas | 1.617 |
| Monto de ventas positivas | USD 478.817,52 |
| Ticket promedio | USD 296,11 |
| Mediana del ticket | USD 174,93 |
| Pedidos entregados | 1.640 |
| Pedidos en tránsito | 184 |
| Pedidos cancelados | 92 |
| Pedidos devueltos | 84 |
| Tasa de cancelación | 4,60% |
| Tasa de devolución | 4,20% |
| Tasa combinada | 8,80% |
| Registros negativos | 26 |

## 4. Principales hallazgos

- Electrónica concentra aproximadamente el 51,11%
  del monto de las ventas positivas entregadas.
- La distribución de los importes presenta una
  asimetría positiva de 2,795.
- Marketplace presenta el mayor ticket promedio
  entre los canales de venta.
- Transferencia presenta el mayor ticket promedio
  entre los métodos de pago.
- Hogar presenta la mayor tasa combinada de
  cancelaciones y devoluciones, con un 11,44%.

## 5. Archivos disponibles

### Notebook

notebooks/analisis_exploratorio.ipynb

### Tablas de resultados

- resumen_estadistico.csv
- rendimiento_categoria.csv
- rendimiento_canal.csv
- rendimiento_metodo_pago.csv
- tasas_cancelacion_devolucion.csv
- impacto_economico.csv
- correlacion_pearson.csv
- ticket_canal_metodo_pago.csv

### Visualizaciones

Los 12 gráficos estadísticos se encuentran
en la carpeta graficos/.

## 6. Recomendaciones para el dashboard

- Mostrar el monto de ventas positivas entregadas.
- Incorporar el ticket promedio y la mediana.
- Comparar el rendimiento por categoría.
- Incorporar filtros por fecha, categoría, canal
  de venta y método de pago.
- Mostrar las tasas de cancelación y devolución.
- Diferenciar los estados de pedido.
- Utilizar los hallazgos para construir el relato
  comercial de la presentación.

Las tasas deben calcularse sobre el total de
transacciones del contexto filtrado.

## 7. Advertencias y limitaciones

Se identificaron 26 registros negativos, de los
cuales 23 corresponden a pedidos entregados.

No deben eliminarse ni clasificarse automáticamente
como devoluciones.

Los valores atípicos se conservaron porque pueden
representar operaciones comerciales válidas.

No se dispone de información suficiente para
determinar reembolsos, costos o ingresos netos
contables definitivos.

La correlación no implica causalidad.

## 8. Estado de entrega

Hito 2: Análisis Exploratorio de Datos,
Estadística Descriptiva y Diagnóstico.

Desarrollo finalizado y disponible para la
continuación del Hito 3.