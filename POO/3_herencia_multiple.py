# Clase base Persona
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        # Inicializa los atributos nombre, edad y nacionalidad
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        # Método que imprime un mensaje simple
        print("Hola, estoy hablando un poco")

# Clase base Artista
class Artista:
    def __init__(self, habilidad):
        # Inicializa el atributo habilidad
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        # Método que devuelve un mensaje con la habilidad
        return f'Mi habilidad es: {self.habilidad}'

# Clase derivada que hereda de Persona y Artista
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        # Llama al constructor de Persona
        Persona.__init__(self, nombre, edad, nacionalidad)
        # Llama al constructor de Artista
        Artista.__init__(self, habilidad)
        # Inicializa los atributos específicos de EmpleadoArtista
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        # Método que combina atributos y métodos de ambas clases base
        print(f'Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}')

# Creación de una instancia de la clase EmpleadoArtista
roberto = EmpleadoArtista("Roberto", 43, "argentino", "Cantar", "Google", 100000)

# Llamada al método presentarse del objeto roberto
roberto.presentarse()

# Verifica si EmpleadoArtista es una subclase de Persona
herencia = issubclass(EmpleadoArtista, Persona)

# Verifica si el objeto roberto es una instancia de la clase Artista
instancia = isinstance(roberto, Artista)

# Imprime el resultado de la verificación
print(instancia)


""""
Conceptos clave:
Herencia múltiple: La clase EmpleadoArtista combina características de las clases Persona y Artista.
Métodos de clase base: Los métodos heredados se utilizan y complementan en la clase derivada.
Verificación de herencia e instancias: issubclass() y isinstance() permiten confirmar relaciones entre clases y objetos.
"""


"""



Explicación detallada:
Clase Persona:

Tiene un constructor que inicializa los atributos básicos (nombre, edad, nacionalidad).
Define un método hablar() que imprime un mensaje.
Clase Artista:

Tiene un atributo específico habilidad.
Define un método mostrar_habilidad() que devuelve un mensaje con la habilidad.
Clase EmpleadoArtista:

Hereda de las clases Persona y Artista.
Su constructor inicializa los atributos heredados usando Persona.__init__ y Artista.__init__.
Añade atributos propios: empresa y salario.
El método presentarse() combina los atributos y métodos de ambas clases base.
Creación del objeto roberto:

Se crea una instancia de EmpleadoArtista con atributos heredados (nombre, edad, nacionalidad, habilidad) y propios (empresa, salario).
Llamada a presentarse():

Este método usa super().mostrar_habilidad() para llamar al método mostrar_habilidad() de Artista.
Combina la información en una presentación que incluye el nombre, la habilidad y la empresa.
Uso de issubclass() y isinstance():

issubclass(EmpleadoArtista, Persona) devuelve True porque EmpleadoArtista hereda de Persona.
isinstance(roberto, Artista) devuelve True porque roberto es una instancia de EmpleadoArtista, que hereda de Artista.

"""