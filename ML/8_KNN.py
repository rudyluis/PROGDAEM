import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor

# Configuración inicial de la página de Streamlit
st.set_page_config(page_title="Regresión KNN para Vehículos", layout="wide")
st.title("Regresión KNN para Estimar Precios de Vehículos")

# Cargar datos
st.header("1. Cargar y Visualizar Datos")
st.write("Sube un archivo CSV con datos de vehículos, que incluya las columnas `kms` y `precio`.")
uploaded_file = st.file_uploader("Subir archivo CSV", type=["csv"])

if uploaded_file:
    carros = pd.read_csv(uploaded_file)
    st.write("Datos cargados:")
    st.dataframe(carros.head())

    # Graficar datos crudos: kms vs precio
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    ax[0].scatter(carros["kms"], carros["precio"], marker="*", 
                  s=100, c=range(carros["kms"].size), alpha=0.6)
    ax[0].set_title("Originales", size=18, color="purple")
    ax[0].set_ylabel("Precio ($)", size=14)
    ax[0].set_xlabel("Kms recorridos", size=14)
    ax[0].ticklabel_format(style="plain")

    # Escalamiento de los datos
    escala_kms = preprocessing.MinMaxScaler()
    escala_precio = preprocessing.MinMaxScaler()
    kms = escala_kms.fit_transform(carros["kms"].values.reshape(-1, 1))
    precio = escala_precio.fit_transform(carros["precio"].values.reshape(-1, 1))

    # Graficar datos escalados: kms vs precio
    ax[1].scatter(kms, precio, marker="*", 
                  s=100, c=range(kms.size), alpha=0.6)
    ax[1].set_title("Escalados", size=18, color="purple")
    ax[1].set_ylabel("Precio (escalado)", size=14)
    ax[1].set_xlabel("Kms recorridos (escalado)", size=14)
    ax[1].ticklabel_format(style="plain")

    st.pyplot(fig)

    # Entrenamiento del modelo KNN
    st.header("2. Entrenamiento del Modelo KNN")
    st.write("El modelo se entrena usando los datos escalados de `kms` y `precio`.")
    knn = KNeighborsRegressor(n_neighbors=3)
    knn.fit(kms, precio)
    st.write("Modelo entrenado con éxito!")

    # Sección de prueba interactiva
    st.header("3. Realizar Predicciones")
    kms_input = st.number_input("Ingresa los kms recorridos para estimar el precio:", min_value=0, max_value=500000, step=1000, value=20000)
    if kms_input:
        # Transformar y predecir el precio para los kms ingresados
        kms_instancia = escala_kms.transform([[kms_input]])
        precio_predicho = knn.predict(kms_instancia)
        precio_predicho_inverso = escala_precio.inverse_transform(precio_predicho)
        st.write(f"Predicción de precio para {kms_input} kms recorridos: **${precio_predicho_inverso[0][0]:.2f}**")

    # Múltiples regresiones de los valores dentro del rango
    st.header("4. Predicciones para Rango de Kilómetros")
    st.write("Visualiza la regresión para todos los kilómetros dentro del rango de los datos.")

    kms_instancias = escala_kms.transform(np.arange(carros["kms"].max()).reshape(-1, 1))
    precio_instancias = knn.predict(kms_instancias)
    todas = escala_precio.inverse_transform(precio_instancias)

    # Graficar los resultados de las múltiples regresiones
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(np.arange(carros["kms"].max()), todas, 
            linewidth=3, color="red", alpha=0.7, label="Regresión KNN")
    ax.scatter(carros["kms"], carros["precio"], marker="*", 
               s=100, c=range(carros["kms"].size), alpha=0.6, label="Datos Originales")
    ax.set_title("Vehículos - KNN Regresión", size=20, color="purple")
    ax.set_ylabel("Precio ($)", size=14)
    ax.set_xlabel("Kms recorridos", size=14)
    ax.ticklabel_format(style="plain")
    ax.legend()
    st.pyplot(fig)

    st.header("5. Análisis y Conclusiones")
    st.write("""
    - **Datos Crudos vs Escalados**: En la primera gráfica, los datos originales muestran la relación entre los kilómetros recorridos y el precio del vehículo.
    - **Escalamiento**: El escalamiento normaliza los datos, lo cual es útil para modelos que se ven afectados por la escala de los valores.
    - **Regresión KNN**: La línea roja en la gráfica muestra la estimación del precio para distintos valores de kilómetros.
    - **Pruebas Interactivas**: La sección de predicciones permite al usuario introducir un valor de kilómetros y obtener una predicción del precio.
    """)

else:
    st.warning("Por favor, sube un archivo CSV para continuar.")
