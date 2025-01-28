# CÁLCULOS ESTADÍSTICOS

# COMANDOS BÁSICOS
datos <- c(74,56,72,40,82,76,72,87,81,50,65,62) # Crear un vector con los datos

# Ordenar los valores del vector de menor a mayor
sort(datos) # 40 50 56 62 65 72 72 74 76 81 82 87

# Mostrar las posiciones que tendrían los datos si estuvieran ordenados de menor a mayor
order(datos) # 4 10  2 12 11  3  7  1  6  9  5  8

# Sumar todos los datos del vector
sum(datos) # 817

# Acumulando la suma de los valores (cumsum)
cumsum(datos) # 74 130 202 242 324 400 472 559 640 690 755 817

# Longitud del vector (número de elementos)
length(datos) # 12

# Obtener el valor mínimo y máximo del conjunto de datos
min(datos) # 40
max(datos) # 87

# MEDIDAS DE TENDENCIA CENTRAL
# Calcular la media (promedio) y la mediana de los datos
mean(datos) # 68.08333
median(datos) # 72

# Moda (frecuencia de los valores más comunes)
# Forma 1: Usar la función table() para contar las ocurrencias
table(datos) # Muestra la frecuencia de cada valor

# Forma 2: Usar data.frame para encontrar el valor más frecuente
freqAbs <- data.frame(table(datos)) # Convertir a data frame
freqAbs # Ver las frecuencias
modaPos <- which(freqAbs$Freq == max(freqAbs$Freq)) # Encontrar la posición de la moda
modaPos # Ver la posición de la moda
moda <- freqAbs$datos[6] # Extraer el valor de la moda
moda # 72

# Forma 3: Usar la librería modeest para calcular la moda
install.packages("modeest") # Instalar el paquete
library(modeest) # Cargar el paquete
mfv(datos) # 72

# MEDIDAS DE POSICIÓN
# Cuartiles: Dividir los datos en 4 partes iguales
quantile(datos) # 0% 25% 50% (mediana) 75% 100%

# Deciles: Dividir los datos en 10 partes iguales (percentiles)
quantile(datos, prob = seq(0, 1, length = 11)) # Muestra los 10 deciles

# Percentiles: Dividir los datos en 100 partes iguales
quantile(datos, prob = seq(0, 1, length = 101)) # Muestra los 100 percentiles

# Para calcular un percentil específico (ejemplo para el 20%)
quantile(datos, prob = 0.2) # Decil 2 (20%) -> 57.2

# Para calcular otro percentil específico (ejemplo para el 65%)
quantile(datos, prob = 0.65) # Percentil 65 -> 74.3

# MEDIDAS DE DISPERSIÓN
# Rango de los datos (máximo - mínimo)
rangoDatos <- max(datos) - min(datos) # Calcular el rango
rangoDatos # 47

# Alternativa: Usar la función range() para obtener el valor mínimo y máximo
range(datos) # Da el mínimo y el máximo
rangoDatos2 <- range(datos) # Guardar los valores en una variable
print(rangoDatos2[2] - rangoDatos2[1]) # Mostrar el rango

# Calcular la varianza (cuasivarianza por defecto) de los datos
var(datos) # 195.9015

# Calcular la desviación típica (cuasidesviación por defecto) de los datos
sd(datos) # 13.99648

# ASIMETRÍA Y CURTOSIS
# Instalar y cargar el paquete 'e1071' para calcular la asimetría y curtosis
install.packages("e1071") # Instalar el paquete
library(e1071) # Cargar la librería

# Calcular la asimetría de los datos
# Si es >0, la distribución es asimétrica a la derecha; si es <0, a la izquierda.
skewness(datos) # -0.5360495 -> Asimetría negativa (a la izquierda)

# Calcular la curtosis de los datos
# Si es >0, la distribución es leptocúrtica; si es <0, platicúrtica.
kurtosis(datos) # -0.935555 -> Curtosis platicúrtica

# EJEMPLOS SENCILLOS

# ENUNCIADO 1: Calcular:
#   - media
#   - mediana
#   - cuasivarianza y varianza
#   - cuasidesviación típica y desviación típica
#   - cuartiles

# Definir el vector de datos
datos1 <- c(1,1,1,2,3,3,1,2,2,1,3,1,1)
n1 <- length(datos1) # Número de elementos en el conjunto de datos

# Obtener resumen básico: m?nimo, Q1, mediana (Q2), media, Q3 y máximo
summary(datos1) # Muestra el resumen estadístico
mean(datos1) # Media
median(datos1) # Mediana

# Calcular la cuasivarianza (con corrección de Bessel)
cuasivarianza1 <- var(datos1)
cuasivarianza1 # 0.7307692

# Calcular la varianza ajustada (sin corrección de Bessel)
varianza1 <- cuasivarianza1 * (n1 - 1) / n1
varianza1 # 0.6745562

# Calcular la cuasidesviación típica (con corrección de Bessel)
cuasidesviacion1 <- sd(datos1)
cuasidesviacion1 # 0.8548504

# Calcular la desviación típica ajustada
desviacion1 <- sqrt(varianza1)
desviacion1 # 0.8213137

# ENUNCIADO 2: Dado el conjunto de datos2, calcular:
#   - media
#   - mediana
#   - Q1 y Q3
#   - mínimo y máximo sin quitar valores atípicos
#   - mínimo y máximo quitando valores atípicos

# Definir el conjunto de datos
datos2 <- c(115,232,181,161,155,137,165,171,139,130,406)
n2 <- length(datos2)

# Calcular resumen sin quitar valores atípicos
summary(datos2) # Muestra el resumen estadístico

# Detectar valores atípicos utilizando boxplot.stats()
boxplot.stats(datos2) # Detecta valores atípicos

# Identificar el valor atípico (406)
# Extraer el valor atípico usando 'boxplot.stats()'
# Los valores atípicos están en el componente '$out'
# En este caso, el valor atípico es el "406"

# Obtener la posición del valor atípico en el conjunto de datos
atypicalPos <- which(datos2 == 406) 

# Eliminar el valor atípico del conjunto de datos
datos2sin <- datos2[-11] # Eliminar el valor en la posición 11 (406)

# Calcular el resumen sin los valores atípicos
summary(datos2sin) # Muestra el resumen sin valores atípicos

