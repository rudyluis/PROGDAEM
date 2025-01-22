import random
valor_dado=random.randrange(1,7)  
opcion=0
while(opcion!=valor_dado):
    opcion=int(input("Introduzca el valor del dado a adivinar>>>"))
    if(valor_dado==opcion):
        print("Ud. adivino el numero")
        break
    else:
        print("Numero Equivocado")
        pregunta=input('Desea continuar con el juego S o N >>>')
        if(pregunta=='N'):
            print('Ud se rindio!!! :(')
            break