# Crear un diccionario vacío
productos = {}

# 1. Añadir productos al diccionario (entrada por teclado)
n_productos = int(input("¿Cuántos productos deseas agregar? "))

for _ in range(n_productos):
    producto = input("Ingrese el nombre del producto: ").capitalize()  # Capitaliza para evitar errores con mayúsculas/minúsculas
    precio = float(input(f"Ingrese el precio de {producto}: "))
    productos[producto] = precio  # Añadir el producto y su precio al diccionario

# 2. Función para obtener el precio de un producto
def obtener_precio(producto):
    # Buscar si el producto existe en el diccionario
    if producto in productos:
        return productos[producto]
    else:
        return "Producto no encontrado"

# 3. Pedir al usuario que ingrese un producto y mostrar su precio
producto_buscado = input("Ingrese el nombre del producto que desea consultar: ").capitalize()

# Llamamos a la función y mostramos el resultado
precio = obtener_precio(producto_buscado)
print(f"El precio de {producto_buscado} es: {precio}")
