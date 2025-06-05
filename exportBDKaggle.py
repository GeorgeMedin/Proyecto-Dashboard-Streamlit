import pandas as pd
import kagglehub
import os
import shutil

ruta_destino = r"C:\Users\ANDRES & JORGE\OneDrive\Documentos\Dashboards en Streamlit\baseDatos"
os.makedirs(ruta_destino, exist_ok=True)

ruta_temp = kagglehub.dataset_download("atharvasoundankar/spotify-global-streaming-data-2024")

print("✅ Descarga exitosa en carpeta temporal:", ruta_temp)

for archivo in os.listdir(ruta_temp):
    origen = os.path.join(ruta_temp, archivo)
    destino = os.path.join(ruta_destino, archivo)
    shutil.copy2(origen, destino)

print("✅ Archivos movidos a:", ruta_destino)

csv_file = next((f for f in os.listdir(ruta_destino) if f.endswith('.csv')), None)

if csv_file:
    df = pd.read_csv(os.path.join(ruta_destino, csv_file))
    print("✅ Primeras filas del archivo:")
    print(df.head())
else:
    print("❌ No se encontró ningún archivo CSV en la carpeta destino.")
