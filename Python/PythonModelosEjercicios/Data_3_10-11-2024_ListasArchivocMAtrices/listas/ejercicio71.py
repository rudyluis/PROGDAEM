def pascal(n):
    #matriz=[[1]* (i+1) for i in range(n)]
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(i+1):
            fila.append(1)
        matriz.append(fila)
    ###### matriz
    for i in range(2,n):
        for j in range (1, i):
            matriz[i][j]= matriz[i-1][j-1]+matriz[i-1][j]

    return matriz



num=int(input('Introduzca un numero'))
for fila in pascal (num):
    print(fila)

matriz_pascal=[]
matriz_pascal=[[ 1 if j==0 or j==1 else matriz_pascal[i-1][j-1]  for j in range (i+1)] for i in range(num)]


for fila in matriz_pascal:
    print(fila)