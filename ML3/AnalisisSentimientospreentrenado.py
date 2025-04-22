import streamlit as st
from transformers import pipeline

# Configuración de la aplicación Streamlit
st.title("Análisis de Sentimientos con BERT")
st.subheader("Ingrese un texto y vea si tiene un sentimiento positivo o negativo.")

# Cargar el modelo de análisis de sentimientos preentrenado de Hugging Face
@st.cache_resource
def load_model():
    # Cargar el pipeline de análisis de sentimientos
    sentiment_analyzer = pipeline("sentiment-analysis")
    return sentiment_analyzer

# Usar el modelo cargado
sentiment_analyzer = load_model()

# Crear un área para ingresar el texto
input_text = st.text_area("Ingrese su texto aquí:")

# Si hay un texto ingresado, mostrar la predicción
if input_text:
    # Realizar el análisis de sentimientos
    result = sentiment_analyzer(input_text)
    
    # Mostrar el resultado
    sentiment = result[0]['label']
    confidence = result[0]['score']
    
    st.write(f"Sentimiento detectado: {sentiment}")
    st.write(f"Confianza: {confidence * 100:.2f}%")

    # Dar un mensaje adicional dependiendo del sentimiento
    if sentiment == 'POSITIVE':
        st.success("¡Parece un mensaje positivo! 😊")
    else:
        st.error("Parece un mensaje negativo. 😔")
