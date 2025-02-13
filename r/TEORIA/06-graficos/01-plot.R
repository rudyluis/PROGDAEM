# GRÁFICOS BÁSICOS -> plot()

# Definir el directorio de trabajo donde se guardarán los gráficos o donde están los datos

#setwd(getwd())

# Crear un gráfico simple con puntos:
# En este caso, se van a graficar los valores (1,1), (2,2), ..., (10,10)
plot(1:10, main = "My Chart", xlab = "X-axis", ylab = "Y-axis")
# "main" define el título del gráfico
# "xlab" define la etiqueta del eje X
# "ylab" define la etiqueta del eje Y

# Podemos definir valores concretos para las variables y graficarlos:
x <- mtcars$wt  # Asignar la columna de "weight" del dataset mtcars a x
y <- mtcars$drat  # Asignar la columna de "rear axle ratio" del dataset mtcars a y
plot(x, y, xlab = "weight", ylab = "rear axle ratio")  # Graficar weight vs rear axle ratio

data(mtcars)
# Crear gráficos con líneas en vez de puntos:
# Usando "type = 'l'" para cambiar de puntos a líneas
plot(1:10, type = "l")  # Gráfico de líneas con los valores 1 a 10

# Podemos dibujar varias líneas en el mismo gráfico usando la función lines():
line1 <- c(0, 8, 14, 42)  # Definir los valores de la primera línea
line2 <- c(2, 4, 6, 8)    # Definir los valores de la segunda línea
plot(line1, type = "l", col = "blue")  # Graficar la primera línea en color azul
lines(line2, type = "l", col = "red")  # Añadir la segunda línea en color rojo

# Dibujar una "X" en el gráfico:
x1 <- c(1, 10)  # Coordenadas para la primera línea de la "X"
y1 <- c(1, 10)
x2 <- c(1, 10)  # Coordenadas para la segunda línea de la "X"
y2 <- c(10, 1)

# Graficar la primera línea de la "X"
plot(x1, y1, type = "l")
# Añadir la segunda línea de la "X"
lines(x2, y2, type = "l")

