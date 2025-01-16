
##46  23  61  8  4  2
def inversa_potencia(n):
    for a in range (n,0,-1):
        print (inversa_numero(2**a), end='  ')
def inversa_numero(n):
    n= str(n)
    return (int(n[::-1]))

inversa_potencia(6)