# -------------------------
# VECTORES
# -------------------------

# CREAR VECTORES
# Los vectores en R se crean usando la función c() (combine).
# Todos los elementos dentro de un vector deben ser del mismo tipo de dato.
nombres <- c("June", "Naia", "Javi", "Itzi")  # Vector de strings
numeros <- c(1, 2, 3.14, 42, 2024)  # Vector de números (pueden ser enteros o decimales)

# También se pueden asignar nombres a los elementos del vector:
edades <- c("James"=18, "Amy"=14, "John"=64)  # Usamos nombres como índice para los valores

# -------------------------
# ELIMINAR VALORES DE UN VECTOR
# Los valores de un vector se pueden eliminar con un índice negativo.
v <- 1:10  # Crea un vector con los números del 1 al 10
v <- v[-c(1,3,5,7)]  # Eliminamos los números 1, 3, 5 y 7 del vector
v  # Resultado: v = 2 4 6 8 9 10

# -------------------------
# ACCEDER A VALORES DE UN VECTOR
# Para acceder a los elementos de un vector, se usan los corchetes [] con el índice deseado.

print(nombres[2])  # Accede al segundo valor de 'nombres' -> "Naia"
print(nombres[-3])  # Omite el valor en la tercera posición, imprime: "June" "Naia" "Itzi"
print(nombres[1:3])  # Imprime los elementos de la posición 1 a la 3 -> "June" "Naia" "Javi"

print(numeros[5])  # Accede al quinto valor de 'numeros' -> 2024

# Acceso con nombres (en caso de tener nombres asignados)
print(edades["James"])  # Accede a "James" y devuelve su valor: 18
print(edades[["James"]])  # Accede directamente al valor 18 de "James"

# -------------------------
# FUNCIONES DE VECTORES
# R ofrece funciones para trabajar con vectores como: longitud, suma, ordenación, etc.

# Longitud del vector (cuántos elementos tiene)
print(length(nombres))  # Imprime: 4, porque 'nombres' tiene 4 elementos

# Sumar todos los elementos del vector
print(sum(numeros))  # Imprime: 2072.14, la suma de los valores en 'numeros'

# Ordenar el vector de menor a mayor
print(sort(numeros))  # Imprime: 1.00 2.00 3.14 42.00 2024.00

# Ordenar el vector de mayor a menor
print(sort(numeros, decreasing = TRUE))  # Imprime: 2024.00 42.00 3.14 2.00 1.00

# Ver qué valores de un vector están en otro
a <- c(1:10)  # Vector 1
b <- c(1, 3, 7, 15, 20)  # Vector 2
b[b %in% a]  # Devuelve los elementos de b que están también en a: 1 3 7

# -------------------------
# CREAR RANGOS
# Los rangos se pueden crear usando dos formas: usando ':' o seq()

x <- seq(1, 10, by = 2)  # Crea un rango desde 1 hasta 10 con un paso de 2
print(x)  # Imprime: 1 3 5 7 9

# Usar ':' para crear un rango simple
1:5  # Crea el vector: 1 2 3 4 5

# -------------------------
# ARITMÉTICA CON VECTORES
# Se pueden realizar operaciones aritméticas entre vectores si tienen la misma longitud.

v1 <- c(2, 6, 1, 5)  # Vector 1
v2 <- c(5, 3, 4, 8)  # Vector 2

# Sumar vectores
print(v1 + v2)  # Suma los elementos de v1 y v2: 7 9 5 13

# Restar vectores
print(v1 - v2)  # Resta los elementos de v1 y v2: -3 -3 -3 -3

# Multiplicar vectores
print(v1 * v2)  # Multiplica los elementos de v1 y v2: 10 18 4 40

# Dividir vectores
print(v1 / v2)  # Divide los elementos de v1 y v2: 0.400 2.000 0.250 0.625

# -------------------------
# MEDIA Y MEDIANA
# La media y la mediana son funciones estadísticas comunes para un vector de datos.

v <- c(2, 6, 1, 5, 42)

# Calcular la media del vector
print(mean(v))  # Imprime: 11.2

# Calcular la mediana del vector
print(median(v))  # Imprime: 5
