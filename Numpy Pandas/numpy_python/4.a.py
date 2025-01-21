import numpy as np
# Suma, resta, multiplicación y división
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

# Producto escalar
"""
(también llamado "dot product" en inglés) es una operación matemática entre dos 
vectores que produce un único valor escalar. Es ampliamente utilizado en álgebra lineal, 
análisis de datos, gráficos 3D y muchas áreas de la ciencia y la ingeniería.
"""
producto_escalar = np.dot(a, b)
print("\nProducto escalar:", producto_escalar)

# Operaciones con números escalares
print("\nMultiplicación por un escalar:", a * 2)
print("Suma de un escalar:", b + 10)
