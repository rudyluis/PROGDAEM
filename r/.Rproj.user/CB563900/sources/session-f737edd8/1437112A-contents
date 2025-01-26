# -------------------------
# TOMA DE DECISIONES -> if, else if, else
# -------------------------

# Definimos una variable x con valor 42
x <- 42

# Condición: si x es mayor o igual a 100, muestra un mensaje
if (x >= 100) {
  print("x es mayor o igual que 100")
 
# Si no es mayor o igual a 100, pero x es menor que 100 y mayor o igual a 0, muestra otro mensaje
}else if (x < 100 & x >= 0) {
  print("x es menor que 100 y mayor o igual a 0")
 
# Si ninguna de las condiciones anteriores se cumple (x es negativo), muestra otro mensaje
}else {
  print("x es un numero negativo (menor que 0)")
}

# -------------------------
# Otro ejemplo de condición: verificamos si x es par o impar
# -------------------------

# Usamos el operador %% para verificar si el resto de dividir x entre 2 es 0 (es decir, es par)
if (x %% 2 == 0) {
  print("x es par")  # Si es divisible por 2, es par
} else {
  print("x es impar")  # Si no es divisible por 2, es impar
}

# -------------------------
# OPERADORES LOGICOS -> "and" (&) y "or" (|)
# -------------------------

# Usamos el operador OR (|) para comprobar si x es igual a 3 o a 2
if (x == 3 | x == 2) {
  print("x es igual a 3, x es igual a 2")  # Se cumple si x es 2 o 3
}

# Usamos el operador AND (&) para comprobar si x está entre 0 y 10 (inclusive)
if (x <= 10 & x >= 0) {
  print("x es menor o igual que 10, y mayor o igual que 0")  # Se cumple si x está entre 0 y 10
}

# -------------------------
# SWITCH
# -------------------------

# Definimos una variable num con valor 3
num <- 3

# La función switch evalúa el valor de num y devuelve el elemento correspondiente
result <- switch(
  num,  # Variable a evaluar
  "Uno", # Si num es 1, devuelve "Uno"
  "Dos", # Si num es 2, devuelve "Dos"
  "Tres", # Si num es 3, devuelve "Tres"
  "Cuatro" # Si num es 4, devuelve "Cuatro"
)
print(result)  # Imprime "Tres", porque num vale 3, y la posición 3 corresponde a "Tres"

# Otro ejemplo con valores de texto
x <- "c"

# switch también funciona con valores de texto
result <- switch(
  x,    # Variable que se evalúa
  "a" = "Uno",  # Si x es "a", devuelve "Uno"
  "b" = "Dos",  # Si x es "b", devuelve "Dos"
  "c" = "Tres", # Si x es "c", devuelve "Tres"
  "d" = "Cuatro" # Si x es "d", devuelve "Cuatro"
)
print(result)  # Imprime "Tres", porque x vale "c" y el valor correspondiente es "Tres"
