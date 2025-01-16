def estrella(n):
    matriz=[[0]*n for _ in range(n)]
    a=1
    for i in range(n):
        for j in range(n):
            if(i==j):
                matriz[i][i] =a
                a+= 1
    for i in range(n):
        matriz[i][n - i - 1] =a
        a+= 1
    return matriz

n=int(input("Introduzca un número: "))
matriz_r=estrella(n)
for fila in matriz_r:
    print(fila)