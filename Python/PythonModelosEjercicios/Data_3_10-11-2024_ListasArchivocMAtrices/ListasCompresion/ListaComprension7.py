def primeros_elementos(*listas):
    resultado=[]
    for lista in listas:
        resultado.append(lista[0])
    return resultado
def primeros_elementos_comprension(*listas):
    resultado=[ lista[0] for lista in listas]
    return resultado

Lista1=[2,3,4,6,7]
Lista2=[7,9,1,4,2]
Lista3=[7,9,1,4,2]
Lista4=[7,9,1,4,2]
Lista5=[7,9,1,4,2]

print(primeros_elementos(Lista1,Lista2,Lista3,Lista4,Lista5))
print(primeros_elementos_comprension(Lista1,Lista2,Lista3,Lista4,Lista5))