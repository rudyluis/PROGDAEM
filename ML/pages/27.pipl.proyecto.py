import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
from scipy.stats import randint

# Cargar los datos
data = pd.read_excel('df/copia.xlsx')

# Crear DataFrame
df = pd.DataFrame(data)
st.write(df)

# Label Encoding
le_año_mes = LabelEncoder()
le_nombre_tipo = LabelEncoder()
le_nombre_categoria = LabelEncoder()

df['año_mes'] = le_año_mes.fit_transform(df['año_mes']) + 1
df['nombre_tipo'] = le_nombre_tipo.fit_transform(df['nombre_tipo']) + 1
df['nombre_categoria'] = le_nombre_categoria.fit_transform(df['nombre_categoria']) + 1

st.write(df)

# Definir variables independientes (X) y dependientes (y)
X = df[['año_mes', 'nombre_tipo', 'nombre_categoria']]
y = df['cantidad_comprada']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de XGBoost
model = xgb.XGBRegressor(random_state=42, objective='reg:squarederror')

# Ajuste de Hiperparámetros con GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],  # Número de árboles
    'max_depth': [3, 6, 10],  # Profundidad máxima de los árboles
    'learning_rate': [0.01, 0.1, 0.3],  # Tasa de aprendizaje
    'subsample': [0.7, 0.8, 1],  # Proporción de muestras para cada árbol
    'colsample_bytree': [0.7, 0.8, 1]  # Fracción de características a considerar
}

# Crear el GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='neg_mean_absolute_error', n_jobs=-1, verbose=2)

# Ajustar el modelo con GridSearchCV
grid_search.fit(X_train, y_train)

# Mostrar los mejores parámetros encontrados
st.write("Mejores parámetros encontrados con GridSearchCV:", grid_search.best_params_)

# Evaluar el modelo ajustado
best_model_grid = grid_search.best_estimator_
y_pred_grid = best_model_grid.predict(X_test)

# Calcular las métricas
mae_grid = mean_absolute_error(y_test, y_pred_grid)
mse_grid = mean_squared_error(y_test, y_pred_grid)
rmse_grid = np.sqrt(mse_grid)
r2_grid = r2_score(y_test, y_pred_grid)

# Mostrar métricas de GridSearchCV
st.write("Error Absoluto Medio (MAE) con GridSearchCV:", mae_grid)
st.write("Error Cuadrático Medio (MSE) con GridSearchCV:", mse_grid)
st.write("Raíz del Error Cuadrático Medio (RMSE) con GridSearchCV:", rmse_grid)
st.write("Coeficiente de Determinación (R²) con GridSearchCV:", r2_grid)

# Ajuste de Hiperparámetros con RandomizedSearchCV
param_dist = {
    'n_estimators': randint(50, 200),  # Número de árboles (aleatorio entre 50 y 200)
    'max_depth': [3, 6, 10],  # Profundidad máxima de los árboles
    'learning_rate': [0.01, 0.1, 0.3],  # Tasa de aprendizaje
    'subsample': randint(70, 100) / 100,  # Proporción de muestras para cada árbol
    'colsample_bytree': randint(70, 100) / 100  # Fracción de características a considerar
}

# Crear el RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=100, cv=5, scoring='neg_mean_absolute_error', n_jobs=-1, verbose=2, random_state=42)

# Ajustar el modelo con RandomizedSearchCV
random_search.fit(X_train, y_train)

# Mostrar los mejores parámetros encontrados
st.write("Mejores parámetros encontrados con RandomizedSearchCV:", random_search.best_params_)

# Evaluar el modelo ajustado
best_model_random = random_search.best_estimator_
y_pred_random = best_model_random.predict(X_test)

# Calcular las métricas
mae_random = mean_absolute_error(y_test, y_pred_random)
mse_random = mean_squared_error(y_test, y_pred_random)
rmse_random = np.sqrt(mse_random)
r2_random = r2_score(y_test, y_pred_random)

# Mostrar métricas de RandomizedSearchCV
st.write("Error Absoluto Medio (MAE) con RandomizedSearchCV:", mae_random)
st.write("Error Cuadrático Medio (MSE) con RandomizedSearchCV:", mse_random)
st.write("Raíz del Error Cuadrático Medio (RMSE) con RandomizedSearchCV:", rmse_random)
st.write("Coeficiente de Determinación (R²) con RandomizedSearchCV:", r2_random)

# Entrada de usuario para predicción
st.sidebar.header("Entrada de datos")
año_mes_input = st.sidebar.selectbox("Seleccione Año-Mes", le_año_mes.classes_)
nombre_tipo_input = st.sidebar.selectbox("Seleccione Nombre Tipo", le_nombre_tipo.classes_)
nombre_categoria_input = st.sidebar.selectbox("Seleccione Nombre Categoria", le_nombre_categoria.classes_)

# Transformar las entradas con el LabelEncoder
año_mes_input_encoded = le_año_mes.transform([año_mes_input])[0]
nombre_tipo_input_encoded = le_nombre_tipo.transform([nombre_tipo_input])[0]
nombre_categoria_input_encoded = le_nombre_categoria.transform([nombre_categoria_input])[0]

# Realizar la predicción con el mejor modelo de GridSearchCV
prediction_grid = best_model_grid.predict([[año_mes_input_encoded, nombre_tipo_input_encoded, nombre_categoria_input_encoded]])

# Realizar la predicción con el mejor modelo de RandomizedSearchCV
prediction_random = best_model_random.predict([[año_mes_input_encoded, nombre_tipo_input_encoded, nombre_categoria_input_encoded]])

# Mostrar las predicciones
st.write(f"Predicción de cantidad comprada con GridSearchCV: {prediction_grid[0]:.2f}")
st.write(f"Predicción de cantidad comprada con RandomizedSearchCV: {prediction_random[0]:.2f}")
