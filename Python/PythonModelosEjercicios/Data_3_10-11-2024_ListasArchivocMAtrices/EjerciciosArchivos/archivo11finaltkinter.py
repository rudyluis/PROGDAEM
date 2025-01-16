import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Archivo donde se almacenarán los contactos
ARCHIVO_CONTACTOS = "contactos.txt"

# Funciones principales
def añadir_contacto():
    """Añade un nuevo contacto."""
    nombre = simpledialog.askstring("Añadir Contacto", "Introduce el nombre:")
    if not nombre:
        messagebox.showwarning("Aviso", "El nombre no puede estar vacío.")
        return
    
    telefono = simpledialog.askstring("Añadir Contacto", "Introduce el teléfono:")
    if not telefono:
        messagebox.showwarning("Aviso", "El teléfono no puede estar vacío.")
        return
    
    correo = simpledialog.askstring("Añadir Contacto", "Introduce el correo:")
    if not correo:
        messagebox.showwarning("Aviso", "El correo no puede estar vacío.")
        return

    # Guardar contacto en el archivo
    with open(ARCHIVO_CONTACTOS, "a") as archivo:
        archivo.write(f"{nombre},{telefono},{correo}\n")
    messagebox.showinfo("Éxito", "Contacto añadido correctamente.")
    actualizar_lista()

def visualizar_contactos():
    """Muestra todos los contactos en la lista."""
    lista_contactos.delete(0, tk.END)  # Limpiar la lista
    if not os.path.exists(ARCHIVO_CONTACTOS):
        messagebox.showinfo("Información", "No hay contactos guardados.")
        return
    
    with open(ARCHIVO_CONTACTOS, "r") as archivo:
        contactos = archivo.readlines()
        if not contactos:
            messagebox.showinfo("Información", "No hay contactos guardados.")
            return
        
        for contacto in contactos:
            nombre, telefono, correo = contacto.strip().split(",")
            lista_contactos.insert(tk.END, f"Nombre: {nombre} | Teléfono: {telefono} | Correo: {correo}")

def eliminar_contacto():
    """Elimina un contacto seleccionado."""
    seleccionado = lista_contactos.curselection()
    if not seleccionado:
        messagebox.showwarning("Aviso", "Debes seleccionar un contacto para eliminar.")
        return

    # Obtener el índice del contacto seleccionado
    indice = seleccionado[0]
    contacto_a_eliminar = lista_contactos.get(indice).split(" | ")[0].split(": ")[1]

    with open(ARCHIVO_CONTACTOS, "r") as archivo:
        contactos = archivo.readlines()

    # Filtrar contactos que no coincidan con el seleccionado
    contactos_actualizados = [contacto for contacto in contactos if not contacto.startswith(contacto_a_eliminar + ",")]

    with open(ARCHIVO_CONTACTOS, "w") as archivo:
        archivo.writelines(contactos_actualizados)
    messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")
    actualizar_lista()

def actualizar_lista():
    """Actualiza la lista de contactos en la interfaz."""
    visualizar_contactos()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Contactos")
ventana.geometry("600x400")

# Etiqueta de título
titulo = tk.Label(ventana, text="Sistema de Gestión de Contactos", font=("Arial", 16))
titulo.pack(pady=10)

# Lista de contactos
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_contactos = tk.Listbox(frame_lista, width=80, height=15, yscrollcommand=scrollbar.set)
lista_contactos.pack(side=tk.LEFT)
scrollbar.config(command=lista_contactos.yview)

# Botones de acción
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_añadir = tk.Button(frame_botones, text="Añadir Contacto", command=añadir_contacto, width=20)
boton_añadir.grid(row=0, column=0, padx=5)

boton_visualizar = tk.Button(frame_botones, text="Visualizar Contactos", command=visualizar_contactos, width=20)
boton_visualizar.grid(row=0, column=1, padx=5)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Contacto", command=eliminar_contacto, width=20)
boton_eliminar.grid(row=0, column=2, padx=5)

# Ejecutar la aplicación
actualizar_lista()
ventana.mainloop()
