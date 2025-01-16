def sumar_numeros(*n):
    sumar=0
    for numero in n:
        sumar+=numero
    return sumar

def sumar_numeros_directo(*n):

    return sum(n)


print(sumar_numeros(1,2,3,4,5,6,7,8))
print(sumar_numeros_directo(1,2,3,4,5,6,7,8))





