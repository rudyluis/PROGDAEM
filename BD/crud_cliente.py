import psycopg2

# Parámetros de conexión a la base de datos PostgreSQL
database_params = {
    'host': 'localhost',
    'database': 'jardineria',
    'user': 'postgres',
    'password': '123456',
    'port': '5432'  # Puerto predeterminado de PostgreSQL
}

def gestionar_cliente_iud(p_operacion, p_id_cliente=None, p_codigo_cliente=None, p_nombre_cliente=None, p_nombre_contacto=None, p_apellido_contacto=None, p_telefono=None, p_fax=None, p_direccion1=None, p_direccion2=None, p_ciudad=None, p_region=None, p_pais=None, p_codigo_postal=None, p_id_empleado_ventas=None, p_limite_credito=None):
    try:
        # Conectarse a la base de datos
        conn = psycopg2.connect(**database_params)
        cursor = conn.cursor()

        # Ejecutar la función gestionar_cliente_iud con los parámetros proporcionados
        cursor.execute("SELECT * from gestionar_cliente_iud(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (p_operacion, p_id_cliente, p_codigo_cliente, p_nombre_cliente, p_nombre_contacto, p_apellido_contacto, p_telefono, p_fax, p_direccion1, p_direccion2, p_ciudad, p_region, p_pais, p_codigo_postal, p_id_empleado_ventas, p_limite_credito))
         
        resultado = cursor.fetchone()

        # Imprimir el resultado
        print(resultado)

        # Confirmar la transacción
        conn.commit()


    except (Exception, psycopg2.Error) as error:
        print("Error al ejecutar la función:", error)

    finally:
        # Cerrar la conexión
        if conn:
            cursor.close()
            conn.close()

# Ejemplo de uso
gestionar_cliente_iud('INSERT', p_codigo_cliente=123, p_nombre_cliente='Cliente de ejemplo', p_nombre_contacto='Contacto', p_apellido_contacto='Apellido', p_telefono='123456789', p_fax='987654321', p_direccion1='Dirección 1', p_direccion2='Dirección 2', p_ciudad='Ciudad', p_region='Región', p_pais='País', p_codigo_postal='12345', p_id_empleado_ventas=1, p_limite_credito=1000.0)
