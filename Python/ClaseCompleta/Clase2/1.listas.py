"""

¿Qué son las listas en Python?
Las listas son una estructura de datos en Python que permiten almacenar múltiples elementos 
en una sola variable. Estos elementos pueden ser de cualquier tipo, como enteros, cadenas, flotantes, u otras listas. 
Las listas son mutables, lo que significa que puedes modificar su contenido después de crearlas.

Características principales de las listas:

Índices: Los elementos de una lista están ordenados y se acceden mediante índices, 
empezando desde 0.
Dinámicas: Pueden cambiar de tamaño agregando o eliminando elementos.
Métodos útiles: Tienen métodos integrados como .append(), .remove(), .pop(), .sort(), etc.



"""


#%% 
# Creamos una lista llamada 'numeros' que contiene una secuencia de números del 1 al 20.
numeros = list(range(1, 21))  # 'range(1, 21)' genera un rango de números del 1 al 20 (excluye el 21).
print(numeros)  # Mostramos la lista completa en pantalla.
print(numeros[4])  # Mostramos el elemento que está en la posición 4 (índice comienza desde 0, así que es el número 5).

#%% 
import random as ran  # Importamos el módulo 'random' para generar números aleatorios. Lo renombramos como 'ran'.
lista_numeros = []  # Creamos una lista vacía llamada 'lista_numeros'.

# Usamos un bucle para solicitar valores al usuario.
for indice in range(1, 7):  # Recorremos los números del 1 al 6 (inclusive).
    # Solicitamos un valor al usuario y lo convertimos en entero.
    n = int(input(f'Valor de índice {indice} para la lista: '))
    lista_numeros.append(n)  # Agregamos el valor ingresado a la lista 'lista_numeros'.
    # Alternativamente, podríamos agregar números aleatorios con:
    # lista_numeros.append(ran.randint(1, 11))  # Genera un número aleatorio entre 1 y 11.
    
print(lista_numeros)  # Mostramos la lista con los valores ingresados por el usuario.

#%% 
lista_inversa = []  # Creamos una lista vacía llamada 'lista_inversa'.
# Extraemos una porción de la lista 'lista_numeros' desde el índice 1 hasta el 3 (excluye el índice 3).
lista_inversa = lista_numeros[1:7]  
print(lista_inversa)  # Mostramos la nueva lista con la porción seleccionada.

#%% 
# Invertimos la lista completa usando 'slicing' con [::-1], que toma los elementos de atrás hacia adelante.
lista_inversa = lista_numeros[::-1]
print(lista_inversa)  # Mostramos la lista invertida.

# %%
