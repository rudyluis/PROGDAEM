# Clase Gato, que no explícitamente hereda de ninguna clase pero por defecto hereda de 'object'
class Gato():
    # El método __init__ es el constructor que se ejecuta cuando se crea una instancia de la clase
    def __init__(self, nombre):
        self.nombre = nombre  # Asigna el nombre del gato a un atributo 'nombre' de la instancia

    # El método __str__ devuelve una representación en forma de cadena del objeto
    def __str__(self):
        return self.nombre  # Devuelve el nombre del gato como cadena

# Clase Pato, explícitamente heredando de 'object', aunque no es necesario en Python 3, ya que hereda de 'object' por defecto
class Pato(object):
    # Constructor que inicializa el atributo 'nombre' de la instancia del pato
    def __init__(self, nombre):
        self.nombre = nombre  # Asigna el nombre del pato a un atributo 'nombre'

# Crear una instancia de la clase Gato, con el nombre 'Bigotes'
gato = Gato("Bigotes")

# Crear una instancia de la clase Pato, con el nombre 'Lucas'
pato = Pato("Lucas")

# Imprimir el diccionario de atributos del objeto 'gato'
# __dict__ devuelve un diccionario con los atributos del objeto
print(gato.__dict__)  # Salida: {'nombre': 'Bigotes'}

# Imprimir el diccionario de atributos del objeto 'pato'
print(pato.__dict__)  # Salida: {'nombre': 'Lucas'}
