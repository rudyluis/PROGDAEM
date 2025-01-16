import random
def min_max(tupla):
    minimo = min(tupla)
    maximo = max(tupla)
    return (minimo, maximo)


def contar_elemento(tupla, elemento):
    return tupla.count(elemento)

def encontrar_indice(tupla, elemento):
    if elemento in tupla:
        return tupla.index(elemento)
    else:
        return -1

def sumar_tupla(tupla):
    return sum(tupla)  

def calcular_promedio(tupla):
    
    promedio = sum(tupla) / len(tupla)
    return promedio

def concatenar_tuplas(tupla1, tupla2):
    return tupla1 + tupla2


# Mostrar la tupla generada

if __name__=="__main__":
    # Ejemplo de uso
    numeros = (3, 7, 2, 8, 5,3)
    numeros = tuple(random.randint(1, 10) for _ in range(6))
    print(numeros)
    resultado = min_max(numeros)
    print(f"El mínimo es {resultado[0]} y el máximo es {resultado[1]}")


    elemento_a_contar = 3
    resultado = contar_elemento(numeros, elemento_a_contar)
    print(f"El elemento {elemento_a_contar} aparece {resultado} veces")



    # Ejemplo de uso

    resultado = sumar_tupla(numeros)
    print(f"La suma de todos los elementos es: {resultado}")

    # promedio tupla

    print(f"EL promedio de la tupla es:{calcular_promedio(numeros)}")

    # Ejemplo de uso
    tupla_a = (1, 2, 3)
    tupla_b = (4, 5, 6)
    resultado = concatenar_tuplas(tupla_a, tupla_b)
    print(f"La tupla concatenada es: {resultado}")

    # Ejemplo de uso
    valores = (10, 20, 30, 40, 50)
    elemento_a_buscar = 30
    resultado = encontrar_indice(valores, elemento_a_buscar)
    if resultado != -1:
        print(f"El elemento {elemento_a_buscar} se encuentra en el índice {resultado}")
    else:
        print(f"El elemento {elemento_a_buscar} no está en la tupla")