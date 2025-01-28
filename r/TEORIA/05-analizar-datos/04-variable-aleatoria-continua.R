# VARIABLE ALEATORIA CONTINUA

# DISTRIBUCIONES
# Las distribuciones continuas comunes son:
# - Uniforme        -> unif
# - Exponencial     -> exp
# - Normal          -> norm

# PREFIJOS
# Función de probabilidad -> "d": Calcula la probabilidad para un valor puntual de X
# Función de distribución -> "p": Calcula la probabilidad acumulada hasta un valor X
# Generar valores aleatorios -> "r": Genera valores aleatorios que siguen la distribución
# Función cuantil -> "q": Calcula la X (cuantil) para una probabilidad acumulada

# DISTRIBUCIÓN UNIFORME
# La distribución uniforme tiene la misma probabilidad de que un valor X esté en cualquier punto del intervalo [min, max].
# Función de probabilidad: dunif(x, min=..., max=...) - devuelve la densidad de probabilidad en X.
# Función de distribución acumulada: punif(x, min=..., max=..., lower.tail=TRUE) - devuelve la probabilidad acumulada hasta X.
# Generar valores aleatorios: runif(n, min=..., max=...) - genera n valores aleatorios de la distribución uniforme.
# Función cuantil: qunif(p, min=..., max=..., lower.tail=TRUE) - devuelve el cuantil X correspondiente a la probabilidad p.

# EJEMPLO DE DISTRIBUCIÓN UNIFORME
# Parámetros: min=10, max=40
# a) Probabilidad de que X sea menor que 30
punif(30, 10, 40) # 0.6666667: P(X < 30)

# b) Probabilidad de que X sea mayor que 20
1 - punif(20, 10, 40) # 0.6666667: P(X > 20), equivalente a punif(20, 10, 40, lower.tail = FALSE)
punif(20, 10, 40, lower.tail = F) # 0.6666667: misma probabilidad

# c) Valor de la función de probabilidad en X=30
dunif(30, 10, 40) # 0.3333333: densidad de probabilidad en X=30

# DISTRIBUCIÓN EXPONENCIAL
# La distribución exponencial describe el tiempo entre eventos en un proceso de Poisson.
# Función de probabilidad: dexp(x, 1/B) - devuelve la densidad de probabilidad en X, donde B es la tasa media de eventos.
# Función de distribución acumulada: pexp(q, 1/B, lower.tail=TRUE) - devuelve la probabilidad acumulada hasta el cuantil q.
# Generar valores aleatorios: qexp(p, 1/B) - genera valores aleatorios de la distribución exponencial.
# Función cuantil: qexp(p, 1/B, lower.tail=TRUE) - devuelve el cuantil X correspondiente a la probabilidad p.

# EJEMPLO DE DISTRIBUCIÓN EXPONENCIAL
# Parámetro: B=10 (tasa de eventos)
# a) Probabilidad de que X sea menor o igual a 8
pexp(8, 1/10) # 0.550671: P(X <= 8)

# b) Probabilidad de que X esté entre 2 y 8
pexp(8, 1/10) - pexp(2, 1/10) # 0.3694018: P(2 <= X <= 8)

# DISTRIBUCIÓN NORMAL
# La distribución normal describe muchas variables en la naturaleza que siguen un patrón simétrico alrededor de una media.
# Función de probabilidad: dnorm(x, mean, sd) - devuelve la densidad de probabilidad en X para una distribución normal.
# Función de distribución acumulada: pnorm(q, mean, sd, lower.tail=TRUE) - devuelve la probabilidad acumulada hasta el cuantil q.
# Generar valores aleatorios: rnorm(n, mean, sd) - genera n valores aleatorios de la distribución normal.
# Función cuantil: qnorm(p, mean, sd, lower.tail=TRUE) - devuelve el cuantil X correspondiente a la probabilidad p.

# EJEMPLO DE DISTRIBUCIÓN NORMAL
# Parámetros: media = 65.6, desviación estándar = 14.74
# a) Probabilidad de que X sea menor que 60
pnorm(60, 65.6, 14.74) # 0.3520029: P(X < 60)

# b) ¿Qué valor de X deja el 12.1% a su derecha?
qnorm(0.121, 65.6, 14.74, lower.tail = FALSE) # 82.84584: X que deja el 12.1% a la derecha

# c) Probabilidad de que X sea mayor que 45
pnorm(45, 65.6, 14.74, lower.tail = FALSE) # 0.918877: P(X > 45)
1 - pnorm(45, 65.6, 14.74) # 0.918877: misma probabilidad

# GRAFICAR FUNCIONES DE PROBABILIDAD (DENSIDAD) Y DISTRIBUCIÓN
# Para graficar funciones de probabilidad y distribución se utiliza la función curve().
# Ejemplo de gráficos para las distribuciones uniforme, exponencial y normal:

# Gráfico de la distribución uniforme
curve(dunif(x, 100, 150), from = 0, to = 200) # Densidad de probabilidad
curve(punif(x, 100, 150), from = 0, to = 200) # Distribución acumulada

# Gráfico de la distribución exponencial
curve(dexp(x, 1/10), from = 0, to = 10) # Densidad de probabilidad
curve(pexp(x, 1/10), from = 0, to = 10) # Distribución acumulada

# Gráfico de la distribución normal
curve(dnorm(x, 65.6, 14.74), from = 0, to = 150) # Densidad de probabilidad
curve(pnorm(x, 65.6, 14.74), from = 0, to = 150) # Distribución acumulada
