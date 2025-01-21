import numpy as np
# Crear una matriz aleatoria de 4x4
matriz = np.random.randint(1, 10, (4, 4))
print("Matriz aleatoria:\n", matriz)

# Encontrar el máximo y mínimo
print("\nMáximo de la matriz:", np.max(matriz))
print("Mínimo de la matriz:", np.min(matriz))

# Calcular la suma de la diagonal
suma_diagonal = np.trace(matriz)
print("\nSuma de la diagonal:", suma_diagonal)

# Normalizar los valores de la matriz (valores entre 0 y 1)
matriz_normalizada = (matriz - np.min(matriz)) / (np.max(matriz) - np.min(matriz))
print("Matriz normalizada:", matriz_normalizada)