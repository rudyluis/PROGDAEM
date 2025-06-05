import pandas as pd
from pymongo import MongoClient

# 1. URL del CSV externo
CSV_URL = "https://raw.githubusercontent.com/rudyluis/DashboardJS/refs/heads/main/video_games_sales.csv"

# 2. Leer el CSV con pandas
df = pd.read_csv(CSV_URL)

# 3. Conexión a MongoDB Atlas
# Reemplaza <usuario>, <contraseña> y <cluster> con tus valores reales

#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient("mongodb+srv://rmanzanedav0001:lGSisb4y4HEoLWTa@cluster0.2eo714p.mongodb.net/")

# 4. Seleccionar base de datos y colección
db = client["videojuegos"]  # Nombre de la base de datos
collection = db["ventas"]   # Nombre de la colección

# 5. Convertir el DataFrame a un diccionario y cargarlo
data = df.to_dict(orient="records")
collection.insert_many(data)

print("Migración completa. Total de registros insertados:", len(data))
