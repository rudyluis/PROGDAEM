class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}')


roberto = EmpleadoArtista("Roberto", 43, "argentino", "Cantar","Google", 100000)

roberto.presentarse()

herencia = issubclass(EmpleadoArtista, Persona)
instancia = isinstance(roberto, Artista)

print(instancia)