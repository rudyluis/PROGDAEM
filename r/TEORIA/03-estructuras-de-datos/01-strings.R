# -------------------------
# STRINGS = cadenas de texto
# -------------------------

# Obtener caracteres o partes del string -> substr()
# La función substr() extrae una subcadena de un string dado el índice de inicio y fin.
str <- "Hola mundo"

# Extrae el primer carácter (índice 1, 1)
substr(str, 1, 1)  # "H"

# Extrae los caracteres desde el índice 6 hasta el 10 (índices 6 a 10)
substr(str, 6, 10)  # "mundo"

# -------------------------
# Separar en caracteres / convertir string en vector de caracteres -> strsplit()
# La función strsplit() divide un string en un vector de caracteres según el separador que especifiquemos.

# Dividir el string en caracteres individuales
strsplit(str, "")  # c("H", "o", "l", "a", " ", "m", "u", "n", "d", "o")

# El string original no se modifica al usar strsplit
str  # "Hola mundo"

# -------------------------
# Concatenar o unir cadenas -> paste()
# La función paste() se usa para unir varios elementos en una sola cadena.
t1 <- "hello"
t2 <- "world"
t3 <- "!"

# Unir las tres cadenas con el espacio predeterminado
result <- paste(t1, t2, t3)
print(result)  # Imprime: "hello world !"

# Se puede especificar un separador con el argumento 'sep'
result <- paste(t1, t2, t3, sep="-")
print(result)  # Imprime: "hello-world-!"

# -------------------------
# Poner string en mayúscula o minúscula
# Las funciones toupper() y tolower() convierten un string a mayúsculas o minúsculas, respectivamente.
txt <- "Hola"

# Convertir a mayúsculas
txt <- toupper(txt)
print(txt)  # Imprime: "HOLA"

# Convertir a minúsculas
txt <- tolower(txt)
print(txt)  # Imprime: "hola"

# -------------------------
# Convertir string en integer
# Si tenemos un string que representa un número y queremos usarlo como número real, lo convertimos con as.integer()
x <- "5"

# Convertir el string "5" a un valor entero
x <- as.integer(x)

# Ahora x es un número y podemos realizar operaciones con él
print(x * 2)  # Imprime: 10
