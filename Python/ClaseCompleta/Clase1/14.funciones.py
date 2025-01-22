def fibonacci(n):
    a=0
    b=1 
    cont=0
    while cont<n:
        print(a, end=' ')
        c=a+b
        a= b
        b= c 
        cont+=1

def funcion_suma(a,b):
    s=a+b
    return s

def factorial_numero (n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return(fact)