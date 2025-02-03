import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from joblib import dump, load

# Configuración inicial de la página de Streamlit
st.set_page_config(page_title="Bike Gear", layout="wide")

# Cargar los datos

data_p = pd.read_excel("df/DatosBikeGear.xlsx", header=0)  # Cambia a la ruta correcta del archivo
data_p.drop(['indice', 'Mes', 'Año',' Fecha', 'Costo Unitario', 'Precio Unitario', 'Categoria del Producto','Costo', 'Ingresos'], axis=1, inplace=True)


# Cargar el dataset
# data_p = ... # Asegúrate de cargar tu dataset aquí

# Definir los modelos disponibles
model_files = {
    "Random Forest": "Random_Forest_model.joblib",
    "Gradient Boosting": "Gradient_Boosting_model.joblib",
    "XGBoost": "XGBoost_model.joblib"
}

# Selección de modelo por parte del usuario
st.write("## Selecciona el Modelo para la Predicción")
selected_model_name = st.selectbox("Selecciona el Modelo", options=model_files.keys())

# Cargar el modelo seleccionado
model_filename = model_files[selected_model_name]
loaded_model = load(model_filename)
st.write(f"Modelo {selected_model_name} cargado exitosamente.")

# Mostrar métricas de evaluación si ya se tiene X_test e y_test
# X_test, y_test deben ser previamente definidos en tu pipeline de datos
# y_pred_loaded = loaded_model.predict(X_test)
# rmse_loaded = np.sqrt(mean_squared_error(y_test, y_pred_loaded))
# st.write(f"RMSE del modelo {selected_model_name} cargado: {rmse_loaded:.2f}")

# Input de usuario para predicciones usando selectboxes
st.write("## Realizar una Predicción")

# Generar combos para la selección de valores de las características
user_input = {
    ##"Año": st.selectbox("Año", sorted(data_p["Año"].unique())),
    ##"Mes": st.selectbox("Mes", sorted(data_p["Mes"].unique())),
    "Edad del Cliente": st.selectbox("Edad del Cliente", sorted(data_p["Edad del Cliente"].unique())),
    "Genero del Cliente": st.selectbox("Género del Cliente", sorted(data_p["Genero del Cliente"].unique())),
    "Ciudad": st.selectbox("Ciudad", sorted(data_p["Ciudad"].unique())),
    "Sucursal": st.selectbox("Sucursal", sorted(data_p["Sucursal"].unique())),
   # "Categoria del Producto": st.selectbox("Categoria del Producto", sorted(data_p["Categoria del Producto"].unique())),
    "Producto": st.selectbox("Producto", sorted(data_p["Producto"].unique()))
}



from sklearn.preprocessing import LabelEncoder

# Realizar codificación Label Encoding para cada columna categórica
label_encoders = {}
for column in data_p.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    data_p[column] = label_encoders[column].fit_transform(data_p[column])

# Convertir el input del usuario a DataFrame y realizar la transformación usando LabelEncoders
user_input_df = pd.DataFrame([user_input])
for column, encoder in label_encoders.items():
    user_input_df[column] = encoder.transform(user_input_df[column])

# Realizar la predicción con el modelo seleccionado
prediction = loaded_model.predict(user_input_df)

# Mostrar la predicción
st.write(f"### Predicción de Cantidad con {selected_model_name}: {prediction[0]:.2f}")
st.write(f"### Predicción de Cantidad con {selected_model_name}: {round(prediction[0],0)}")
