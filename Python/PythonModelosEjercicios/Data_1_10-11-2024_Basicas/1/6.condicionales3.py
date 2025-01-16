# Solicita la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Condicionales anidadas para clasificar la edad
if edad >= 0:
    if edad <= 12:
        categoria = "Niño/a"
    elif edad <= 17:
        categoria = "Adolescente"
    elif edad <= 64:
        categoria = "Adulto/a"
    else:
        categoria = "Adulto/a mayor"
    print(f"Te encuentras en la categoría: {categoria}")
else:
    print("Por favor, ingresa una edad válida.")