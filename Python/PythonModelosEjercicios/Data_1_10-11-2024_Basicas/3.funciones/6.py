#### inicio de la funcion
#### variables globales->>> se aplicand en todo el programa (funciona)
#### variable locales--->>> solo se aplicand para las funciones
##### una funcion tiene variables locales y que se envian y reciben
####  funcion tiene la opcion de return   (retorna una respuesta de la funcion)
def verificar_primos(num):
   
    cont=1
    sw=0
    while(cont<=num):
        if(num % cont ==0):
            sw+=1
        cont+=1
    if(sw==2):
        return(True)
        ##print(f'El numero {num} es primo')
    else:
        return(False)
        ##print(f'El numero {num} no es primo')
### fin de la funcion

###3 Estructura Principal de la aplicacion
n=int(input('Introduzca un numero'))
resultado=verificar_primos(n)
if(resultado):
    print(f'El numero {n} es primo')
else:
    print(f'El numero {n} no es primo')



