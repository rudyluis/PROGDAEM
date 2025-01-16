import random
def bublesort(lista):
    n=len(lista)
    for i in range(n):
        for j in range(n-i-1):
            if(lista[j]>lista[j+1]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista
#### main
if __name__ == "__main__":
    n= int(input('Cantidad de elementos'))
    minimo=int(input('minimo Valor'))
    maximo=int(input('maximo Valor'))

    lista= random.sample(range(minimo,maximo),n)
    print(lista)
    print(bublesort(lista)) 