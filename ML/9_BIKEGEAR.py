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
@st.cache_data
def load_data():
    data = pd.read_excel("df/DatosBikeGear.xlsx", header=0)  # Cambia a la ruta correcta del archivo
    return data

data = load_data()
data_p =data.copy()
# Título de la app
st.title("Predicción de Cantidad con Machine Learning")

# Mostrar los primeros registros

with st.expander("## Vista de los primeros registros"):
    st.write(data.head())

# Eliminar múltiples columnas innecesarias
data.drop(['indice', 'Mes', 'Año',' Fecha', 'Costo Unitario', 'Precio Unitario','Categoria del Producto', 'Costo', 'Ingresos'], axis=1, inplace=True)

from sklearn.preprocessing import LabelEncoder

# Realizar codificación Label Encoding para cada columna categórica
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])



# Si prefieres One-Hot Encoding, puedes usar:
# data = pd.get_dummies(data, drop_first=True)

with st.expander("Datos transformados:"):
    st.write(data)

### standarizar

# Matriz de correlación
st.write("## Matriz de Correlación")

# Selección dinámica de columnas para la matriz de correlación
st.write("### Selección de columnas para la matriz de correlación")
selected_columns = st.multiselect("Selecciona las columnas para la matriz de correlación", options=data.columns, default=data.columns[:5])

# Calcular la matriz de correlación para las columnas seleccionadas
if len(selected_columns) >= 2:
    correlation_matrix = data[selected_columns].corr()
    
    # Visualizar la matriz de correlación actualizada
    st.write("## Matriz de Correlación Actualizada")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.write("Por favor, selecciona al menos dos columnas para calcular la matriz de correlación.")




# Selección de características
X = data.iloc[:, :-1]
y = data["Cantidad"]

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Parámetros ajustables por el usuario
st.write("## Variables de Evaluación")
col_a, col_b , col_c= st.columns(3)
with col_a:
    n_estimators = st.slider("Número de Árboles (n_estimators)", 10, 300, 100)
with col_b:
    max_depth = st.slider("Profundidad Máxima (max_depth)", 2, 20, 10)
with col_c:
    min_samples_split = st.slider("Mínimo de muestras para dividir (min_samples_split)", 2, 10, 2)

# Modelos de regresión
models = {
    "Random Forest": RandomForestRegressor(
        n_estimators=n_estimators, max_depth=max_depth, min_samples_split=min_samples_split, random_state=42
    ),
    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=n_estimators, max_depth=max_depth, min_samples_split=min_samples_split, random_state=42
    ),
    "XGBoost": XGBRegressor(
        n_estimators=n_estimators, max_depth=max_depth, learning_rate=0.1, random_state=42
    )
}

# Entrenar y evaluar cada modelo
results = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    cv_score = cross_val_score(model, X, y, cv=5, scoring="neg_mean_squared_error")
    cv_rmse = np.sqrt(-cv_score.mean())
    results[model_name] = {"RMSE": rmse, "R2": r2, "CV_RMSE": cv_rmse}

    # Guardar el modelo entrenado
    model_filename = f"{model_name.replace(' ', '_')}_model.joblib"
    dump(model, model_filename)
    st.write(f"Modelo {model_name} guardado como {model_filename}")

# Mostrar los resultados en un DataFrame
results_df = pd.DataFrame(results).T
st.write("## Resultados de los Modelos")
st.write(results_df)

# Gráfico de barras de las métricas de rendimiento
fig = px.bar(
    results_df, 
    x=results_df.index, 
    y="RMSE", 
    title="Comparación de RMSE entre Modelos", 
    labels={"x": "Modelo", "y": "RMSE"}, 
    color="RMSE"
)
st.plotly_chart(fig)

# Input de usuario para predicciones usando selectboxes
st.write("## Realizar una Predicción")

# Generar combos para la selección de valores de las características
user_input = {
    "Año": st.selectbox("Año", sorted(data_p["Año"].unique())),
    "Mes": st.selectbox("Mes", sorted(data_p["Mes"].unique())),
    "Edad del Cliente": st.selectbox("Edad del Cliente", sorted(data_p["Edad del Cliente"].unique())),
    "Genero del Cliente": st.selectbox("Género del Cliente", sorted(data_p["Genero del Cliente"].unique())),
    "Ciudad": st.selectbox("Ciudad", sorted(data_p["Ciudad"].unique())),
    "Sucursal": st.selectbox("Sucursal", sorted(data_p["Sucursal"].unique())),
    "Categoria del Producto": st.selectbox("Categoria del Producto", sorted(data_p["Categoria del Producto"].unique())),
    "Producto": st.selectbox("Producto", sorted(data_p["Producto"].unique()))
}

# Convertir el input del usuario a DataFrame y realizar la transformación usando LabelEncoders
user_input_df = pd.DataFrame([user_input])
for column, encoder in label_encoders.items():
    user_input_df[column] = encoder.transform(user_input_df[column])

# Selección de modelo para predecir
selected_model_name = st.selectbox("Selecciona el Modelo para la Predicción", options=models.keys())
selected_model = models[selected_model_name]

# Realizar la predicción
prediction = selected_model.predict(user_input_df)

# Mostrar la predicción
st.write(f"### Predicción de Cantidad con {selected_model_name}: {prediction[0]:.2f}")

