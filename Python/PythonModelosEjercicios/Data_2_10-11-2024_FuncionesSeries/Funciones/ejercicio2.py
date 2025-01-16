import funciones
num =int(input('>>>>>'))
for a in range(1,num+1):
    ##resul=funciones.sumatoria(a)
    ##fact=funciones.factorial(resul)
    print(funciones.factorial(funciones.sumatoria(a)),end=' ')