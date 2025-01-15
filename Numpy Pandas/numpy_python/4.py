import numpy as np
# Crear un array lleno de ceros
array_ceros = np.zeros((3, 3))
print("Array de ceros:\n", array_ceros)

# Crear un array lleno de unos
array_unos = np.ones((2, 4))
print("\nArray de unos:\n", array_unos)

# Crear un array con valores aleatorios
array_aleatorio = np.random.random((3, 3))
print("\nArray aleatorio:\n", array_aleatorio)

# Crear un array con valores dentro de un rango
array_rango = np.arange(0, 10, 2)
print("\nArray con valores de 0 a 10, con paso 2:", array_rango)

# Crear un array con valores espaciados uniformemente
array_espaciado = np.linspace(0, 1, 5,dtype=float)
print("\nArray con 5 valores entre 0 y 1:", array_espaciado)
