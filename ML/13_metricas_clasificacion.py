import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Definición de funciones
def metricas(clases_reales, clases_predichas):
    """ Calcular las métricas utilizando sklearn """
    st.write(clases_reales)
    st.write(clases_predichas)
    matriz = confusion_matrix(clases_reales, clases_predichas)
    accuracy = accuracy_score(clases_reales, clases_predichas)
    precision = precision_score(clases_reales, clases_predichas)
    recall = recall_score(clases_reales, clases_predichas)
    f1 = f1_score(clases_reales, clases_predichas)
    return matriz, accuracy, precision, recall, f1

def visualiza_metricas(clases_reales, clases_predichas, titulo):
    """ Visualiza la matriz de confusión y métricas """
    
    # Cálculo de métricas
    matriz, accuracy, precision, recall, f1 = metricas(clases_reales, clases_predichas)
    
    # Visualización con Matplotlib
    fig, ax = plt.subplots(figsize=(4, 4))
    matriz_df = pd.DataFrame(matriz, index=["Reprueba", "Aprueba"], columns=["Reprueba", "Aprueba"])
    cax = ax.matshow(matriz_df, cmap="Blues", alpha=0.7)
    plt.colorbar(cax)
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            ax.text(x=j, y=i, s=matriz[i, j], va='center', ha='center', size='xx-large')
    
    # Configuración de etiquetas
    ax.set_xlabel("Predicción")
    ax.set_ylabel("Real")
    ax.set_title(titulo, color="red", fontsize=18)

    # Mostrar métricas en Streamlit
    st.pyplot(fig)
    st.write("### Métricas de Rendimiento")
    st.write(f"- **Exactitud (Accuracy)**: {accuracy:.2f}")
    st.write(f"- **Precisión**: {precision:.2f}")
    st.write(f"- **Sensibilidad (Recall)**: {recall:.2f}")
    st.write(f"- **F1-Score**: {f1:.2f}")

# Aplicación en Streamlit
st.title("Visualización de Métricas de Clasificación")
st.write("Este ejemplo ilustra cómo varían las métricas de un clasificador bajo diferentes escenarios de predicción.")

# Escenarios de clasificación
escenarios = {
    "Perfecto": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    "Erróneo": [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    "Indeciso": [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    "Reprobador": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Pasador": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

# Selección del escenario
escenario = st.selectbox("Selecciona el tipo de clasificador", list(escenarios.keys()))
clases_reales = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

clases_predichas = escenarios[escenario]

# Visualizar métricas para el escenario seleccionado
visualiza_metricas(clases_reales, clases_predichas, escenario)
