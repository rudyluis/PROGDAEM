import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Crear el DataFrame con valores faltantes
data = {
    'Producto': ['TV', 'Refrigerador', 'Smartphone', 'Auriculares', 'Laptop', 'Galletas', 'Cereal'],
    'Precio': [500, 800, np.nan, 50, 1200, 2, np.nan],
    'Ventas_Mensuales': [20, np.nan, 50, 200, np.nan, 500, np.nan],
    'Categoría': ['Electrónica', 'Electrónica', 'Electrónica', 'Electrónica', 'Electrónica', 'Alimentos', 'Alimentos'],
    'Inventario_Disponible': [15, 10, np.nan, 100, 5, 300, 150]
}

df = pd.DataFrame(data)
df_copy2=df.copy()
# Mostrar el dataset original
print("Datos originales con valores faltantes:")
print(df)

imputer= SimpleImputer(strategy='mean')
df[['Precio','Ventas_Mensuales','Inventario_Disponible']]=imputer.fit_transform(df[['Precio','Ventas_Mensuales','Inventario_Disponible']])

print('\n Datos despues de la imputacion simple ')
print(df)

######MAECI


df_mice=df_copy2.copy()

from sklearn.experimental import enable_iterative_imputer  # Necesario para activar el iterador
from sklearn.impute import IterativeImputer

imputer_mice= IterativeImputer(max_iter=10, random_state=0)
df_mice[['Precio','Ventas_Mensuales','Inventario_Disponible']]=imputer_mice.fit_transform(df_mice[['Precio','Ventas_Mensuales','Inventario_Disponible']])

print('\n Datos despues de la imputacion por Algoritmo de MICE ')
print(df_mice)