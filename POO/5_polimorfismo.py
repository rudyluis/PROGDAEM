# Definición de la clase Gato
class Gato():
    # Método para devolver el sonido que hace un gato
    def sonido(self):
        return "Miau"

# Definición de la clase Perro
class Perro():
    # Método para devolver el sonido que hace un perro
    def sonido(self):
        return "Guau"

# Función que acepta cualquier tipo de animal y llama a su método sonido
def hacer_sonido(animal):
    print(animal.sonido())  # Llama al método sonido del objeto animal (gato o perro)

# Crear una instancia de Gato
gato = Gato()

# Crear una instancia de Perro
perro = Perro()

# Llamada a la función hacer_sonido, pasando el objeto perro
hacer_sonido(perro)  # Imprime "Guau" porque perro.sonido() devuelve "Guau"

# Llamada al método sonido directamente desde el objeto perro
print(perro.sonido())  # También imprime "Guau" porque el método sonido en Perro devuelve "Guau"


"""
Definición de las clases Gato y Perro:

Ambas clases tienen un método llamado sonido(). El método sonido de la clase Gato devuelve el string "Miau", mientras que el de la clase Perro devuelve "Guau".
Función hacer_sonido():

La función hacer_sonido() recibe un parámetro animal que puede ser cualquier instancia de una clase que tenga el método sonido().
Dentro de la función, se llama a animal.sonido(), lo que invoca el método sonido correspondiente a la clase del objeto que se pasa (ya sea un Gato o un Perro).
Aquí es donde entra el polimorfismo: la función hacer_sonido puede aceptar instancias de diferentes clases (como Gato o Perro) y, según la clase del objeto, se ejecutará el método adecuado.
Creación de instancias:

Se crean dos objetos: gato de la clase Gato y perro de la clase Perro.
Llamada a hacer_sonido(perro):

Cuando se llama a hacer_sonido(perro), el objeto perro es pasado como argumento a la función.
La función invoca el método sonido() de la clase Perro, lo que produce el resultado "Guau".
Llamada directa a perro.sonido():

Cuando se hace print(perro.sonido()), también se ejecuta el método sonido de la clase Perro, que devuelve "Guau".
Polimorfismo:
El polimorfismo se refiere a la capacidad de una función o método de operar con objetos de diferentes tipos, siempre que estos objetos tengan el mismo nombre de método. En este caso, aunque gato y perro son objetos de clases diferentes, ambos tienen un método sonido(), por lo que puedes llamar a hacer_sonido(animal) sin importar si el objeto es un Gato o un Perro. Python manejará el llamado al método de acuerdo con el tipo real del objeto pasado (gracias a la resolución dinámica de métodos).

Resumen:
Polimorfismo en acción: se puede invocar el mismo método (sonido()) en objetos de diferentes clases, y el comportamiento del método depende de la clase del objeto que se pasa.

"""