#%%
#Importing packages
import numpy as np
import pandas as pd




#Working with data
lista = [1,2,3,4,5,6,7,8,9]
#Llevando una lista de python a numpy
lista2 = np.array(lista)

#Otra manera de hacer una lista
#a =np.array([1,2,3])
#print(f"a = {a}Type = {type(a)}")

#Imprimiendo las listas
print(f"Type = {type(lista)}")
print(f"Type = {type(lista2)}")

# Verificar las dimensiones y forma del array
print("Dimensiones:", lista2.ndim)
print("Forma:", lista2.shape)

#%%
#Creando objetos de multiples dimensiones
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz2 = np.array(matriz)

#Imprimiendo las matrices
print(f"Type = {type(matriz)}")
print(f"Type = {type(matriz2)}")

# Verificar las dimensiones y forma del array
print("Dimensiones:", matriz2.ndim)
print("Forma:", matriz2.shape)

#%%
#Indexing lista
##print(f"lista[0] = {lista[0]}lista[1] = {lista[1]}")
##print(f'lista[3] + lista[7] = {lista[3]} + {lista[7]} = {lista[3]+lista[7]}')


#Indexing matrices
##print(f'matriz[0] = {matriz[0]}')
##print(f'matriz[1] = {matriz[1]}')
#3print(f'matriz[2] = {matriz[2]}')

#Indexing por filas y columnas solo se puede con numpy
##print(f'matriz2[0,1] = {matriz2[0,1]}')
#%%

#slicing 
print(f'{lista2[::3]}')
print(f'{matriz2[0::3]}')

#También esto nos arrojará un error
#matriz[1:,0:2]
#TypeError: list indices must be integers or slices, not tuple

#Como se puede ver la forma de acceder correctamente es
print(f'matriz2[1:,0:2] = {matriz2[1:,0:2]}')
#Hay que recordar que el slicing no toma en cuenta el segundo digito despues de los 2 puntos

