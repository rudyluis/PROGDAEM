def matriz_tablero(n):
    tablero=[]
    for fila in range(n):
        fila_tablero=[]
        for columna in range (n):
            if((fila+columna)%2==0):
                fila_tablero.append(1)
            else:    
                fila_tablero.append(0)
        tablero.append(fila_tablero)
    return tablero


num=int(input('Introduzca un valor n>>>>>'))
for fila in matriz_tablero(num):
    print(fila)
