def fibonaccio(n):
    fibonacci=[0,1]  ## fibo solo es el nombre de la lista
    for a in range(2,n):
        valor=fibonacci[a-1]+fibonacci[a-2]
        fibonacci.append(valor)
    return fibonacci

n=int(input('Introduzca un numero >>>>>>'))
b=list(fibonaccio(n))
print(b)
b.sort(reverse=True) 
print(b)


