import pandas as pd

#  EXTRACCIÓN
print("Leyendo archivo CSV...")
df = pd.read_csv("ventas.csv")

# TRANSFORMACIÓN
print("Procesando datos...")
df['total'] = df['cantidad'] * df['precio_unitario']

resumen = df.groupby("categoria")['total'].agg(['sum', 'mean', 'count']).reset_index()

# CARGA (simulada con impresión)
print("\n Resumen por categoría:")
print(resumen)

# Información adicional
print("\n Proceso ETL finalizado correctamente.")