# Función para calcular el promedio de una lista de números
def calcular_promedio(lista):
    if len(lista) == 0:
        return "La lista está vacía"
    return sum(lista) / len(lista)

# Ejemplo de uso
numeros = [10, 20, 30, 40, 50]
print(f"El promedio es: {calcular_promedio(numeros)}")