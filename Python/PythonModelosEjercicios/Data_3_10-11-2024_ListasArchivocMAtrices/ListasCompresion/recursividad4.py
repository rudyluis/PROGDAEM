##n=10
##[10,5,16,8,4,2,1]
def collatz(n):
    collatz=[n]
    while (n>1):
        if n%2==0:
            n//=2   
        else:
            n=(3*n)+1
        collatz.append(n)   
    return collatz

def collatz_r(n, secuencia=None):
    if( secuencia is None):
        secuencia=[n]
    if( n==1):
        return secuencia
    elif n %2== 0:
        siguiente=n//2
    else:
        siguiente=3*n+1
    secuencia.append(siguiente)
    return collatz_r(siguiente,secuencia)

if __name__ == '__main__':
    n=int(input("ingrese un numero"))
    collatz = collatz_r(n)  
    print(collatz)