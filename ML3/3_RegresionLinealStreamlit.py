# Importar librerías necesarias
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Cargar el dataset
dataset = pd.read_csv('df/Salary_Data.csv')

# Validar si hay valores nulos en el dataset
if dataset.isnull().values.any():
    st.warning("El dataset contiene valores nulos. Por favor, revisa los datos.")
else:
    st.success("El dataset no tiene valores nulos. Continuando con el análisis...")

# Definir variables independientes (X) y dependientes (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Dividir el dataset en conjunto de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Escalado de variables (opcional)
scaler = StandardScaler()
use_scaling = False  # Cambiar a True si se desea escalar las variables

if use_scaling:
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    st.info("Las variables han sido escaladas.")
else:
    st.info("No se ha aplicado escalado de variables.")

# Crear el modelo de Regresión Lineal Simple con el conjunto de entrenamiento
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predecir el conjunto de test
y_pred = regression.predict(X_test)

# Calcular y mostrar las métricas de evaluación
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

st.write(f"Error Absoluto Medio (MAE): {mae:.2f}")
st.write(f"Error Cuadrático Medio (MSE): {mse:.2f}")
st.write(f"Coeficiente de Determinación (R²): {r2:.2f}")

# Visualizar los resultados del conjunto de entrenamiento con Plotly Express
fig_train = px.scatter(x=X_train.flatten(), y=y_train, title="Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)",
                        labels={'x': "Años de Experiencia", 'y': "Sueldo (en $)"})
fig_train.add_scatter(x=X_train.flatten(), y=regression.predict(X_train), mode='lines', name='Ajuste del modelo', line=dict(color='blue'))
st.plotly_chart(fig_train)

# Visualizar los resultados del conjunto de test con Plotly Express
fig_test = px.scatter(x=X_test.flatten(), y=y_test, title="Sueldo vs Años de Experiencia (Conjunto de Testing)",
                       labels={'x': "Años de Experiencia", 'y': "Sueldo (en $)"})
fig_test.add_scatter(x=X_train.flatten(), y=regression.predict(X_train), mode='lines', name='Ajuste del modelo', line=dict(color='blue'))
st.plotly_chart(fig_test)

# Sección para hacer pruebas con el modelo
st.sidebar.header("Prueba de Predicción")
years_of_experience = st.sidebar.number_input("Introduce los años de experiencia:", min_value=0.0, max_value=50.0, value=1.0, step=0.1)

# Hacer la predicción
predicted_salary = regression.predict(np.array([[years_of_experience]]))

st.sidebar.write(f"Predicción del sueldo para {years_of_experience} años de experiencia: ${predicted_salary[0]:.2f}")
