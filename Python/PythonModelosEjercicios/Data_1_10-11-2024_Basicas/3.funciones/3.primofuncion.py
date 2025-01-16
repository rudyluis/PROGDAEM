#### inicio de la funcion
def verificar_primos():
    n=int(input('Introduzca un numero'))
    cont=1
    sw=0
    while(cont<=n):
        if(n % cont ==0):
            sw+=1
        cont+=1
    if(sw==2):
        print(f'El numero {n} es primo')
    else:
        print(f'El numero {n} no es primo')
### fin de la funcion

verificar_primos()

