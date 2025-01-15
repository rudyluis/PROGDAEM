import numpy as np
# Crear un array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Estadísticas básicas
print("Suma total:", np.sum(data))
print("Media:", np.mean(data))
print("Mediana:", np.median(data))
print("Varianza:", np.var(data))
print("Desviación estándar:", np.std(data))

# Suma por filas y columnas
print("\nSuma por filas:", np.sum(data, axis=1))
print("Suma por columnas:", np.sum(data, axis=0))
