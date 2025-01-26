from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, Numeric

# Crear el motor de base de datos
engine = create_engine('postgresql://postgres:123456@localhost:5432/jardineria')


# Función para gestionar el cliente
def gestionar_cliente_iud(p_operacion, p_id_cliente=None, **kwargs):
    params = {
        'p_operacion': p_operacion,
        'p_id_cliente': p_id_cliente,
        'p_codigo_cliente': kwargs['codigocliente'],
        'p_nombre_cliente': kwargs['nombrecliente'],
        'p_nombre_contacto': kwargs['nombrecontacto'],
        'p_apellido_contacto': kwargs['apellidocontacto'],
        'p_telefono': kwargs['telefono'],
        'p_fax': kwargs['fax'],
        'p_direccion1': kwargs['lineadireccion1'],
        'p_direccion2': kwargs['lineadireccion2'],
        'p_ciudad': kwargs['ciudad'],
        'p_region': kwargs['region'],
        'p_pais': kwargs['pais'],
        'p_codigo_postal': kwargs['codigopostal'],
        'p_id_empleado_ventas': kwargs['idcodigoempleadoventas'],
        'p_limite_credito': kwargs['limite_credito']
    }
    with engine.connect() as conn:

        try:
            
            sql = text("SELECT * FROM gestionar_cliente_iud(:p_operacion, :p_id_cliente, :p_codigo_cliente, :p_nombre_cliente, :p_nombre_contacto, :p_apellido_contacto, :p_telefono, :p_fax, :p_direccion1, :p_direccion2, :p_ciudad, :p_region, :p_pais, :p_codigo_postal, :p_id_empleado_ventas, :p_limite_credito)")

            # Ejecutar la consulta SQL
            result = conn.execute(sql, params)
            conn.commit()

            print(result.scalar())
        except Exception as e:
            return f'Error: {str(e)}'

# Función para mostrar el menú
def mostrar_menu():
    print("1. Insertar cliente")
    print("2. Actualizar cliente")
    print("3. Eliminar cliente")
    print("4. Salir")

# Función principal
def main():
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

# Función para insertar un cliente
def insertar_cliente():
    kwargs = obtener_datos_cliente()
    mensaje = gestionar_cliente_iud('INSERT', **kwargs)
    print(mensaje)

# Función para actualizar un cliente
def actualizar_cliente():
    id_cliente = input("Ingrese el ID del cliente a actualizar: ")
    kwargs = obtener_datos_cliente()
    mensaje = gestionar_cliente_iud('UPDATE', p_id_cliente=id_cliente, **kwargs)
    print(mensaje)

# Función para eliminar un cliente
def eliminar_cliente():
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")
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
    mensaje = gestionar_cliente_iud('DELETE', p_id_cliente=id_cliente,**kwargs)
    print(mensaje)

# Función para obtener los datos del cliente desde el usuario
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

if __name__ == "__main__":
    main()
