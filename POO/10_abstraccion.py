"""
Una clase abstracta es una clase en la programación orientada a objetos que no se puede instanciar 
directamente, es decir, no puedes crear objetos de esa clase. Su principal propósito es servir como una base para otras clases. 
Las clases abstractas permiten definir una interfaz común para un grupo de clases relacionadas, 
pero delegan los detalles de la implementación a las clases derivadas.

Características principales de una clase abstracta:
No se puede instanciar: No puedes crear un objeto de una clase abstracta. 
En su lugar, se utiliza como base para otras clases que implementan sus métodos abstractos.

Métodos abstractos: Los métodos abstractos son aquellos que se definen en la clase abstracta 
pero no tienen una implementación. Las clases derivadas deben implementar estos métodos. En Python, se definen con el decorador @abstractmethod del módulo abc.

Puede tener métodos concretos: Aunque los métodos abstractos no tienen implementación, 
una clase abstracta puede tener métodos que sí tienen una implementación completa. Estos métodos pueden ser heredados directamente por las clases derivadas.

Propósito: Una clase abstracta proporciona una estructura base común para otras clases. 
Define un contrato que las clases derivadas deben seguir, asegurando que ciertos métodos estén presentes y sean implementados.

"""


"""

La librería abc en Python significa "Abstract Base Classes" (Clases Base Abstractas) 
y proporciona herramientas para definir clases abstractas y métodos abstractos.
Una clase abstracta es una clase que sirve como base para otras clases y que no se puede instanciar directamente.
"""


from abc import ABC, abstractmethod

# Clase base abstracta para los métodos de pago
class MetodoPago(ABC):

    @abstractmethod
    def procesar_pago(self, monto):
        """Cada método de pago implementará su propia lógica de procesamiento."""
        pass

    @abstractmethod
    def verificar_saldo(self):
        """Cada método de pago tendrá su propia forma de verificar saldo."""
        pass

# Clase derivada 1: Pago con Tarjeta de Crédito
class TarjetaCredito(MetodoPago):

    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def verificar_saldo(self):
        print(f"💳 Verificando saldo disponible en la tarjeta {self.numero}...")

    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"✅ Pago de ${monto} realizado con tarjeta {self.numero}. Nuevo saldo: ${self.saldo}")
        else:
            print("❌ Saldo insuficiente en la tarjeta.")

# Clase derivada 2: Pago con PayPal
class PayPal(MetodoPago):

    def __init__(self, email, saldo):
        self.email = email
        self.saldo = saldo

    def verificar_saldo(self):
        print(f"📧 Verificando saldo de la cuenta PayPal: {self.email}...")

    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"✅ Pago de ${monto} realizado con PayPal ({self.email}). Nuevo saldo: ${self.saldo}")
        else:
            print("❌ Fondos insuficientes en PayPal.")

# Clase derivada 3: Pago con Criptomonedas
class Criptomoneda(MetodoPago):

    def __init__(self, wallet_id, saldo):
        self.wallet_id = wallet_id
        self.saldo = saldo

    def verificar_saldo(self):
        print(f"🪙 Verificando saldo en la billetera cripto {self.wallet_id}...")

    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"✅ Pago de ${monto} realizado con criptomonedas ({self.wallet_id}). Nuevo saldo: ${self.saldo}")
        else:
            print("❌ Saldo insuficiente en la billetera de criptomonedas.")

# Lista con diferentes métodos de pago
metodos_pago = [
    TarjetaCredito("1234-5678-9876-5432", 1000),
    PayPal("usuario@email.com", 500),
    Criptomoneda("0xABC123DEF456", 300)
]

# Procesar pagos con diferentes métodos (polimorfismo)
for metodo in metodos_pago:
    print("\n--- Nuevo Pago ---")
    metodo.verificar_saldo()
    metodo.procesar_pago(250)  # Intentar pagar $250 con cada método

"""


Clase base abstracta MetodoPago:
La clase MetodoPago es abstracta porque hereda de ABC (Abstract Base Class), 
lo que significa que no puede ser instanciada directamente.
Define dos métodos abstractos: verificar_saldo y procesar_pago, 
los cuales no tienen implementación en la clase base, pero deben ser implementados por cualquier clase 
que herede de MetodoPago.
Clases derivadas: TarjetaCredito, PayPal, Criptomoneda:
Las clases TarjetaCredito, PayPal y Criptomoneda heredan de MetodoPago y 
proporcionan implementaciones concretas para los métodos abstractos verificar_saldo y procesar_pago.
Polimorfismo en acción: A pesar de que cada clase tiene su propia implementación de estos métodos, 
todas comparten la misma interfaz definida en la clase base (MetodoPago), lo que permite utilizarlas 
de manera intercambiable en el código principal.
Abstracción:
La clase MetodoPago es un ejemplo de abstracción. Oculta los detalles de cómo cada tipo de pago
 (tarjeta de crédito, PayPal, criptomonedas) maneja la verificación de saldo y el procesamiento de pagos, pero asegura que todos los métodos de pago tienen la misma estructura básica.
Cada clase derivada implementa la lógica interna del método según el tipo de pago específico, pero los usuarios solo interactúan con los métodos públicos verificar_saldo y procesar_pago, sin necesidad de conocer los detalles de la implementaci




"""