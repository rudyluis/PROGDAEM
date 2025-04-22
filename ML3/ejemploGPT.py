import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Título de la aplicación
st.title("🤖 Chatbot para Inscripción en la Universidad")

# Cargar el modelo y el tokenizador
@st.cache_resource
def load_model():
    model_name = "DeepESP/gpt2-spanish"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()

# Historial de conversación
if "history" not in st.session_state:
    st.session_state.history = []

# Base de Conocimientos
faq = {
    "requisitos": "Para inscribirte necesitas: copia de tu identificación, certificado de estudios previos, y pago de matrícula.",
    "fechas": "La inscripción está abierta del 15 de enero al 15 de marzo.",
    "contacto": "Para más información, escribe a admisiones@universidad.edu o llama al +123456789.",
}

# Entrada del usuario
user_input = st.text_input("Tú:", placeholder="¿Cómo puedo inscribirme?")

# Procesar la entrada del usuario y generar respuesta
if st.button("Enviar"):
    if user_input:
        # Buscar en la base de conocimientos primero
        respuesta = None
        for clave, valor in faq.items():
            if clave in user_input.lower():
                respuesta = valor
                break
        
        # Si no está en las FAQ, usar GPT para generar respuesta
        if not respuesta:
            st.session_state.history.append({"role": "user", "content": user_input})
            context = "\n".join([f"{entry['role']}: {entry['content']}" for entry in st.session_state.history])
            inputs = tokenizer.encode(context + "\nchatbot:", return_tensors="pt")
            outputs = model.generate(
                inputs,
                max_length=3000,
                temperature=0.7,
                top_p=0.9,
                top_k=50,
                pad_token_id=tokenizer.eos_token_id
            )
            respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True).split("chatbot:")[-1].strip()

        # Agregar respuesta del chatbot al historial
        st.session_state.history.append({"role": "chatbot", "content": respuesta})

# Mostrar el historial de conversación
st.subheader("Chat:")
for entry in st.session_state.history:
    if entry["role"] == "user":
        st.write(f"**Tú:** {entry['content']}")
    else:
        st.write(f"**Chatbot:** {entry['content']}")
