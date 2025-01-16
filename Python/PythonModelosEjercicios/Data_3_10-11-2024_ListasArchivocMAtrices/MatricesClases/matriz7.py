def matriz_pascal(n):
    matriz= [[1]*(i+1) for i in range (n)]
    for i in range (2, n):
        for j in range (1,i):
            matriz [i][j]=matriz[i-1][j-1]+ matriz[i-1][j]
    return matriz
def imprimir_matriz(matriz):
    for f in matriz:
        print(f)
n=5
matriz_pascal2=matriz_pascal(n)
imprimir_matriz(matriz_pascal2)               