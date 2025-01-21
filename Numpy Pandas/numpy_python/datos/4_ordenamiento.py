# Autor: Krzysztof Sopyła (krzysztofsopyla@gmail.com)
# Twitter: ksopyla
# Blog: https://ksopyla.com
# Si deseas usar este material en tu propio entrenamiento, por favor avísame.
#%%
import numpy as np

# Ordenamiento (sorting)
a = np.array([[1, 4], [3, 1]])

# Ordenar a lo largo del último eje (por filas).
# Cada fila se ordena de menor a mayor.
print("Ordenar por filas (último eje):")
print(np.sort(a))
#%%
# Ordenar el array aplanado (sin importar su forma original).
# Todos los elementos se ordenan como si fueran un único vector.
print("Ordenar el array aplanado:")
print(np.sort(a, axis=None))
#%%
# Ordenar a lo largo del primer eje (por columnas).
# Cada columna se ordena de menor a mayor.
print("Ordenar por columnas (primer eje):")
print(np.sort(a, axis=0))

#%%
# Índices del ordenamiento (argsort)
x = np.array([3, 1, 2])

# `argsort` devuelve los índices que ordenarían el array.
# Por ejemplo, en este caso, los índices `[1, 2, 0]` indican que
# para ordenar `x`, debemos tomar los elementos en el orden `1, 2, 0`.
print("Índices para ordenar un array:")
print(np.argsort(x))
#%%
# Ejemplo con un array 2D
x = np.array([[0, 3], [2, 2]])

# `argsort` a lo largo del primer eje (por columnas).
# Devuelve los índices que ordenarían las columnas.
ind = np.argsort(x, axis=0)
print("Índices para ordenar por columnas (primer eje):")
print(ind)

# Usar `np.take_along_axis` para aplicar el ordenamiento según los índices calculados.
print("Array ordenado por columnas (primer eje):")
print(np.take_along_axis(x, ind, axis=0))


# Encontrar el índice del máximo valor (argmax)
a = np.arange(6).reshape(2, 3) + 10
# `a` es ahora:
# [[10 11 12]
#  [13 14 15]]

# Encontrar el índice del valor máximo en el array aplanado.
# En este caso, el máximo valor es `15` en la posición 5.
print("Índice del máximo valor en el array aplanado:")
print(np.argmax(a))

# Encontrar los índices del valor máximo a lo largo del primer eje (por columnas).
# Por ejemplo, para cada columna, los valores máximos están en las filas `[1, 1, 1]`.
print("Índices de los máximos valores por columnas (primer eje):")
print(np.argmax(a, axis=0))

# Encontrar los índices del valor máximo a lo largo del segundo eje (por filas).
# En cada fila, el índice del valor máximo está en `[2, 2]`.
print("Índices de los máximos valores por filas (segundo eje):")
print(np.argmax(a, axis=1))

# %%
