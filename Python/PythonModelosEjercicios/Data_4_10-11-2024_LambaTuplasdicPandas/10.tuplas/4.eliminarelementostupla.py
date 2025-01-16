def eliminar_duplicados():
    entrada = input("Ingresa varios números separados por comas: ")
    tupla_numeros = tuple(map(int, entrada.split(',')))
    tupla_sin_duplicados = tuple(set(tupla_numeros))
    return tupla_sin_duplicados

# Ejemplo de uso
sin_duplicados = eliminar_duplicados()
print("Tupla sin duplicados:", sin_duplicados)

def ordenar_tupla():
    entrada = input("Ingresa varios números separados por comas: ")
    tupla_numeros = tuple(map(int, entrada.split(',')))
    tupla_ordenada = tuple(sorted(tupla_numeros))
    return tupla_ordenada

# Ejemplo de uso
ordenada = ordenar_tupla()
print("Tupla ordenada:", ordenada)