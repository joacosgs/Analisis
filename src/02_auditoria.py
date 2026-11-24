
from pathlib import Path
import pandas as pd

# Rutas del proyecto
BASE = Path(__file__).resolve().parent.parent
SOURCE = BASE / "data" / "raw" / "unidad6-grupo1-ecommerce-retail.csv"
DOCS = BASE / "docs"

DOCS.mkdir(exist_ok=True)

# Carga de los datos originales
df = pd.read_csv(SOURCE, encoding="utf-8")

print("=" * 60)
print("CLICK&BUY LATAM - AUDITORIA INICIAL")
print("Responsables: Lucas y Federico")
print("=" * 60)

# Dimensiones
print("\nFilas originales:", df.shape[0])
print("Columnas originales:", df.shape[1])

# Valores nulos
print("\nVALORES NULOS POR COLUMNA:")
print(df.isna().sum())

# Registros duplicados
duplicados = df.duplicated(subset="ID_Transaccion").sum()

print("\nRegistros duplicados:", duplicados)
print("Transacciones unicas:", df["ID_Transaccion"].nunique())

# Fechas con formatos diferentes
fechas_irregulares = (
    ~df["Fecha"].astype(str).str.fullmatch(r"\d{4}-\d{2}-\d{2}")
).sum()

print("\nFechas con formato diferente:", fechas_irregulares)

# Precios con simbolos monetarios
precios_simbolos = (
    df["Precio_Unitario"].astype(str).str.contains("$", regex=False)
).sum()

print("Precios con simbolo monetario:", precios_simbolos)

# Cantidades negativas
cantidades_negativas = (df["Cantidad"] < 0).sum()

print("Cantidades negativas:", cantidades_negativas)

# Estados de los pedidos
print("\nESTADOS DE LOS PEDIDOS:")
print(df["Estado_Pedido"].value_counts())

# Auditoria por columna
auditoria = pd.DataFrame({
    "Variable": df.columns,
    "Tipo_Dato": df.dtypes.astype(str).values,
    "Valores_Nulos": df.isna().sum().values,
    "Porcentaje_Nulos": (
        df.isna().mean().values * 100
    ).round(2),
    "Valores_Unicos": df.nunique().values
})

# Resumen de problemas detectados
resumen = pd.DataFrame({
    "Indicador": [
        "Filas originales",
        "Columnas originales",
        "Transacciones unicas",
        "Registros duplicados",
        "Valores nulos totales",
        "Fechas con formato diferente",
        "Precios con simbolo monetario",
        "Cantidades negativas"
    ],
    "Cantidad": [
        df.shape[0],
        df.shape[1],
        df["ID_Transaccion"].nunique(),
        duplicados,
        df.isna().sum().sum(),
        fechas_irregulares,
        precios_simbolos,
        cantidades_negativas
    ]
})

# Exportacion de los informes
auditoria.to_csv(
    DOCS / "auditoria_inicial.csv",
    index=False,
    encoding="utf-8-sig"
)

resumen.to_csv(
    DOCS / "resumen_auditoria.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nAUDITORIA COMPLETADA CORRECTAMENTE")
print("Informes guardados en la carpeta docs.")
