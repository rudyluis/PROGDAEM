l=[1,2,3]
print(l)
l2=['Juan','Pedro', 'Maria']
print(l2)
l3=[1,'Juan', 3.4, True]
print(l3)
l4=[1,'Juan', 3.4, True, [5,6]]
print(l4)
print(l4[4])
s=list("Python")  ### la palabra List convierte una cadena en lista simple
print(s)
print(s[::-1])
print(s[::-2])
#### para determinar una posicion solo se coloca los corchetes [indice]
"""

• len(l) : Devuelve el número de elementos de la lista l.
• min(l) : Devuelve el mínimo elemento de la lista l siempre que los datos sean comparables.
• max(l) : Devuelve el máximo elemento de la lista l siempre que los datos sean comparables.
• sum(l) : Devuelve la suma de los elementos de la lista l, siempre que los datos se puedan
sumar.
• dato in l : Devuelve True si el dato dato pertenece a la lista l y False en caso contrario.
• l.index(dato) : Devuelve la posición que ocupa en la lista l el primer elemento con valor
dato.
• l.count(dato) : Devuelve el número de veces que el valor dato está contenido en la lista l.
• all(l) : Devuelve True si todos los elementos de la lista l son True y False en caso contrario.
• any(l) : Devuelve True si algún elemento de la lista l es True y False en caso contrario.
"""


a=[3,8,-4,2,0,1,0]

print("El tamaño de la lista es--->",len(a))
print("El valor minimo es ",min(a))
print("El valor maximo es ",max(a))
print("La suma de los elementos es",sum(a))
print(-2 in a)
print("La posicion del valor de 2 es-->",a.index(2))
print("el valor de 0 se repite es-->",a.count(0))
print(any(a))

"""OPERACIONES
l1 + l2 : Crea una nueva lista concatenan los elementos de la listas l1 y l2.
• l.append(dato) : Añade dato al final de la lista l.
• l.extend(sequencia) : Añade los datos de sequencia al final de la lista l.
• l.insert(índice, dato) : Inserta dato en la posición índice de la lista l y desplaza los
elementos una posición a partir de la posición índice.
• l.remove(dato) : Elimina el primer elemento con valor dato en la lista l y desplaza los que
están por detrás de él una posición hacia delante.
• l.pop([índice]) : Devuelve el dato en la posición índice y lo elimina de la lista l, despla‑
zando los elementos por detrás de él una posición hacia delante.
• l.sort() : Ordena los elementos de la lista l de acuerdo al orden predefinido, siempre que los
elementos sean comparables.
• l.reverse() : invierte el orden de los elementos de la lista l.

"""
a=[3,8,-4,2,0,1,0]
##9
a.append(9)
print(a)
### [3,4,5]
b=[3,4,5]
a.extend(b)
print(a)

a.insert(4,18)
print(a)

a.remove(-4)
print(a)

dato=a.pop(1)
print(dato)
print(a)
a[5]=-7
print(a)
a.sort()
print(a)
a.reverse()
print(a)

b=a   
print(b)
a.remove(5)
print(a)
print(b)

c=list(a)
print(c)
a.remove(4)
print(a)
print(c)
print(b)
















