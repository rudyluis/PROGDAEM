mi_lista = ["manzana", "perro", "banana", "gato", "elefante"]
print(mi_lista)
mi_lista.sort()  ### ordenacion normal ascendente A-Z
print(mi_lista)

mi_lista.sort(reverse=True)  ## ordenacion reversa  z-a
print(mi_lista)

mi_lista.sort(key=len)  ### ordenacion cantidad de caracteres
print(mi_lista)