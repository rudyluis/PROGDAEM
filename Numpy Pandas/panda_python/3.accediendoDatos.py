#%%

import pandas as pd
import numpy as np
from io import StringIO

# Ruta del archivo CSV
file_path = "simple_data.csv"

#%% 
# Crear DataFrame, leer datos desde el CSV

# Cargar el archivo CSV en un DataFrame
dt = pd.read_csv(file_path)
print(dt)

#%% 
# Seleccionar columnas específicas

# Leer solo las columnas 'Imie' y 'wiek' desde el archivo CSV
dt = pd.read_csv(file_path, usecols=['Imie', 'wiek'])
print(dt.head())  # Mostrar las primeras filas

#%% 
# Convertir y castear los datos a un formato especial

# Leer el archivo CSV y especificar tipos de datos para las columnas
dt = pd.read_csv(file_path,
                 usecols=['Imie', 'wiek'],
                 dtype={'wiek': np.int16})  # Convertir 'wiek' a tipo entero de 16 bits
print(dt.head())  # Mostrar las primeras filas

#%% 
# Convertir los datos usando un convertidor personalizado

# Definir una función que multiplica el valor de 'Imie' por 5
def imie_converter(imie):
    return imie*5

# Leer el archivo CSV aplicando un convertidor personalizado
dt = pd.read_csv(file_path,
                 usecols=['Imie', 'wiek'],
                 dtype={'Imie': str, 'wiek': np.int8},  # Convertir 'Imie' a string y 'wiek' a tipo int8
                 converters={"Imie": imie_converter})  # Usar el convertidor definido para 'Imie'
print(dt)

# %%
