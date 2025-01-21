"""
El decorador @property en Python se usa para convertir un método en una propiedad. 
Esto permite que un método se comporte como un atributo, es decir, 
puedes acceder a él sin necesidad de llamar al método de manera explícita (sin paréntesis). 
Es una forma de hacer que el acceso a los atributos sea más limpio, sin perder la posibilidad de incluir lógica adicional cuando sea necesario (por ejemplo, validación).

¿Cómo funciona @property?
Cuando usas @property, creas un método que se comporta como un atributo. 
Este método será llamado cuando accedas a la propiedad, pero desde el exterior del código parece ser simplemente un atributo.

Además, puedes definir un getter (para obtener el valor) 
y un setter (para modificar el valor) para gestionar cómo se acceden y modifican esos atributos.
"""


class Persona:
    # Método constructor (__init__) para inicializar los atributos
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado para almacenar el nombre
        self.__edad = edad      # Atributo privado para almacenar la edad

    # Decorador @property convierte este método en una propiedad
    @property
    def nombre(self):
        return self.__nombre  # Retorna el valor del atributo privado __nombre

    # Decorador @nombre.setter permite modificar el valor de la propiedad nombre
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre  # Asigna el nuevo valor a __nombre

    # Decorador @nombre.deleter permite eliminar la propiedad nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre  # Elimina el atributo privado __nombre

# Crear una instancia de la clase Persona
dalto = Persona("Lucas", 21)  # Inicializa el objeto con nombre 'Lucas' y edad 21

# Obtener el nombre usando el getter (método nombre) de la propiedad
nombre = dalto.nombre  
print(nombre)  # Imprime 'Lucas', que es el valor inicial de la propiedad nombre

# Cambiar el nombre usando el setter (modifica el valor de la propiedad)
dalto.nombre = "Pepe"  # Modifica el nombre a 'Pepe' usando la sintaxis de asignación

# Obtener el nuevo nombre usando el getter nuevamente
nombre = dalto.nombre  
print(nombre)  # Imprime 'Pepe', que es el nuevo valor de la propiedad nombre

# Eliminar el atributo privado __nombre usando el deleter
del dalto.nombre  # Elimina la propiedad nombre

# Imprime un mensaje al final, como señal de que el código ha finalizado
print("¡Qué haces!")
