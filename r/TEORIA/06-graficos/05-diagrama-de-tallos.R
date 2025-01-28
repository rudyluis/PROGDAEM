# DIAGRAMA DE TALLOS Y HOJAS

# Creamos un vector de datos, algunos con decimales
datos <- c(1.1, 1, 1.2, 2, 3, 3, 1, 2, 2, 2.3, 1, 3, 1, 1)

# Ver la longitud del vector de datos
length(datos)  # El resultado será 14, ya que hay 14 datos

# Crear el diagrama de tallos y hojas
stem(datos)

# El resultado impreso será:
# 1 | 0000012  -> Esto indica que hay 5 datos con valor 1.0, uno con 1.1 y otro con 1.2
# 2 | 0003     -> Esto indica que hay 3 datos con valor 2.0 y uno con 2.3
# 3 | 000     -> Esto indica que hay 3 datos con valor 3.0

# En el diagrama:
# - Los números a la izquierda del '|' representan la parte entera del número.
# - Los números a la derecha del '|' representan los decimales, con cada repetición indicando la frecuencia de un valor específico.
# En total, los números a la derecha suman 14, lo que coincide con la longitud de los datos.

# Ahora, creamos otro conjunto de datos con valores decimales
datos2 <- c(2.11, 2.3, 1, 1.4, 3.78, 3.14)

# Crear el diagrama de tallos y hojas para este nuevo conjunto de datos
stem(datos2)

# El resultado será:
# 1 | 04    -> Esto indica que hay un dato con valor 1.0 y otro con 1.4
# 2 | 13    -> Esto indica que hay un dato con valor 2.1 y otro con 2.3
# 3 | 18    -> Esto indica que hay un dato con valor 3.1 y otro con 3.7

# Observamos que el diagrama no muestra los valores decimales con más de un decimal completo,
# ya que los valores son redondeados y solo se imprime un decimal, lo que limita la precisión.

