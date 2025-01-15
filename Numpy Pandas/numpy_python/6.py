import numpy as np
# Crear un array 2D

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Acceder a un elemento específico
print("Elemento en [0, 2]:", array[0, 2])

# Seleccionar una fila
print("\nPrimera fila:", array[0, :])

# Seleccionar una columna
print("Segunda columna:", array[:, 1])

# Subarray
print("\nSubarray:\n", array[0:2, 1:3])
