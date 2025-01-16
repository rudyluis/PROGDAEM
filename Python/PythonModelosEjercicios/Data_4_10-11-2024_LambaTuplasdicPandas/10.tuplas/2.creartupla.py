def crear_tupla_desde_entrada():
    entrada = input("Ingresa varios números separados por comas: ")
    tupla_numeros = tuple(map(int, entrada.split(',')))
    return tupla_numeros

# Ejemplo de uso
numeros = crear_tupla_desde_entrada()
print("La tupla creada es:", numeros)