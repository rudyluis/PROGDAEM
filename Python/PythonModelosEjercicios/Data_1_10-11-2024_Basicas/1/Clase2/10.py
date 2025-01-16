import math



while True:
    print("--- Calculadora Básica ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo (residuo de división)")
    print("6. Potencia (base^exponente)")
    print("7. Raíz cuadrada")
    print("8. Salir")
    opcion = int(input("Elige una opción (1-8): "))
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    match opcion:
        case 1:
            # Suma
            print(f"Resultado de la suma: {num1 + num2}")
        case 2:
            # Resta
            print(f"Resultado de la resta: {num1 - num2}")
        case 3:
            # Multiplicación
            print(f"Resultado de la multiplicación: {num1 * num2}")
        case 4:
            # División
            if num2 != 0:
                print(f"Resultado de la división: {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
        case 5:
            # Módulo
            if num2 != 0:
                print(f"Resultado del módulo: {num1 % num2}")
            else:
                print("Error: No se puede calcular el módulo con divisor igual a cero.")
        case 6:
            # Potencia
            print(f"Resultado de la potencia: {num1 ** num2}")
        case 7:
            # Raíz cuadrada
            num = float(input("Introduce el número: "))
            if num >= 0:
                print(f"Resultado de la raíz cuadrada: {math.sqrt(num)}")
            else:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        case 8:
            # Salir
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 8.")
