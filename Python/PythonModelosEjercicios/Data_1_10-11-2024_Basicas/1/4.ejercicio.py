x=int(input('Introduzca x'))
y=int(input('Introduzca y'))
z=int(input('Introduzca z'))
s=(x+y)/(x-y)
##print(s)
resulta=s+z
print('El resultado es--->'+str(resulta))



# Solicitar dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Operaciones
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2 if num2 != 0 else "No se puede dividir por cero")
print("¿El primer número es mayor que el segundo?:", num1 > num2)


# Evaluar una expresión compleja con operadores aritméticos y lógicos
resultado = (5 + 3 * 2 > 10) and (4 % 2 == 0 or not False)
print("El resultado de la expresión es:", resultado)