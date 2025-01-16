# Declarar diferentes tipos de variables
numero = 42
cadena = "Python es genial"
booleano = False
decimal = 3.14

# Imprimir el tipo de cada variable usando type()
print("El tipo de 'numero' es:", type(numero))  # Salida: <class 'int'>
print("El tipo de 'cadena' es:", type(cadena))  # Salida: <class 'str'>
print("El tipo de 'booleano' es:", type(booleano))  # Salida: <class 'bool'>
print("El tipo de 'decimal' es:", type(decimal))  # Salida: <class 'float'>

# Solicitar al usuario un dato y mostrar su tipo
entrada_usuario = input("Ingresa algo: ")
print("El tipo de lo ingresado es:", type(entrada_usuario))

# Nota: La entrada del usuario siempre será del tipo 'str' (cadena) por defecto.
