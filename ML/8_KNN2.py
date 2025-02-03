import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Configuración inicial de la página de Streamlit
st.set_page_config(page_title="Regresión KNN para Vehículos", layout="wide")
st.title("Regresión KNN para Estimar Precios de Vehículos")

# Cargar datos
st.header("1. Cargar y Validar Datos")
st.write("Sube un archivo CSV con datos de vehículos, que incluya las columnas `kms` y `precio`.")
uploaded_file = st.file_uploader("Subir archivo CSV", type=["csv"])

if uploaded_file:
    # Leer los datos
    try:
        carros = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error al leer el archivo CSV: {e}")
        st.stop()

    # Verificar que las columnas requeridas existan
    if not {'kms', 'precio'}.issubset(carros.columns):
        st.error("El archivo CSV debe contener las columnas 'kms' y 'precio'.")
        st.stop()

    # Eliminar filas con valores nulos
    carros = carros.dropna(subset=['kms', 'precio'])

    # Verificar que no haya valores negativos
    if (carros['kms'] < 0).any() or (carros['precio'] < 0).any():
        st.error("Los valores de 'kms' y 'precio' deben ser positivos.")
        st.stop()

    st.write("Datos cargados y validados:")
    st.dataframe(carros.head())

    # Graficar histogramas de kms y precio
    st.subheader("Distribución de los datos originales")
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].hist(carros["kms"], bins=20, color='blue', alpha=0.7)
    ax[0].set_title("Distribución de Kms", size=18)
    ax[0].set_xlabel("Kms recorridos", size=14)
    ax[0].set_ylabel("Frecuencia", size=14)

    ax[1].hist(carros["precio"], bins=20, color='green', alpha=0.7)
    ax[1].set_title("Distribución de Precio", size=18)
    ax[1].set_xlabel("Precio ($)", size=14)
    ax[1].set_ylabel("Frecuencia", size=14)

    st.pyplot(fig)


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

    # Escalamiento de los datos
    escala_kms = preprocessing.MinMaxScaler()
    escala_precio = preprocessing.MinMaxScaler()
    kms = escala_kms.fit_transform(carros["kms"].values.reshape(-1, 1))
    precio = escala_precio.fit_transform(carros["precio"].values.reshape(-1, 1))

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

    # Cálculo de métricas de error
    st.header("5. Evaluación del Modelo")
    precio_pred = escala_precio.inverse_transform(knn.predict(kms))
    mae = mean_absolute_error(carros["precio"], precio_pred)
    mse = mean_squared_error(carros["precio"], precio_pred)
    rmse = np.sqrt(mse)

    st.write(f"- **MAE (Error Absoluto Medio):** {mae:.2f}")
    st.write(f"- **MSE (Error Cuadrático Medio):** {mse:.2f}")
    st.write(f"- **RMSE (Raíz del Error Cuadrático Medio):** {rmse:.2f}")

    from sklearn.metrics import r2_score

    # Calcular R^2
    r2 = r2_score(carros["precio"], escala_precio.inverse_transform(knn.predict(kms)))
    st.write(f"- **Coeficiente de determinación (R^2):** {r2:.2f}")


    # Gráfico de errores
    st.subheader("Gráfico de Errores")
    errores = carros["precio"] - precio_pred.flatten()
    fig, ax = plt.subplots()
    ax.hist(errores, bins=20, color='orange', alpha=0.7)
    ax.set_title("Distribución de Errores de Predicción", size=18)
    ax.set_xlabel("Error (Real - Predicho)", size=14)
    ax.set_ylabel("Frecuencia", size=14)
    st.pyplot(fig)

    st.header("6. Análisis y Conclusiones")
    st.write("""
    - **Validaciones Realizadas**: Aseguramos que los datos no contengan valores nulos ni negativos.
    - **Distribución de los Datos**: Los histogramas muestran la distribución de kilómetros y precios.
    - **Escalamiento y Modelo KNN**: El modelo fue entrenado con datos normalizados para un mejor rendimiento.
    - **Evaluación del Modelo**: Las métricas MAE, MSE y RMSE nos ayudan a entender la precisión de nuestras predicciones.
    - **Gráfico de Errores**: Nos muestra la distribución de los errores, ayudando a identificar sesgos en las predicciones.
    """)

else:
    st.warning("Por favor, sube un archivo CSV para continuar.")
