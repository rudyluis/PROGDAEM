grupos = [[10, 20, 30], [5, 10], [25, 35, 45],[1,2,3.6]]
promedios = list(map(lambda grupo: sum(grupo) / len(grupo), grupos))
print(promedios)  # Resultado: [20.0, 10.0, 35.0]


palabras = [("casa", 1), ("perro", 2), ("gato", 3), ("abeja", 4)]
palabras_ordenadas = sorted(palabras, key=lambda palabra: palabra[0][1])
print(palabras_ordenadas)
# Resultado: [('casa', 1), ('abeja', 4), ('gato', 3), ('perro', 2)]


# Definimos una función lambda para calcular el área de una figura geométrica dependiendo del tipo
area_figura = lambda tipo, *dimensiones: (
    dimensiones[0] ** 2 if tipo == "cuadrado" and len(dimensiones) == 1 else
    dimensiones[0] * dimensiones[1] if tipo == "rectángulo" and len(dimensiones) == 2 else
    (dimensiones[0] * dimensiones[1]) / 2 if tipo == "triángulo" and len(dimensiones) == 2 else
    "Tipo o dimensiones no válidas"
)

# Cálculo del área para diferentes figuras
print(area_figura("cuadrado", 4))        # Resultado: 16
print(area_figura("rectángulo", 5, 3))   # Resultado: 15
print(area_figura("triángulo", 6, 4))    # Resultado: 12.0
print(area_figura("pentágono", 5))       # Resultado: "Tipo o dimensiones no válidas"
