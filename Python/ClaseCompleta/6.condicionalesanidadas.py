edad= int(input("Ingrese la edad:"))
if(edad>=0):
    if(edad<=12):
        categoria="Niño/Niña"
    elif(edad <=17):
        categoria= "Adolescente"
    elif(edad<=25):
        categoria="Adulto"
    elif(edad <=65):
        categoria="Adulto/Mayor"
    else:
        categoria="Persona muy mayor"
    
    print(f"La edad se encuentra en la categoria {categoria}")
else:
    print('Porfavor ingrese una edad valida')


#%%
# Solicitar la edad al usuario
try:
    edad = int(input("Ingrese su edad: "))
    
    if edad < 0:
        # Edad negativa no es válida
        print("Por favor, ingrese una edad válida (número positivo).")
    else:
        # Clasificación de acuerdo a la edad
        if edad <= 12:
            categoria = "Niño/Niña"
        elif edad <= 17:
            categoria = "Adolescente"
        elif edad <= 25:
            categoria = "Joven Adulto"
        elif edad <= 65:
            categoria = "Adulto"
        else:
            categoria = "Persona Mayor"

        # Mostrar el resultado
        print(f"La edad ingresada pertenece a la categoría: {categoria}")

except ValueError:
    # Manejo de error si el usuario no ingresa un número
    print("Error: Por favor, ingrese un número entero válido.")
# %%
