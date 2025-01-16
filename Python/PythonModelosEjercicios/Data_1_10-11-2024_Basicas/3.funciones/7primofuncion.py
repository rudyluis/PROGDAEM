##inicio funcion
def factorial_numero(numero):
    fact=1
    for i in range(1,numero+1):
        fact*=i
    return fact
## fin funcion

n = int(input('Introduzca un valor: '))
resultado=factorial_numero(n)
print(f"{n}!={resultado}")
