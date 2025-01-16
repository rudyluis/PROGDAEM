def sumarListas(*n):
    print(n)
    lista_resultado=[]
    for lista in n:
        lista_resultado.extend(lista)
    print(lista_resultado)
    print (sum(lista_resultado))
    return 0

def sumarListasComprension(*n):
    return sum([ e for lista in n for e in lista])

def interseccionListas(*listas):
    resultado=set(listas[0])
    print(resultado)
    for lista in listas:
        resultado&=set(lista)

    print(list(resultado))
    return 0

Lista1=[2,3,4,6,7]
Lista2=[7,9,1,4,2]
Lista3=[7,9,1,4,2]
Lista4=[7,9,1,4,2]
Lista5=[7,9,1,4,2]

print(sumarListas(Lista1,Lista2,Lista3,Lista4,Lista5))
interseccionListas(Lista1,Lista2,Lista3,Lista4,Lista5)

print(sumarListasComprension(Lista1,Lista2,Lista3,Lista4,Lista5))


