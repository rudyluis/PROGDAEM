import Lista16

def vectorPares(lista,n):
    lista=Lista16.serializar(n)
    tam=len(lista)
    par,impar=0,1
    for _ in range(tam):
        if(_ % 2==0):
            par+=2
            lista[_]=par
        else:
            lista[_]=impar
            impar+=2
    return lista

n= int(input('n>>>>>'))
listaVector=[]
print(vectorPares(listaVector,n))