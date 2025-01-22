"""

¿Qué es un diccionario en Python?
Un diccionario es una estructura de datos en Python que almacena elementos en pares clave: valor. 
Es similar a un mapa o tabla de datos, donde cada clave actúa como un identificador único 
para acceder a su valor asociado.


"""
#%%
# Crear un diccionario con información personal
persona = {
    "nombre": "Rudy",  # 'nombre' es la clave, "Rudy" es el valor
    "apellido": "Manzaneda",
    "edad": 37,
    "ciudad": "Cochabamba",
    "ocupacion": "Ingeniero"  # Último par clave: valor
}

# Imprimir el diccionario completo
print(persona)

# Acceder a valores mediante claves
print(f"El nombre de la persona es {persona['nombre']} {persona['apellido']}")
#%%
# Iterar sobre el diccionario: obtener claves y valores
for clave, valor in persona.items():  # .items() devuelve pares clave-valor
    print(f"{clave}: {valor}")
#%%
# Crear un diccionario con listas como valores
estudiantes = {
    "Juan": [85, 90, 88],  # Las claves son nombres, los valores son listas de notas
    "Ana": [51, 85, 92],
    "Pedro": [92, 88, 91]
}

# Acceder a las notas de un estudiante específico
print("Las notas de Pedro son:", estudiantes["Pedro"])
#%%
# Crear un diccionario anidado (diccionario dentro de otro)
empleados = {
    "empleado_1": {  # Clave del primer empleado
        "nombre": "Rudy",
        "apellido": "Manzaneda",
        "edad": 37,
        "ciudad": "Cochabamba",
        "ocupacion": "Ingeniero"
    },
    "empleado_2": {  # Clave del segundo empleado
        "nombre": "Ramiro",
        "apellido": "Veizaga",
        "edad": 40,
        "ciudad": "La Paz",
        "ocupacion": "Médico"
    }
}

# Imprimir todo el diccionario de empleados
print(empleados)

# Acceder a un valor dentro del diccionario anidado
print(f"La profesión del empleado {empleados['empleado_2']['nombre']} es {empleados['empleado_2']['ocupacion']}")

#%%
print(empleados.keys())
#%%
print(empleados.values())
#%%
print(empleados.items())
# %%
