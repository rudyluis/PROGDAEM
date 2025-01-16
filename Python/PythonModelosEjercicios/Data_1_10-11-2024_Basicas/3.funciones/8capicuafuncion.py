### incio funcion
def es_capicua(n):
    cont=0
    num=0
    aux=n
    while(n!=0):   ### <>   python !=
        dig= n%10
        num= num*10+dig
        ###n=n//10  ### division entera //
        n//=10
    if(aux==num):
        return True
    else:
        return False
### fin funcion
n=int(input('Introduzca un valor n >>>>>'))   
if(es_capicua(n)):
    print('el numero es capicua')
else:
    print('El numero no es capicua')