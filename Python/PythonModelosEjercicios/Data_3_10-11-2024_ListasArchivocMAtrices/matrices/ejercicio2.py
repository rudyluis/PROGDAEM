import random



def crear_matriz(n,m):
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(m):
            valor= random.randint(1,101)
            fila.append(valor)
        matriz.append(fila)
    return matriz

n=random.randint(3,10)
m=random.randint(3,10)
matriz_r= crear_matriz(n,m)
##print(matriz_r)

for fila in matriz_r:
    print(fila)