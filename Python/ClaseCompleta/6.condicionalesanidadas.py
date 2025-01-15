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