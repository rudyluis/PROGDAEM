import funciones
num =int(input('>>>>>'))
for a in range(1,num+1):
    sum= funciones.sumatoria(a)
    fact = funciones.factorial(a)
    print(sum,end=',')
    print(fact, end=',')
