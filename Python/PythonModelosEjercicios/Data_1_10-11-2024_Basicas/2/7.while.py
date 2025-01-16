x=0
suma=0;
n= int(input('Introduzca un valor n notas >>>>'))
while x<n:
    x=x+1
    nota= int(input('Introduzca las notas >>>>'))
    suma= suma+nota

promedio = suma/n
print('El promedio es>>>>', str(promedio))

