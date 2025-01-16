numeros=list(range(1,21))
print(numeros)
print(numeros[4])

import random as ran
lista_numeros=[]
for indice in range (1,7):
    #append es un opcion delistas para agregar elementos
    n=int(input(f'Valor de indice {indice} para la lista'))
    lista_numeros.append(n)
    ##lista_numeros.append(ran.randint(1,11))
print(lista_numeros)

lista_inversa=[]
lista_inversa=lista_numeros[1:3]
print(lista_inversa)

lista_inversa=lista_numeros[::-1]
print(lista_inversa)
