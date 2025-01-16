numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]


palabras = ["hola", "mundo", "python", "listas"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # ['HOLA', 'MUNDO', 'PYTHON', 'LISTAS']

multiplicados = [x * 3 for x in range(1, 6)]
print(multiplicados)  # [3, 6, 9, 12, 15]