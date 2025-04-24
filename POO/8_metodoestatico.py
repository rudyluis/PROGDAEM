class Calculadora:
    
    @staticmethod
    def suma(a, b):
        return a + b
    
    @staticmethod
    def resta(a, b):
        return a - b

# Llamar al método estático usando la clase
print(Calculadora.suma(5, 3))  # Salida: 8
print(Calculadora.resta(5, 3))  # Salida: 2

# Llamar al método estático usando una instancia
calculadora = Calculadora()
print(calculadora.suma(5, 3))  # Salida: 8
print(calculadora.resta(5, 3))  # Salida: 2

"""

El decorador @staticmethod en Python se utiliza para definir un método estático dentro de una clase. 
Un método estático es un método que no depende de la instancia de la clase ni de los atributos de la clase. 
Esto significa que puedes llamarlo sin necesidad de crear un objeto de esa clase.

¿Para qué se usa?
Un método estático es útil cuando necesitas realizar una operación que está relacionada con la clase, 
pero que no necesita acceder a ningún atributo o método de la instancia. 
Se utiliza cuando la funcionalidad del método no requiere información sobre la instancia o la clase, 
pero aún así tiene sentido que forme parte de la clase.

Características:
No recibe el primer parámetro self (referente a la instancia) ni el parámetro cls (referente a la clase), ya que no necesita acceso a ellos.
Puedes llamar a un método estático a través de la clase o de una instancia.
Se usa cuando el comportamiento de la función es independiente del estado de los objetos de la clase.

"""
"""
@property
Convierte un método en una propiedad de solo lectura.
"""

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

p = Persona("Juan")
print(p.nombre)  # 


"""
@classmethod
Se usa para definir un método que opera sobre la clase en lugar de una instancia.

"""
class Circulo:
    pi = 3.1416

    @classmethod
    def cambiar_pi(cls, nuevo_valor):
        cls.pi = nuevo_valor

Circulo.cambiar_pi(3.14)
print(Circulo.pi)  # 3.14