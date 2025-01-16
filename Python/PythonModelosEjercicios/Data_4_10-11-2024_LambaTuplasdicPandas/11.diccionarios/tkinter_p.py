import tkinter as tk

# Función que se ejecuta cuando se hace clic en el botón
def saludo():
    etiqueta.config(text="¡Hola, Tkinter!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Aplicación")
ventana.geometry("300x200")

# Crear una etiqueta con un texto inicial
etiqueta = tk.Label(ventana, text="¡Bienvenidos!")
etiqueta.pack(pady=10)

# Crear un botón que ejecutará la función 'saludo' al hacer clic
boton = tk.Button(ventana, text="Haz clic aquí", command=saludo)
boton.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
