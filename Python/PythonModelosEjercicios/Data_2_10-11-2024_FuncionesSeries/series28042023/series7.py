## 1 1 2 4 7 11 18 36 65 101 166 332 599 
## si es par el termino siguiente sumas los dos siguientes
## si es impar el termino siguiente sumas los tres siguientes
def secuencia_semillas(a,b,n):
    c= a+b
    print(a, end=' ')
    print(b, end=' ')
    print(c, end=' ')
    for i in range(1,n+1,1):
        if(c%2==0):
            valor= a+b+c
        else:
            valor=b+c
        a=b
        b=c
        c=valor
        print(valor, end=' ')

secuencia_semillas(1,1,10)