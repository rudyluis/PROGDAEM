n = int(input('Introduzca la cantidad de Notas>>>>>'))
x=0
suma=0
while(x<n):
    nota=int(input('Introduzca una nota>>>'))
    ##x=x+1
    ##suma=suma+nota
    x+=1
    suma+=nota

promedio = suma/n

print('El promedio es: ', promedio)