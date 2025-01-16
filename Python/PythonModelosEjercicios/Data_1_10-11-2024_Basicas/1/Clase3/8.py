# Función para mostrar el menú
def mostrar_menu():
    print("Menú de operaciones con listas:")
    print("1. Añadir un elemento")
    print("2. Eliminar un elemento")
    print("3. Mostrar la lista")
    print("4. Salir")

# Función para manejar las operaciones
def manejar_lista():
    lista = []
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción (1-4): "))
        
        if opcion == 1:
            elemento = input("Introduce el elemento a añadir: ")
            lista.append(elemento)
        elif opcion == 2:
            if lista:
                elemento = input("Introduce el elemento a eliminar: ")
                if elemento in lista:
                    lista.remove(elemento)
                else:
                    print("Elemento no encontrado.")
            else:
                print("La lista está vacía.")
        elif opcion == 3:
            print("Lista actual:", lista)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Llamar a la función
manejar_lista()
