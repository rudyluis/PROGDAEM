import Listas8
def separar_pares_impares(lista):
    pares=[]
    impares=[]
    for numero in lista:
        if(numero %2 ==0):
            pares.append(numero)
        else:
            impares.append(numero)
    ##for i in range(len(lista))
      ##3  if(lista[i]%2==0)   
    return pares, impares
Lista_e=[]
Listas8.serializar(Lista_e,20)
print(Lista_e)
pares,impares=separar_pares_impares(Lista_e)
print(f"Pares: {pares}, Impares:{impares}")
print(f"Suma Pares: {sum(pares)}, Suma Impares:{sum(impares)}")