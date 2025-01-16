import Matrices3 as matr
def tablero(matriz_ajedrez):
    for i in range(len(matriz_ajedrez)):
        for j in range(len(matriz_ajedrez[i])):
            if (i + j) % 2 == 0:
                matriz_ajedrez[i][j] = 1
    return matriz_ajedrez

def mostrarMatriz(matriz_ajedrez):
    for fila in matriz_ajedrez:
        print(fila)

n= int(input('>>>>>>'))
matriz_tablero=matr.Matrizserializada(n)
matriz_tablero=tablero(matriz_tablero)
mostrarMatriz(matriz_tablero)


