# Solicita la puntuación al usuario
puntuacion = int(input("Ingresa tu puntuación (0-100): "))

# Usando match-case para clasificar la puntuación en letras
match puntuacion:
    case p if 90 <= p <= 100:
        calificacion = "A"
    case p if 80 <= p < 90:
        calificacion = "B"
    case p if 70 <= p < 80:
        calificacion = "C"
    case p if 60 <= p < 70:
        calificacion = "D"
    case p if 0 <= p < 60:
        calificacion = "F"
    case _:
        calificacion = "Puntuación inválida"

print(f"Tu calificación es: {calificacion}")
