import random
def min_max(tupla):
    minimo= min(tupla)
    maximo= max(tupla)
    return (minimo,maximo)


def promedio_tupla(tupla):
    promedio =sum(tupla)/len(tupla)
    return promedio

def encontrar_indice(tupla, elemento):
    if elemento in tupla:
        return tupla.index(elemento)
    else:
        return -1


if __name__=="__main__":
    numeros=(3,7,2,8,5,3)
    print(numeros)
    numeros=tuple(random.randint(1,10) for i in range (10))
    print(numeros)
    resultado=min_max(numeros)
    print(f"El minimo es {resultado[0]} y el valor maximo es {resultado[1]}")
    print(f"La suma de todos los elementos de la tupla {numeros} es:{sum(numeros)}")
    print(f"El promedio de los elementos de la tupla es {promedio_tupla(numeros)}")


    numeros2=tuple(random.randint(1,10) for i in range (10))
    print(numeros2)
    print(numeros+numeros2)

    elemento_buscar= random.randint(1,10)
    print("Elemento a buscar es", elemento_buscar)

    resultado= encontrar_indice(numeros, elemento_buscar)
    if resultado!=-1:
        print(f"El elemento {elemento_buscar} se encuentra en el indice {resultado}")
    else:
        print(f"El elemento {elemento_buscar} no esta en la tupla")
        

