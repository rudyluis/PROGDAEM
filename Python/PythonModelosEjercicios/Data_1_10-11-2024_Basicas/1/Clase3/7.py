# Función lambda para verificar si un número es par o impar
es_par = lambda x: "Par" if x % 2 == 0 else "Impar"

# Ejemplo de uso
numero = 7
print(f"El número {numero} es {es_par(numero)}")