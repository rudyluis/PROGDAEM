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
  )

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
