class libro:
    def __init__(self, titulo, autor, genero, precio, stock):
        self._titulo=titulo
        self._autor=autor
        self._genero=genero
        self._precio=precio
        self._stock=stock

    def obtener_precio(self):
        return self._precio
    
    def restar_stock(self, cantidad):
        self._stock-=cantidad

    def obtener_info(self):
        print('Titulo:',self._titulo)
        print('Autor:',self._autor)
        print('Precio:',self._precio)
        print('Stock:',self._stock)

class cliente:
    def __init__(self, nombre, email):
        self._nombre=nombre
        self._email=email
    def mostrar_info(self):
        print('Nombre:', self._nombre)
        print('email:', self._email)

class transaccion:
    def __init__(self, cliente, libro, cantidad):
        self._cliente =cliente
        self._libro= libro
        self._cantidad=cantidad

    def procesar_transaccion(self):
        if(self._libro._stock>=self._cantidad):
            self._libro.restar_stock(self._cantidad)
            precio_total= self._cantidad* self._libro.obtener_precio()
            print('Total a pagar-->', precio_total)
            print('Transaccion completada, Gracias por su compra!!!!')
        else:
            print('No hay suficiente stock disponible!!!!') 


if __name__=="__main__":
    libro1= libro('El principito','Alguien','Infantil',100, 10)
    libro1.obtener_info()
    libro1.obtener_precio()

    cliente1 = cliente('Marco','marco@abc.com')
    cliente1.mostrar_info()


    transaccion1= transaccion(cliente1, libro1,5)
    transaccion1.procesar_transaccion()

    transaccion2= transaccion(cliente1, libro1,9)
    transaccion2.procesar_transaccion()