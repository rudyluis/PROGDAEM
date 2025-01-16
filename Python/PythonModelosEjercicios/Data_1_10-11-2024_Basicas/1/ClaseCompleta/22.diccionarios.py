persona={
    "nombre":"Rudy",
    "apellido":"Manzaneda",
    "edad":37,
    "ciudad":"Cochabamba", 
    "ocupacion":"Ingeniero"  ## ocupacion=clave   Ingeniero= valor
}

print(persona)
print(f"el nombre de la persona es {persona["nombre"]+" "+persona["apellido"]}")

for clave, valor in persona.items():
    print(f"{clave}:{valor}")

estudiantes={
    "Juan":[85,90,88],
    "Ana": [51,85,92],
    "Pedro":[92,88,91]
}

print("Las notas son:",estudiantes["Pedro"])

empleados={
    "empleado_1":{
        "nombre":"Rudy",
        "apellido":"Manzaneda",
        "edad":37,
        "ciudad":"Cochabamba", 
        "ocupacion":"Ingeniero"  ## ocupacion=clave   Ingeniero= valor
    },
    "empleado_2":{
        "nombre":"Ramiro",
        "apellido":"Veizaga",
        "edad":40,
        "ciudad":"La Paz", 
        "ocupacion":"Medico"  ## ocupacion=clave   Ingeniero= valor
    }
}

print(empleados)

print(f"la profesion del empleado {empleados["empleado_2"]["nombre"]}  es {empleados["empleado_2"]["ocupacion"]}")