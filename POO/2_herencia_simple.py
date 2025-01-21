# Definición de la clase Persona, que tiene atributos básicos y un método de hablar
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        # El constructor inicializa los atributos 'nombre', 'edad' y 'nacionalidad' de la persona
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        # El método hablar imprime un mensaje indicando que la persona está hablando
        print("Hola, estoy hablando un poco")

# Definición de la clase Empleado, que hereda de la clase Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # Se llama al constructor de la clase base (Persona) usando 'super()'
        super().__init__(nombre, edad, nacionalidad)
        # La clase Empleado tiene atributos adicionales 'trabajo' y 'salario'
        self.trabajo = trabajo
        self.salario = salario

# Definición de la clase Estudiante, que también hereda de la clase Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        # Se llama al constructor de la clase base (Persona) usando 'super()'
        super().__init__(nombre, edad, nacionalidad)
        # La clase Estudiante tiene atributos adicionales 'notas' y 'universidad'
        self.notas = notas
        self.universidad = universidad

# Creación de una instancia de la clase Empleado con nombre 'Roberto', edad 43, nacionalidad 'argentino', trabajo 'Programador' y salario 100000
roberto = Empleado("Roberto", 43, "argentino", "Programador", 100000)

# Llamada al método 'hablar' del objeto 'roberto'
# Como la clase Empleado hereda de Persona, el método 'hablar' también está disponible para 'roberto'
roberto.hablar()  # Salida esperada: "Hola, estoy hablando un poco"


"""
Explicación de cada parte:
Clase Persona:

Tiene tres atributos: nombre, edad, y nacionalidad, los cuales son inicializados en el constructor __init__.
Tiene un método hablar() que imprime un mensaje.
Clase Empleado (hereda de Persona):

Usa super().__init__(nombre, edad, nacionalidad) para llamar al constructor de la clase base (Persona) y así inicializar los atributos heredados (nombre, edad, nacionalidad).
Agrega dos atributos adicionales: trabajo y salario, que son específicos de la clase Empleado.
Clase Estudiante (hereda de Persona):

Similar a la clase Empleado, usa super().__init__(nombre, edad, nacionalidad) para inicializar los atributos heredados.
Añade los atributos específicos notas y universidad.
Instancia de Empleado:

Se crea un objeto llamado roberto de la clase Empleado, con los atributos nombre, edad, nacionalidad, trabajo y salario proporcionados en el constructor.
Llamada al método hablar:

Aunque roberto es un objeto de la clase Empleado, esta clase hereda de Persona, por lo que el método hablar() definido en Persona está disponible en roberto.
Al ejecutar roberto.hablar(), se imprime el mensaje: Hola, estoy hablando un poco.
"""


"""
Conceptos clave:
Herencia: Las clases Empleado y Estudiante heredan de Persona, 
lo que les permite usar el constructor y los métodos de Persona.
Uso de super(): super() se usa para llamar al constructor de la clase base (Persona) 
desde las clases derivadas (Empleado y Estudiante), evitando duplicar el código de inicialización.
Polimorfismo: El método hablar() es heredado por Empleado, 
lo que permite que objetos de la clase Empleado y otras clases que hereden de Persona puedan usar este método.


"""