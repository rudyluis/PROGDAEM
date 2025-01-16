# Diccionario para almacenar las ventas
ventas = {}

# Función para agregar una venta
def agregar_venta():
    id_venta = input("Ingrese el ID de la venta: ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio_unitario = float(input("Ingrese el precio unitario: "))
    total = cantidad * precio_unitario

    # Guardamos la venta en el diccionario
    ventas[id_venta] = {
        "producto": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    }
    print("\nVenta agregada exitosamente.")

# Función para mostrar todas las ventas
def mostrar_ventas():
    if not ventas:
        print("\nNo hay ventas registradas.")
        return
    
    print("\n--- Registro de Ventas ---")
    for id_venta, detalles in ventas.items():
        print(f"ID: {id_venta} | Producto: {detalles['producto']} | Cantidad: {detalles['cantidad']} | Precio Unitario: {detalles['precio_unitario']} | Total: {detalles['total']}")

# Función para editar una venta
def editar_venta():
    id_venta = input("\nIngrese el ID de la venta que desea editar: ")
    
    if id_venta in ventas:
        producto = input("Ingrese el nuevo nombre del producto: ")
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio_unitario = float(input("Ingrese el nuevo precio unitario: "))
        total = cantidad * precio_unitario

        # Actualizamos la venta en el diccionario
        ventas[id_venta] = {
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "total": total
        }
        print("\nVenta actualizada exitosamente.")
    else:
        print("\nVenta no encontrada.")

# Función para eliminar una venta
def eliminar_venta():
    id_venta = input("\nIngrese el ID de la venta que desea eliminar: ")
    
    if id_venta in ventas:
        del ventas[id_venta]
        print("\nVenta eliminada exitosamente.")
    else:
        print("\nVenta no encontrada.")

# Función principal del programa
def menu():
    while True:
        print("\n--- Menú de Registro de Ventas ---")
        print("1. Agregar venta")
        print("2. Mostrar ventas")
        print("3. Editar venta")
        print("4. Eliminar venta")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            editar_venta()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida, intente de nuevo.")

# Ejecutar el programa
if __name__=="__main__":
    menu()
