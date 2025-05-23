# -------------------------
# DATA FRAMES -> Para almacenar diferentes tipos de datos en dos dimensiones
# -------------------------

# Un Data Frame es una tabla en la que cada columna tiene un nombre y puede contener cualquier tipo de dato.

# CREAR UN DATA FRAME
# Se crea usando la función `data.frame()`. Cada columna puede tener un tipo de dato diferente.
people <- data.frame("id"=1:2, "name"=c("Cristina", "Naia"), "age"=c(28, 24))
# Aquí creamos una tabla con 2 filas (2 personas) y 3 columnas: id, name y age.
# Las columnas tienen diferentes tipos de datos (numérico para "id" y "age", y texto para "name").

print(people)
# Imprime:
#   id     name age
# 1  1 Cristina  28
# 2  2     Naia  24

# -------------------------
# ACCEDER A LOS DATOS
# Se pueden acceder a las columnas de un Data Frame de varias maneras.
print(people[[2]])     # Imprime la segunda columna ("name"): Cristina Naia
print(people[["name"]]) # También accede a la columna "name"
print(people$name)     # Lo mismo que las dos líneas anteriores

print(people[2])       # Accede a la segunda columna como un Data Frame
# Imprime:
#     name
# 1 Cristina
# 2     Naia

print(people[2, 3])    # Accede a la fila 2, columna 3 (imprime: 24)
print(people[[2, "age"]]) # Accede a la fila 2, columna "age" (imprime: 24)

# -------------------------
# AÑADIR NUEVOS DATOS
# Se pueden agregar nuevas columnas a un Data Frame.
people$rugbyTeam <- c("CUDER", "UBR")
print(people)
# Imprime el Data Frame actualizado:
#   id     name age rugbyTeam
# 1  1 Cristina  28     CUDER
# 2  2     Naia  24       UBR

# -------------------------
# FILTRAR DATOS
# Podemos filtrar el Data Frame usando condiciones.
print(people[people$age > 25, ])  # Muestra todos los datos donde la edad es mayor que 25
# Imprime solo la persona mayor de 25:
#   id     name age rugbyTeam
# 1  1 Cristina  28     CUDER

# También se puede usar la función `subset()` para filtrar:
print(subset(people, age > 25)) # Lo mismo que antes

# -------------------------
# WHICH()
# La función `which()` devuelve las posiciones de los elementos que cumplen una condición.
print(people)  # Para ver el Data Frame
print(which(people$rugbyTeam == "CUDER"))  # Muestra: 1
print(which(people$rugbyTeam == "UBR"))    # Muestra: 2

# -------------------------
# OPERACIONES CON DATA FRAMES
# Las columnas de un Data Frame son vectores, por lo que se pueden usar funciones como `mean()`.
print(mean(people$age))  # Imprime la media de las edades: 26

# -------------------------
# EXAMINAR UN DATA FRAME
# La función `summary()` da un resumen estadístico de cada columna.
summary(people)
# Imprime:
#       id             name        age      rugbyTeam        
# Min.   :1.00   Cristina:1   Min.   :24   Length:2          
# 1st Qu.:1.25   Naia    :1   1st Qu.:25   Class :character  
# Median :1.50                Median :26   Mode  :character  
# Mean   :1.50                Mean   :26                     
# 3rd Qu.:1.75                3rd Qu.:27                     
# Max.   :2.00                Max.   :28                    

# -------------------------
# FACTORS
# Los factores son útiles cuando un Data Frame tiene columnas de texto.
# Los factores almacenan los valores una única vez y mantienen el número de repeticiones.

estaciones <- factor(c("Invierno", "Primavera", "Verano", "Otoño", "Invierno"))
# Creamos un factor con los nombres de las estaciones del año.

print(levels(estaciones))  # Muestra los valores únicos de los factores (niveles)
# Imprime: "Invierno" "Otoño" "Primavera" "Verano"

print(table(estaciones))  # Muestra cuántas veces se repite cada nivel del factor
# Imprime:
# estaciones
# Invierno   Otoño   Primavera   Verano 
#        2       1           1        1 

# -------------------------
# AÑADIR FACTORS A UN DATA FRAME
# También podemos agregar columnas de factores a un Data Frame.
gender <- factor(c("Female", "Female"))
people$gender <- gender  # Añade la columna de género como factor
print(people)
# Imprime:
#   id     name age rugbyTeam gender
# 1  1 Cristina  28     CUDER Female
# 2  2     Naia  24       UBR Female
