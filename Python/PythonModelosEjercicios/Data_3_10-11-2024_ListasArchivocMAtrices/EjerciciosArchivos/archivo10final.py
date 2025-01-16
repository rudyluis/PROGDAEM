import os

# Archivo donde se almacenarán los contactos
ARCHIVO_CONTACTOS = "contactos.txt"

def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n--- Menú de Gestión de Contactos ---")
    print("1. Añadir un contacto")
    print("2. Visualizar contactos")
    print("3. Eliminar un contacto")
    print("4. Salir")
    return input("Elige una opción: ")

def añadir_contacto():
    """Permite añadir un nuevo contacto al archivo."""
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()

    # Validar que los campos no estén vacíos
    if not nombre or not telefono or not correo:
        print("Todos los campos son obligatorios.")
        return

    # Guardar contacto en el archivo
    with open(ARCHIVO_CONTACTOS, "a") as archivo:
        archivo.write(f"{nombre},{telefono},{correo}\n")
    print("Contacto añadido exitosamente.")

def visualizar_contactos():
    """Muestra todos los contactos almacenados."""
    if not os.path.exists(ARCHIVO_CONTACTOS):
        print("No hay contactos guardados.")
        return

    print("\n--- Lista de Contactos ---")
    with open(ARCHIVO_CONTACTOS, "r") as archivo:
        contactos = archivo.readlines()
        if not contactos:
            print("No hay contactos guardados.")
            return
        
        for i, contacto in enumerate(contactos, start=1):
            nombre, telefono, correo = contacto.strip().split(",")
            print(f"{i}. Nombre: {nombre}, Teléfono: {telefono}, Correo: {correo}")

def eliminar_contacto():
    """Elimina un contacto por su nombre."""
    if not os.path.exists(ARCHIVO_CONTACTOS):
        print("No hay contactos guardados.")
        return

    nombre_a_eliminar = input("Introduce el nombre del contacto a eliminar: ").strip()

    with open(ARCHIVO_CONTACTOS, "r") as archivo:
        contactos = archivo.readlines()

    # Filtrar contactos que no coincidan con el nombre a eliminar
    contactos_actualizados = [contacto for contacto in contactos if not contacto.startswith(nombre_a_eliminar + ",")]

    if len(contactos_actualizados) == len(contactos):
        print("No se encontró un contacto con ese nombre.")
    else:
        with open(ARCHIVO_CONTACTOS, "w") as archivo:
            archivo.writelines(contactos_actualizados)
        print("Contacto eliminado exitosamente.")

# Programa principal
while True:
    opcion = mostrar_menu()

    if opcion == "1":
        añadir_contacto()
    elif opcion == "2":
        visualizar_contactos()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        print("Gracias por usar el sistema de gestión de contactos. ¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
