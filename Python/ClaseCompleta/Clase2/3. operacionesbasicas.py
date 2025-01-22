#%%
# Lista vacía
lista_vacia = []

# Lista con elementos
frutas = ["manzana", "banana", "cereza", "kiwi"]

#%%
# Agregar un elemento
frutas.append("naranja")
print("Con append:", frutas)  # ["manzana", "banana", "naranja"]

# Agregar varios elementos
frutas.extend(["pera", "uva"])
print("Con extend:", frutas)  # ["manzana", "banana", "naranja", "pera", "uva"]

# Insertar un elemento en una posición específica
frutas.insert(1, "cereza")
print("Con insert:", frutas)  # ["manzana", "cereza", "banana", "naranja", "pera", "uva"]

#%%
# Eliminar por valor
frutas.remove("banana")
print("Con remove:", frutas)  # ["manzana", "naranja", "pera"]

# Eliminar por índice
eliminado = frutas.pop(1)
print("Con pop:", frutas)     # ["manzana", "pera"]
print("Elemento eliminado:", eliminado)  # "naranja"

# Vaciar la lista
frutas.clear()
print("Con clear:", frutas)   # []

#%%
numeros = [4, 2, 8, 1, 5]

# Ordenar en orden ascendente
numeros.sort()
print("Con sort (asc):", numeros)  # [1, 2, 4, 5, 8]

# Ordenar en orden descendente
numeros.sort(reverse=True)
print("Con sort (desc):", numeros)  # [8, 5, 4, 2, 1]

# Invertir el orden
numeros.reverse()
print("Con reverse:", numeros)  # [1, 2, 4, 5, 8]

# Ordenar sin modificar la lista original
nueva_lista = sorted(numeros)
print("Con sorted:", nueva_lista)  # [1, 2, 4, 5, 8]
print("Lista original:", numeros)  # [8, 5, 4, 2, 1]

#%%
colores = ["rojo", "azul", "verde", "azul", "amarillo"]

# Buscar el índice de un elemento
indice = colores.index("azul")
print("Índice de 'azul':", indice)  # 1

# Contar apariciones
cantidad = colores.count("azul")
print("Cantidad de 'azul':", cantidad)  # 2
