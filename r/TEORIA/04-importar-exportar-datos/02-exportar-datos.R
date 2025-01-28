# ========================
# EXPORTAR DATOS EN R
# ========================

# RECORDATORIOS IMPORTANTES:
# - Es necesario tener instaladas y activas las librerías necesarias para trabajar con archivos Excel, como `readxl` y `openxlsx`.
# - Es preferible trabajar en el directorio donde se van a guardar los datos exportados para facilitar la organización.

# ========================
# CONFIGURAR EL DIRECTORIO DE TRABAJO
# ========================

# Cambiar el directorio de trabajo donde se guardarán los archivos exportados.
# Asegúrate de especificar la ruta correcta en tu máquina.
setwd("D:/rudy.manzaneda/Documents/GitHub/PROGDAEM/r/teoria/04-importar-exportar-datos") # Cambia el directorio de trabajo.

# Confirmar el directorio actual para verificar que estamos en el lugar correcto.
print(getwd()) # Muestra el directorio de trabajo actual.

# ========================
# CREAR UN DATA FRAME
# ========================

# 1. Crear vectores con datos numéricos.
# `num` es un vector que contiene los números del 1 al 10.
num <- 1:10 # Equivalente a `c(1:10)` o `c(1,2,3,...,10)`.

# `num_cuadrado` es el resultado de elevar al cuadrado los valores del vector `num`.
num_cuadrado <- num ^ 2

# `num_cubo` es el resultado de elevar al cubo los valores del vector `num`.
num_cubo <- num ^ 3

# 2. Crear un data frame combinando los vectores.
# Un data frame es una estructura tabular que organiza los datos en filas y columnas.
numeros <- data.frame(num, num_cuadrado, num_cubo)

# Ver el contenido del data frame para asegurarnos de que se creó correctamente.
print(numeros) # Muestra el contenido completo del data frame.

# Nota: Los datos creados directamente en R, como este data frame, ya son accesibles sin necesidad de usar `attach()`.

# Ejemplo de operaciones con el data frame:
print(num) # Accede directamente al vector `num`.
print(mean(num_cuadrado)) # Calcula y muestra el promedio de `num_cuadrado`.

# ========================
# EXPORTAR DATOS A FORMATO .txt
# ========================

# Usamos la función `write.table()` para exportar el data frame a un archivo `.txt`.
# Argumentos importantes:
# - file: Nombre del archivo de salida (incluyendo extensión .txt).
# - sep: Especifica el separador entre columnas, "\t" indica tabulador.
# - dec: Indica el símbolo para separar decimales, "." en este caso.
# - row.names: FALSE para no incluir los números de las filas en el archivo.
# - col.names: TRUE para incluir los nombres de las columnas en el archivo.
write.table(numeros, 
            file = "numeros-exportados.txt", 
            sep = "\t", 
            dec = ".", 
            row.names = FALSE, 
            col.names = TRUE)

# ========================
# EXPORTAR DATOS A FORMATO EXCEL
# ========================

# Instalar y cargar la librería `openxlsx` si no está instalada.
# Esto es necesario para trabajar con archivos Excel.
if (!requireNamespace("openxlsx", quietly = TRUE)) install.packages("openxlsx")

# Cargar la librería para usar sus funciones.
library(openxlsx)

# Usamos la función `write.xlsx()` para exportar el data frame a un archivo Excel (.xlsx).
# Argumentos importantes:
# - file: Nombre del archivo de salida (incluyendo extensión .xlsx).
write.xlsx(numeros, file = "numeros-exportados.xlsx")

# ========================
# CONCLUSIONES
# ========================

# En este script, hemos aprendido:
# 1. Cómo crear un data frame combinando vectores.
# 2. Cómo exportar datos a un archivo de texto (.txt) utilizando `write.table()`.
# 3. Cómo exportar datos a un archivo Excel (.xlsx) utilizando `write.xlsx()`.
# 4. La importancia de configurar correctamente el directorio de trabajo.

