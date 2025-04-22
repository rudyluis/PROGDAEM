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
# Cargar el modelo entrenado
model = tf.keras.models.load_model("ModeloSentimientosEntrenado.h5")
st.success("Modelo Cargado Correctamente....")

# Interfaz para ingresar texto para predicción
st.subheader("Prueba de Predicción")

review = st.text_area("Ingrese una reseña de película:")
num_words = 10000
if review:
    # Preprocesar el texto ingresado
    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts([review])
    review_sequence = tokenizer.texts_to_sequences([review])
    review_padded = pad_sequences(review_sequence, maxlen=200)

    # Realizar la predicción
    prediction = model.predict(review_padded)
    sentiment = "Positivo" if prediction >= 0.5 else "Negativo"

    st.write(f"La reseña es clasificada como: {sentiment} con una probabilidad de {prediction[0][0]:.2f}")


