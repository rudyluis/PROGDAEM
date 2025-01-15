from   primos_listas import generar_lista_aleatoria  as ga 
numeros=[1,2,3,4,5]


cuadrados = []  # Lista vacía para almacenar resultados
for x in numeros:
    cuadrados.append(x**2)  # Calcula el cuadrado y lo agrega a la lista

print(cuadrados)  # [1, 4, 9, 16, 25]


cuadrados=[x**2 for x in numeros]
print(cuadrados)

numeros = ga(15,5,99)
print(numeros)
pares=[x for x in numeros if x %2==0]
print(pares)
###
pares2= [x for x in ga(15,5,99)]
print(pares)

###
palabras=["hola","mundo", "python", "listas"]

## listas por comprension tiene 3 partes
## parte del medio corresponde al for (recorrido de cada elemento de la lista)
## parte derecha esta la condicional
## parte izquierda el valor o la operacion que se aplica al elemento de la lista
## siempre en corchetes
mayusculas= [palabra.upper() for palabra in palabras]
print(mayusculas)
segmento= [palabra[0:2].upper() for palabra in palabras]

print(segmento)


import random

serie=[random.randint(0,100) for _ in range(random.randint(0,100))]
print(serie)

print('La suma de los valores de la lista es:',sum([_ **2 for _ in serie ]))



def es_primo(numero):
    sw=0 
    for i in range(1,numero+1):
        if(numero%i==0):
            sw+=1
    if(sw==2):
        return True
    else:
        return False 

pares=[x for x in numeros if es_primo(x)]
print(pares)