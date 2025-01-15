class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor"
    
    def __hablar(self):
        print("hola, como estas?")

objeto = MiClase()
print(objeto.__hablar())



