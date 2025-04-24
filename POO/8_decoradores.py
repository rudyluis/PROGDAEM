# Decorador para contar las veces que se llama a un método
def contar_llamadas(func):
    def wrapper(self, *args, **kwargs):
        self._contador_llamadas += 1  # Incrementamos el contador de la instancia
        print(f"El método {func.__name__} ha sido llamado {self._contador_llamadas} veces")
        return func(self, *args, **kwargs)
    return wrapper

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._contador_llamadas = 0  # Inicializamos el contador de llamadas por instancia
    
    @contar_llamadas  # Aplicamos el decorador al método
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando...")

    @contar_llamadas  # Aplicamos el decorador a otro método
    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando...")

# Creamos un objeto de la clase Coche
mi_coche = Coche("Ford", "Mustang")

# Llamamos a los métodos decorados
mi_coche.arrancar()  # Primera vez
mi_coche.arrancar()  # Segunda vez
mi_coche.frenar()    # Primera vez
mi_coche.frenar()    # Segunda vez
mi_coche.frenar()    # Tercera vez

# Creamos otro objeto de la clase Coche
mi_coche2 = Coche("Chevrolet", "Camaro")

# Llamamos a los métodos del nuevo objeto
mi_coche2.arrancar()  # Primera vez
mi_coche2.frenar()    # Primera vez


"""
Los decoradores en programación orientada a objetos (POO) en Python sirven para modificar o extender el comportamiento de métodos o propiedades en clases sin modificar directamente su código. Se usan principalmente para:

Encapsular lógica adicional sin alterar el código original del método o propiedad.

Implementar patrones de diseño como el Singleton o el acceso controlado.

Aplicar validaciones o restricciones de acceso a métodos de clases.

Añadir funcionalidad como logging, caching o autenticación.
"""