import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine, text
from st_aggrid import AgGrid
import warnings

warnings.filterwarnings('ignore')

# Configuración de conexión a la base de datos
engine = create_engine("mysql+pymysql://root@localhost/bikegear")

# Configuración de la página
st.set_page_config(page_title="BikeGear", page_icon=":bar_chart", layout="wide")
st.title("Ventas de BikeGear")

# CSS personalizado
st.markdown(
    """
        <style>
           .stMetric{
                background-color:#FFFACD;
                border: 1px solid #E0E0E0;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1)
           }
        </style>
    """, unsafe_allow_html=True
)

## Consulta de datos General
with engine.connect() as conn:
    query=text("""
        select 
        v.id_venta,v.fecha, v.anio, v.mes, v.edad_cliente, v.genero,v.cantidad,v.costo_unitario, v.precio_unitario,
        v.id_producto, p.nombre_producto, cp.id_categoria_producto, cp.nombre_categoria,
        s.id_sucursal, s.nombre_sucursal, c.id_ciudad, c.nombre_ciudad
    from venta v
    inner join producto p on v.id_producto=p.id_producto
    inner join categoria_producto cp on cp.id_categoria_producto= p.id_categoria_producto
    inner join sucursal s on s.id_sucursal = v.id_sucursal
    inner join ciudad c on c.id_ciudad= s.id_ciudad
    
    """)
    result= conn.execute(query)
    df=pd.DataFrame(result.fetchall(), columns=result.keys())
    ##st.write(df)
    with st.expander('Datos Generales'):
        AgGrid(df)


# Consulta para obtener los años y meses únicos
with engine.connect() as conn:
    years = pd.read_sql("SELECT DISTINCT anio FROM venta ORDER BY anio", conn)['anio'].tolist()
    months = pd.read_sql("SELECT DISTINCT mes FROM venta", conn)['mes'].tolist()
    
# Filtros de año y mes
col1, col2 = st.columns(2)
with col1:
    year = st.selectbox("Seleccione el año:", years)
with col2:
    month = st.selectbox("Seleccione Mes", months)

# Consulta SQL filtrada por año y mes
with engine.connect() as conn:
    query  = text("""
            select v.*, p.nombre_producto, cp.nombre_categoria, s.nombre_sucursal , c.nombre_ciudad
        from
        venta v
        inner join producto p on v.id_producto= p.id_producto
        inner join categoria_producto cp on cp.id_categoria_producto= p.id_categoria_producto
        inner join sucursal s on s.id_sucursal = v.id_sucursal
        inner join ciudad c on c.id_ciudad= s.id_ciudad
        WHERE v.anio = :year AND v.mes = :month
    """)

    filtered_df = pd.read_sql(query, conn, params={"year": year, "month": month})

# Filtros adicionales (Ciudad, Sucursal, Categoría)
st.sidebar.header("Escoge tu opción")
ciudad_filter = st.sidebar.multiselect("Seleccione la ciudad", filtered_df["nombre_ciudad"].unique())
if ciudad_filter:
    filtered_df = filtered_df[filtered_df["nombre_ciudad"].isin(ciudad_filter)]

sucursal_filter = st.sidebar.multiselect("Seleccione la sucursal", filtered_df["nombre_sucursal"].unique())
if sucursal_filter:
    filtered_df = filtered_df[filtered_df["nombre_sucursal"].isin(sucursal_filter)]

categoria_filter = st.sidebar.multiselect("Seleccione la Categoría", filtered_df["nombre_categoria"].unique())
if categoria_filter:
    filtered_df = filtered_df[filtered_df["nombre_categoria"].isin(categoria_filter)]

# Métricas
col_a, col_b, col_c = st.columns(3)
with col_a:
    ingresos_totales = filtered_df["ingreso"].sum()
    st.metric("Ingresos Totales", f"Bs.{ingresos_totales:,.2f}")
with col_b:
    producto_mas_vendido = filtered_df.groupby("nombre_producto")["cantidad"].sum().idxmax()
    cantidad_mas_vendida = filtered_df.groupby("nombre_producto")["cantidad"].sum().max()
    st.metric(f"Producto más Vendido: {producto_mas_vendido}", f"Unids: {cantidad_mas_vendida}")
with col_c:
    costo_total = filtered_df["costo"].sum()
    st.metric("Costo Total", f"Bs.{costo_total:,.2f}")

# Gráfico de Ingresos por Producto
categoria_df = filtered_df.groupby("nombre_producto")["ingreso"].sum().reset_index()
col1, col2 = st.columns(2)
with col1:
    st.subheader("Ingresos por Categoría")
    fig = px.bar(categoria_df, x="nombre_producto", y="ingreso", text_auto='.2s', template="seaborn", color="nombre_producto")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de Ingresos por Ciudad
with col2:
    ciudad_df = filtered_df.groupby("nombre_ciudad")["ingreso"].sum().reset_index()
    st.subheader("Ingresos por Ciudad")
    fig_pie = px.pie(ciudad_df, values="ingreso", names="nombre_ciudad", hole=0.5)
    st.plotly_chart(fig_pie, use_container_width=True)

# Expander para ver datos de categoría y ciudad
cl1, cl2 = st.columns(2)
with cl1:
    with st.expander("Ver Datos de Categoría"):
        st.write(categoria_df.style.background_gradient(cmap="Blues"))
        csv = categoria_df.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar Datos", data=csv, file_name="Categoria.csv", mime="text/csv")
with cl2:
    with st.expander("Ver Datos por Ciudad"):
        st.write(ciudad_df.style.background_gradient(cmap="Oranges"))
        csv = ciudad_df.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar Datos", data=csv, file_name="Ciudad.csv", mime="text/csv")

# Gráfico de Treemap
st.subheader("Vista Jerárquica de Ventas")
fig_tree = px.treemap(filtered_df, path=["nombre_ciudad", "nombre_sucursal", "nombre_producto"], values="ingreso", color="nombre_producto")
st.plotly_chart(fig_tree, use_container_width=True)



# Gráfico de dispersión para Ingresos vs Costo
st.subheader("Gráfico de Dispersión para Ingresos vs Costo")
fig_scatter = px.scatter(filtered_df, x="ingreso", y="costo", size="cantidad", hover_name="nombre_categoria", color="nombre_producto")
st.plotly_chart(fig_scatter, use_container_width=True)

# Gráfico de línea para serie de ingresos anuales
with engine.connect() as conn:
    query  = text("""
                select v.*, p.nombre_producto, cp.nombre_categoria, s.nombre_sucursal , c.nombre_ciudad
            from
            venta v
            inner join producto p on v.id_producto= p.id_producto
            inner join categoria_producto cp on cp.id_categoria_producto= p.id_categoria_producto
            inner join sucursal s on s.id_sucursal = v.id_sucursal
            inner join ciudad c on c.id_ciudad= s.id_ciudad
            WHERE v.anio = :year
        """)

    filtered_df2 = pd.read_sql(query, conn,params={"year": year})
# Diccionario de mapeo de meses en español a números
meses_espanol = {
    "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04", "Mayo": "05", "Junio": "06",
    "Julio": "07", "Agosto": "08", "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
}

# Mapear los nombres de los meses al número correspondiente
filtered_df2["mes_num"] = filtered_df2["mes"].map(meses_espanol)
# Crear una columna de fecha combinando año y mes
filtered_df2["fecha"] = pd.to_datetime(filtered_df2["anio"].astype(str) + "-" + filtered_df2["mes_num"] + "-01")
# Agrupar los datos por fecha (mes) y calcular los ingresos totales
line_chart_df = filtered_df2.groupby(filtered_df2["fecha"].dt.to_period("M"))["ingreso"].sum().reset_index()

# Convertir la columna de periodo a timestamp
line_chart_df["fecha"] = line_chart_df["fecha"].dt.to_timestamp()
# Generar el gráfico de línea para ingresos anuales
st.subheader("Serie de Ingresos Anuales")
fig_line = px.line(line_chart_df, x="fecha", y="ingreso", labels={"ingreso": "Monto"})
st.plotly_chart(fig_line, use_container_width=True)



# Consulta SQL para obtener los datos filtrados por año y mes
with engine.connect() as conn:

    # Gráfico 1: Histograma de Ingresos
    st.subheader("Distribución de Ingresos")
    # Consulta SQL para obtener los ingresos por producto
    query_histograma_ingresos = f"""
    SELECT v.ingreso
    FROM venta v
    WHERE v.anio = {year} AND v.mes = '{month}'
    """
    histograma_ingresos_df = pd.read_sql(query_histograma_ingresos, conn)

fig_histograma = px.histogram(histograma_ingresos_df, x="ingreso", nbins=20, 
                               title="Distribución de Ingresos por Venta", labels={"ingreso": "Monto de Ingreso"})
st.plotly_chart(fig_histograma, use_container_width=True)



# Diagrama de Cajas para Ingresos
st.subheader("Diagrama de Cajas de Ingresos por Producto")
fig_boxplot = px.box(filtered_df, x="nombre_producto", y="ingreso", 
                     title="Distribución de Ingresos por Producto", 
                     labels={"ingreso": "Monto de Ingreso", "nombre_producto": "Producto"}, color="nombre_producto")
st.plotly_chart(fig_boxplot, use_container_width=True)

# Diagrama de Cajas para Cantidades Vendidas
st.subheader("Diagrama de Cajas de Cantidades Vendidas por Producto")
fig_boxplot_qty = px.box(filtered_df, x="nombre_producto", y="cantidad", 
                         title="Distribución de Cantidades Vendidas por Producto", 
                         labels={"cantidad": "Cantidad Vendida", "nombre_producto": "Producto"})
st.plotly_chart(fig_boxplot_qty, use_container_width=True)


# ECDF de los Ingresos por Género
st.subheader("ECDF de Ingresos por Género")
fig = px.ecdf(filtered_df, x="ingreso", color="genero", 
              labels={"ingreso": "Monto de Ingreso", "genero": "Género"})
st.plotly_chart(fig, use_container_width=True)


# Consulta SQL para obtener los ingresos por sucursal
with engine.connect() as conn:
    query = f"""
    SELECT s.nombre_sucursal AS sucursal, SUM(v.ingreso) AS ingresos, c.nombre_ciudad
    FROM venta v
    JOIN sucursal s ON v.id_sucursal = s.id_sucursal
    inner join ciudad c on c.id_ciudad = s.id_ciudad
    WHERE v.anio = {year} 
    GROUP BY s.nombre_sucursal
    ORDER BY ingresos DESC
"""
    print(query)
    sucursal_df = pd.read_sql(query, conn)
if ciudad_filter:
    sucursal_df = sucursal_df[sucursal_df["nombre_ciudad"].isin(ciudad_filter)]


# Gráfico de pastel para mostrar ingresos por sucursal
st.subheader("Distribución de Ingresos por Sucursal")
fig_pie_sucursal = px.pie(sucursal_df, values="ingresos", names="sucursal", hole=0.4,
                          title="Ingresos por Sucursal")
st.plotly_chart(fig_pie_sucursal, use_container_width=True)