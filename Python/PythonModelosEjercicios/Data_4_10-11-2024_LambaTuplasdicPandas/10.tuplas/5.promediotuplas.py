def calcular_promedio():
    entrada = input("Ingresa varios números separados por comas: ")
    tupla_numeros = tuple(map(int, entrada.split(',')))
    promedio = sum(tupla_numeros) / len(tupla_numeros)
    return promedio

# Ejemplo de uso
promedio = calcular_promedio()
print("El promedio de los números es:", promedio)