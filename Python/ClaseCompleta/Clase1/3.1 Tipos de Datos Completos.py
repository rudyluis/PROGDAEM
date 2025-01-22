# Ejemplo de tipos de datos básicos en Python

# 1. Enteros (int)
entero = 42
print("Entero:", entero)
print("Tipo de dato:", type(entero))
print("Operaciones con enteros:")
print("Suma:", entero + 10)
print("Resta:", entero - 5)
print("Multiplicación:", entero * 2)
print("División entera:", entero // 3)
print("Potencia:", entero ** 2)
print()

# 2. Flotantes (float)
flotante = 3.14
print("Flotante:", flotante)
print("Tipo de dato:", type(flotante))
print("Operaciones con flotantes:")
print("Suma:", flotante + 1.86)
print("División:", flotante / 2)
print("Redondeo:", round(flotante, 1))
print("Conversión a entero:", int(flotante))  # Trunca el valor decimal
print()

# 3. Cadenas de texto (str)
cadena = "Hola, mundo"
print("Cadena de texto:", cadena)
print("Tipo de dato:", type(cadena))
print("Operaciones con cadenas:")
print("Longitud:", len(cadena))
print("Mayúsculas:", cadena.upper())
print("Minúsculas:", cadena.lower())
print("Reemplazar palabras:", cadena.replace("Hola", "Adiós"))
print("Concatenación:", cadena + " ¡Bienvenido!")
print("Multiplicación de cadenas:", cadena * 2)
print()

# 4. Booleanos (bool)
booleano_verdadero = True
booleano_falso = False
print("Booleano (verdadero):", booleano_verdadero)
print("Booleano (falso):", booleano_falso)
print("Tipo de dato:", type(booleano_verdadero))
print("Operaciones con booleanos:")
print("AND lógico:", booleano_verdadero and booleano_falso)
print("OR lógico:", booleano_verdadero or booleano_falso)
print("Negación:", not booleano_verdadero)
print()

# Interacción entre tipos
print("Interacción entre tipos:")
entero = 10
flotante = 2.5
cadena = "Python"
print("Suma de entero y flotante:", entero + flotante)  # Resultado es un flotante
print("Concatenación de cadena y entero:", cadena + " " + str(entero))  # Conversión necesaria
print("Comparación de booleanos:", booleano_verdadero == (entero > flotante))  # True
print()

# Ejemplo práctico: un pequeño formulario
nombre = "Juan"
edad = 25
es_estudiante = True
print("Formulario:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Es estudiante: {'Sí' if es_estudiante else 'No'}")
