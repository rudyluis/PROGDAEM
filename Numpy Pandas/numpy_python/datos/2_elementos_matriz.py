#%%
import numpy as np
#%%
# Crear un array de rango 2 con forma (3, 4)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)           # Muestra el array
print(a[0, 1])     # Accede al elemento en la fila 0, columna 1 (imprime "2")
#%%
# Extraer un subarray (primeras 2 filas y columnas 1 y 2)
b = a[:2, 1:3]
print(b)           # Imprime: [[2 3]
                   #           [6 7]]
#%%
# Cambiar un elemento del subarray afecta al array original
b[0, 0] = 77
print(a[0, 1])     # Imprime "77"
#%%
# Acceso a filas
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
row_r1 = a[1, :]    # Vista de rango 1 de la segunda fila
row_r2 = a[1:2, :]  # Vista de rango 2 de la segunda fila
print(row_r1, row_r1.shape)  # Imprime "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Imprime "[[5 6 7 8]] (1, 4)"
#%%
# Acceso a columnas
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Imprime "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Imprime "[[ 2] [ 6] [10]] (3, 1)"
#%%
# Indexación con arrays de enteros
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 1, 0]])  # Imprime "[1 4 5]"
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Imprime "[1 4 5]"
print(a[[0, 0], [1, 1]])  # Imprime "[2 2]"
print(np.array([a[0, 1], a[0, 1]]))  # Imprime "[2 2]"
#%%
# Modificación de elementos usando índices enteros
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])  # Imprime "[ 1  6  7 11]"
a[np.arange(4), b] += 10
print(a)  # Imprime: [[11  2  3]
          #          [ 4  5 16]
          #          [17  8  9]
          #          [10 21 12]]
#%%
# Indexación booleana
a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print(bool_idx)  # Imprime: [[False False]
                 #          [ True  True]
                 #          [ True  True]]
print(a[bool_idx])  # Imprime "[3 4 5 6]"
print(a[a > 2])     # Imprime "[3 4 5 6]"
