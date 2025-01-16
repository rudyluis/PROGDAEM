# Solicitar al usuario dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizar operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2  # División normal
division_entera = num1 // num2  # División entera
modulo = num1 % num2  # Residuo de la división
potencia = num1 ** num2  # Potencia

# Mostrar resultados con explicaciones
print("\nResultados de las operaciones aritméticas:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print(f"División entera: {num1} // {num2} = {division_entera}")
print(f"Módulo: {num1} % {num2} = {modulo}")
print(f"Potencia: {num1} ** {num2} = {potencia}")