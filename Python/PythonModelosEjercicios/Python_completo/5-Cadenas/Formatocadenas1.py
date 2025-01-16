lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

separador = "; "

# Separar nuestro string por ;
resultado = lenguajes.split(";")
print(resultado)

# Crear lista a string
nuevo_string = separador.join(resultado)
print(nuevo_string)