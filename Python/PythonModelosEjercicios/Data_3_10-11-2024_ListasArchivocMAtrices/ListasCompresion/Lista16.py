def serializar(n):
    lista=[]
    for _ in range(0,n):
        lista.append(0)
    return(lista)

def serieVector(lista,n):
    lista=serializar(n)
    tam=len(lista)
    cont=0
    final=tam-1
    for _ in range(tam//2):
        cont+=1
        lista[_]=cont
        cont+=1
        lista[final]=cont
        final-=1
    if(tam % 2!=0):
        lista[tam//2]=cont+1
    return lista
### principal
if __name__ == "__main__":
    n= int(input('n>>>>>'))
    listaVector=[]
    print(serieVector(listaVector,n))
