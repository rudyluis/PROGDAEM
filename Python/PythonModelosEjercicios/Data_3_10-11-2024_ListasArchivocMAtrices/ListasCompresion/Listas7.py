import random
lista_aleatoria=[]
copia=[]
n=int(input("Introduzca un numero -->"))
for _ in range(n):
    numero_aleatorio=random.randint(-99,100)
    lista_aleatoria.append(numero_aleatorio)
    copia.append(0)
print(lista_aleatoria)
for _ in range(len(copia)):
    if(lista_aleatoria[_] % 2==0):
        ###b[i]=a[i]
        copia[_]=lista_aleatoria[_]

print(copia)