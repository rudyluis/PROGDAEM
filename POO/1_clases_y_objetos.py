# Definición de la clase Celular
class Celular:
    # El método __init__ es el constructor de la clase, se ejecuta al crear una instancia
    def __init__(self, marca, modelo, camara):
        self.marca = marca  # Asigna el valor de 'marca' al atributo 'marca' de la instancia
        self.modelo = modelo  # Asigna el valor de 'modelo' al atributo 'modelo' de la instancia
        self.camara = camara  # Asigna el valor de 'camara' al atributo 'camara' de la instancia

    # Método para realizar una llamada
    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')  # Imprime un mensaje indicando que se está haciendo una llamada con el modelo del celular

    # Método para cortar la llamada
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')  # Imprime un mensaje indicando que se cortó la llamada desde el modelo del celular

    # El método __str__ devuelve una representación en forma de cadena del objeto
    def __str__(self):
        return f'Celular {self.marca} {self.modelo} con cámara de {self.camara}'

# Creación de la primera instancia de la clase Celular
celular1 = Celular("Samsung", "S23", "48MP")  # Se crea un objeto 'celular1' con la marca "Samsung", modelo "S23" y cámara de "48MP"

# Creación de la segunda instancia de la clase Celular
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")  # Se crea un objeto 'celular2' con la marca "Apple", modelo "Iphone 15 Pro" y cámara de "96MP"

# Llamar al método 'llamar' del objeto 'celular2'
celular2.llamar()  # Este código llama el método 'llamar' para el objeto 'celular2' (Apple Iphone 15 Pro)

# Imprimir la representación en cadena del objeto celular2
print(str(celular2))  # Ahora imprimirá correctamente la información del celular

print(celular2.__dict__)