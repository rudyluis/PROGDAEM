import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
# Verificar la instalación
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("Keras version:", tf.keras.__version__)

# Cargar los datos
columnas = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'diagnostico'
]
data = pd.read_csv('https://raw.githubusercontent.com/rudyluis/DataCSV/main/processed.cleveland.csv', names=columnas, na_values="?")

# Descripción de los datos
print(data.describe())

# Transformar la columna 'diagnostico' a valores binarios
data['diagnostico'] = data['diagnostico'].apply(lambda x: int(x > 0))

# Imprimir la tabla de datos procesados
print(data)

# Preparación de los Datos de Entrenamiento
X = data.drop('diagnostico', axis=1)
Y = data['diagnostico']

# Verificar valores nulos en Y
print("Valores nulos en Y:", Y.isnull().sum())

# Verificar valores nulos en X
print("Valores nulos en X:\n", X.isnull().sum())

# Llenar valores nulos en X
X = X.fillna(-1)
print("Valores nulos en X después de llenar:\n", X.isnull().sum())

# Verificar las dimensiones de X
print("Columnas de X:", X.columns)
print("Dimensiones de X:", X.shape)

# Convertir X y Y a matrices numpy
X = X.values
Y = Y.values

# Establecimiento de la Arquitectura de la Red
model = Sequential()
model.add(Input(shape=(13,)))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Imprimir el resumen del modelo
model.summary()

# Entrenar el modelo
model.fit(X, Y, validation_split=0.1, epochs=150, batch_size=10)
