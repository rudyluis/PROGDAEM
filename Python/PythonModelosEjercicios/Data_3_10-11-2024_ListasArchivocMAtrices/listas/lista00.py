import random

def es_primo(numero):
    """Función que verifica si un número es primo."""
    sw=0
    for i in range(1, numero+1):
        if numero % i == 0:
            sw+=1
    if sw==2:
        return True
    else:
        return False

def obtener_primos(lista):
    """Función que devuelve una lista con los números primos de otra lista."""
    primos = []
    for num in lista:
        if es_primo(num):
            primos.append(num)
    return primos

# Generar una lista de números aleatorios
def generar_lista_aleatoria(tamano, rango_inicio, rango_fin):
    """Genera una lista aleatoria de tamaño `tamano` dentro del rango dado."""
    lista = []
    for _ in range(tamano):
        lista.append(random.randint(rango_inicio, rango_fin))
    return lista

# Parámetros para la lista aleatoria
tamano = 10
rango_inicio = 1
rango_fin = 50

# Generar y procesar la lista
lista_aleatoria = generar_lista_aleatoria(tamano, rango_inicio, rango_fin)
print("Lista generada:", lista_aleatoria)

primos = obtener_primos(lista_aleatoria)
print("Números primos en la lista:", primos)

lista_unida= primos+lista_aleatoria
print(lista_unida)


