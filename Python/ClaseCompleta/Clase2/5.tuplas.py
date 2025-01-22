"""
Una tupla es una colección inmutable, ordenada y versátil en Python, 
ideal para representar datos que no deben cambiar a lo largo del programa.
"""
import random  # Importa la librería para generar números aleatorios.

# Función para encontrar el valor mínimo y máximo de una tupla
def min_max(tupla):
    minimo = min(tupla)  # Encuentra el mínimo valor en la tupla.
    maximo = max(tupla)  # Encuentra el máximo valor en la tupla.
    return (minimo, maximo)  # Retorna ambos valores como una nueva tupla.

# Función para calcular el promedio de los elementos de una tupla
def promedio_tupla(tupla):
    promedio = sum(tupla) / len(tupla)  # Calcula el promedio (suma dividida entre la cantidad de elementos).
    return promedio

# Función para encontrar el índice de un elemento en una tupla
def encontrar_indice(tupla, elemento):
    if elemento in tupla:  # Verifica si el elemento está en la tupla.
        return tupla.index(elemento)  # Retorna el índice del elemento.
    else:
        return -1  # Retorna -1 si el elemento no está en la tupla.

# Bloque principal del programa
if __name__ == "__main__":  # Punto de entrada del script.
    # Tupla inicial
    numeros = (3, 7, 2, 8, 5, 3)  # Se crea una tupla con valores fijos.
    print(numeros)

    # Generar una nueva tupla de 10 números aleatorios entre 1 y 10
    numeros = tuple(random.randint(1, 10) for i in range(10))  # Genera una tupla con valores aleatorios.
    print(numeros)

    # Encontrar el valor mínimo y máximo en la tupla
    resultado = min_max(numeros)  # Llama a la función `min_max`.
    print(f"El mínimo es {resultado[0]} y el máximo es {resultado[1]}")

    # Sumar todos los elementos de la tupla
    print(f"La suma de todos los elementos de la tupla {numeros} es: {sum(numeros)}")

    # Calcular el promedio de los elementos
    print(f"El promedio de los elementos de la tupla es {promedio_tupla(numeros)}")

    # Generar otra tupla de números aleatorios
    numeros2 = tuple(random.randint(1, 10) for i in range(10))
    print(numeros2)

    # Concatenar las dos tuplas
    print(numeros + numeros2)

    # Buscar un elemento aleatorio en la tupla
    elemento_buscar = random.randint(1, 10)  # Genera un número aleatorio para buscar.
    print("Elemento a buscar es", elemento_buscar)

    # Llamar a la función para encontrar el índice del elemento
    resultado = encontrar_indice(numeros, elemento_buscar)
    if resultado != -1:  # Si el índice no es -1, el elemento existe en la tupla.
        print(f"El elemento {elemento_buscar} se encuentra en el índice {resultado}")
    else:  # Si el índice es -1, el elemento no está en la tupla.
        print(f"El elemento {elemento_buscar} no está en la tupla")
