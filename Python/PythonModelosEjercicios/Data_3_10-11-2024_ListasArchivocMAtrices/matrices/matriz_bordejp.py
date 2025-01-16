

def matriz_borde(n):

    matriz = [[0] * n for _ in range(n)]

    numero = 1

    for i in range(n):

        matriz[0][i] = numero

        numero += 1

    for i in range(1, n):

        matriz[i][n - 1] = numero

        numero += 1

    for i in range(n - 2, -1, -1):

        matriz[n - 1][i] = numero

        numero += 1

    for i in range(n - 2, 0, -1):

        matriz[i][0] = numero

        numero += 1

    for i in range(1, n - 1):

        for j in range(1, n - 1):

            matriz[i][j] = numero

            numero += 1
    for i in range(1, n - 1):

        for j in range(1, n - 1):

            matriz[i][j] = 0

    return matriz
n=int(input())
for fila in (matriz_borde(n)):
    print(fila)










