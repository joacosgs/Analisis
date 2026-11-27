# Entrega a los siguientes equipos

## Dataset base
`data/processed/dataset_limpio.csv`

La limpieza y validación inicial ya están realizadas. No repetirla salvo que se documente un nuevo hallazgo.

### Data Analyst
Entregar notebook EDA documentado; estadísticas univariadas (media, mediana, IQR, desviación estándar, asimetría); gráficos histogramas KDE, boxplots segmentados y scatter; correlación Pearson con explicación de correlación no implica causalidad; 3–5 hallazgos de negocio.

Investigar categorías, canales, métodos de pago, ticket, descuentos, cancelaciones/devoluciones y registros negativos/outliers.

### BI
Crear dashboard funcional Power BI (.pbix) o Streamlit; KPIs, filtros, storytelling y propuesta estratégica. Definir junto con analista qué estados cuentan para ingresos netos, no asumir que cada registro representa ingreso realizado.

### Columnas de control agregadas
Diferencia_Monto_Calculado_USD, Monto_Consistente, Cantidad_Negativa, flags de outliers IQR y Z-score para Precio, Cantidad y Monto. Son indicadores de revisión, no instrucciones para eliminar registros.
