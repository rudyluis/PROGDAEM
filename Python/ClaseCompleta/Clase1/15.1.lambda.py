sumar = lambda a, b: a + b

# Ejemplo de uso
resultado = sumar(5, 3)
print(resultado)  # Resultado: 8




# Función lambda para calcular el cuadrado de un número
cuadrado = lambda x: x ** 2

# Usando la función lambda
print(cuadrado(5))  # Resultado: 25


numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Resultado: [1, 4, 9, 16]


numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Resultado: [2, 4, 6]

productos = [("Laptop", 850), ("Teléfono", 399), ("Monitor", 159)]
productos_ordenados = sorted(productos, key=lambda x: x[1])
print(productos_ordenados)
# Resultado: [('Monitor', 159), ('Teléfono', 399), ('Laptop', 850)]