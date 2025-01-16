def filtrar_pares():
    entrada = input("Ingresa varios números separados por comas: ")
    tupla_numeros = tuple(map(int, entrada.split(',')))
    tupla_pares = tuple(num for num in tupla_numeros if num % 2 == 0)
    return tupla_pares

# Ejemplo de uso
pares = filtrar_pares()
print("Los números pares son:", pares)