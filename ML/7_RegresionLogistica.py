import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import pandas as pd
# Configuración de la página en Streamlit
st.set_page_config(page_title="Regresion Logistica ", page_icon=":heart:", layout="wide")
# Título de la aplicación
st.title("Análisis de Frecuencia Cardíaca y Taquicardia con Regresión Logística")

# Datos de frecuencia cardíaca
frecuencias_cardiacas = [[65], [70], [80], [80], [80],
                         [90], [95], [100], [105], [110],
                         [105], [110], [110], [120], [120],
                         [130], [140], [180], [185], [190]]

clase = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Leer el archivo CSV
# Supongamos que el archivo se llama 'frecuencias_cardiacas.csv' y tiene dos columnas: 'frecuencia' y 'clase'.
dataset = pd.read_csv('df/frecuencias_cardiacas.csv')

# Extraer las características y la variable de clase
frecuencias_cardiacas = dataset[['frecuencia']].values  # Tomamos la columna 'frecuencia' como matriz
clase = dataset['clase'].values  # Tomamos la columna 'clase' como vector

# Creamos conjuntos de entrenamiento y de prueba del modelo
datos_entrena, datos_prueba, clase_entrena, clase_prueba = \
    train_test_split(frecuencias_cardiacas, clase, test_size=0.30, random_state=42)

# Creamos el modelo de Regresión Logística
modelo = LogisticRegression().fit(datos_entrena, clase_entrena)

# Predicciones y probabilidades
predicciones = modelo.predict(datos_prueba)
probalidades = modelo.predict_proba(datos_prueba)

# Validaciones
st.subheader("Resultados del Modelo")
st.write("Predicciones:", predicciones.tolist())
st.write("Probabilidades de clase (Normal y Taquicardia):", probalidades.tolist())
st.write("Precisión del modelo:", modelo.score(datos_prueba, clase_prueba))

# Matrices de confusión
cm = confusion_matrix(clase_prueba, predicciones)
st.subheader("Matriz de Confusión")
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
ax.set_xlabel('Predicción')
ax.set_ylabel('Realidad')
ax.set_xticklabels(['Normal', 'Taquicardia'])
ax.set_yticklabels(['Normal', 'Taquicardia'])
st.pyplot(fig)

# Reporte de clasificación
st.subheader("Reporte de Clasificación")
st.text(classification_report(clase_prueba, predicciones))

# Gráfica de la función logística
st.subheader("Función Logística")
b0 = modelo.intercept_[0]
b1 = modelo.coef_[0][0]

# Gráfica de la función logística
x_values = np.arange(60, 200, 0.1)
y_values = 1 / (1 + np.exp(-(b0 + b1 * x_values)))

plt.figure(figsize=(8, 4))
plt.plot(x_values, y_values, color='blue', label='Función Logística')
plt.title("Función Logística de Predicción de Taquicardia", fontsize=14.0)
plt.ylabel("Probabilidad de Taquicardia", fontsize=13.0)
plt.xlabel("Frecuencia cardíaca (latidos por minuto)", fontsize=13.0)
plt.axhline(y=0.5, color='r', linestyle='--', label='Umbral 0.5')
plt.legend()
st.pyplot(plt)

# Sección para prueba de información
st.sidebar.subheader("Prueba de Información Nueva")
frecuencia_nueva = st.sidebar.number_input("Ingrese la frecuencia cardíaca (latidos por minuto):", min_value=60, max_value=220)

if st.sidebar.button("Predecir Taquicardia"):
    probabilidad = 1 / (1 + np.exp(-(b0 + b1 * frecuencia_nueva)))
    prediccion = "Taquicardia" if probabilidad >= 0.5 else "Normal"
    st.sidebar.write(f"La probabilidad de taquicardia para una frecuencia de {frecuencia_nueva} bpm es: {probabilidad:.2f}")
    st.sidebar.write(f"La predicción es: {prediccion}")

# Finaliza la aplicación
st.sidebar.write("¡Gracias por usar el análisis de frecuencia cardíaca!")
