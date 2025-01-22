import random
def generar_lista_aleatoria(n,ri,rf):
    lista=[]
    for i in range(n):
        lista.append(random.randint(ri,rf))
    return lista

def obtener_primos(lista):
    primos=[]
    for num in lista:
        if es_primo(num):
            primos.append(num)
    return primos 

def es_primo(numero):
    sw=0 
    for i in range(1,numero+1):
        if(numero%i==0):
            sw+=1
    if(sw==2):
        return True
    else:
        return False 


if __name__=="__main__":
    n= int(input('Introduzca el tamaño de la lista'))
    rango_inicio=int(input('Rango de Inicio>>>'))
    rango_final=int(input('Rango Final>>>>'))
    lista_original= generar_lista_aleatoria(n,rango_inicio,rango_final)
    print("Lista original-->", lista_original)

    primos = obtener_primos(lista_original)
    print("La Lista de los numeros primos es --->", primos)

    lista_unida= lista_original+primos
    print("Las Listas unidas son>>>", lista_unida)

