# VIDEO - Crear clases

# Para crear una clase en Python, se utiliza la palabra clave "class"
# En este caso, estamos creando una clase llamada "Usuario"
class Usuario():
    pass  # La palabra clave "pass" se utiliza para indicar que la clase está vacía por ahora

# Aquí estamos creando dos instancias de la clase "Usuario"
# La instanciación de una clase se hace al asignar el nombre de la clase a una variable
codi = Usuario()  # Crea un objeto de la clase Usuario llamado "codi"
facilito = Usuario()  # Crea otro objeto de la clase Usuario llamado "facilito"

# Imprimir el tipo del objeto "facilito"
# type() devuelve el tipo de la variable. En este caso, debe mostrar que "facilito" es una instancia de la clase "Usuario"
print(type(facilito))  # Salida esperada: <class '__main__.Usuario'>
