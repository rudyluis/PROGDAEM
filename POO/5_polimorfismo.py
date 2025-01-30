# Definición de la clase Coche
class Coche():
    # Método para devolver el sonido que hace un coche
    def sonido(self):
        return "Vroom"

# Definición de la clase Moto
class Moto():
    # Método para devolver el sonido que hace una moto
    def sonido(self):
        return "Brrrm"

# Función que acepta cualquier tipo de vehículo y llama a su método sonido
def hacer_sonido(vehiculo):
    print(vehiculo.sonido())  # Llama al método sonido del objeto vehiculo (coche o moto)

# Crear una instancia de Coche
coche = Coche()

# Crear una instancia de Moto
moto = Moto()

# Llamada a la función hacer_sonido, pasando el objeto moto
hacer_sonido(moto)  # Imprime "Brrrm" porque moto.sonido() devuelve "Brrrm"

# Llamada al método sonido directamente desde el objeto coche
print(coche.sonido())  # Imprime "Vroom" porque el método sonido en Coche devuelve "Vroom"



"""
Definición de las Clases Coche y Moto
En este código, se definen dos clases: Coche y Moto.

Ambas clases tienen un método llamado sonido(), pero con implementaciones distintas:
Coche.sonido() devuelve "Vroom", representando el sonido de un coche.
Moto.sonido() devuelve "Brrrm", representando el sonido de una moto.
Función hacer_sonido()
Esta función recibe un objeto vehiculo, que puede ser cualquier instancia de una clase que tenga el método sonido().

Dentro de la función, se llama a vehiculo.sonido(), lo que ejecuta el método correspondiente según la clase del objeto pasado como argumento.
Aquí es donde entra el polimorfismo: la función hacer_sonido() puede trabajar con diferentes clases (como Coche o Moto), siempre que estas implementen un método sonido().
Creación de Instancias y Ejecución
Se crean dos objetos: coche de la clase Coche y moto de la clase Moto.
Cuando llamamos hacer_sonido(moto), el método sonido() de la clase Moto se ejecuta y devuelve "Brrrm".
De manera similar, si ejecutamos print(coche.sonido()), imprimirá "Vroom".
Polimorfismo en Acción
El polimorfismo permite que una misma función (hacer_sonido()) pueda operar con objetos de distintas clases, siempre que implementen el método sonido().

Aunque coche y moto pertenecen a clases diferentes, ambas clases tienen un método sonido(), por lo que la función puede trabajar con ambos sin necesidad de verificar su tipo.
Python resuelve dinámicamente cuál método ejecutar según la clase del objeto recibido.
Resumen
✔ Polimorfismo: Permite que un mismo método (sonido()) tenga diferentes implementaciones según la clase del objeto.
✔ Flexibilidad: La función hacer_sonido() puede aceptar distintos tipos de objetos sin modificar su código.
✔ Reutilización: Se pueden agregar nuevas clases con un método sonido() sin necesidad de modificar hacer_sonido(), lo que hace el código más escalable.


"""