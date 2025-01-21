"""
El MRO (Method Resolution Order) es el orden de resolución de métodos que Python utiliza para determinar qué método o atributo debe ser llamado cuando se hace referencia a un método o atributo en una clase que tiene herencia (incluida la herencia múltiple).

Conceptos principales:
Definición:

El MRO es una lista que describe el orden en que Python buscará métodos o atributos en una jerarquía de clases cuando se llama a un método o atributo en un objeto.
Búsqueda en el MRO:

Python comienza en la clase del objeto y sigue el orden definido en el MRO para buscar el método o atributo.
Si no lo encuentra en la clase actual, pasa a las clases base en el orden definido por el MRO.
Reglas del MRO en herencia múltiple:

En herencia simple (una clase base), el orden es claro: de la clase actual a la clase base.
En herencia múltiple, Python utiliza el algoritmo C3 Linearization para determinar un orden consistente, asegurando que las clases base no se visiten antes que sus subclases.

"""


# Definición de la clase A
class A:
    # Definición del método hablar en la clase A
    def hablar(self):
        print("Hola desde A")  # Imprime un mensaje específico para A

# Definición de la clase F
class F:
    # Definición del método hablar en la clase F
    def hablar(self):
        print("Hola desde F")  # Imprime un mensaje específico para F

# Definición de la clase B, que hereda de A
class B(A):
    # Definición del método hablar en la clase B
    def hablar(self):
        print("Hola desde B")  # Imprime un mensaje específico para B

# Definición de la clase C, que hereda de F
class C(F):
    # Definición del método hablar en la clase C
    def hablar(self):
        print("Hola desde C")  # Imprime un mensaje específico para C

# Definición de la clase D, que hereda de B y C (herencia múltiple)
class D(B, C):
    # Definición del método hablar en la clase D
    def hablar(self):
        print("Hola desde D")  # Imprime un mensaje específico para D

# Crear una instancia de la clase D
d = D()

# Llamar al método hablar de la clase F directamente
F.hablar(d)  # Aquí se invoca el método hablar de la clase F, no el de la clase D.



print(D.__mro__)
# O también:
print(D.mro())