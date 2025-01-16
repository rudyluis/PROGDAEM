n=int(input('Introduzca un numero'))

matriz_identida= [[ 1 if i<=j else 0 for j in range (n)] for i in range(n)]


for fila in matriz_identida:
    print(fila)