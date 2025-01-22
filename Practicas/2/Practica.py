from abc import ABC, abstractmethod
from datetime import datetime


# Clase abstracta: Usuario
class Usuario(ABC):
    def __init__(self, nombre, email):
        self._nombre = nombre  # Encapsulamiento (nombre protegido)
        self._email = email

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Subclase Cliente
class Cliente(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.historial_compras = []

    def agregar_a_historial(self, compra):
        self.historial_compras.append(compra)

    def mostrar_informacion(self):
        print(f"Cliente: {self.nombre} - Email: {self.email}")
        print("Historial de Compras:")
        for compra in self.historial_compras:
            print(f"- {compra}")


# Subclase Administrador
class Administrador(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)

    def mostrar_informacion(self):
        print(f"Administrador: {self.nombre} - Email: {self.email}")


# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre  # Encapsulamiento
        self._precio = precio
        self._stock = stock

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = nuevo_stock

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Stock: {self.stock}"


# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.usuarios = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en la tienda.")
        else:
            for producto in self.productos:
                print(producto)

    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        return None

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_compra(self, cliente, nombre_producto, cantidad):
        producto = self.buscar_producto(nombre_producto)
        if producto is None:
            print(f"El producto '{nombre_producto}' no existe en la tienda.")
            return
        if producto.stock < cantidad:
            print(f"Stock insuficiente para el producto '{nombre_producto}'. Disponible: {producto.stock}")
            return
        # Realizar la compra
        total = producto.precio * cantidad
        producto.stock -= cantidad
        cliente.agregar_a_historial(f"{nombre_producto} (x{cantidad}) - Total: ${total:.2f}")
        print(f"Compra realizada con éxito: {nombre_producto} (x{cantidad}) - Total: ${total:.2f}")


# Decorador: registro de acciones
def registrar_actividad(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Acción ejecutada: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# Extendiendo funcionalidades con decoradores
class TiendaConRegistro(Tienda):
    @registrar_actividad
    def agregar_producto(self, producto):
        super().agregar_producto(producto)

    @registrar_actividad
    def realizar_compra(self, cliente, nombre_producto, cantidad):
        super().realizar_compra(cliente, nombre_producto, cantidad)


# --- Simulación ---
# Crear usuarios
cliente1 = Cliente("Ana", "ana@gmail.com")
admin = Administrador("Carlos", "admin@tienda.com")

# Crear productos
producto1 = Producto("Laptop", 800, 10)
producto2 = Producto("Smartphone", 500, 20)
producto3 = Producto("Teclado", 50, 50)

# Crear tienda
tienda = TiendaConRegistro("Tech Store")

# Registrar usuarios y agregar productos
tienda.registrar_usuario(cliente1)
tienda.registrar_usuario(admin)
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Menú de simulación
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Mostrar productos")
    print("2. Realizar compra")
    print("3. Mostrar información de cliente")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Productos Disponibles ---")
        tienda.mostrar_productos()

    elif opcion == "2":
        print("\n--- Realizar Compra ---")
        nombre_producto = input("Ingrese el nombre del producto: ")
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            tienda.realizar_compra(cliente1, nombre_producto, cantidad)
        except ValueError:
            print("La cantidad debe ser un número entero.")

    elif opcion == "3":
        print("\n--- Información de Cliente ---")
        cliente1.mostrar_informacion()

    elif opcion == "4":
        print("¡Gracias por usar la tienda en línea!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
