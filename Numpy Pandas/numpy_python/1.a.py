#%%
import numpy as np

#%%
# Crear un array lleno de ceros
array_ceros = np.zeros((3, 3))
print("Array de ceros:\n", array_ceros)

#%%
# Crear un array lleno de unos
array_unos = np.ones((2, 4))
print("\nArray de unos:\n", array_unos)

#%%
# Crear un array con valores aleatorios
array_aleatorio = np.random.random((3, 3))
print("\nArray aleatorio:\n", array_aleatorio)


#%%
# Crear un array con valores aleatorios enteros
array_aleatorio = np.random.randint(0, 10 ,size=(3, 3))
print("\nArray aleatorio:\n", array_aleatorio)

#%%
# Crear un array con valores dentro de un rango
array_rango = np.arange(0, 10, 2)
print("\nArray con valores de 0 a 10, con paso 2:", array_rango)
#%%
# Crear un array con valores espaciados uniformemente
array_espaciado = np.linspace(0, 1, 5,dtype=float)    ##dtype=
print("\nArray con 5 valores entre 0 y 1:", array_espaciado)
#%%


# Generar 5 puntos entre 0 y 10, incluyendo el 10
array = np.linspace(0, 10, num=5, endpoint=True)
print("Con endpoint=True:", array)

#%%
#END POINT FALSE
import numpy as np

# Generar 5 puntos entre 0 y 10, pero sin incluir el 10
array = np.linspace(0, 10, num=5, endpoint=False)
print("Con endpoint=False:", array)



#%%
data = np.array([1,2,3])
# Estadísticas básicas
print("Suma total:", np.sum(data))
print("Media:", np.mean(data))
print("Mediana:", np.median(data))
print("Varianza:", np.var(data))
print("Desviación estándar:", np.std(data))

#%%

# Crear un array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Estadísticas básicas
print("Suma total:", np.sum(data))
print("Media:", np.mean(data))
print("Mediana:", np.median(data))
print("Varianza:", np.var(data))
print("Desviación estándar:", np.std(data))

# Suma por filas y columnas
#axis 1 = filas
#axis 2 = columnas
print("\nSuma por filas:", np.sum(data, axis=1))
print("Suma por columnas:", np.sum(data, axis=0))

# %%
