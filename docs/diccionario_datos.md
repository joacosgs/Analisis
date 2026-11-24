
# Diccionario de datos - Click&Buy Latam

## Información general

- Materia: Introducción al Análisis de Datos.
- Proyecto: Trabajo Práctico Integrador.
- Caso: E-Commerce y Retail.
- Responsables: Lucas y Federico.
- Rol: Ingeniería de Datos.
- Fuente: unidad6-grupo1-ecommerce-retail.csv.
- Codificación: UTF-8.
- Filas originales: 2040.
- Columnas originales: 12.
- Transacciones únicas: 2000.
- Clave primaria esperada: ID_Transaccion.

## Diccionario de variables

| Variable | Tipo original | Tipo esperado | Descripción | Observaciones |
|---|---|---|---|---|
| ID_Transaccion | Texto | Texto | Identificador de la transacción | 40 registros duplicados por ID |
| Fecha | Texto | Fecha | Fecha de la operación comercial | 138 formatos diferentes al estándar |
| ID_Cliente | Texto | Texto | Identificador del cliente | Puede repetirse |
| Categoria | Texto | Texto | Categoría del producto vendido | 80 valores nulos |
| Producto | Texto | Texto | Nombre del producto | Sin valores nulos |
| Precio_Unitario | Texto | Decimal | Precio de una unidad en USD | 58 registros con símbolo monetario |
| Cantidad | Entero | Entero | Cantidad de unidades de la operación | 27 registros negativos |
| Descuento_Pct | Decimal | Decimal | Proporción de descuento aplicado | 100 valores nulos |
| Monto_Total_USD | Decimal | Decimal | Importe total registrado en dólares | Sin valores nulos |
| Metodo_Pago | Texto | Texto | Método de pago utilizado | Sin valores nulos |
| Canal_Venta | Texto | Texto | Canal por el cual se realizó la compra | Sin valores nulos |
| Estado_Pedido | Texto | Texto | Estado actual de la operación | Sin valores nulos |

## Categorías de productos

- Electrónica.
- Hogar.
- Deportes.
- Indumentaria.
- Belleza.

## Métodos de pago

- Tarjeta Crédito.
- Tarjeta Débito.
- Transferencia.
- MercadoPago.

## Canales de venta

- Sitio Web.
- App Mobile.
- Marketplace.

## Estados de los pedidos

| Estado | Registros originales |
|---|---:|
| Entregado | 1672 |
| En Tránsito | 189 |
| Cancelado | 94 |
| Devuelto | 85 |
| Total | 2040 |

## Consideraciones de calidad

- El archivo original debe conservarse sin modificaciones.
- Los identificadores de transacción deben ser únicos.
- Las fechas deben normalizarse al formato AAAA-MM-DD.
- Los precios deben convertirse a valores numéricos.
- Los descuentos se expresan como proporciones.
- Por ejemplo, 0.20 representa un descuento del 20%.
- Los valores nulos deben tratarse mediante criterios justificados.
- Las cantidades negativas deben investigarse antes de corregirse o eliminarse.
- Las cancelaciones y devoluciones deben analizarse por separado.

## Arquitectura de almacenamiento

- data/raw: almacenamiento del dataset original.
- data/processed: almacenamiento del dataset limpio.
- src: scripts de procesamiento.
- docs: documentación y auditorías.
- notebooks: análisis reproducibles.
- graficos: visualizaciones estadísticas.
- dashboard: tablero interactivo de Power BI.

## Entrega a Ingeniería Analítica

Los datos originales y los informes de auditoría
serán entregados a Gabriel y El Gordo, responsables
de la limpieza y transformación del dataset.

La etapa de Ingeniería de Datos no modifica
los registros originales.
