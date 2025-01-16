import random
def serializar(lista,n, minimo=1,maximo=100): 
    for _ in range(n):
        numero_aleatorio=random.randint(minimo,maximo)
        lista.append(numero_aleatorio)
    return lista
def min_max(lista):
    minimo_lista=min(lista)
    maximo_lista=max(lista)
    return minimo_lista,maximo_lista

if __name__ == "__main__":
    lista_aleatoria=[]
    n=int(input("Introduzca un numero -->"))
    print(serializar(lista_aleatoria,n))
    a,b=min_max(lista_aleatoria)
    print(f"El valor minimo de la lista es {a}")
    print(f"El valor maximo de la lista es {b}")


