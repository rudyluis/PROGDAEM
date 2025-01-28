# VARIABLE ALEATORIA DISCRETA

# DISTRIBUCIONES
# Se mencionan las principales distribuciones de probabilidad discretas:
# - Binomial            -> binom
# - Hipergeométrica     -> hyper
# - Poisson             -> pois
# - Binomial negativa   -> nbinom

# PREFIJOS
# Función de probabilidad -> "d": Calcula la probabilidad para un valor puntual de X
# Función de distribución -> "p": Calcula la probabilidad acumulada hasta un valor X
# Generar valores aleatorios -> "r": Genera valores aleatorios que siguen la distribución
# Función cuantil -> "q": Calcula la X (cuantil) para una probabilidad acumulada

# EJEMPLO: Vamos a trabajar con una variable aleatoria que sigue una distribución binomial.
# Los parámetros son n=10 (número de ensayos) y p=0.3 (probabilidad de éxito en cada ensayo).

# a) Probabilidad de que tome el valor 4 (x=4)

# Para obtener la probabilidad de que X sea igual a 4, utilizamos la función de probabilidad "d"
# Distribución binomial -> prefijo "d" y la función correspondiente es "binom"
# dbinom(x, n, p) nos da la probabilidad de que X tome el valor 4
x <- 4
n <- 10
p <- 0.3
dbinom(x, n, p) # Probabilidad de que X = 4 -> 0.2001209

# También se puede escribir de forma compacta
dbinom(4, 10, 0.3) # 0.2001209

# b) Probabilidad acumulada hasta llegar al valor de 4.
# Esto significa calcular P(X <= 4), la probabilidad de que X tome un valor igual o menor que 4.

# Para calcular la probabilidad acumulada, utilizamos el prefijo "p" y la función "binom" nuevamente
# pbinom(x, n, p) nos da la probabilidad acumulada hasta el valor 4
pbinom(x, n, p) # Probabilidad acumulada hasta X = 4 -> 0.8497317


# CREAR SUCESOS ALEATORIOS

# Para generar sucesos aleatorios que siguen una distribución, usamos la función "sample()".
# Sample selecciona valores de un vector (x) de acuerdo con las condiciones que le indiquemos.

# Ejemplo: Lanzamiento de un dado

# Definimos el dado como un vector de números del 1 al 6
dado <- 1:6

# Simulamos un solo lanzamiento del dado. El valor obtenido es aleatorio.
sample(dado, 1) # Lanzamiento de un dado -> puede salir 4, por ejemplo

# Simulamos 5 lanzamientos del dado, permitiendo que se repitan los valores.
sample(dado, 5, replace = TRUE) # Lanzar el dado 5 veces -> 5 4 2 3 2

# Si el dado estuviera "trucado" y tuviera más probabilidad de sacar ciertos valores,
# podemos especificar las probabilidades de cada lado.

# Definimos las probabilidades de cada cara del dado. La cara con el número 6 tiene más probabilidad.
probDado <- c(0.1, 0.1, 0.1, 0.1, 0.1, 0.5) # Más probabilidad de sacar 6

# Simulamos 5 lanzamientos del dado trucado. Los valores que salen siguen las probabilidades definidas.
sample(dado, 5, replace = TRUE, prob = probDado) # Ejemplo: 1 6 6 3 6


# REPRESENTACIÓN DE LAS FUNCIONES DE PROBABILIDAD Y DISTRIBUCIÓN

# Vamos a ilustrar la distribución binomial para lanzar 5 dados, y queremos calcular la probabilidad
# de obtener entre 0 y 5 veces el valor 1 o 2 (es decir, X: obtener 1 o 2).

# Primero definimos el vector de resultados posibles para el número de veces que salga 1 o 2 (de 0 a 5).
z <- 0:5

# Generamos el gráfico de la función de probabilidad para esta distribución binomial.
# Usamos dbinom para obtener las probabilidades y tipo "h" para dibujar barras (diagrama de barras).
plot(z, dbinom(z, 5, 2/6), type = "h") 
# Esto muestra la probabilidad de obtener 0, 1, 2, 3, 4, o 5 veces 1 o 2 en 5 lanzamientos.

# Ahora vamos a mostrar la función de distribución acumulada (CDF).
# Usamos pbinom para obtener las probabilidades acumuladas.
plot(z, pbinom(z, 5, 2/6), type = "s")
# El tipo "s" dibuja una línea escalonada para la función acumulada, mostrando la probabilidad de
# obtener hasta 0, 1, 2, 3, 4 o 5 veces el valor 1 o 2.

