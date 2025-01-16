persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Lima"
}
print(persona)

print(persona["nombre"])  # Salida: Juan


  
persona["edad"] = 26  # Modificar un valor existente
persona["ocupacion"] = "Ingeniero"  # Agregar un nuevo par clave-valor
print(persona)

persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Lima"
}
del persona["ciudad"]
print(persona)


persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Lima"
}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

frase = "hola mundo hola python"
contador = {}

for palabra in frase.split():
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)  # Salida: {'hola': 2, 'mundo': 1, 'python': 1}

estudiantes = {
    "Juan": [85, 90, 88],
    "Ana": [78, 85, 92],
    "Pedro": [92, 88, 91]
}
print(estudiantes["Ana"])  # Salida: [78, 85, 92]

operaciones = {
    "suma": lambda x, y: x + y,
    "resta": lambda x, y: x - y,
    "multiplicacion": lambda x, y: x * y,
    "division": lambda x, y: x / y if y != 0 else "Indefinido"
}

print(operaciones["suma"](10, 5))  # Salida: 15
print(operaciones["division"](10, 0))  # Salida: Indefinido

empleados = {
    "empleado_1": {
        "nombre": "Juan",
        "edad": 30,
        "cargo": "Analista"
    },
    "empleado_2": {
        "nombre": "Ana",
        "edad": 28,
        "cargo": "Desarrollador"
    }
}
print(empleados["empleado_1"]["cargo"])  # Salida: Analista


productos = {
    "producto1": 150,
    "producto2": 50,
    "producto3": 200,
    "producto4": 80
}

productos_filtrados = {k: v for k, v in productos.items() if v > 100}
print(productos_filtrados)  # Salida: {'producto1': 150, 'producto3': 200}


inventario = {
    "manzanas": 20,
    "bananas": 15,
    "naranjas": 10
}

fruta = "manzanas"
if fruta in inventario:
    print(f"{fruta} disponible con cantidad: {inventario[fruta]}")
else:
    print(f"{fruta} no está en el inventario")

#actualizar informacíon

info_persona = {"nombre": "Pedro", "edad": 40}
info_adicional = {"ciudad": "Barcelona", "profesion": "Ingeniero"}

info_persona.update(info_adicional)
print(info_persona)

#ordenar un diccionario 
ventas = {
    "producto1": 200,
    "producto2": 150,
    "producto3": 300
}

ventas_ordenadas = dict(sorted(ventas.items(), key=lambda item: item[1], reverse=True))
print(ventas_ordenadas)  # Salida ordenada por valor en orden descendente