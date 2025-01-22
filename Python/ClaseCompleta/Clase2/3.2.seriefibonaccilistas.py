""" def fibonacci2(n):
    a=0
    b=1 
    cont=0
    while cont<n:
        print(a, end=' ')
        c=a+b
        a= b
        b= c 
        cont+=1

        """

def fibonacci(n):
    fibo=[0,1]
    for a in range (2, n+1):
        fibo.append(fibo[a-1]+fibo[a-2])
    return fibo


if __name__=="__main__":
    Serie_fibo=fibonacci(int(input('Introduzca el valor')))
    print(Serie_fibo)
