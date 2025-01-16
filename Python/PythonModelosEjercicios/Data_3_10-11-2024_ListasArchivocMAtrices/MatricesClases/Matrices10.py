import math

##Coeficiente binomial C(n, k)
def coeficiente_binomial(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

##Matriz de Pascal de tamaño n
def matriz_pascal(n):
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            matriz[i][j] = coeficiente_binomial(i, j)
    return matriz

##Mostrar matrices
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

##Función principal
if __name__ == "__main__":
    n = 8
    matriz_pascal_n = matriz_pascal(n)
    mostrar_matriz(matriz_pascal_n)