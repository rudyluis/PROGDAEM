import numpy as np
# Crear un array


array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Acceder a un elemento específico
print("Elemento en [0, 2]:", array[0, 2])

# Seleccionar una fila
print("\nPrimera fila:", array[0, :])

# Seleccionar una columna
print("Segunda columna:", array[:, 1])

# Subarray
print("\nSubarray:\n", array[0:2, 1:3])

array = np.array([[1, 2], [3, 4], [5, 6]])
# contar elementos
print("Tamaño del array", np.size(array))
# Transposición
print("Array original:\n", array)
print("\nArray transpuesto:\n", array.T)

# Redimensionar
array_reshaped = array.reshape((2, 3))
print("\nArray redimensionado:\n", array_reshaped)

# Concatenación de arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print("\nConcatenación vertical:\n", np.vstack((a, b)))
print("Concatenación horizontal:\n", np.hstack((a, b.T)))
