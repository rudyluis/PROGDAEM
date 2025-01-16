def matriz_identidad(n):
    matriz=[[0]* n  for _ in range(n)]
    """matriz=[]
    for i in range(n):
        lista=[]
        for j in range(n):
            lista.append(0)
        matriz.append(lista)
        """
    ###return matriz

    ###for i in range(n):
       ## for j in range(n):
         ##   if(i==j):
           ##     matriz[i][j]=1
    
    for i in range(n):
        matriz[i][i]=1
    return matriz
       

n= int(input('Introduzca un valor >>>>>'))
matriz_r=matriz_identidad(n)

for fila in matriz_r:
    print(fila)
 
