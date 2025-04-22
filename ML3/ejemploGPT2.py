import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Título de la aplicación
st.title("Generación de Texto en Español con GPT-2")

# Cargar modelo y tokenizador preentrenados en español
@st.cache_resource  # Cache para mejorar el rendimiento
def load_model():
    model_name = "datificate/gpt2-small-spanish"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()

# Entrada del usuario
prompt = st.text_input("Escribe una frase para que el modelo continúe:", "Hola, ¿cómo estás?")

# Configuración de parámetros de generación
max_length = st.slider("Longitud máxima del texto generado", min_value=50, max_value=300, value=100)
temperature = st.slider("Temperatura (controla la creatividad)", min_value=0.1, max_value=1.0, value=0.7)
top_k = st.slider("Top-K (reduce opciones menos probables)", min_value=1, max_value=100, value=50)
top_p = st.slider("Top-P (nucleus sampling)", min_value=0.1, max_value=1.0, value=0.9)

# Generar texto al hacer clic en el botón
if st.button("Generar Texto"):
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    outputs = model.generate(
        inputs,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        num_return_sequences=1,
        no_repeat_ngram_size=2
    )

    # Decodificar la salida del modelo
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Mostrar el texto generado
    st.subheader("Texto Generado:")
    st.write(generated_text)
