# Función con *args para sumar un número variable de argumentos
def suma_varios(*args):
    return sum(args)

# Ejemplo de uso
print(f"La suma es: {suma_varios(1, 2, 3, 4, 5)}")


def suma_numeros(*args):
    total = sum(args)
    return total

# Llamadas a la función
print(suma_numeros(2, 4, 6))  # Salida: 12
print(suma_numeros(1, 1, 1, 1, 1))  # Salida: 5
print(suma_numeros())  # Salida: 0 (caso sin argumentos)


def encontrar_maximo(*args):
    if not args:  # Verificar si no se pasan argumentos
        return "No se proporcionaron números"
    return max(args)

# Llamadas a la función
print(encontrar_maximo(10, 20, 30, 5, 15))  # Salida: 30
print(encontrar_maximo(3, -1, -5, 100, 50))  # Salida: 100
print(encontrar_maximo())  # Salida: No se proporcionaron números