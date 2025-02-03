import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor

# Generación de datos simulados (una línea recta con algo de ruido)
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # Característica (entrada)
y = 4 + 3 * X + np.random.randn(100, 1)  # Etiqueta (salida), y = 4 + 3X + ruido

# Crear el modelo de regresión utilizando SGD (descenso estocástico del gradiente)
model = SGDRegressor(max_iter=1000, tol=1e-3, eta0=0.1)  # max_iter es el número de iteraciones, eta0 es la tasa de aprendizaje

# Ajustar el modelo a los datos
model.fit(X, y.ravel())  # .ravel() convierte y en un vector 1D, que es lo que espera el modelo

# Obtener los parámetros (pendiente y coeficiente)
theta_1_opt = model.coef_
theta_0_opt = model.intercept_

print(f"Parámetros óptimos: theta_0 = {theta_0_opt[0]}, theta_1 = {theta_1_opt[0]}")

# Graficar los datos y la línea de regresión ajustada
plt.scatter(X, y, color='blue', label='Datos')
plt.plot(X, model.predict(X), color='red', label='Línea de regresión ajustada')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal con SGD (Gradiente Descendente)')
plt.legend()
plt.show()
