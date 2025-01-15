from primos_listas import generar_lista_aleatoria  as ga 
numeros=[1,2,3,4,5]
cuadrados=[x**2 for x in numeros]
print(cuadrados)

numeros = ga(15,5,99)
print(numeros)
pares=[x for x in numeros if x %2==0]
print(pares)


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
