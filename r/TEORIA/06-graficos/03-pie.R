# GRÁFICO DE SECCIONES ("QUESITOS")

# Crear un gráfico básico de "quesito" usando el vector x para los tamaños de las secciones
# y el vector y para las etiquetas de las secciones. 
x <- c(8, 10, 42, 14)  # Datos que representan los tamaños de cada sección
y <- c("A", "B", "C", "D")  # Etiquetas para cada sección del gráfico
pie(x, labels = y)  # Crear gráfico de secciones con etiquetas correspondientes

# Otro ejemplo: 
# Usamos tapply() para agrupar los datos en base a la columna "gear" del dataset mtcars,
# y luego aplicamos la función mean() para calcular el promedio de la columna "hp" 
# (horsepower) en cada grupo de "gear".
x <- tapply(mtcars$hp, mtcars$gear, mean)  # Promedio de hp para cada valor de gear

# Obtener las etiquetas de las secciones utilizando la función names()
labels <- names(x)  # Las etiquetas serán los valores de "gear"

# Crear el gráfico de secciones con las etiquetas correspondientes
pie(x, labels = labels, main = "Average HP by Gears")  # Gráfico con título personalizado
