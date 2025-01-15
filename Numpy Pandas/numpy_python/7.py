import numpy as np
# Crear un array
array = np.array([[1, 2], [3, 4], [5, 6]])

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
