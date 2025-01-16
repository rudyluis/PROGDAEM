# Función para generar la serie de Fibonacci
def generar_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

# Función para sumar los primeros 'n' números de Fibonacci
def sumar_fibonacci(n):
    fibonacci = generar_fibonacci(n)
    return sum(fibonacci)

# Función para calcular el promedio de los primeros 'n' números de Fibonacci
def promedio_fibonacci(n):
    fibonacci = generar_fibonacci(n)
    return sum(fibonacci) / len(fibonacci)


if (__name__=='__main__'):
    # Ejemplo de uso
    print("Primeros 10 números de Fibonacci:", generar_fibonacci(10))
    print("Suma de los primeros 10 números de Fibonacci:", sumar_fibonacci(10))
    print("Promedio de los primeros 10 números de Fibonacci:", promedio_fibonacci(10))