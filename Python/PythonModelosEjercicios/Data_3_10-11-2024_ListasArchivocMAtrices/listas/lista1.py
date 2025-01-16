
s= [1, "dos", True]
print(s)
s= [1, [3,4], True]
print(s)

##### Creación de listas mediante la función list()

print(list("Python"))
a=list("Python")
print(a[0])
print(a[1:4])
print(a[::-1])

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
print(len(a));
a=[5,3,5,8,7]
print(min(a));
print(max(a));
print(sum(a));
print(5 in a)
print(a.index(3))
print(a.count(5))
print(all(a))
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
###agregar un valor al final
a.append(9)
print(a)
a.extend([6,9,4])
print(a)
a.insert(4,19)
print(a)
a.remove(7)
print(a)
a.pop(4)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

"""
Existen dos formas de copiar listas:
• Copia por referencia l1 = l2: Asocia la la variable l1 la misma lista que tiene asociada la va‑
riable l2, es decir, ambas variables apuntan a la misma dirección de memoria. Cualquier cam‑
bio que hagamos a través de l1 o l2 afectará a la misma lista.


"""

b=a
print(b)
b.remove(5)
print(b)
print(a)

"""
• Copia por valor l1 = list(l2): Crea una copia de la lista asociada a l2 en una dirección de
memoria diferente y se la asocia a l1. Las variables apuntan a direcciones de memoria diferen‑
tes que contienen los mismos datos. Cualquier cambio que hagamos a través de l1 no afectará
a la lista de l2 y viceversa.
"""
c=list(a)
c.remove(5)
print(a)
print(c)




