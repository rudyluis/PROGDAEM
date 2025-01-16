import Matrices3  as Mat
def matrizCruz(matriz):
    n=len(matriz[0])
    mitad=int((n-1)/2)
    cont=0
    if(n%2!=0):
        for f in range(n):
            cont+=1
            matriz[f][mitad]=cont
        for c in range (n):
            cont+=1
            if(c!=mitad):
                matriz[mitad][c]=cont                
    else:
        print('El tamaño de la matriz no es impar')
    
    return matriz

Mat.mostrarMatriz(matrizCruz(Mat.Matrizserializada(5)))
