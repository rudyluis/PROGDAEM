# Función para calcular promedio
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Pedir números al usuario
numeros = []
while True:
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    if entrada.lower() == "fin":
        break
    numeros.append(float(entrada))

# Calcular y mostrar el promedio
if numeros:
    promedio = calcular_promedio(numeros)
    print(f"El promedio de los números es: {promedio:.2f}")
else:
    print("No se ingresaron números.")