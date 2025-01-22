# Definición de variables y tipos de datos
# Este ejemplo muestra cómo las variables pueden cambiar de tipo dinámicamente en Python

# Ejemplo básico: cambio de tipo de datos
x = 1
print("x =", x, "| Tipo de dato:", type(x))  # Entero (int)

x = 2.4
print("x =", x, "| Tipo de dato:", type(x))  # Flotante (float)

x = '1'
print("x =", x, "| Tipo de dato:", type(x))  # Cadena de texto (str)

x = True
print("x =", x, "| Tipo de dato:", type(x))  # Booleano (bool)

# Constantes
PI = 3.14  # Por convención, las constantes se escriben en mayúsculas
print("El valor de PI es:", PI)

# Operaciones aritméticas y asignaciones
x = 5
print("\nValor inicial de x:", x)

# Incremento
x += 10  # x = x + 10
print("Después de sumar 10, x =", x)

# Decremento
x -= 6  # x = x - 6
print("Después de restar 6, x =", x)

# Multiplicación
x *= 3  # x = x * 3
print("Después de multiplicar por 3, x =", x)

# División
x /= 2  # x = x / 2
print("Después de dividir entre 2, x =", x)

# Potencia
x **= 2  # x = x ** 2
print("Después de elevar al cuadrado, x =", x)

# División entera
x //= 2  # x = x // 2
print("Después de la división entera entre 2, x =", x)

# Módulo
x %= 2  # x = x % 2
print("Resto de dividir entre 2, x =", x)

# Nota adicional: manejar tipos de datos mixtos
x = 10
y = 3.5
resultado = x + y
print("\nLa suma de un entero y un flotante da como resultado un tipo:", type(resultado))

# Ejemplo adicional para reforzar conceptos
nombre = "Juan"
edad = 30
es_estudiante = True
print(f"\nEl nombre es {nombre}, tiene {edad} años y es estudiante: {es_estudiante}")
