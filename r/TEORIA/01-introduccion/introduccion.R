# Esto es un comentario, puedes escribir lo que quieras explicando el código.
# En R, los comentarios comienzan con '#'.

# --------------------
# FUNCIONES BÁSICAS DE SALIDA
# --------------------

# La función `print()` muestra valores en la consola.
# En RStudio, puedes ver el valor de una variable escribiendo solo su nombre.
print("Hola, mundo") # *Ejemplo: imprimir un mensaje.

# --------------------
# VARIABLES
# --------------------
# Para asignar valores a variables, usamos '=' o '<-'.  
# El operador '<-' es el más común en R.

# R es *case-sensitive*: "num" y "Num" son variables diferentes.
num <- 42    # Asignación con '<-'.
Num <- 88    # Distinta a "num".

# --------------------
# TIPOS DE DATOS
# --------------------

# NUMÉRICOS (pueden tener decimales).
var1 <- 3.14

# ENTEROS (sin decimales). Usa 'L' para especificar un entero.
var2 <- 88L

# TEXTO (strings). Usa comillas simples o dobles.
var3 <- "Hola" # Comillas dobles.
var4 <- 'Hola' # Comillas simples.

# Si necesitas incluir comillas dentro del texto, usa '\'.
print("Esto incluye \"comillas\" dentro del texto.")
cat("Sin barras: \"comillas\"\n") # `cat()` no imprime las barras.

# BOOLEANOS (TRUE o FALSE, o simplemente T y F).
verdadero <- TRUE
falso <- FALSE

# --------------------
# OPERACIONES ARITMÉTICAS
# --------------------
# <- alt +- para hacerlo rapido  (tecla de asigancion rapido)

x <- 11
y <- 4

# Suma y resta.
print(x + y)  # 11 + 4 = 15
print(x - y)  # 11 - 4 = 7

# Multiplicación y división.
print(x * y)  # 11 * 4 = 44
print(x / y)  # 11 / 4 = 2.75

# Potencias (dos maneras de escribirlo).
print(x ^ y)  # 11 elevado a 4: 14641.
print(x ** y) # Equivalente: 14641.

# Módulo (resto de la división).
print(x %% y) # 11 %% 4 = 3 (resto).

# División entera (resultado sin decimales).
print(x %/% y) # 11 %/% 4 = 2.

# Funciones `min()` y `max()`.
print(min(x, y)) # El menor de los dos: 4.
print(max(x, y)) # El mayor de los dos: 11.

# Raíz cuadrada: `sqrt()`.
print(sqrt(64)) # Raíz cuadrada de 64: 8.

# Repetir valores con `rep()`.
print(rep(98, 5))             # Repite 98 cinco veces.
print(rep(c("Sí", "No"), 3))  # Repite "Sí", "No" tres veces.

# --------------------
# OPERADORES RELACIONALES
# --------------------
# Devuelven TRUE o FALSE según la comparación.

print(4 < 2)  # ¿4 es menor que 2? -> FALSE.
print(3 >= 3) # ¿3 es mayor o igual a 3? -> TRUE.

# --------------------
# INTRODUCCIÓN DE DATOS
# --------------------

# Usando `scan()` para introducir varios valores separados por ENTER.
input <- scan() # Para detener la entrada, pulsa ENTER con un espacio vacío.
print(input)    # Muestra el vector con los valores introducidos.

# Usando `readline()` para introducir un valor único (como texto).
input <- readline(prompt = "Introduce algo: ")
print(input)  # Muestra lo que el usuario introdujo como cadena de texto.

# Si necesitas trabajar con el valor como número, conviértelo.
input <- as.numeric(input)  # Convierte a tipo numérico.
print(input)  # Muestra el valor convertido.

