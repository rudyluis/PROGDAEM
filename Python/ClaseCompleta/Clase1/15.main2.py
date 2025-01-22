#import funciones
from funciones import fibonacci as f
from funciones import funcion_suma as suma_f
from funciones import factorial_numero as facto
## funciones integras de la aplicacion
def contador(n):
    x=0
    while x<n:
    #x=x+1
        x+=1
        print(x)

### cabecera principal de la aplicacion
if(__name__=='__main__'):
    n= int(input('Introduzca el valor de n>>>'))
    ##funciones.fibonacci(n)
    f(n)

    ##suma=funciones.funcion_suma(4,5)
    suma= suma_f(4,5)
    print("la suma es ", suma)

    factorial=facto(n)
    print(factorial)
    contador(n)
