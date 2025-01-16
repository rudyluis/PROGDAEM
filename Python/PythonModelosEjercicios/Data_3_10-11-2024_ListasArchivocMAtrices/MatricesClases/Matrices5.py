import Matrices3
def matriz_worm(matriz):
    cont=0
    n=len(matriz[0])
    for f in range(n):
        if(f % 2==0):
            for c in range(n):
                cont+=1
                matriz[f][c]=cont
        else:    
            for c in range(n-1,-1,-1):
                cont+=1
                matriz[f][c]=cont
    return matriz

Matrices3.mostrarMatriz(matriz_worm(Matrices3.Matrizserializada(9)))


