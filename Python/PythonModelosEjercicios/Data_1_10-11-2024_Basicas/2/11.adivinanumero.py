import random
valor_dado= random.randrange(1,7)
cont=0
opcion=0
while(opcion!=valor_dado):   ####
    opcion=int(input("Introduzca el valor del dado a adivinar>>>>"))
    if(valor_dado==opcion):
        print("Ud. adivino el numero al intento #"+str(cont))
        break
    else:
        cont+=1
        pregunta=input('Desea continuar en el juego S o N >>>')
        if(pregunta=='N'):
            print('Ud no lo logro!!!! :(')
            break
    
    

