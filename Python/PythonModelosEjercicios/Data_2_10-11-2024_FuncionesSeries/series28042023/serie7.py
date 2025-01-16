
##Series 2 -6 12 -36 72 -216 432 
## por 2 si es impar
## por 3 si es par
### inicio =1 
def intercalado(n, sem1,sem2,inicio):
    dato=inicio*sem1
    v= 1
    print(dato, end=' ')
    for a in range(1, n,1):
        if(a %2==0):
            dato*=sem1
            print(dato, end=' ')
        else:
            dato*=sem2
            print(dato*-1, end=' ')
intercalado(7,2,3,1)
    