import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Definición de funciones
def metricas(clases_reales, clases_predichas):
    """ Calcular las métricas utilizando sklearn """
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
    
    # Visualización de la matriz de confusión con etiquetas
    plt.figure(figsize=(3, 3))
    matriz_df = pd.DataFrame(matriz, columns=["0 : Reprueba", "1 : Aprueba"], index=["0 : Reprueba", "1 : Aprueba"])
    plt.matshow(matriz_df, cmap="Blues", vmin=0, vmax=10, fignum=1)
    plt.title("Reales")
    plt.ylabel("Predichas")
    plt.xticks(range(len(matriz_df.columns)), matriz_df.columns, rotation=45)
    plt.yticks(range(len(matriz_df.index)), matriz_df.index)
    
    # Etiquetas dentro de la matriz
    etiquetas = [["Verdaderos\nnegativos", "Falsos\npositivos"],
                 ["Falsos\nnegativos", "Verdaderos\npositivos"]]
    
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            plt.text(j, i + 0.14, str(matriz[i, j]), fontsize=30, ha="center", va="center")
            plt.text(j, i - 0.25, etiquetas[i][j], fontsize=11.5, ha="center", va="center")
    plt.text(-1, 0, titulo, fontsize=25, color="red")
    
    # Mostrar matriz de confusión en Streamlit
    st.pyplot(plt)
    
    # Mostrar métricas y sus fórmulas en Streamlit
    st.write("### Métricas de Rendimiento")
    st.write(f"- **Exactitud (Accuracy)**: {accuracy:.2f}")
    st.latex(r"Accuracy = \frac{TP + TN}{TP + TN + FP + FN}")
    
    st.write(f"- **Precisión**: {precision:.2f}")
    st.latex(r"Precision = \frac{TP}{TP + FP}")
    
    st.write(f"- **Sensibilidad (Recall)**: {recall:.2f}")
    st.latex(r"Recall = \frac{TP}{TP + FN}")
    
    st.write(f"- **F1-Score**: {f1:.2f}")
    st.latex(r"F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}")

# Aplicación en Streamlit
st.title("Visualización de Métricas de Clasificación")
st.write("Este ejemplo ilustra cómo varían las métricas de un clasificador bajo diferentes escenarios de predicción. Selecciona un tipo de clasificador para ver las métricas.")

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
