"""
El encapsulamiento es uno de los pilares fundamentales de la programación orientada a objetos (POO) 
y hace referencia al principio de ocultar los detalles internos de una clase 
y exponer solo lo necesario a través de métodos públicos. 
Esto ayuda a proteger el estado interno de un objeto, 
garantizando que solo se pueda acceder o modificar mediante métodos controlados.

"""
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (no se puede acceder directamente fuera de la clase)

    # Método público para obtener el saldo
    def obtener_saldo(self):
        return self.__saldo

    # Método público para realizar un depósito
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito realizado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    # Método público para realizar un retiro
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro realizado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("No hay suficiente saldo o la cantidad es inválida.")

# Crear una cuenta bancaria
cuenta = CuentaBancaria("Juan Pérez", 1000)

# Consultar saldo a través del método público
print(f"Saldo actual: {cuenta.obtener_saldo()}")

# Intentar acceder directamente al saldo (esto dará error porque es un atributo privado)
# print(cuenta.__saldo)  # Esto generaría un AttributeError

# Realizar depósitos y retiros
cuenta.depositar(500)
cuenta.retirar(300)

# Consultar saldo después de las operaciones
print(f"Saldo final: {cuenta.obtener_saldo()}")



"""
Explicación del código:
Atributo privado:

El atributo __saldo es privado, lo que significa que no puede ser accedido directamente fuera de la clase.
Si intentamos acceder a cuenta.__saldo desde fuera de la clase, 
Python lanzará un error AttributeError.
Métodos públicos:

obtener_saldo(): Es un método público que permite obtener el saldo actual de la cuenta. 
Proporciona acceso al atributo privado de manera controlada.
depositar(cantidad): Es un método público que permite realizar un depósito en la cuenta. 
Se asegura de que solo se pueda depositar una cantidad positiva.
retirar(cantidad): Es un método público que permite retirar dinero de la cuenta, 
pero solo si la cantidad es positiva y no excede el saldo disponible.
Beneficios del encapsulamiento:

Protección: Evita que el saldo de la cuenta sea modificado directamente desde fuera de la clase, 
lo que previene errores y asegura que las operaciones se realicen correctamente.
Control: A través de los métodos públicos, se puede validar si las operaciones (depósitos y retiros) son válidas y seguras, como evitar retiros por encima del saldo disponible.
Abstracción: El usuario de la clase no necesita conocer los detalles internos de cómo se maneja el saldo, solo necesita interactuar con los métodos que proporcionan la funcionalidad necesaria.
"""