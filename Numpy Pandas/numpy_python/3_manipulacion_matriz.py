# Autor: Krzysztof Sopyła (krzysztofsopyla@gmail.com)
# Twitter: ksopyla
# Blog: http://ksopyla.com
# Documentación de Numpy: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html
#%%
import numpy as np

# Crear un array de 0 a 23
a1 = np.arange(0, 24, step=1)
print(a1)
#%%
# Reestructurar el array en una matriz de (2, 12)
a2 = np.reshape(a1, (2, 12))
print(a2)
#%%
# Cambiar un elemento del array afecta a todas sus vistas
a1[0] = 12345
print(a2)
# Restaurar el valor original
a1[0] = 0
#%%
# Reestructurar en matrices de diferentes formas
a3 = np.reshape(a2, (3, 8))
print(a3)
a4 = np.reshape(a2, (4, 6))
print(a4)
a5 = np.reshape(a2, (6, 4))
print(a5)
#%%
# Comparar reshape y resize
a1 = np.ones((3, 3))
a2 = np.ones((8, 3)) * 2
a3 = np.ones((3, 7)) * 3

# Concatenar matrices a lo largo de un eje existente
print(np.concatenate((a1, a2), axis=0))
# Concatenar a lo largo del eje 1
print(np.concatenate((a1, a3), axis=1))
#%%
# Apilar matrices creando un nuevo eje
v1 = np.arange(1, 5)
v2 = np.arange(5, 9)
print(v1)
print(v2)
vv = np.stack((v1, v2), axis=0)  # Apilar filas
vh = np.stack((v1, v2), axis=1)  # Apilar columnas
print(vv)
print(vh)
#%%
# Apilar matrices en 3D
a = np.reshape(np.arange(1, 9), (2, 4))
b = np.reshape(np.arange(1, 9), (2, 4)) + 10
#%%
# Apilar una matriz sobre otra
ab0 = np.stack((a, b), axis=0)
print(ab0)
print(ab0.shape)
print(ab0[0, :, :])
#%%
# Apilar una matriz detrás de otra
ab1 = np.stack((a, b), axis=1)
print(ab1)
print(ab1.shape)
print(ab1[0, :, :])
#%%
# Apilar matrices lado a lado
ab2 = np.stack((a, b), axis=2)
print(ab2)
print(ab2.shape)
print(ab2[0, :, :])
#%%
# Dividir un array en subarrays
x = np.arange(15)
xs = np.split(x, 3)
print(xs)
#%%
# Dividir un array en índices específicos
xs = np.split(x, [3, 5, 6, 10])
print(xs)
#%%
# Repetir un array
b = np.array([0, 1, 2])
print(np.tile(b, 2))  # Repetir una vez
print(np.tile(b, (2, 2)))  # Repetir en una cuadrícula de 2x2
#%%
# Repetir una matriz
c = np.array([[0, 1, 2], [3, 4, 5]])
print(c)
print(np.tile(c, 3))  # Repetir la matriz horizontalmente
