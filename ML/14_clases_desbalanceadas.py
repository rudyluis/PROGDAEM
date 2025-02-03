import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Título y Descripción
st.title("Clasificación de Cáncer: Comparación de Sobremuestreo y Submuestreo")
st.write("""
Este análisis muestra cómo afectan distintas técnicas de muestreo a la precisión de un modelo de regresión logística para la detección de cáncer.
- **Desbalanceado**: Modelo entrenado con la cantidad de datos original.
- **Submuestreo**: Se reduce la cantidad de instancias de la clase mayoritaria (personas sanas).
- **Sobremuestreo**: Se incrementa la cantidad de instancias de la clase minoritaria (personas con cáncer) replicando datos.
""")

# Cargar los datos
personas = pd.read_csv("df/cancer_desbalance.csv", header=None)
prueba = pd.read_csv("df/cancer_prueba.csv", header=None)

# Gráfica de la distribución de datos
num_sanas = personas[personas[30] == 0][0].size
num_cancer = personas[personas[30] == 1][0].size
st.write("### Distribución de Datos Original")
st.bar_chart(pd.DataFrame({"Personas": [num_sanas, num_cancer]}, index=["Sanas", "Cáncer"]))

# Definir la función para visualizar la matriz de confusión
def mostrar_matriz_confusion(clases_reales, clases_predichas, titulo):
    """Visualiza la matriz de confusión y muestra la precisión"""
    matriz = confusion_matrix(clases_reales, clases_predichas)
    accuracy = accuracy_score(clases_reales, clases_predichas)

    fig, ax = plt.subplots()
    cax = ax.matshow(matriz, cmap="Pastel1")
    fig.colorbar(cax)

    # Etiquetas de la matriz de confusión
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Sana\n(Verdaderos Negativos)", "Cáncer\n(Verdaderos Positivos)"])
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Sana\n(Falsos Negativos)", "Cáncer\n(Falsos Positivos)"])
    plt.xlabel("Predicción")
    plt.ylabel("Real")
    plt.title(titulo)

    # Añadir valores a la matriz de confusión
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            ax.text(j, i, matriz[i, j], ha='center', va='center', color='black', fontsize=16)

    st.write(f"### {titulo}")
    st.pyplot(fig)
    st.write(f"**Precisión (Accuracy):** {accuracy:.2f}")

    # Mostrar clases reales y predichas en forma de tabla
    datos_tabla = pd.DataFrame({
        "Clases Reales": clases_reales.reshape(-1),
        "Clases Predichas": clases_predichas
    })
    with st.expander("### Clases Reales y Predichas"):
        st.write(datos_tabla)

# Preparación de datos de sobremuestreo y submuestreo
datos_cancer = personas[personas[30] == 1]
datos_sanas = personas[personas[30] == 0]

# Sobremuestreo
sobremuestreo_cancer = datos_cancer.sample(n=290, replace=True, random_state=0)
sobremuestro = pd.concat([sobremuestreo_cancer, datos_sanas])
datos_sobremuestreo = sobremuestro.iloc[:, :-1]
clase_sobremuestreo = sobremuestro.iloc[:, -1:]

# Submuestreo
submuestreo_sanas = datos_sanas.sample(n=20, replace=False, random_state=0)
submuestreo = pd.concat([datos_cancer, submuestreo_sanas])
datos_submuestreo = submuestreo.iloc[:, :-1]
clase_submuestreo = submuestreo.iloc[:, -1:]

# Datos de entrenamiento desbalanceados (originales)
desbalanceado = pd.concat([datos_cancer, datos_sanas])
datos_desbalanceado = desbalanceado.iloc[:, :-1]
clase_desbalanceado = desbalanceado.iloc[:, -1:]

# Datos de prueba
datos_prueba = prueba.iloc[:, :-1]
clase_prueba = prueba.iloc[:, -1:]

# Entrenamiento y evaluación para el modelo desbalanceado
st.write("## Resultados con Datos Desbalanceados")
modelo = LogisticRegression().fit(datos_desbalanceado, clase_desbalanceado.values.ravel())
predicciones_desbalanceado = modelo.predict(datos_prueba)
mostrar_matriz_confusion(clase_prueba.values, predicciones_desbalanceado, "Modelo Desbalanceado")

# Entrenamiento y evaluación para el modelo con submuestreo
st.write("## Resultados con Submuestreo")
modelo = LogisticRegression().fit(datos_submuestreo, clase_submuestreo.values.ravel())
predicciones_submuestreo = modelo.predict(datos_prueba)
mostrar_matriz_confusion(clase_prueba.values, predicciones_submuestreo, "Modelo con Submuestreo")

# Entrenamiento y evaluación para el modelo con sobremuestreo
st.write("## Resultados con Sobremuestreo")
modelo = LogisticRegression().fit(datos_sobremuestreo, clase_sobremuestreo.values.ravel())
predicciones_sobremuestreo = modelo.predict(datos_prueba)
mostrar_matriz_confusion(clase_prueba.values, predicciones_sobremuestreo, "Modelo con Sobremuestreo")
