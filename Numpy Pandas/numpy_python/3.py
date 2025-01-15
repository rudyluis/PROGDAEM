import numpy as np

# Crear un array unidimensional
array_1d = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:", array_1d)

# Crear un array bidimensional (matriz)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray bidimensional:\n", array_2d)

# Verificar el tipo de datos del array
print("\nTipo de datos:", array_1d.dtype)

# Verificar las dimensiones y forma del array
print("Dimensiones:", array_2d.ndim)
print("Forma:", array_2d.shape)
