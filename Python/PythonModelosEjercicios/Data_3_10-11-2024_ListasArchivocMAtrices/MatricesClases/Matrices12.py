def generar_matriz_borde(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    numeros = 1
    indice = 0

    for i in range(n):
        matriz[0][i] = numeros
        numeros+=1

    for i in range(1, n):
        matriz[i][-1] = numeros
        numeros+=1

    for i in range(n-2, 0, -1):
        matriz[n-1][i] = numeros
        numeros+=1

    for i in range(n-1, 0, -1):
        matriz[i][0] = numeros
        numeros+=1

    return matriz

n=int(input('n>>>>>'))

matriz_borde = generar_matriz_borde(n)
for fila in matriz_borde:
    print(fila)