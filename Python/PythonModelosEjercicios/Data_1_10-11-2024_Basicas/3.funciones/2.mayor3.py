# Función para encontrar el mayor de tres números
def encontrar_mayor(a, b, c):
    if a >= b and a >= c:
        mayor = a
    elif b >= a and b >= c:
        mayor = b
    else:
        mayor = c
    return mayor

# Ejemplo de uso
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

mayor = encontrar_mayor(num1, num2, num3)
print(f"El mayor de los tres números es: {mayor}")