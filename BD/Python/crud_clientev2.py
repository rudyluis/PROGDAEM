import psycopg2

# Conectarse a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="jardineria",
    user="postgres",
    password="123456",
    port="5432"
)
cursor = conn.cursor()

def gestionar_cliente_iud(p_operacion, p_id_cliente=None, **kwargs):
    # Definir los valores para la función
    valores = {
        "p_operacion": p_operacion,
        "p_id_cliente": p_id_cliente      
    }
    valores.update(kwargs)  # Agregar otros argumentos clave-valor
    print(valores)
    # Ejecutar la función en la base de datos
    cursor.callproc('gestionar_cliente_iud', list(valores.values()))

    # Obtener el resultado
    result = cursor.fetchone()
    conn.commit()
    cursor.close
    return result[0] if result else None

def mostrar_menu():
    print("1. Insertar cliente")
    print("2. Actualizar cliente")
    print("3. Eliminar cliente")
    print("4. Salir")

def insertar_cliente():
    # Obtener datos del usuario
    kwargs=obtener_datos_cliente()
    # Agregar otros campos según tus necesidades

    # Llamar a la función para insertar cliente
    mensaje = gestionar_cliente_iud('INSERT', **kwargs )
    print(mensaje)

def actualizar_cliente():
    # Obtener datos del usuario
    id_cliente = input("Ingrese el ID del cliente a actualizar: ")
    kwargs=obtener_datos_cliente()
    # Agregar otros campos según tus necesidades

    # Llamar a la función para actualizar cliente
    mensaje = gestionar_cliente_iud('UPDATE', p_id_cliente=id_cliente, **kwargs)
    print(mensaje)

def eliminar_cliente():
    # Obtener ID del cliente a eliminar
    id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
    kwargs={
        "codigocliente": None,
        "nombrecliente": None,
        "nombrecontacto": None,
        "apellidocontacto": None,
        "telefono": None,
        "fax": None,
        "lineadireccion1": None,
        "lineadireccion2": None,
        "ciudad": None,
        "region": None,
        "pais": None,
        "codigopostal": None,
        "idcodigoempleadoventas": None,
        "limite_credito": None
    }
    # Llamar a la función para eliminar cliente
    mensaje = gestionar_cliente_iud('DELETE', p_id_cliente=id_cliente,**kwargs)
    print(mensaje)

def obtener_datos_cliente():
    codigo_cliente = input("Ingrese el código del cliente: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    nombre_contacto = input("Ingrese el nombre de contacto: ")
    apellido_contacto = input("Ingrese el apellido de contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    fax = input("Ingrese el número de fax: ")
    direccion1 = input("Ingrese la dirección 1: ")
    direccion2 = input("Ingrese la dirección 2: ")
    ciudad = input("Ingrese la ciudad: ")
    region = input("Ingrese la región: ")
    pais = input("Ingrese el país: ")
    codigo_postal = input("Ingrese el código postal: ")
    id_empleado_ventas = input("Ingrese el ID del empleado de ventas: ")
    limite_credito = input("Ingrese el límite de crédito: ")
    return {
        "codigocliente": codigo_cliente,
        "nombrecliente": nombre_cliente,
        "nombrecontacto": nombre_contacto,
        "apellidocontacto": apellido_contacto,
        "telefono": telefono,
        "fax": fax,
        "lineadireccion1": direccion1,
        "lineadireccion2": direccion2,
        "ciudad": ciudad,
        "region": region,
        "pais": pais,
        "codigopostal": codigo_postal,
        "idcodigoempleadoventas": id_empleado_ventas,
        "limite_credito": limite_credito
    }

# Ciclo principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        insertar_cliente()
    elif opcion == "2":
        actualizar_cliente()
    elif opcion == "3":
        eliminar_cliente()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intente de nuevo.")

# Cerrar la conexión
cursor.close()
conn.close()
