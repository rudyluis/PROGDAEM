def generar_matriz_borde(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    numeros = 1
    inicial=0
    final=n
    fila=0
    columna=n-1

    inicial2=1
    final2=n

    inicial3=0
    final3=n-2
    fila3=n-1

    columna4=0
    inicial4=n-1
    final4=0
    while numeros<=n*n:  
        for i in range(inicial,final,1):  #### 1,n-1,1     2,n-2,1  3 ,n-3 1
            matriz[fila][i] = numeros
            numeros+=1
        inicial=inicial+1
        final=final-1
        fila=fila+1

        for i in range(inicial2, final2):  ### 2, n-1   3, n-2
            matriz[i][columna] = numeros
            numeros+=1
        columna=columna-1
        inicial2=inicial2+1
        final2=final2-1

        
        for i in range(final3, inicial3, -1):   #n-2, 0   n-3 1 
            matriz[fila3][i] = numeros
            numeros+=1

        final3=final3-1
        inicial3=inicial3+1
        fila3=fila3-1

        
        for i in range(inicial4, final4, -1):   ##n-1  0      n-2 1
            matriz[i][columna4] = numeros
            numeros+=1
        columna4=columna4+1
        inicial4=inicial4-1
        final4=final4+1
    return matriz

n=int(input('n>>>>>'))

matriz_borde = generar_matriz_borde(n)
for fila in matriz_borde:
    print(fila)