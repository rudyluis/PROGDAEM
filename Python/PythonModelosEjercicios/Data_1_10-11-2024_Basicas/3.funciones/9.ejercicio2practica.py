# Crear una lista de números enteros del 1 al 20
numeros = list(range(1, 21))

# 1. Filtrar los números impares usando lista por comprensión
impares = [num for num in numeros if num % 2 != 0]
print("Números impares:", impares)

# 2. Sumar todos los números pares de la lista
pares = filter(lambda x: x % 2 == 0, numeros)
suma_pares = sum(pares)
print("Suma de números pares:", suma_pares)

# 3. Ordenar la lista de forma descendente
numeros.sort(reverse=True)
print("Lista ordenada de forma descendente:", numeros)