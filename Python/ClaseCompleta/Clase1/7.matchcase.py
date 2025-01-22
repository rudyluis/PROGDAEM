# calificacion sobre un valor de nota 
"""
    Este es un programa de prueba
    para la clase de programacion en python 
"""
puntuacion = int(input("Ingrese la calificacion (0-100)"))

match puntuacion:
    case p if(p>=90 and p<=100):
        calificacion='A'
    case p if(p>=80 and p<90):
        calificacion='B'
    case p if(70<=p<80):
        calificacion='C'    
    case p if(60<=p<70):
        calificacion='D'    
    case p if(0<=p<60):
        calificacion='F'
    case _:
        calificacion = "Puntuacion Invalida"

print(f"La calificacion es: {calificacion}")