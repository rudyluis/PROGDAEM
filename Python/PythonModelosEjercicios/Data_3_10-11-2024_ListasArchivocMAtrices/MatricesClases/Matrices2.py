import random

def crearMatriz(n,m):
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(m):
            valor= random.randint(1,101)
            fila.append(valor)
        matriz.append(fila)
    return matriz
def mostrarMatriz(Matriz):
    for fila in Matriz:
        print(fila)     
##### estructura principal
n= random.randint(3,10)
m= random.randint(3,10)
respMatriz=crearMatriz(n,m)
mostrarMatriz(respMatriz)
