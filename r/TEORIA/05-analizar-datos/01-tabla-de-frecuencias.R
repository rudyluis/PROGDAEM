# ======================================
# TABLA DE FRECUENCIAS - PASO A PASO
# ======================================

# En este ejemplo, se construirán los intervalos y una tabla de frecuencias que incluye:
# - Clases (intervalos)
# - Frecuencia absoluta
# - Frecuencia relativa
# - Frecuencia absoluta acumulada
# - Frecuencia relativa acumulada

# ======================================
# PASO 1: INGRESO DE DATOS
# ======================================

# Los datos se introducen manualmente, pero podrían importarse desde un archivo.
datos <- c(50, 68, 84, 86, 64, 67, 78, 87, 110, 85, 52, 65, 52, 93, 72, 70, 105, 85, 30, 42, 74, 30, 70, 65, 49)

# Ordenamos los datos para tener una idea de su distribución.
# Esto ayuda a identificar el rango y los posibles límites de los intervalos.
print(sort(datos))

# Guardamos la cantidad total de datos en una variable.
numDatos <- length(datos) # Total de datos = 25
print(numDatos)

# ======================================
# PASO 2: DETERMINAR NÚMERO Y TAMAÑO DE INTERVALOS
# ======================================

# Calculamos el número de intervalos con la fórmula de Sturges (raíz cuadrada del número de datos).
num_intervalos <- sqrt(numDatos)
print(num_intervalos) # Resultado = 5 (se redondea al entero inferior).

# Calculamos la amplitud teórica del intervalo.
amplitud_intervalo <- (max(datos) - min(datos)) / num_intervalos
print(amplitud_intervalo) # Resultado = 16

# Redondeamos la amplitud a 20 (según las indicaciones del enunciado).
# Esto facilita la agrupación de los datos en intervalos uniformes.

# ======================================
# PASO 3: DEFINIR LOS LÍMITES DE LOS INTERVALOS
# ======================================

# El valor mínimo es 30 y el máximo es 110.
# Definimos los límites manualmente asegurándonos de incluir todos los valores.
limites <- c(20, 40, 80, 100, 120) 
print(limites)

# Usamos `cut()` para clasificar los datos en intervalos.
# Argumentos importantes:
# - `datos`: El vector de datos.
# - `limites`: Los límites definidos anteriormente.
# - `right = FALSE`: Define que los intervalos serán abiertos por la derecha ([dato1, dato2)).
intervalos <- cut(datos, limites, right = FALSE)

# Verificamos a qué intervalo pertenece cada dato.
print(intervalos)

# ======================================
# PASO 4: CREAR LA TABLA DE FRECUENCIAS
# ======================================

# Usamos la función `table()` para contar la cantidad de datos en cada intervalo.
tabla <- table(intervalos)
print(tabla)

# Convertimos la tabla a un formato de data frame para facilitar su manejo.
tablaVertical <- as.data.frame(tabla)
print(tablaVertical)

# ======================================
# PASO 5: CÁLCULO DE FRECUENCIAS
# ======================================

# Extraemos las columnas de la tabla generada.
Clases <- tablaVertical$intervalos # Intervalos o clases.
FrecAbsoluta <- tablaVertical$Freq # Frecuencia absoluta de cada intervalo.

# Calculamos la frecuencia relativa dividiendo la frecuencia absoluta entre el total de datos.
FrecRelativa <- FrecAbsoluta / numDatos
print(FrecRelativa)

# Calculamos la frecuencia absoluta acumulada usando `cumsum()`.
FrecAbsAcumulada <- cumsum(FrecAbsoluta)
print(FrecAbsAcumulada)

# Calculamos la frecuencia relativa acumulada también con `cumsum()`.
FrecRelAcumulada <- cumsum(FrecRelativa)
print(FrecRelAcumulada)

# Creamos el data frame final con todas las columnas de la tabla de frecuencias.
tablaFreq <- data.frame(Clases, FrecAbsoluta, FrecRelativa, FrecAbsAcumulada, FrecRelAcumulada)
print(tablaFreq)

# ======================================
# PASO 6: EXPORTAR LA TABLA DE FRECUENCIAS
# ======================================

# Cambiamos el directorio de trabajo al lugar donde se guardarán los archivos exportados.
# NOTA: Cambia esta ruta a la que corresponda en tu sistema.
directorio_actual <- getwd()
setwd(directorio_actual)

# Exportar la tabla como archivo .txt usando `write.table()`.
# Argumentos importantes:
# - `file`: Ruta y nombre del archivo de salida.
# - `quote`: FALSE para no incluir comillas alrededor de los datos.
# - `sep`: Separador de columnas; "\t" indica tabulador.
# - `dec`: Separador de decimales; "." en este caso.
# - `row.names`: FALSE para no incluir números de fila.
# - `col.names`: TRUE para incluir los nombres de las columnas.
ruta_relativa <- file.path(getwd(), "/tablaFreq1.txt")
write.table(tablaFreq, file = ruta_relativa, quote = FALSE, sep = "\t", dec = ".", row.names = FALSE, col.names = TRUE)

# Exportar la tabla como archivo Excel usando el paquete `openxlsx`.
# Si no está instalado, lo instalamos automáticamente.
if (!requireNamespace("openxlsx", quietly = TRUE)) install.packages("openxlsx")

# Cargamos la librería `openxlsx`.
library(openxlsx)

# Usamos `write.xlsx()` para exportar el data frame a Excel.
ruta_relativa <- file.path(getwd(), "/tablaFreq1.xlsx")
write.xlsx(tablaFreq, file = ruta_relativa)

# ======================================
# CONCLUSIONES
# ======================================

# Este código muestra cómo:
# 1. Definir intervalos y clasificar datos en ellos usando `cut()`.
# 2. Crear una tabla de frecuencias con frecuencias absolutas, relativas y acumuladas.
# 3. Exportar tablas de frecuencias en formatos .txt y Excel.

