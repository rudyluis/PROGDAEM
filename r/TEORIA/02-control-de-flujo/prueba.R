# Cargamos la librería dplyr para realizar operaciones con datos, como agrupar y resumir.
library(dplyr)

# Cargamos la librería ggplot2 para crear gráficos personalizados.
library(ggplot2)

# Resumir datos: 
# Usamos el dataset mtcars (incorporado en R) para calcular estadísticas agrupadas.
resumen <- mtcars %>%          
  group_by(cyl) %>%              # Agrupa los datos por la columna 'cyl' (número de cilindros).
  summarize(
    MediaHP = mean(hp),          # Calcula la media de la columna 'hp' (potencia).
    MediaMPG = mean(mpg)         # Calcula la media de la columna 'mpg' (millas por galón).
  )print()

# Imprimimos el resultado del resumen para verificar las estadísticas calculadas.
print(resumen)

# Crear un gráfico de barras para visualizar la potencia media por número de cilindros.
ggplot(data = resumen, aes(x = factor(cyl), y = MediaHP)) +  # Definimos los datos y mapeamos las variables:
  geom_bar(stat = "identity", fill = "coral") +              # Creamos un gráfico de barras con valores predefinidos.
  theme_minimal() +                                          # Aplicamos un tema minimalista al gráfico.
  labs(
    title = "Potencia Media por Número de Cilindros",        # Agregamos un título al gráfico.
    x = "Cilindros",                                         # Etiqueta para el eje X.
    y = "Potencia Media (HP)"                                # Etiqueta para el eje Y.
  )

# Operaciones básicas con variables
x <- 10                  # Definimos la variable x con un valor de 10.
y <- 5                   # Definimos la variable y con un valor de 5.
suma <- x + y            # Calculamos la suma de x e y.
print(suma)              # Imprimimos el resultado de la suma (en este caso, 15).


ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point()


ggplot(mtcars, aes(x = factor(cyl))) +
  geom_bar(fill="coral")

ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) +
  geom_point(size = 3) +
  ggtitle("Peso vs Consumo por Cilindros") +
  xlab("Peso (1000 lbs)") +
  ylab("Millas por Galón (mpg)")


ggplot(pressure, aes(x = temperature, y = pressure)) +
  geom_line(color = "blue", size = 1)

ggplot(mtcars, aes(x = mpg)) +
  geom_histogram(binwidth = 2, fill = "blue", color = "black")


ggplot(mtcars, aes(x = factor(cyl), y = mpg)) +
  geom_boxplot(fill = "lightgreen")

# Crear un data frame en R
df <- data.frame(
  nombre = c("Ana", "Juan", "Luis"),
  edad = c(25, 30, 35),
  ciudad = c("Madrid", "Barcelona", "Sevilla")
)

print(df)

# Crear un data frame en R
df <- data.frame(
  nombre = c("Ana", "Juan", "Luis"),
  edad = c(25, 30, 35),
  ciudad = c("Madrid", "Barcelona", "Sevilla")
)

print(df)



install.packages("data.table")  # Instalar si no lo tienes
library(data.table)  # Cargar la librería
dt <- data.table(
  nombre = c("Ana", "Juan", "Luis"),
  edad = c(25, 30, 35),
  ciudad = c("Madrid", "Barcelona", "Sevilla")
)

print(dt)

dt[edad > 25]  # Filtrar filas donde edad > 25
dt[, .(nombre, ciudad)]  # Seleccionar solo las columnas "nombre" y "ciudad"
dt[, edad_doble := edad * 2]  # Agregar una nueva columna
print(dt)
