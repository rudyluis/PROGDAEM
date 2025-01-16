
import random
def sumaMatrices(matriz1,matriz2):
    f1=len(matriz1)
    c1=len(matriz1[0])
    f2=len(matriz2)
    c2=len(matriz2[0])
    if(f1!=f2 and c1!=c2):
        print('No se puede sumar directamente')
        return 0
    else:
        resultado=[]
        for i in range(len(matriz1)):
            fila=[]
            for j in range(len(matriz1[i])):
                suma=matriz1[i][j]+matriz2[i][j]
                fila.append(suma)
            resultado.append(fila)
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

### principal

n=int(input('Introduzca la dimension de la matriz1'))
m=int(input('Introduzca la dimension de la matriz2'))

Matriz1=crearMatriz(n,n)
print("Matriz 1")
mostrarMatriz(Matriz1)
Matriz2=crearMatriz(m,m)
print("Matriz 2")
mostrarMatriz(Matriz2)
print("La Suma de las Matrices es:")
MatrizSuma=sumaMatrices(Matriz1,Matriz2)
mostrarMatriz(MatrizSuma)


