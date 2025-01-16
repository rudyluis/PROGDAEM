# Lista de productos en el inventario como tuplas (ID, Nombre, Categoría, Precio)
inventario = [
    (101, "Laptop", "Electrónica", 850.99),
    (102, "Teléfono", "Electrónica", 399.99),
    (103, "Impresora", "Oficina", 199.99),
    (104, "Escritorio", "Muebles", 129.99),
    (105, "Silla", "Muebles", 89.99),
    (106, "Cafetera", "Hogar", 49.99),
    (107, "Monitor", "Electrónica", 159.99),
]

# Función para buscar productos por categoría
def buscar_por_categoria(inventario, categoria):
    return [producto for producto in inventario if producto[2] == categoria]

# Función para calcular el valor total del inventario
def valor_total_inventario(inventario):
    return sum(producto[3] for producto in inventario)

# Función para encontrar el producto más caro y el más barato
def producto_extremo(inventario):
    mas_caro = max(inventario, key=lambda producto: producto[3])
    mas_barato = min(inventario, key=lambda producto: producto[3])
    return mas_caro, mas_barato

# Ejemplo de uso:

# Buscar productos en la categoría 'Electrónica'
productos_electronica = buscar_por_categoria(inventario, "Electrónica")
print("Productos en la categoría 'Electrónica':")
for producto in productos_electronica:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[3]:.2f}")

# Calcular el valor total del inventario
total_inventario = valor_total_inventario(inventario)
print(f"\nValor total del inventario: ${total_inventario:.2f}")

# Encontrar el producto más caro y el más barato
mas_caro, mas_barato = producto_extremo(inventario)
print(f"\nProducto más caro: {mas_caro[1]}, Precio: ${mas_caro[3]:.2f}")
print(f"Producto más barato: {mas_barato[1]}, Precio: ${mas_barato[3]:.2f}")
