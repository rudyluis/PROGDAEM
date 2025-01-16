def matriz_caracol(filas, columnas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    valor = 1
    inicio_fila = 0
    fin_fila = filas - 1
    inicio_columna = 0
    fin_columna = columnas - 1

    # Rellenar el borde superior de izquierda a derecha
    for i in range(inicio_columna, fin_columna + 1):
        matriz[inicio_fila][i] = valor
        valor += 1
    inicio_fila += 1

    # Rellenar el borde derecho de arriba hacia abajo
    for i in range(inicio_fila, fin_fila + 1):
        matriz[i][fin_columna] = valor
        valor += 1
    fin_columna -= 1

    # Rellenar el borde inferior de derecha a izquierda
    for i in range(fin_columna, inicio_columna - 1, -1):
        matriz[fin_fila][i] = valor
        valor += 1
    fin_fila -= 1

    # Rellenar el borde izquierdo de abajo hacia arriba
    for i in range(fin_fila, inicio_fila - 1, -1):
        matriz[i][inicio_columna] = valor
        valor += 1
    inicio_columna += 1

    return matriz

# Ejemplo de uso
num=int(input('Introduzca un numero'))
##filas = 5
##columnas = 5
matriz = matriz_caracol(num, num)

# Imprimir la matriz
for fila in matriz:
    for elemento in fila:
        print(f'{elemento:2}', end=' ')
    print()
