#### busqueda por profundidad
##lista=[1,2,2,3,3,4,4,5,5]
##lista=[1,2,3,4,5]
import Listas8
def eliminar_duplicados(lista):
    lista_sin_duplicados=[]
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados
##Lista_e=[1,2,2,3,3,4,4,5,5]
Lista_e=[]
Listas8.serializar(Lista_e,10)
print(Lista_e)
print("Lista sin elementos duplicados ")
print(eliminar_duplicados(Lista_e))



