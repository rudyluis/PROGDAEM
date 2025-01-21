"""
Una clase abstracta es una clase en la programación orientada a objetos que no se puede instanciar 
directamente, es decir, no puedes crear objetos de esa clase. Su principal propósito es servir como una base para otras clases. 
Las clases abstractas permiten definir una interfaz común para un grupo de clases relacionadas, 
pero delegan los detalles de la implementación a las clases derivadas.

Características principales de una clase abstracta:
No se puede instanciar: No puedes crear un objeto de una clase abstracta. 
En su lugar, se utiliza como base para otras clases que implementan sus métodos abstractos.

Métodos abstractos: Los métodos abstractos son aquellos que se definen en la clase abstracta 
pero no tienen una implementación. Las clases derivadas deben implementar estos métodos. En Python, se definen con el decorador @abstractmethod del módulo abc.

Puede tener métodos concretos: Aunque los métodos abstractos no tienen implementación, 
una clase abstracta puede tener métodos que sí tienen una implementación completa. Estos métodos pueden ser heredados directamente por las clases derivadas.

Propósito: Una clase abstracta proporciona una estructura base común para otras clases. 
Define un contrato que las clases derivadas deben seguir, asegurando que ciertos métodos estén presentes y sean implementados.

"""


"""

La librería abc en Python significa "Abstract Base Classes" (Clases Base Abstractas) 
y proporciona herramientas para definir clases abstractas y métodos abstractos.
Una clase abstracta es una clase que sirve como base para otras clases y que no se puede instanciar directamente.
"""

from abc import ABC, abstractmethod

# Clase base abstracta
class Animal(ABC):
    
    # Método abstracto (sin implementación)
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def moverse(self):
        pass

# Clase derivada 1: Perro
class Perro(Animal):
    
    def hacer_sonido(self):
        print("Guau")
    
    def moverse(self):
        print("El perro corre")

# Clase derivada 2: Gato
class Gato(Animal):
    
    def hacer_sonido(self):
        print("Miau")
    
    def moverse(self):
        print("El gato camina lentamente")

# Crear instancias de las clases derivadas
perro = Perro()
gato = Gato()

# Llamar a los métodos implementados
perro.hacer_sonido()  # Imprime: Guau
perro.moverse()       # Imprime: El perro corre

gato.hacer_sonido()   # Imprime: Miau
gato.moverse()        # Imprime: El gato camina lentamente


"""

Clase base abstracta Animal:

Esta clase hereda de ABC (Abstract Base Class) que la convierte en una clase abstracta.
Los métodos hacer_sonido y moverse son métodos abstractos, lo que significa que no tienen implementación en la clase Animal, pero deben ser implementados por cualquier clase que herede de Animal.
Clases derivadas Perro y Gato:

Ambas clases heredan de Animal y proporcionan implementaciones concretas para los métodos abstractos hacer_sonido y moverse.
Si intentamos crear una instancia de la clase Animal o dejar de implementar cualquiera de los métodos abstractos en las clases derivadas, Python lanzará un error.
Abstracción:

Usamos la clase Animal para abstraer lo común entre todas las clases de animales (como el método hacer_sonido y moverse).
Cada animal (perro, gato, etc.) puede tener su propia implementación de esos métodos, lo que es un ejemplo claro de la abstracción: estamos ocultando los detalles de cómo hacen el sonido y cómo se mueven, pero sabemos que todos los animales deben tener estas acciones.
Beneficios de la abstracción:
Oculta detalles de implementación: Los usuarios solo interactúan con los métodos públicos de la clase, sin necesidad de saber cómo están implementados internamente.
Facilita la extensión: Puedes crear nuevas clases que hereden de la clase abstracta sin tener que modificar la clase base. Cada subclase puede proporcionar su propia implementación.
Reutilización de código: Puedes definir métodos comunes en la clase base, lo que evita duplicación de código.
Reglas en Python:
No puedes instanciar una clase abstracta directamente.
Todas las clases derivadas deben implementar todos los métodos abstractos de la clase base para ser instanciadas.

"""