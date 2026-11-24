
# Click&Buy Latam - Análisis de Datos

## Información del proyecto

- Universidad: Universidad Tecnológica Nacional (UTN).
- Carrera: Tecnicatura Universitaria en Programación.
- Materia: Introducción al Análisis de Datos.
- Trabajo Práctico Integrador.
- Grupo: 1.
- Caso de negocio: E-Commerce y Retail.

## Objetivo

Analizar el rendimiento comercial de Click&Buy Latam,
identificar el impacto de los canales de venta y los
métodos de pago en el ticket promedio, estudiar las
cancelaciones y devoluciones y proponer estrategias
para maximizar los ingresos netos.

## Integrantes y distribución de roles

| Rol | Integrantes |
|---|---|
| Ingeniería de Datos | Lucas y Federico |
| Ingeniería Analítica | Gabriel y Santiago (El Gordo) |
| Análisis y Ciencia de Datos | Santiago y Mariano |
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

## Estructura del proyecto

    Analisis/
    ├── data/
    │   ├── raw/
    │   └── processed/
    ├── src/
    │   ├── 01_ingesta.py
    │   └── 02_auditoria.py
    ├── docs/
    │   ├── auditoria_inicial.csv
    │   ├── resumen_auditoria.csv
    │   └── diccionario_datos.md
    ├── notebooks/
    ├── graficos/
    ├── dashboard/
    ├── .gitignore
    ├── requirements.txt
    └── README.md

## Instalación y configuración

### 1. Clonar el repositorio

    git clone https://github.com/joacosgs/Analisis.git
    cd Analisis

### 2. Crear el entorno virtual

    py -V:3.13 -m venv .venv

### 3. Instalar las dependencias

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt

## Etapa 1 - Ingeniería de Datos

Responsables: Lucas y Federico.

Actividades realizadas:

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

    .\.venv\Scripts\python.exe src/01_ingesta.py

### Ejecutar la auditoría

    .\.venv\Scripts\python.exe src/02_auditoria.py

### Resultados de la auditoría inicial

| Indicador | Resultado |
|---|---:|
| Filas originales | 2040 |
| Columnas | 12 |
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

## Etapa 2 - Ingeniería Analítica

Responsables: Gabriel y Santiago (El Gordo).

- Limpieza y transformación de datos.
- Tratamiento de valores nulos.
- Eliminación de duplicados.
- Normalización de formatos.
- Detección de valores atípicos.
- Generación del dataset limpio.

Estado: pendiente de integración.

## Etapa 3 - Análisis y Ciencia de Datos

Responsables: Santiago y Mariano.

- Análisis exploratorio de datos (EDA).
- Estadística descriptiva.
- Análisis univariado y bivariado.
- Correlación de Pearson.
- Generación de gráficos.
- Elaboración de conclusiones comerciales.

Estado: pendiente de integración.

## Etapa 4 - Power BI y Storytelling

Responsables: Joaquín y Leonel.

- Modelado de datos.
- Creación de medidas DAX.
- Diseño de indicadores KPI.
- Desarrollo del dashboard interactivo.
- Propuestas estratégicas de negocio.

Estado: pendiente de integración.

## Estado del proyecto

- [x] Configuración del repositorio.
- [x] Arquitectura de almacenamiento.
- [x] Ingeniería de Datos.
- [ ] Ingeniería Analítica.
- [ ] Análisis Exploratorio de Datos.
- [ ] Dashboard en Power BI.
- [ ] Informe técnico final.
- [ ] Presentación y defensa.
