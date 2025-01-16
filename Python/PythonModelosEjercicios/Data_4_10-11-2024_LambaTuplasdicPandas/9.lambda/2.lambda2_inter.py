temperaturas_celsius = [0, 20, 37, 100]
convertir_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temperaturas_celsius))
print(convertir_fahrenheit)  # Resultado: [32.0, 68.0, 98.6, 212.0]


palabras = ["Python", "es", "un", "lenguaje", "divertido"]
palabras_largas = list(filter(lambda palabra: len(palabra) > 5, palabras))
print(palabras_largas)  # Resultado: ['Python', 'lenguaje', 'divertido']


personas = [
    {"nombre": "Ana", "edad": 29},
    {"nombre": "Luis", "edad": 23},
    {"nombre": "Sofía", "edad": 35}
]
personas_ordenadas = sorted(personas, key=lambda persona: persona["edad"])
print(personas_ordenadas)
# Resultado: [{'nombre': 'Luis', 'edad': 23}, {'nombre': 'Ana', 'edad': 29}, {'nombre': 'Sofía', 'edad': 35}]
