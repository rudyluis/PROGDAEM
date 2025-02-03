# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Cargar el dataset
dataset = pd.read_csv('df/Salary_Data.csv')

# Validar si hay valores nulos en el dataset
if dataset.isnull().values.any():
    print("El dataset contiene valores nulos. Por favor, revisa los datos.")
else:
    print("El dataset no tiene valores nulos. Continuando con el análisis...")

# Definir variables independientes (X) y dependientes (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
X = dataset[['YearsExperience']].values
y = dataset[['Salary']].values
print(X)
print(y)
# Dividir el dataset en conjunto de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Escalado de variables (opcional)
scaler = StandardScaler()
use_scaling = False  # Cambiar a True si se desea escalar las variables

if use_scaling:
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    print("Las variables han sido escaladas.")
else:
    print("No se ha aplicado escalado de variables.")

# Crear el modelo de Regresión Lineal Simple con el conjunto de entrenamiento
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predecir el conjunto de test
y_pred = regression.predict(X_test)

# Calcular y mostrar las métricas de evaluación
mae = mean_absolute_error(y_test, y_pred)
mse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error Absoluto Medio (MAE): {mae:.2f}")
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
print(f"Coeficiente de Determinación (R²): {r2:.2f}")

# Visualizar los resultados del conjunto de entrenamiento
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color="red", label="Datos reales (entrenamiento)")
plt.plot(X_train, regression.predict(X_train), color="blue", label="Ajuste del modelo")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.legend()
plt.grid(True)
plt.show()

# Visualizar los resultados del conjunto de test
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color="green", label="Datos reales (test)")
plt.plot(X_train, regression.predict(X_train), color="blue", label="Ajuste del modelo")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.legend()
plt.grid(True)
plt.show()
