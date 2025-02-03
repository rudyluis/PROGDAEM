import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd
from st_aggrid import AgGrid
# Configura la conexión a la base de datos
DB_URL = "mysql+pymysql://root@localhost/bikegear"
engine = create_engine(DB_URL)

with engine.connect() as conn:
        query = text(f"""
        select 
                v.id_venta,v.fecha,  v.anio, v.mes, v.edad_cliente, v.genero,v.cantidad,v.costo_unitario, v.precio_unitario,
                v.id_producto, p.nombre_producto, cp.id_categoria_producto, cp.nombre_categoria,
                s.id_sucursal, s.nombre_sucursal, c.id_ciudad, c.nombre_ciudad
            from venta v
            inner join producto p on v.id_producto=p.id_producto
            inner join categoria_producto cp on cp.id_categoria_producto= p.id_categoria_producto
            inner join sucursal s on s.id_sucursal = v.id_sucursal
            inner join ciudad c on c.id_ciudad= s.id_ciudad
            order by id_venta
        
      """)
        result = conn.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        
# Función para obtener opciones de la tabla `producto`
# Función para obtener opciones de la tabla `producto`
def obtener_productos():
    with engine.connect() as conn:
        query = text("SELECT id_producto, nombre_producto FROM producto")
        result = conn.execute(query).fetchall()
        
        # Convertimos el resultado en un diccionario de la forma {nombre_producto: id_producto}
        productos = {row[1]: row[0] for row in result}
        return productos

# Función para obtener opciones de la tabla `sucursal`
# Función para obtener opciones de la tabla `sucursal`
def obtener_sucursales():
    with engine.connect() as conn:
        query = text("SELECT id_sucursal, nombre_sucursal FROM sucursal")
        result = conn.execute(query).fetchall()
        
        # Convertimos el resultado en un diccionario de la forma {nombre_sucursal: id_sucursal}
        sucursales = {row[1]: row[0] for row in result}
        return sucursales

# Función para obtener una venta específica
def obtener_venta(id_venta):
    with engine.connect() as conn:
        query = text(f"""
        select 
                v.id_venta,v.fecha,  v.anio, v.mes, v.edad_cliente, v.genero,v.cantidad,v.costo_unitario, v.precio_unitario,
                v.id_producto, p.nombre_producto, cp.id_categoria_producto, cp.nombre_categoria,
                s.id_sucursal, s.nombre_sucursal, c.id_ciudad, c.nombre_ciudad
            from venta v
            inner join producto p on v.id_producto=p.id_producto
            inner join categoria_producto cp on cp.id_categoria_producto= p.id_categoria_producto
            inner join sucursal s on s.id_sucursal = v.id_sucursal
            inner join ciudad c on c.id_ciudad= s.id_ciudad
            where   id_venta = {id_venta}
            order by id_venta
        
      """)
        result = conn.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df
        


# Obtener datos de productos y sucursales
productos = obtener_productos()
sucursales = obtener_sucursales()


# Función para mostrar los registros de la tabla `venta`
def listar_ventas():
    with engine.connect() as conn:
        query = text("""
        select 
                v.id_venta,v.fecha,  v.anio, v.mes, v.edad_cliente, v.genero,v.cantidad,v.costo_unitario, v.precio_unitario,
                v.id_producto, p.nombre_producto, cp.id_categoria_producto, cp.nombre_categoria,
                s.id_sucursal, s.nombre_sucursal, c.id_ciudad, c.nombre_ciudad
            from venta v
            inner join producto p on v.id_producto=p.id_producto
            inner join categoria_producto cp on cp.id_categoria_producto= p.id_categoria_producto
            inner join sucursal s on s.id_sucursal = v.id_sucursal
            inner join ciudad c on c.id_ciudad= s.id_ciudad
            order by id_venta;
        """
        )
        result = conn.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    ##st.dataframe(df)
    AgGrid(df)

# Función para agregar un nuevo registro en `venta`
def agregar_venta(fecha, id_sucursal, anio, mes, edad_cliente, genero, cantidad, costo_unitario, precio_unitario, costo, ingreso, id_producto):
    try:
        with engine.connect() as conn:
            query = text("""
                INSERT INTO venta (fecha, id_sucursal, anio, mes, edad_cliente, genero, cantidad, costo_unitario, precio_unitario, costo, ingreso, id_producto)
                VALUES (:fecha, :id_sucursal, :anio, :mes, :edad_cliente, :genero, :cantidad, :costo_unitario, :precio_unitario, :costo, :ingreso, :id_producto)
            """)
            params = {
                "fecha": fecha,
                "id_sucursal": id_sucursal,
                "anio": anio,
                "mes": mes,
                "edad_cliente": edad_cliente,
                "genero": genero,
                "cantidad": cantidad,
                "costo_unitario": costo_unitario,
                "precio_unitario": precio_unitario,
                "costo": costo,
                "ingreso": ingreso,
                "id_producto": id_producto
            }
            conn.execute(query, params)
            conn.commit()
        st.success("Venta agregada exitosamente")
        # Captura cualquier excepción y muestra el error en Streamlit
    except Exception as e:
        
        st.error(f"Ocurrió un error al intentar agregar la venta: {e}")


def actualizar_venta(id_venta, **fields):
    if not fields:
        st.warning("No se han proporcionado campos para actualizar.")
        return
    
    try:
        with engine.connect() as conn:
            # Construir la parte de la consulta para los campos
            set_clause = ", ".join([f"{key} = :{key}" for key in fields])
            
            # Consulta UPDATE dinámica
            
            query = text(f"UPDATE venta SET {set_clause} WHERE id_venta = :id_venta")
            params = {"id_venta": id_venta, **fields}
            # Ejecutar la consulta con los parámetros

            conn.execute(query, params)
            conn.commit()
        st.success("Venta actualizada exitosamente")

    except Exception as e:
        st.error(f"Ocurrió un error al actualizar la venta: {e}")


# Función para eliminar un registro de `venta`
def eliminar_venta(id_venta):
    with engine.connect() as conn:
        query = text(f"DELETE FROM venta WHERE id_venta = {id_venta}")
        
        # Pasamos el parámetro como un diccionario
        conn.execute(query)
        conn.commit()
        st.warning("Venta eliminada exitosamente")

# Interfaz en Streamlit
st.title("Gestión de Ventas")

menu = st.sidebar.selectbox("Opciones", ["Listar Ventas", "Agregar Venta", "Actualizar Venta", "Eliminar Venta"])

if menu == "Listar Ventas":
    listar_ventas()

elif menu == "Agregar Venta":
    st.subheader("Agregar una nueva venta")
    

    # Selección de fecha y datos de venta
    fecha = st.date_input("Fecha de venta")
    anio = st.number_input("Año", min_value=2000, max_value=2100, step=1)
    mes = st.text_input("Mes")
    edad_cliente = st.number_input("Edad del Cliente", min_value=0, max_value=120)
    genero = st.selectbox("Género del Cliente", ["M", "F"])
    cantidad = st.number_input("Cantidad", min_value=1)
    costo_unitario = st.number_input("Costo Unitario")
    precio_unitario = st.number_input("Precio Unitario")
    costo = st.number_input("Costo Total")
    ingreso = st.number_input("Ingreso Total")

    # Menú desplegable para seleccionar sucursal y producto
    sucursal_seleccionada = st.selectbox("Selecciona la Sucursal", list(sucursales.keys()))
    producto_seleccionado = st.selectbox("Selecciona el Producto", list(productos.keys()))

    # Obtener IDs seleccionados para sucursal y producto
    id_sucursal = sucursales[sucursal_seleccionada]
    id_producto = productos[producto_seleccionado]


    
    if st.button("Agregar Venta"):
        agregar_venta(fecha, id_sucursal, anio, mes, edad_cliente, genero, cantidad, costo_unitario, precio_unitario, costo, ingreso, id_producto)

elif menu == "Actualizar Venta":
    st.subheader("Actualizar una venta existente")
    # Seleccionar ID de la venta que se quiere actualizar
    id_venta = st.number_input("ID de la venta a actualizar:", min_value=1, step=1)

    # Obtener los datos actuales de la venta
    venta = obtener_venta(id_venta)
    print(venta)
    
    st.write(venta)

        # Mostrar datos actuales y permitir actualización
    sucursales = obtener_sucursales()
    productos = obtener_productos()
        # Crear un combo box para la sucursal
    nombre_sucursal = [sucursal for sucursal in sucursales]
    id_sucursal = st.selectbox("Seleccionar Sucursal", nombre_sucursal, index=nombre_sucursal.index(venta['nombre_sucursal'][0]))

        # Crear un combo box para el producto
    nombre_producto = [producto for producto in productos]
    id_producto = st.selectbox("Seleccionar Producto", nombre_producto, index=nombre_producto.index(venta['nombre_producto'][0]))

        # Capturar los otros valores para la actualización
    cantidad = st.number_input("Cantidad", min_value=1, value=int(venta['cantidad'][0]) )
    costo_unitario = st.number_input("Costo Unitario", min_value=0.0, value=float(venta['costo_unitario'][0]))
    precio_unitario = st.number_input("Precio Unitario", min_value=0.0, value=float(venta['precio_unitario'][0]))
        # Botón de actualización
    if st.button("Actualizar Venta"):
            # Actualizar la venta
            # Usando un diccionario para los campos a actualizar

            
            df_ventas = df.copy()

            id_sucursal = df_ventas[df_ventas['nombre_sucursal'] == id_sucursal]['id_sucursal'].unique()
            id_producto = df_ventas[df_ventas['nombre_producto'] == id_producto]['id_producto'].unique()

            campos_a_actualizar = {
                'id_sucursal': int(id_sucursal[0]),
                'id_producto': int(id_producto[0]),
                'cantidad': cantidad,
                'costo_unitario': costo_unitario,
                'precio_unitario': precio_unitario
            }

            st.write(campos_a_actualizar)
            actualizar_venta(id_venta, **campos_a_actualizar)
            st.success("Venta actualizada correctamente.")

    

elif menu == "Eliminar Venta":
    st.subheader("Eliminar una venta")
    id_venta = st.number_input("ID Venta", min_value=1)
    if st.button("Eliminar Venta"):
        eliminar_venta(id_venta)


