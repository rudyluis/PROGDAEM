def repetir_numero(n):
    
    for i in range(1,n+1):
        ser=''
        for j in range(1,i+1):
            ser=ser+str(i)
        print(ser, end=' ')

def inversa_potencia(n):
    for a in range(n,0,-1):
        print(inverso_n(2**a), end=' ')
        
def inverso_n(n):
    n =str(n)
    return(int(n[::-1]))

def fibonacci_raro(a,b,n):
    c=a+b
    print(a, end=' ')
    print(b, end=' ')
    print(c, end=' ')

    for i in range(1,n+1,1):
        if(c%2==0):
            valor=a+b+c
        else:
            valor=c+b
        a=b
        b=c
        c=valor
        print(valor,end='  ')

def Factorial(n):
    m=1
    for i in range(1,n+1):
        m*=i
    return(m)
def sumatoria(n):
    s=0
    n= str(n)
    ##s= s+(int(d) for d in str(sumatoria))

    for i in range(0,len(n),1):
        s=s+int(n[i])
    return(s)
def sumatoria_factorial(n):
    for a in range(n,0,-1):
        print(sumatoria(Factorial(a)), end='  ')
def conway(n):
    serien='1'
    print(serien, end=' ')
    for i in range(2,n+1):
        s=serien+'$'
        cont=1
        numero=''
        for j in range(1,len(s)):
            if(s[j]!=s[j-1]):
                numero+=(str(cont)+s[j-1])
                cont=1
            else:
                cont+=1
        print(numero, end=' ')
        serien=numero


def series_progesivas(n):
    cont=1
    num=''
    valor=''
    while(cont<=n):
        num=''
        for i in range(1, cont+1,1):
            num+=str(i)
        inverso=''
        inverso= num[::-1]
        valor=valor+(num+inverso)
        cont+=1
    print(valor)

