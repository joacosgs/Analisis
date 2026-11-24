from pathlib import Path
import pandas as pd
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"data/raw/unidad6-grupo1-ecommerce-retail.csv"
OUTPUT=ROOT/"data/processed/dataset_limpio.csv"
PRODUCT_CATEGORY={'Aspiradora Robot': 'Hogar', 'Auriculares Bluetooth': 'Electrónica', 'Batidora Planetaria': 'Hogar', 'Bicicleta MTB': 'Deportes', 'Buzo con Capucha': 'Indumentaria', 'Cafetera Express': 'Hogar', 'Campera Impermeable': 'Indumentaria', 'Colchoneta Yoga': 'Deportes', 'Crema Antiage': 'Belleza', 'Kit Maquillaje': 'Belleza', 'Lámpara LED': 'Hogar', 'Mancuernas 10kg': 'Deportes', 'Pantalón Jean': 'Indumentaria', 'Pelota Fútbol': 'Deportes', 'Perfume Floral': 'Belleza', 'Remera Algodón': 'Indumentaria', 'Secador de Pelo': 'Belleza', 'Serum Facial': 'Belleza', 'Set de Sartenes': 'Hogar', 'Smart TV 55"': 'Electrónica', 'Smartphone Pro': 'Electrónica', 'Tablet 10"': 'Electrónica', 'Teclado Mecánico': 'Electrónica', 'Vestido Casual': 'Indumentaria', 'Zapatillas Running': 'Deportes'}

def iqr_flag(s):
    x=pd.to_numeric(s,errors="coerce"); q1=x.quantile(.25); q3=x.quantile(.75); i=q3-q1
    if pd.isna(i) or i==0: return pd.Series(False,index=x.index)
    return (x<q1-1.5*i)|(x>q3+1.5*i)

def z_flag(s,threshold=3):
    x=pd.to_numeric(s,errors="coerce"); sd=x.std(ddof=0)
    if pd.isna(sd) or sd==0: return pd.Series(False,index=x.index)
    return ((x-x.mean()).abs()/sd)>threshold

def main():
    original=pd.read_csv(INPUT,dtype={"ID_Transaccion":"string"})
    df=original.copy()
    for c in df.columns:
        if df[c].dtype=="object" or str(df[c].dtype).startswith("string"):
            df[c]=df[c].astype("string").str.strip().replace({"":pd.NA,"nan":pd.NA,"None":pd.NA})
    df["Precio_Unitario"]=pd.to_numeric(df["Precio_Unitario"].astype("string").str.replace("$","",regex=False).str.replace(",","",regex=False),errors="coerce")
    parsed=pd.to_datetime(df["Fecha"],errors="coerce",format="mixed",dayfirst=True)
    df["Fecha"]=parsed.dt.strftime("%Y-%m-%d"); df.loc[parsed.isna(),"Fecha"]=pd.NA
    cat=df["Producto"].map(PRODUCT_CATEGORY); mask=df["Categoria"].isna() & cat.notna()
    df.loc[mask,"Categoria"]=cat[mask]
    df["Categoria_Imputada"]=mask
    zero_mask=df["Descuento_Pct"].isna() & np.isclose(df["Monto_Total_USD"],df["Precio_Unitario"]*df["Cantidad"],atol=.01,rtol=0)
    df.loc[zero_mask,"Descuento_Pct"]=0.0
    df["Descuento_Imputado"]=zero_mask
    dup=df[df["ID_Transaccion"].duplicated(keep=False)]
    if not dup.empty:
       conflicts = int(
    dup.drop(columns=["ID_Transaccion"])
    .groupby(dup["ID_Transaccion"])
    .nunique(dropna=False)
    .gt(1)
    .any(axis=1)
    .sum()
)
    if conflicts: raise ValueError(f"{conflicts} IDs duplicados conflictivos; revisión manual requerida.")
    before=len(df); df=df.drop_duplicates(subset="ID_Transaccion",keep="first").copy()
    calculated=df["Precio_Unitario"]*df["Cantidad"]*(1-df["Descuento_Pct"])
    df["Diferencia_Monto_Calculado_USD"]=(df["Monto_Total_USD"]-calculated).round(2)
    df["Monto_Consistente"]=np.isclose(df["Monto_Total_USD"],calculated,atol=.01,rtol=0,equal_nan=False)
    df["Cantidad_Negativa"]=df["Cantidad"]<0
    for c,n in [("Precio_Unitario","Precio"),("Cantidad","Cantidad"),("Monto_Total_USD","Monto")]:
        df[f"Outlier_IQR_{n}"]=iqr_flag(df[c]); df[f"Outlier_ZScore_{n}"]=z_flag(df[c])
    OUTPUT.parent.mkdir(parents=True,exist_ok=True); df.to_csv(OUTPUT,index=False,encoding="utf-8-sig")

    # Reproducir la ficha y matriz de auditoría en cada ejecución.
    docs=ROOT/"docs"; docs.mkdir(parents=True,exist_ok=True)
    metrics=[
        ("Filas originales",len(original),"Fuente original"),
        ("Columnas originales",len(original.columns),""),
        ("Duplicados por ID eliminados",len(original)-len(df),"Deduplicación por clave primaria"),
        ("Filas finales",len(df),""),
        ("IDs únicos finales",df["ID_Transaccion"].nunique(),""),
        ("Categorías faltantes iniciales",int(original["Categoria"].isna().sum()),""),
        ("Categorías imputadas",int(df["Categoria_Imputada"].sum()),"Mapeo producto-categoría observado"),
        ("Categorías nulas finales",int(df["Categoria"].isna().sum()),""),
        ("Descuentos faltantes iniciales",int(original["Descuento_Pct"].isna().sum()),""),
        ("Descuentos imputados",int(df["Descuento_Imputado"].sum()),"Solo cuando fórmula respalda 0"),
        ("Descuentos nulos finales",int(df["Descuento_Pct"].isna().sum()),""),
        ("Fechas inválidas finales",int(df["Fecha"].isna().sum()),""),
        ("Cantidades negativas iniciales",int(original["Cantidad"].lt(0).sum()),""),
        ("Cantidades negativas finales",int(df["Cantidad_Negativa"].sum()),"Conservadas y señalizadas"),
        ("Montos inconsistentes",int((~df["Monto_Consistente"]).sum()),"Tolerancia 0.01 USD"),
        ("Nulos totales finales",int(df.isna().sum().sum()),"")
    ]
    for col in df.columns:
        metrics.append((f"Nulos finales — {col}",int(df[col].isna().sum()),str(df[col].dtype)))
    for label in ["Precio","Cantidad","Monto"]:
        metrics.extend([
            (f"Outliers IQR — {label}",int(df[f"Outlier_IQR_{label}"].sum()),"Marcados, no eliminados; 1.5*IQR"),
            (f"Outliers Z-score — {label}",int(df[f"Outlier_ZScore_{label}"].sum()),"Marcados, no eliminados; |z|>3")
        ])
    pd.DataFrame(metrics,columns=["Metrica","Valor","Detalle"]).to_csv(docs/"auditoria_resumen.csv",index=False,encoding="utf-8-sig")

    quality=[]
    treatments={"ID_Transaccion":"Deduplicación por clave primaria","Fecha":"Parsing mixto a formato ISO",
                "Precio_Unitario":"Remover símbolo monetario y convertir a numérico",
                "Categoria":"Imputación basada en Producto","Descuento_Pct":"Imputación 0 solo con respaldo de fórmula"}
    for col in original.columns:
        quality.append({"Variable":col,"Tipo_original":str(original[col].dtype),"Tipo_final":str(df[col].dtype),
            "Nulos_iniciales":int(original[col].isna().sum()),"Nulos_finales":int(df[col].isna().sum()),
            "Unicos_iniciales":int(original[col].nunique()),"Unicos_finales":int(df[col].nunique()),
            "Tratamiento":treatments.get(col,"Normalización de espacios si corresponde; sin imputación")})
    pd.DataFrame(quality).to_csv(docs/"matriz_auditoria_calidad.csv",index=False,encoding="utf-8-sig")

    print(f"Filas: {len(original)} -> {len(df)} | duplicados por ID eliminados: {before-len(df)}")
    print(f"Categorías completadas: {int(mask.sum())} | descuentos imputados 0: {int(zero_mask.sum())}")
    print(f"Fechas inválidas: {int(parsed.isna().sum())} | montos inconsistentes: {int((~df['Monto_Consistente']).sum())}")
    print(f"Nulos finales: {int(df.isna().sum().sum())} | CSV: {OUTPUT}")
if __name__=="__main__": main()
