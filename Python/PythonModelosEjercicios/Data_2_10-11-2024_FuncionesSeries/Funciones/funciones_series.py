def fibonacci(n):
    a=0
    b=1
    if(n==0):
        print(a)
        return 'fin'
    if(n>=1):
        print(a,b,end=' ')

    for i in range (2, n,1):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
def cuadrado_perfecto(num):
    for i in range(1, num+1,1):
        valor=i**2
        print(valor,end=' ')
    return 'Fin de cadena'