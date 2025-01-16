
##Mostrar matrices
def mostrarMatriz(Matriz):
    for fila in Matriz:
        print(fila)
##Función principal
if __name__=="__main__":

    print("Por comprension")
    Matriz2=[[1 if(i<=j) else 0 for j in range(5)] for i in range(5)]
    mostrarMatriz(Matriz2)