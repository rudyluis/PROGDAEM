def Matrizserializada(n):
    matriz=[[0]*n for _ in range(n)]
    return matriz
def MatrizIdentidad(matriz):
    n=len(matriz[0])
    for i in range(n):
        for j in range(n):
            if(i==j):
                matriz[i][j]=1
    return matriz
def mostrarMatriz(Matriz):
    for fila in Matriz:
        print(fila)   


def mostrar_otra_matriz(matriz):
    n=len(matriz[0])
    for i in range(n):
        j=n-1-i
        matriz[i][j]=1
    return matriz
    
def mostrarmatriz(matriz):
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    M=Matrizserializada(9)
    mostrarMatriz(MatrizIdentidad(M))
    m=Matrizserializada(9)   
    matriz_identidad=MatrizIdentidad(m)  
    matriz_con_otra_diagonal=mostrar_otra_matriz(matriz_identidad)
    print("matriz identidad")
    mostrarmatriz(matriz_identidad)


