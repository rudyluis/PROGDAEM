"""
Los getters y setters son métodos que se utilizan para acceder y modificar los atributos de una clase de manera controlada, 
permitiendo encapsular la manipulación de los datos. 
En Python, estos métodos son comúnmente usados para asegurar que se pueda validar la entrada o proporcionar un acceso solo de lectura o escritura.
"""
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    # Getter para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para establecer el nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Getter para obtener la edad
    def get_edad(self):
        return self.__edad

    # Setter para establecer la edad con validación
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")

# Crear un objeto de la clase Persona
persona = Persona("Juan", 30)

# Usar los getters para obtener los atributos
print("Nombre:", persona.get_nombre())  # Obtiene el nombre
print("Edad:", persona.get_edad())      # Obtiene la edad

# Usar los setters para modificar los atributos
persona.set_nombre("Carlos")  # Modifica el nombre
persona.set_edad(35)          # Modifica la edad

# Verificar los cambios
print("Nuevo nombre:", persona.get_nombre())
print("Nueva edad:", persona.get_edad())

# Intentar establecer una edad inválida
persona.set_edad(-5)  # Intento de establecer una edad negativa


"""
Explicación del código:
Atributos privados:

Los atributos __nombre y __edad son privados (comienzan con __), lo que significa que no pueden ser accedidos directamente desde fuera de la clase.
Getters:

El getter para el nombre es el método get_nombre(), que devuelve el valor del atributo privado __nombre.
El getter para la edad es el método get_edad(), que devuelve el valor del atributo privado __edad.
Setters:

El setter para el nombre es el método set_nombre(nuevo_nombre), 
que establece el valor del atributo privado __nombre con el valor proporcionado.
El setter para la edad es el método set_edad(nueva_edad). 
Este setter tiene una validación: solo permite establecer una edad positiva. Si se intenta asignar una edad negativa, el método imprime un mensaje de error y no cambia el valor del atributo.
"""