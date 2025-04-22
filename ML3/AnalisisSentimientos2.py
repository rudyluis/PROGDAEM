import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb

# Cargar el conjunto de datos IMDB de Keras
st.title("Entrenamiento de Modelo de Sentimientos con Keras")
st.subheader("Usando el dataset de reseñas de películas IMDB")

# Cargar los datos IMDB (50,000 reseñas etiquetadas como positivas o negativas)
num_words = 10000  # Solo consideraremos las 10,000 palabras más frecuentes
##(maxlen=200)  # Limitar a las 200 palabras más largas por reseña

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)

# Preprocesamiento de los datos
st.write("Preprocesando los datos...")

# Rellenamos las secuencias para tener una longitud uniforme
x_train = pad_sequences(x_train, maxlen=200)
x_test = pad_sequences(x_test, maxlen=200)

st.write("Datos preparados para entrenamiento")


# Crear el modelo con Keras
st.write("Creando el modelo...")

model = Sequential([
    Embedding(input_dim=num_words, output_dim=64, input_length=200),
    LSTM(128, return_sequences=True),
    GlobalAveragePooling1D(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')  # Salida para clasificación binaria
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

st.write("Modelo creado con éxito.")


# Entrenamiento del modelo
st.write("Entrenando el modelo...")

history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=64,
    validation_data=(x_test, y_test),
    verbose=1
)

# Mostrar el progreso del entrenamiento
st.write("Entrenamiento finalizado con éxito.")


import matplotlib.pyplot as plt

# Crear la figura para mostrar la evolución de la precisión y la pérdida
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Precisión
ax[0].plot(history.history['accuracy'], label='Precisión (train)')
ax[0].plot(history.history['val_accuracy'], label='Precisión (val)')
ax[0].set_title('Precisión')
ax[0].set_xlabel('Épocas')
ax[0].set_ylabel('Precisión')
ax[0].legend()

# Pérdida
ax[1].plot(history.history['loss'], label='Pérdida (train)')
ax[1].plot(history.history['val_loss'], label='Pérdida (val)')
ax[1].set_title('Pérdida')
ax[1].set_xlabel('Épocas')
ax[1].set_ylabel('Pérdida')
ax[1].legend()

# Mostrar los gráficos en Streamlit
st.pyplot(fig)


# Evaluar el modelo en el conjunto de test
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
st.write(f"Precisión en el conjunto de prueba: {test_acc * 100:.2f}%")
model.save('ModeloSentimientosEntrenado.h5')
st.success('Modelo Creado y entreando')