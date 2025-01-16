import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Diccionario para almacenar las ventas
ventas = {}

# Función para agregar una venta
def agregar_venta():
    venta_id = entry_venta_id.get()
    producto = entry_producto.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()

    # Verificar que los campos no estén vacíos
    if not (venta_id and producto and cantidad and precio):
        messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
        return

    try:
        cantidad = int(cantidad)
        precio = float(precio)
    except ValueError:
        messagebox.showwarning("Valor Inválido", "La cantidad debe ser un número entero y el precio debe ser un número decimal.")
        return

    # Almacenar la venta en el diccionario
    ventas[venta_id] = {"producto": producto, "cantidad": cantidad, "precio": precio, "total": cantidad * precio}
    
    # Limpiar los campos de entrada
    entry_venta_id.delete(0, tk.END)
    entry_producto.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

    # Actualizar la tabla de ventas
    mostrar_ventas()

# Función para mostrar las ventas registradas en el Treeview
def mostrar_ventas():
    # Limpiar la tabla actual
    for row in treeview_ventas.get_children():
        treeview_ventas.delete(row)

    # Añadir las ventas al Treeview
    for venta_id, datos in ventas.items():
        treeview_ventas.insert("", "end", values=(venta_id, datos['producto'], datos['cantidad'], datos['precio'], datos['total']))

# Función para eliminar una venta seleccionada
def eliminar_venta():
    selected_item = treeview_ventas.selection()
    if not selected_item:
        messagebox.showwarning("Selección vacía", "Por favor, seleccione una venta para eliminar.")
        return
    venta_id = treeview_ventas.item(selected_item)["values"][0]
    del ventas[venta_id]
    mostrar_ventas()

# Función para modificar una venta seleccionada
def modificar_venta():
    selected_item = treeview_ventas.selection()
    if not selected_item:
        messagebox.showwarning("Selección vacía", "Por favor, seleccione una venta para modificar.")
        return

    venta_id = treeview_ventas.item(selected_item)["values"][0]
    venta = ventas[venta_id]

    # Llenar los campos con los datos de la venta seleccionada
    entry_venta_id.delete(0, tk.END)
    entry_venta_id.insert(0, venta_id)
    entry_producto.delete(0, tk.END)
    entry_producto.insert(0, venta["producto"])
    entry_cantidad.delete(0, tk.END)
    entry_cantidad.insert(0, venta["cantidad"])
    entry_precio.delete(0, tk.END)
    entry_precio.insert(0, venta["precio"])

    # Modificar la venta
    def guardar_modificacion():
        nuevo_producto = entry_producto.get()
        nueva_cantidad = entry_cantidad.get()
        nuevo_precio = entry_precio.get()

        if not (nuevo_producto and nueva_cantidad and nuevo_precio):
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
            return

        try:
            nueva_cantidad = int(nueva_cantidad)
            nuevo_precio = float(nuevo_precio)
        except ValueError:
            messagebox.showwarning("Valor Inválido", "La cantidad debe ser un número entero y el precio debe ser un número decimal.")
            return

        ventas[venta_id] = {"producto": nuevo_producto, "cantidad": nueva_cantidad, "precio": nuevo_precio, "total": nueva_cantidad * nuevo_precio}
        mostrar_ventas()

        # Limpiar los campos
        entry_venta_id.delete(0, tk.END)
        entry_producto.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_precio.delete(0, tk.END)

    # Botón para guardar la modificación
    btn_guardar_modificacion = tk.Button(ventana, text="Guardar Modificación", command=guardar_modificacion)
    btn_guardar_modificacion.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Ventas")
ventana.geometry("700x500")

# Etiquetas y campos de entrada
frame_entradas = tk.Frame(ventana)
frame_entradas.pack(pady=10)

tk.Label(frame_entradas, text="ID de Venta:").grid(row=0, column=0, padx=5)
entry_venta_id = tk.Entry(frame_entradas)
entry_venta_id.grid(row=0, column=1, padx=5)

tk.Label(frame_entradas, text="Producto:").grid(row=1, column=0, padx=5)
entry_producto = tk.Entry(frame_entradas)
entry_producto.grid(row=1, column=1, padx=5)

tk.Label(frame_entradas, text="Cantidad:").grid(row=2, column=0, padx=5)
entry_cantidad = tk.Entry(frame_entradas)
entry_cantidad.grid(row=2, column=1, padx=5)

tk.Label(frame_entradas, text="Precio:").grid(row=3, column=0, padx=5)
entry_precio = tk.Entry(frame_entradas)
entry_precio.grid(row=3, column=1, padx=5)

# Botón para agregar la venta
btn_agregar_venta = tk.Button(ventana, text="Agregar Venta", command=agregar_venta)
btn_agregar_venta.pack(pady=10)

# Crear Treeview (tabla) para mostrar las ventas
treeview_ventas = ttk.Treeview(ventana, columns=("ID", "Producto", "Cantidad", "Precio", "Total"), show="headings")
treeview_ventas.heading("ID", text="ID de Venta")
treeview_ventas.heading("Producto", text="Producto")
treeview_ventas.heading("Cantidad", text="Cantidad")
treeview_ventas.heading("Precio", text="Precio")
treeview_ventas.heading("Total", text="Total")
treeview_ventas.pack(pady=10)

# Botones de modificar y eliminar
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_modificar_venta = tk.Button(frame_botones, text="Modificar Venta", command=modificar_venta)
btn_modificar_venta.grid(row=0, column=0, padx=10)

btn_eliminar_venta = tk.Button(frame_botones, text="Eliminar Venta", command=eliminar_venta)
btn_eliminar_venta.grid(row=0, column=1, padx=10)

# Iniciar la aplicación
ventana.mainloop()
