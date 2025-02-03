# Importar librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

# Cargar el dataset
dataset = pd.read_csv('df/ingreso.csv')  # Cambia a la ruta de tu archivo
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Dividir el dataset en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Escalado de variables
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar el modelo de Regresión Lineal Simple
regression = LinearRegression()
regression.fit(X_train_scaled, y_train)
y_pred = regression.predict(X_test_scaled)

# Evaluar el modelo de Regresión Lineal Simple
mae = mean_absolute_error(y_test, y_pred)
mse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Regresión Lineal Simple -> MAE: {mae:.2f}, MSE: {mse:.2f}, R²: {r2:.2f}")

# Crear y entrenar el modelo de Regresión Polinómica (grado 2)
poly_features = PolynomialFeatures(degree=2)
X_train_poly = poly_features.fit_transform(X_train_scaled)
X_test_poly = poly_features.transform(X_test_scaled)

regression_poly = LinearRegression()
regression_poly.fit(X_train_poly, y_train)
y_pred_poly = regression_poly.predict(X_test_poly)

# Evaluar el modelo de Regresión Polinómica
mae_poly = mean_absolute_error(y_test, y_pred_poly)
mse_poly = root_mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)
print(f"Regresión Polinómica -> MAE: {mae_poly:.2f}, MSE: {mse_poly:.2f}, R²: {r2_poly:.2f}")

# Visualizar resultados de Regresión Lineal Simple
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color="red", label="Datos reales")
plt.plot(X_test, y_pred, color="blue", label="Regresión Lineal Simple")
plt.title("Regresión Lineal Simple - Predicciones vs Datos Reales")
plt.xlabel("Horas")
plt.ylabel("Ingreso")
plt.legend()
plt.show()

# Visualizar resultados de Regresión Polinómica
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color="red", label="Datos reales")
plt.plot(X_test, y_pred_poly, color="green", label="Regresión Polinómica (grado 2)")
plt.title("Regresión Polinómica - Predicciones vs Datos Reales")
plt.xlabel("Horas")
plt.ylabel("Ingreso")
plt.legend()
plt.show()

# Comparación de ambos modelos en un gráfico
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color="red", label="Datos reales")
plt.plot(X_test, y_pred, color="blue", label="Regresión Lineal Simple")
plt.plot(X_test, y_pred_poly, color="green", label="Regresión Polinómica (grado 2)")
plt.title("Comparación de Modelos de Regresión")
plt.xlabel("Horas")
plt.ylabel("Ingreso")
plt.legend()
plt.show()
