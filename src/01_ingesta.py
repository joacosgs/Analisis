
from pathlib import Path
import pandas as pd

# Rutas del proyecto
BASE = Path(__file__).resolve().parent.parent
SOURCE = BASE / "data" / "raw" / "unidad6-grupo1-ecommerce-retail.csv"


def ingesta():

    # Carga del archivo CSV
    df = pd.read_csv(SOURCE, encoding="utf-8")

    # Columnas esperadas del dataset
    columnas_esperadas = [
        "ID_Transaccion",
        "Fecha",
        "ID_Cliente",
        "Categoria",
        "Producto",
        "Precio_Unitario",
        "Cantidad",
        "Descuento_Pct",
        "Monto_Total_USD",
        "Metodo_Pago",
        "Canal_Venta",
        "Estado_Pedido"
    ]

    # Validación de la estructura
    if list(df.columns) != columnas_esperadas:
        raise ValueError("El esquema del dataset es incorrecto")

    if df["ID_Transaccion"].isna().any():
        raise ValueError("Existen identificadores nulos")

    # Inspección inicial
    print("=" * 60)
    print("CLICK&BUY LATAM - INGENIERIA DE DATOS")
    print("Responsables: Lucas y Federico")
    print("=" * 60)

    print("\nArchivo cargado correctamente.")
    print("\nDimensiones del dataset:", df.shape)

    print("\nCantidad de filas:", df.shape[0])
    print("Cantidad de columnas:", df.shape[1])

    print("\nColumnas del dataset:")
    print(df.columns.tolist())

    print("\nTipos de datos:")
    print(df.dtypes)

    print("\nPrimeras cinco filas:")
    print(df.head().to_string(index=False))

    print("\nInformacion general:")
    df.info()

    print("\nValidacion del esquema: CORRECTA")

    return df


if __name__ == "__main__":
    ingesta()
