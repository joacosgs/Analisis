# Click&Buy Latam - Análisis de Datos

## Información del proyecto

- Universidad: Universidad Tecnológica Nacional (UTN).
- Carrera: Tecnicatura Universitaria en Programación.
- Materia: Introducción al Análisis de Datos.
- Trabajo Práctico Integrador.
- Grupo: 1.
- Caso de negocio: E-Commerce y Retail.
- Empresa analizada: Click&Buy Latam.

## Objetivo general

Analizar el rendimiento comercial de Click&Buy Latam,
identificar la relación entre los canales de venta y los
métodos de pago con el ticket promedio, estudiar las
cancelaciones y devoluciones y proponer estrategias
orientadas a mejorar los ingresos netos.

El proyecto comprende la ingesta, auditoría, preparación,
exploración, interpretación y visualización de datos
para contribuir a la toma de decisiones comerciales.

## Integrantes y distribución de roles

| Rol | Integrantes |
|---|---|
| Ingeniería de Datos | Lucas y Federico |
| Ingeniería Analítica | Gabriel y Santiago (El Gordo) |
| Análisis y Ciencia de Datos | Santiago Juárez y Mariano Torres Mari |
| Power BI y Storytelling | Joaquín y Leonel |

## Tecnologías utilizadas

- Python 3.13
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Power BI
- Visual Studio Code
- Git y GitHub

## Hitos del proyecto

| Hito | Descripción | Estado |
|---|---|---|
| Hito 1 | Ingesta, Auditoría y Preparación de Datos | Finalizado |
| Hito 2 | Análisis Exploratorio, Estadística Descriptiva y Diagnóstico | Finalizado |
| Hito 3 | Tablero Interactivo, Informe Técnico y Propuesta Estratégica | Pendiente |

## Estructura del proyecto

    Analisis/
    ├── data/
    │   ├── raw/
    │   │   └── unidad6-grupo1-ecommerce-retail.csv
    │   └── processed/
    │       └── dataset_limpio.csv
    ├── src/
    │   ├── 01_ingesta.py
    │   ├── 02_auditoria.py
    │   └── 03_limpieza_ingenieria_analitica.py
    ├── docs/
    │   ├── auditoria_inicial.csv
    │   ├── resumen_auditoria.csv
    │   ├── auditoria_resumen.csv
    │   ├── diccionario_datos.md
    │   ├── matriz_auditoria_calidad.csv
    │   ├── ingenieria_analitica/
    │   │   ├── auditoria_resumen.csv
    │   │   ├── entrega_a_siguientes_areas.md
    │   │   ├── ficha_tecnica_calidad.md
    │   │   └── matriz_auditoria_calidad.csv
    │   └── analisis_de_datos/
    │       ├── correlacion_pearson.csv
    │       ├── impacto_economico.csv
    │       ├── rendimiento_canal.csv
    │       ├── rendimiento_categoria.csv
    │       ├── rendimiento_metodo_pago.csv
    │       ├── resumen_estadistico.csv
    │       ├── tasas_cancelacion_devolucion.csv
    │       ├── ticket_canal_metodo_pago.csv
    │       └── entrega_a_business_intelligence.md
    ├── notebooks/
    │   ├── ingenieria_analitica.ipynb
    │   └── analisis_exploratorio.ipynb
    ├── graficos/
    │   ├── 01_histograma_monto.png
    │   ├── 02_boxplot_monto.png
    │   ├── 03_boxplot_categoria.png
    │   ├── 04_ingresos_categoria.png
    │   ├── 05_ticket_canal.png
    │   ├── 06_ticket_metodo_pago.png
    │   ├── 07_heatmap_ticket_combinado.png
    │   ├── 08_cancelaciones_devoluciones.png
    │   ├── 09_boxplot_descuentos.png
    │   ├── 10_scatter_precio_monto.png
    │   ├── 11_scatter_descuento_monto.png
    │   └── 12_heatmap_pearson.png
    ├── .gitignore
    ├── requirements.txt
    └── README.md

La carpeta dashboard/ será incorporada durante
el desarrollo del Hito 3.

## Instalación y configuración

### 1. Requisitos previos

- Python 3.13.
- Git.
- Visual Studio Code.
- Extensión Python para VS Code.
- Extensión Jupyter para VS Code.

### 2. Clonar el repositorio

    git clone https://github.com/joacosgs/Analisis.git
    cd Analisis

### 3. Acceder a la rama de desarrollo

    git switch dev
    git pull origin dev

### 4. Crear el entorno virtual

    python -m venv .venv

### 5. Activar el entorno virtual en Windows

    .\.venv\Scripts\Activate.ps1

### 6. Instalar las dependencias

    python -m pip install -r requirements.txt

### 7. Verificar las dependencias

    python -c "import pandas, numpy, matplotlib, seaborn, ipykernel; print('OK')"

---

# Hito 1 - Ingesta, Auditoría y Preparación de Datos

## Etapa 1 - Ingeniería de Datos

**Responsables:** Lucas y Federico.

### Objetivo

Realizar la carga controlada del dataset original,
validar su estructura e identificar problemas de
calidad antes de realizar las transformaciones.

### Actividades realizadas

- Carga del dataset original.
- Validación de la codificación UTF-8.
- Validación del esquema.
- Inspección de filas y columnas.
- Identificación de tipos de datos.
- Detección de valores nulos.
- Detección de transacciones duplicadas.
- Identificación de formatos inconsistentes.
- Generación de informes de auditoría.
- Elaboración del diccionario de datos.
- Organización de la arquitectura de almacenamiento.

### Ejecutar la ingesta

    python src/01_ingesta.py

### Ejecutar la auditoría inicial

    python src/02_auditoria.py

### Resultados de la auditoría inicial

| Indicador | Resultado |
|---|---:|
| Filas originales | 2040 |
| Columnas originales | 12 |
| Transacciones únicas | 2000 |
| Registros duplicados | 40 |
| Categorías nulas | 80 |
| Descuentos nulos | 100 |
| Valores nulos totales | 180 |
| Fechas irregulares | 138 |
| Precios con símbolo monetario | 58 |
| Cantidades negativas | 27 |

El dataset original se conserva sin modificaciones
dentro de la carpeta data/raw.

**Estado:** Finalizado e integrado en dev.

## Etapa 2 - Ingeniería Analítica

**Responsables:** Gabriel y Santiago (El Gordo).

### Objetivo

Transformar el dataset original en un conjunto de
datos preparado para el análisis estadístico y
la visualización comercial.

### Actividades realizadas

- Eliminación de duplicados por clave primaria.
- Tratamiento de categorías faltantes mediante
  la relación entre producto y categoría.
- Imputación de descuentos con validación de
  la fórmula comercial.
- Conversión de precios a valores numéricos.
- Normalización de fechas.
- Normalización de cadenas de texto.
- Validación de montos calculados.
- Identificación de cantidades negativas.
- Detección de valores atípicos mediante IQR
  y Z-score.
- Generación del dataset limpio.
- Elaboración de documentación y auditoría final.

### Ejecutar la limpieza

    python src/03_limpieza_ingenieria_analitica.py

### Dataset resultante

    data/processed/dataset_limpio.csv

### Resultados de calidad

| Indicador | Resultado |
|---|---:|
| Filas iniciales | 2040 |
| Filas finales | 2000 |
| Columnas originales | 12 |
| Columnas finales | 23 |
| Duplicados eliminados | 40 |
| Categorías imputadas | 80 |
| Descuentos imputados | 100 |
| Valores nulos finales | 0 |
| Fechas inválidas | 0 |
| Montos inconsistentes | 0 |
| Cantidades negativas conservadas | 26 |

Las cantidades negativas y los valores atípicos
se conservaron y señalizaron mediante columnas
de control para su posterior análisis.

**Estado:** Finalizado e integrado en dev.

---

# Hito 2 - Análisis Exploratorio de Datos, Estadística Descriptiva y Diagnóstico

## Etapa 3 - Análisis y Ciencia de Datos

**Responsables:** Santiago Juárez y Mariano Torres Mari.

### Objetivo

Aplicar los conceptos desarrollados en la Unidad 4
para identificar patrones, describir distribuciones,
analizar relaciones entre variables y formular
hipótesis comerciales sobre Click&Buy Latam.

### Metodología

Se aplicaron tres tipologías de análisis:

- Análisis descriptivo: ¿Qué sucedió?
- Análisis exploratorio: ¿Qué patrones existen?
- Análisis diagnóstico: ¿Por qué pudo haber sucedido?

### Actividades realizadas

- Validación independiente del dataset limpio.
- Identificación y clasificación de estados de pedido.
- Análisis de cantidades negativas.
- Definición de criterios comerciales.
- Análisis estadístico univariado.
- Cálculo de media, mediana y moda.
- Cálculo de varianza y desviación estándar.
- Cálculo de cuartiles y rango intercuartílico.
- Análisis de asimetría y curtosis.
- Identificación de valores atípicos mediante IQR.
- Histogramas con curva KDE.
- Diagramas de caja generales y segmentados.
- Análisis del rendimiento comercial por categoría.
- Ticket promedio por canal y método de pago.
- Análisis combinado de canales y métodos de pago.
- Análisis de cancelaciones y devoluciones.
- Análisis del impacto monetario por estado.
- Análisis de descuentos.
- Gráficos de dispersión.
- Matriz de correlación de Pearson.
- Formulación de hipótesis comerciales.
- Elaboración de cinco hallazgos analíticos.
- Exportación de resultados para Business Intelligence.

### Criterios comerciales

Para calcular el monto de ventas y el ticket promedio
se consideran exclusivamente las operaciones que
cumplen las siguientes condiciones:

- Estado del pedido: Entregado.
- Cantidad mayor que cero.
- Monto total mayor que cero.

Los pedidos cancelados, devueltos y en tránsito
se analizan por separado.

Los registros negativos y los valores atípicos
no fueron eliminados del dataset limpio.

Los ingresos calculados representan el monto de
ventas positivas entregadas y no equivalen
necesariamente a ingresos netos contables.

### Resultados generales

| Indicador | Resultado |
|---|---:|
| Transacciones totales | 2000 |
| Ventas positivas entregadas | 1617 |
| Monto de ventas positivas | USD 478.817,52 |
| Ticket promedio | USD 296,11 |
| Mediana del ticket | USD 174,93 |
| Desviación estándar | USD 336,34 |
| Primer cuartil (Q1) | USD 86,14 |
| Tercer cuartil (Q3) | USD 385,49 |
| Rango intercuartílico (IQR) | USD 299,35 |
| Asimetría | 2,795 |
| Valores atípicos del monto | 107 |

### Distribución de estados de pedido

| Estado | Cantidad | Porcentaje |
|---|---:|---:|
| Entregado | 1640 | 82,00% |
| En Tránsito | 184 | 9,20% |
| Cancelado | 92 | 4,60% |
| Devuelto | 84 | 4,20% |
| Total | 2000 | 100% |

### Rendimiento comercial por categoría

| Categoría | Monto de ventas positivas |
|---|---:|
| Electrónica | USD 244.723,44 |
| Hogar | USD 110.662,00 |
| Deportes | USD 69.977,56 |
| Indumentaria | USD 32.863,39 |
| Belleza | USD 20.591,13 |

### Ticket promedio por canal

| Canal | Ticket promedio |
|---|---:|
| Marketplace | USD 301,32 |
| Sitio Web | USD 300,50 |
| App Mobile | USD 286,83 |

### Ticket promedio por método de pago

| Método de pago | Ticket promedio |
|---|---:|
| Transferencia | USD 323,99 |
| Tarjeta Crédito | USD 291,83 |
| MercadoPago | USD 283,51 |
| Tarjeta Débito | USD 281,43 |

### Principales correlaciones de Pearson

| Variables | Coeficiente r |
|---|---:|
| Precio unitario y monto total | 0,732 |
| Cantidad y monto total | 0,524 |
| Descuento y monto total | -0,076 |

Los coeficientes obtenidos representan asociaciones
lineales entre variables.

Parte de estas asociaciones responde a la propia
construcción matemática del monto total.

La correlación no implica causalidad.

### Hallazgos comerciales

1. Electrónica concentra aproximadamente el 51,11%
   del monto de las ventas positivas entregadas,
   siendo la categoría de mayor participación.

2. Los importes presentan una distribución con
   asimetría positiva. Los valores elevados influyen
   sobre la media, por lo que resulta conveniente
   utilizar conjuntamente la media y la mediana.

3. Marketplace presenta el mayor ticket promedio
   entre los canales y Transferencia entre los
   métodos de pago. Estas diferencias no demuestran
   relaciones causales.

4. Las cancelaciones y devoluciones representan
   conjuntamente el 8,80% de las transacciones.
   Hogar presenta la mayor tasa combinada,
   con aproximadamente un 11,44%.

5. Se identificaron 26 registros con cantidades
   negativas, de los cuales 23 figuran como
   entregados. Su significado comercial requiere
   una revisión adicional.

### Visualizaciones generadas

| Archivo | Contenido |
|---|---|
| 01_histograma_monto.png | Histograma con KDE |
| 02_boxplot_monto.png | Boxplot general |
| 03_boxplot_categoria.png | Boxplot por categoría |
| 04_ingresos_categoria.png | Rendimiento por categoría |
| 05_ticket_canal.png | Ticket promedio por canal |
| 06_ticket_metodo_pago.png | Ticket promedio por método de pago |
| 07_heatmap_ticket_combinado.png | Comparación de canal y método de pago |
| 08_cancelaciones_devoluciones.png | Tasas por categoría |
| 09_boxplot_descuentos.png | Distribución según descuento |
| 10_scatter_precio_monto.png | Relación precio y monto |
| 11_scatter_descuento_monto.png | Relación descuento y monto |
| 12_heatmap_pearson.png | Matriz de correlación de Pearson |

### Ejecutar el análisis exploratorio

1. Abrir el proyecto en Visual Studio Code.
2. Activar el entorno virtual.
3. Abrir notebooks/analisis_exploratorio.ipynb.
4. Seleccionar el kernel correspondiente a .venv.
5. Ejecutar todas las celdas mediante Run All.

El notebook genera automáticamente los gráficos
y las tablas de resultados correspondientes.

### Entregables

- Notebook de análisis exploratorio documentado.
- Doce gráficos estadísticos en formato PNG.
- Ocho tablas de resultados en formato CSV.
- Documento de entrega a Business Intelligence.
- Cuatro hipótesis comerciales.
- Cinco hallazgos analíticos.

**Estado:** Desarrollo finalizado, pendiente de
integración en dev.

---

# Hito 3 - Tablero Interactivo, Informe Técnico Final y Propuesta Estratégica

## Etapa 4 - Power BI y Storytelling

**Responsables:** Joaquín y Leonel.

### Objetivo

Transformar los resultados del análisis estadístico
en visualizaciones interactivas que faciliten la
interpretación y la toma de decisiones comerciales.

### Actividades previstas

- Modelado de datos.
- Creación de medidas DAX.
- Diseño de indicadores KPI.
- Desarrollo del dashboard interactivo.
- Incorporación de filtros y segmentaciones.
- Visualización del rendimiento comercial.
- Visualización de cancelaciones y devoluciones.
- Aplicación de principios de Gestalt.
- Elaboración del relato comercial.
- Formulación de propuestas estratégicas.
- Preparación del informe técnico final.
- Preparación de la presentación para la defensa.

### Fuente de datos

    data/processed/dataset_limpio.csv

### Resultados de referencia

    docs/analisis_de_datos/

### Visualizaciones de referencia

    graficos/

### Entregable previsto

Tablero interactivo desarrollado en Power BI,
acompañado del informe técnico y la propuesta
estratégica de negocio.

**Estado:** Pendiente de desarrollo e integración.

---

## Flujo de trabajo del proyecto

    Dataset original
          |
          v
    Ingeniería de Datos
    Ingesta y auditoría inicial
          |
          v
    Ingeniería Analítica
    Limpieza y transformación
          |
          v
    Análisis y Ciencia de Datos
    Estadística, EDA y diagnóstico
          |
          v
    Power BI y Storytelling
    Dashboard y toma de decisiones

## Metodología de trabajo con Git

El proyecto utiliza ramas independientes para
organizar el trabajo colaborativo.

| Rama | Función |
|---|---|
| main | Versión final y estable |
| dev | Integración de las etapas |
| feature/ingeniero-de-datos | Ingeniería de Datos |
| feature/ingenieria-analitica | Ingeniería Analítica |
| feature/analisis-de-datos | Análisis y Ciencia de Datos |

Cada equipo desarrolla su etapa en una rama
independiente y utiliza Pull Requests para
incorporar los cambios a dev.

Una vez finalizados y verificados los tres hitos,
los cambios podrán integrarse a main.

## Estado general del proyecto

- [x] Configuración del repositorio.
- [x] Arquitectura de almacenamiento.
- [x] Configuración del entorno de desarrollo.
- [x] Ingeniería de Datos.
- [x] Auditoría inicial.
- [x] Ingeniería Analítica.
- [x] Generación del dataset limpio.
- [x] Hito 1 finalizado.
- [x] Estadística descriptiva.
- [x] Análisis Exploratorio de Datos.
- [x] Análisis bivariado y correlaciones.
- [x] Generación de gráficos estadísticos.
- [x] Formulación de hipótesis.
- [x] Elaboración de hallazgos comerciales.
- [x] Exportación de resultados.
- [x] Hito 2 desarrollado.
- [ ] Integración del Hito 2 en dev.
- [ ] Dashboard en Power BI.
- [ ] Propuesta estratégica.
- [ ] Informe técnico final.
- [ ] Hito 3 finalizado.
- [ ] Integración final en main.
- [ ] Presentación y defensa.

---

Trabajo Práctico Integrador - Grupo 1.

Introducción al Análisis de Datos.

Universidad Tecnológica Nacional (UTN) - 2026.