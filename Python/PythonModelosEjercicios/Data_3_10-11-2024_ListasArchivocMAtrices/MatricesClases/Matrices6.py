import Matrices3  as Mat

def worm_cruz(matriz):
    cont=0
    n=len(matriz[0])
    if(n>=6 & n%2==0):
        mitad2=int(n/2)
        mitad1=int((n/2)-1)
        for f in range(n):
            cont+=1
            matriz[f][mitad1]=cont
        for f in range(n-1,-1,-1):
            cont+=1
            matriz[f][mitad2]=cont
        for c in range(n):
            if(c!= mitad1 and c!=mitad2):
                cont+=1
                matriz[mitad1][c]=cont
        for c in range(n-1,-1,-1):
            if(c!= mitad1 and c!=mitad2):
                cont+=1
                matriz[mitad2][c]=cont
    else:
        print('El tamaño de la matriz no cumple con los requisitos')
    return matriz

Mat.mostrarMatriz(worm_cruz(Mat.Matrizserializada(6)))
