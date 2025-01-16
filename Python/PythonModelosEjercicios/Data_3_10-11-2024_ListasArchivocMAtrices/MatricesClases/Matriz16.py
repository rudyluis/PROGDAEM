import random
def multiplicaMatrices(matriz1,matriz2):
    f1=len(matriz1)
    c1=len(matriz1[0])
    f2=len(matriz2)
    c2=len(matriz2[0])
    if(c1!= f2):
        print('No se puede multiplicar directamente')
        return 0
    else:
        suma=0
        resultado=[[0]*c2 for _ in range(f1)]
        for i in range(len(matriz1)):
            for j in range(len(matriz1[i])):
                for k in range (len(matriz2[0])):
                    resultado[i][j]+= matriz1[i][k]*matriz2[k][j]
        return resultado
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

n=int(input('Introduzca la dimension de la matriz1'))
m=int(input('Introduzca la dimension de la matriz2'))

Matriz1=crearMatriz(n,n)
print("Matriz 1")
mostrarMatriz(Matriz1)
Matriz2=crearMatriz(m,m)
print("Matriz 2")
mostrarMatriz(Matriz2)
print("La Multiplicacion de las Matrices es:")
MatrizMulti=multiplicaMatrices(Matriz1,Matriz2)
mostrarMatriz(MatrizMulti)