"""

Las listas por comprensión en Python son una forma concisa y elegante de crear nuevas listas 

basadas en iteraciones y condiciones aplicadas a elementos de un iterable, 
como una lista, tupla o rango. Permiten realizar operaciones en una sola línea que, 
de otro modo, requerirían varios pasos utilizando un bucle for.

[nueva_expresión for elemento in iterable if condición]

Partes principales:
nueva_expresión: La operación que se aplica a cada elemento del iterable (por ejemplo, transformar el elemento, realizar un cálculo, etc.).
for elemento in iterable: Itera sobre cada elemento del iterable.
if condición (opcional): Filtra los elementos, aplicando la operación solo a aquellos que cumplan la condición.
Ventajas de las listas por comprensión
Concisión: Reducen el código necesario para crear una lista.
Legibilidad: Al ser compactas, son fáciles de leer y entender para operaciones simples.
Eficiencia: Son generalmente más rápidas que los bucles tradicionales para crear listas en Python.
"""
#%%
numeros = [1, 2, 3, 4, 5]  # Lista inicial de números.
cuadrados = [x**2 for x in numeros]  # Calculamos el cuadrado de cada número usando listas por comprensión.
print(cuadrados)  # Resultado: [1, 4, 9, 16, 25]
#%%
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista del 1 al 10.
pares = [x for x in numeros if x % 2 == 0]  # Incluimos solo los números pares.
print(pares)  # Resultado: [2, 4, 6, 8, 10]

#%%

palabras = ["hola", "mundo", "python", "listas"]  # Lista de palabras.
mayusculas = [palabra.upper() for palabra in palabras]  # Convertimos cada palabra a mayúsculas.
print(mayusculas)  # Resultado: ['HOLA', 'MUNDO', 'PYTHON', 'LISTAS']
#%%
multiplicados = [x * 3 for x in range(1, 6)]  # Multiplicamos cada número del 1 al 5 por 3.
print(multiplicados)  # Resultado: [3, 6, 9, 12, 15]

#%% Importación de funciones y generación de listas
"""
from primos_listas import generar_lista_aleatoria as ga  
# Se importa la función `generar_lista_aleatoria` y se renombra como `ga`.

numeros = [1, 2, 3, 4, 5]  # Lista inicial.

#%% Cálculo de cuadrados con bucle for
cuadrados = []  # Lista vacía.
for x in numeros:  # Iteramos sobre cada número.
    cuadrados.append(x**2)  # Calculamos el cuadrado y lo añadimos a la lista.
print(cuadrados)  # Resultado: [1, 4, 9, 16, 25]

# Alternativa con listas por comprensión.
cuadrados = [x**2 for x in numeros]
print(cuadrados)  # Resultado: [1, 4, 9, 16, 25]

#%% Generar lista aleatoria y encontrar pares
numeros = ga(15, 5, 99)  # Genera una lista de 15 números aleatorios entre 5 y 99.
print(numeros)
pares = [x for x in numeros if x % 2 == 0]  # Selecciona los números pares.
print(pares)

pares2 = [x for x in ga(15, 5, 99) if x % 2 == 0]  # Mismo proceso en una línea.
print(pares2)
"""
#%% Manipulación de cadenas
palabras = ["hola", "mundo", "python", "listas"]

# Convertir a mayúsculas.
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # ['HOLA', 'MUNDO', 'PYTHON', 'LISTAS']

# Extraer y convertir en segmentos.
segmento = [palabra[0:2].upper() for palabra in palabras]  # Tomamos los primeros 2 caracteres en mayúsculas.
print(segmento)  # ['HO', 'MU', 'PY', 'LI']

#%% Generar listas aleatorias dinámicas
import random
serie = [random.randint(0, 100) for _ in range(random.randint(0, 100))]  
# Genera una lista con longitud y valores aleatorios.
print(serie)

# Sumar cuadrados de los elementos en la lista.
print('La suma de los valores cuadrados de la lista es:', sum([_**2 for _ in serie]))

#%% Verificar números primos
from random import randint as r
def es_primo(numero):
    sw = 0  # Contador de divisores.
    for i in range(1, numero + 1):
        if numero % i == 0:  # Verificamos divisibilidad.
            sw += 1
    return sw == 2  # Un número primo tiene exactamente 2 divisores (1 y él mismo).

numeros = [r(0, 100) for _ in range(random.randint(0, 100))]  

pares = [x for x in numeros if es_primo(x)]  # Filtramos los números primos de la lista `numeros`.
print(pares)

# %%
