# -------------------------
# LISTAS -> pueden guardar diferentes tipos de datos
# -------------------------

# CREAR LISTAS
# Las listas en R pueden almacenar diferentes tipos de datos (cadenas, vectores, números, etc.)
lista1 <- list("June", "hola", c(1, 2, 3), 52.3)
# En este caso, la lista contiene:
# 1. Un string ("June")
# 2. Un string ("hola")
# 3. Un vector con los números (1, 2, 3)
# 4. Un número decimal (52.3)

# -------------------------
# ACCEDER A LOS VALORES DE UNA LISTA
# Para acceder a los valores de una lista, se utiliza '[[]]' en lugar de '[]' (que se usa para vectores).

print(lista1[[3]])  # Imprime: 1 2 3, accede al tercer elemento que es un vector

# También podemos acceder a los elementos usando nombres, si se les asignan nombres a los elementos:
lista2 <- list("name"="Naia", "age"=24, "gender"=1, "student"=TRUE)

print(lista2$name)  # Accede al valor asociado con el nombre "name" -> Imprime: "Naia"
print(lista2[[1]])  # Accede al primer valor de la lista, que es "Naia" -> Imprime: "Naia"

# -------------------------
# AÑADIR NUEVOS VALORES A LAS LISTAS
# Se pueden agregar nuevos elementos a una lista utilizando el operador '$' o '[[]]'.

# Forma 1: Usando '$' para añadir un nuevo elemento con nombre
lista2$country <- "Spain"  # Añade "Spain" como valor bajo el nombre "country"
print(lista2)  # Muestra la lista con el nuevo valor añadido

# Forma 2: Usando '[[]]' para añadir un nuevo elemento con nombre
lista2[["favSport"]] <- "Rugby"  # Añade "Rugby" bajo el nombre "favSport"
print(lista2)  # Muestra la lista con el nuevo valor añadido

# -------------------------
# CONVERTIR UNA LISTA EN VECTOR
# Las listas pueden convertirse en vectores con 'unlist()' para realizar operaciones aritméticas sobre ellos.

nums <- list(2, 4, 6)  # Lista con números
numsVector <- unlist(nums)  # Convertir la lista a un vector

# Ahora 'numsVector' es un vector y podemos usar operaciones de vectores sobre él:
print(sort(numsVector, decreasing = TRUE))  # Imprime: 6 4 2 (vectores ordenados de mayor a menor)
print(mean(numsVector))  # Imprime: 4 (media del vector)

# Nota: Convertir una lista en un vector hace que todos sus elementos pasen a ser del mismo tipo,
# ya que los vectores solo pueden contener elementos del mismo tipo.
