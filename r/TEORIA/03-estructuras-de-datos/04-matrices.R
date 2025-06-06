# -------------------------
# MATRICES -> Igual que los vectores, pero de dos dimensiones
# -------------------------

# CREAR MATRICES
# Para crear matrices en R, se utiliza la función matrix().
# La función recibe un vector de datos y se le puede especificar el número de filas (nrow) y el número de columnas (ncol).

m <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, ncol = 3)

# Esto crea una matriz de 2 filas y 3 columnas con los valores proporcionados.
# Los valores se llenan por columnas de manera predeterminada.
print(m)
# Imprime:
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6

# Si solo se proporciona 'nrow', 'ncol' se calculará automáticamente, y viceversa.

# -------------------------
# AÑADIR NOMBRES A LAS FILAS Y COLUMNAS
# Puedes añadir nombres a las filas y columnas para hacer que la matriz sea más legible.
rownames(m) <- c("R1", "R2")  # Asignamos nombres a las filas
colnames(m) <- c("C1", "C2", "C3")  # Asignamos nombres a las columnas

# Ahora la matriz se verá como:
#    C1 C2 C3
# R1  1  3  5
# R2  2  4  6

print(m)

# -------------------------
# ACCEDER A LOS VALORES DE UNA MATRIZ
# Para acceder a un valor específico de la matriz, se usa la sintaxis [fila, columna].

print(m[1, 3])  # Imprime: 5 -> fila 1, columna 3
print(m[1, ])   # Imprime: 1 3 5 -> fila 1 (toda la fila)
print(m[, 2])   # Imprime: 3 4 -> columna 2 (toda la columna)

# -------------------------
# ASIGNAR NUEVOS VALORES
# Puedes cambiar los valores de la matriz de manera sencilla asignando un nuevo valor a una posición específica.

m[1, 1] <- 0  # Cambia el valor en la fila 1, columna 1 de 1 a 0
print(m)  # Imprime la matriz actualizada: 
#    C1 C2 C3
# R1  0  3  5
# R2  2  4  6

# -------------------------
# OPERACIONES CON MATRICES

# Traspuesta: Se puede obtener la traspuesta de una matriz con la función 't()'.
# La traspuesta de una matriz intercambia filas por columnas.
print(t(m))  # Imprime la matriz traspuesta
# Imprime:
# 0 2
# 3 4
# 5 6
