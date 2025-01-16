def matriz_pascal(n):
    matriz=[[1]* (i+1) for i in range(n)]
    print(matriz)
    for i in range(2,n):
        for j in range(1,i):
            print(i,j,"=",i-1,j-1,"+",i-1,j)
            matriz[i][j]=matriz[i-1][j-1]+matriz[i-1][j]
    return(matriz)

n=6
##matriz_pascal(n)

for lista in matriz_pascal(n):
    print(lista)

n = 5 # Tamaño de la matriz
matriz = [[0] * n for _ in range(n)]  # Inicializar la matriz con ceros

contador = 1  # Inicializar el contador en 1

# Rellenar la diagonal principal con el valor del contador
for i in range(n):
    matriz[i][i] = contador
    contador += 1

# Rellenar las diagonales secundarias con el valor del contador
for i in range(n):
    matriz[i][n - i - 1] = contador
    contador += 1

# Mantener el valor del término del medio
if n%2==1:
    matriz[i//2][i//2] = n//2+1

# Imprimir la matriz
for fila in matriz:
    print(fila)