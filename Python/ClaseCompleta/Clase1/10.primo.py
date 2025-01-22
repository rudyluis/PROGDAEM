cont = 1
## <> !=
opcion='S'
while(opcion!='N'):
    n=int(input('Introduzca un numero'))
    sw = 0
    for cont in range(1, n+1):
        if(n % cont==0):
            sw+=1
    if(sw==2):
        print(f'El numero {n} es primo')
    else:
        print(f'El numero {n} no es primo') 
    opcion=input('Desea continuar con el programa [S] o [N]')   

print("Fin del Programa  :(")