def factorial (n):
    fact=1
    for _ in range(1,n+1):
        fact*=_
    return fact

def sumatoria1(n,x):
    sumatoria=0
    for i in range(1,n+1):
        numerador=(-1**i)*x**(2*i+1)
        denominador= factorial(2*i+1)
        sumatoria+=(numerador/denominador)
        print(f'Para i={i}= [{numerador}]/[{denominador}]\n')
    return sumatoria


### main

if __name__ == "__main__":
    n= int(input('n>>>>'))
    x= int(input('x>>>>'))

    valor_sumatoria=sumatoria1(n,x)
    print('La sumatoria es-->',valor_sumatoria)
