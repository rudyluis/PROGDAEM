# IMPORTAR DATOS EN R DESDE ARCHIVOS .txt Y EXCEL

# =======================
# CONFIGURAR EL DIRECTORIO DE TRABAJO
# =======================

# `getwd()` permite ver en qué directorio se está trabajando actualmente.
# Esto es útil para saber desde dónde se buscarán o guardarán los archivos.
print(getwd()) # Muestra el directorio actual.

# Cambiar el directorio de trabajo con `setwd()`.
# Especifica la ruta completa donde están los archivos a importar.
setwd("D:/rudy.manzaneda/Documents/GitHub/PROGDAEM/r/teoria/04-importar-exportar-datos") # Cambia el directorio de trabajo.

# Confirmar el cambio de directorio para asegurarnos de que se realizó correctamente.
print(getwd()) # Verifica el nuevo directorio de trabajo.

# =======================
# IMPORTAR DATOS DESDE ARCHIVO .txt
# =======================

# Leer datos desde un archivo de texto (.txt) usando `read.table()`.
# Explicación de los argumentos:
# - file: Ruta del archivo a leer (puede ser solo el nombre si el archivo está en el directorio actual).
# - header: TRUE indica que la primera fila contiene los nombres de las columnas.
# - sep: Especifica cómo están separados los datos, "\t" indica tabulador.
# - dec: Indica el símbolo que se usa para separar decimales, "." en este caso.
# Ruta relativa
ruta_relativa <- file.path(getwd(), "datos-para-importar/costes.txt")
print(ruta_relativa)
data_txt <- read.table(file = ruta_relativa, header = TRUE, sep = "\t", dec = ".")

# Imprimir los primeros registros del data frame para comprobar la importación.
print(head(data_txt)) # `head()` muestra las primeras filas del data frame.

# =======================
# ACCEDER A LOS DATOS IMPORTADOS
# =======================
str(data_txt)
# Acceder a una columna específica del data frame utilizando `$`.
# Aquí accedemos a la columna `costo_unit`.
print(data_txt$costo_unit) # Imprime los valores de la columna `costo_unit`.


# Convertir la columna `costo_unit` a numérico reemplazando comas por puntos si es necesario
data_txt$costo_unit <- as.numeric(gsub(",", ".", data_txt$costo_unit))


# Calcular el promedio de la columna `costo_unit` utilizando la función `mean()`.
print(mean(data_txt$costo_unit)) # Calcula y muestra el promedio de los valores.

# =======================
# IMPORTAR DATOS DESDE UN ARCHIVO EXCEL
# =======================

# Para importar datos de Excel, se necesitan paquetes adicionales.
# En este caso, usaremos `readxl`.
# Primero, verificamos si está instalado, y si no, lo instalamos.
if (!requireNamespace("readxl", quietly = TRUE)) install.packages("readxl")

# Cargar la librería `readxl` para trabajar con archivos Excel.
library(readxl)

# Leer datos desde un archivo Excel (.xlsx) usando `read_excel()`.
# No se necesitan especificar separadores, ya que `read_excel()` detecta automáticamente el formato.
ruta_relativa <- file.path(getwd(), "datos-para-importar/costes.xlsx")
print(ruta_relativa)

data_xlsx <- read_excel(ruta_relativa)

# Verificar que los datos se hayan importado correctamente mostrando las primeras filas.
print(head(data_xlsx)) # `head()` muestra las primeras filas del data frame.

# =======================
# ACCEDER A LOS DATOS DEL ARCHIVO EXCEL
# =======================

# Acceder a una columna específica del data frame Excel utilizando `$`.
# En este caso, accedemos a la columna `costo.unit`.
print(data_xlsx$costo.unit) # Imprime los valores de la columna `costo.unit`.

# =======================
# CONCLUSIONES
# =======================

# En este script, hemos aprendido:
# 1. Cómo configurar el directorio de trabajo en R usando `getwd()` y `setwd()`.
# 2. Cómo importar datos desde un archivo .txt utilizando `read.table()`.
# 3. Cómo instalar y usar librerías para leer archivos Excel con `readxl`.
# 4. Cómo acceder y manipular columnas específicas de los datos importados.

