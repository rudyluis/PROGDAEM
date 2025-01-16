n=int(input('Introduzca un numero >>>>>>'))
fibonacci=[0,1]  ## fibo solo es el nombre de la lista
for a in range(2,n):
    valor=fibonacci[a-1]+fibonacci[a-2]
    fibonacci.append(valor)
    ##fibonacci.append(fibonacci[a-1]+fibonacci[a-2])  ## es para agregar elements
print(fibonacci)
