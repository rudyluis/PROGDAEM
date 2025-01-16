# Diccionario de estudiantes con calificaciones
estudiantes = {
    'Juan': 85,
    'Ana': 55,
    'Carlos': 70,
    'Lucía': 45,
    'Pedro': 90
}

# Mostrar los estudiantes aprobados
print("Estudiantes aprobados:")
for estudiante, calificacion in estudiantes.items():
    if calificacion >= 60:
        print(estudiante)