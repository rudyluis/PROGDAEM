# GRÁFICOS DE BARRAS

# Crear un gráfico de barras simple partiendo de una variable de datos
# En este caso, usamos la columna "hp" (horsepower) del dataset mtcars
barplot(mtcars$hp)

# Podemos usar "names.arg" para establecer los nombres de las etiquetas para
# las barras del gráfico. Aquí estamos utilizando los nombres de las filas
# de mtcars como etiquetas para cada barra.
barplot(mtcars$hp, names.arg = rownames(mtcars))
# rownames(mtcars) obtiene los nombres de las filas de mtcars, que son los nombres de los modelos de autos

# Otro ejemplo, usando un conjunto de datos personalizado:
data <- c(10, 42, 8, 100)  # Datos para las barras
x <- c("A", "B", "C", "D")  # Etiquetas para las barras
barplot(data, names.arg = x)  # Crear gráfico de barras con las etiquetas personalizadas

# Para crear un gráfico de barras horizontal, usamos el parámetro: horiz = TRUE
barplot(mtcars$hp, horiz = TRUE)  # Gráfico de barras horizontal usando la columna "hp"

# Un ejemplo con colores y etiquetas personalizadas
barplot(data, names.arg = x, horiz = TRUE, col = "blue")  # Barras horizontales de color azul
