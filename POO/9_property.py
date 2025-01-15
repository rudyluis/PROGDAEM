class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # Esto define un método nombre como una propiedad utilizando el decorador @property. 
    # Esto significa que puedes acceder al nombre de la persona como si fuera un atributo.
    @property
    def nombre(self):
        return self.__nombre
    
    # Aquí defines un método setter para la propiedad nombre. 
    # Esto te permite modificar el nombre de la persona utilizando la sintaxis de asignación, como dalto.nombre = "Pepe".
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    # Este es el método deleter para la propiedad nombre. 
    # Te permite eliminar el nombre de la persona utilizando la palabra clave del
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
dalto = Persona("Lucas", 21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe"

nombre = dalto.nombre
print(nombre)

del dalto.nombre

print("¡Qué haces!")

