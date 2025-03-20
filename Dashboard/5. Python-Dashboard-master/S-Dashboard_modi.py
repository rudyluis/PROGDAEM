import streamlit as st
import pandas as pd
import plotly.express as px
import os
import warnings
# Supresión de advertencias
warnings.filterwarnings('ignore')
# Configuración de la página en Streamlit
st.set_page_config(page_title="BikeGear", page_icon=":bar_chart:", layout="wide")
# Inyectar CSS para dar estilo a todos los elementos h1
st.markdown(
    """
    <style>
    h1 {
        background-color: #1E90FF; /* Fondo azul */
        color: white; /* Texto blanco */
        padding: 10px; /* Espaciado interno */
        border-radius: 15px; /* Bordes redondeados */
        text-align: center; /* Centrar el texto */
        margin-bottom: 20px; /* Espacio debajo de cada h1 */
    }
     h2, h3, h4, h5, h6 {
        background-color: #1E90FF; /* Fondo azul */
        color: white; /* Texto blanco */
        padding: 10px; /* Espaciado interno */
        border-radius: 15px; /* Bordes redondeados */
        text-align: left; /* Centrar el texto */
        margin-bottom: 20px; /* Espacio debajo de cada encabezado */
        font-size: 18px; /* Tamaño de fuente más pequeño, ajusta según sea necesario */
    }
    </style>
    """,
    unsafe_allow_html=True
)

      # Inyectar CSS para dar estilo a todas las métricas
st.markdown(
        """
        <style>
        /* Estilo para todos los elementos de clase 'stMetric' */
        .stMetric{
            background-color: #FFFACD; /* Fondo amarillo claro */
            border: 1px solid #E0E0E0; /* Borde gris claro */
            padding: 10px;
            border-radius: 10px; /* Bordes redondeados */
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Sombra suave */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Inyectar CSS para dar estilo a los elementos con 'data-testid="stFullScreenFrame"'
st.markdown(
    """
    <style>
    /* Estilo para los elementos con el atributo data-testid="stFullScreenFrame" */
    [data-testid="stFullScreenFrame"] {
        border-top: 3px solid #1E90FF; /* Borde superior azul */
        border-bottom: 3px solid #1E90FF; /* Borde inferior azul */
        border-left: 3px solid #1E90FF; /* Borde izquierdo azul */
        border-radius: 15px 0px 0px 15px; /* Bordes redondeados solo en las esquinas superiores e inferiores izquierdas */
        padding: 5px;
        margin-bottom: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Título de la aplicación
st.title(":bar_chart: Almacén de Ventas 'BikeGear'")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

# Cargar el archivo Excel
df = pd.read_excel("DatosBikeGear.xlsx", header=0)

# Definir las columnas para la selección de año y mes
col1, col2 = st.columns((2))

# Lista con el orden correcto de los meses
orden_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
               "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Ordenar los meses únicos en el DataFrame usando la lista anterior
meses_ordenados = sorted(df["Mes"].unique(), key=lambda mes: orden_meses.index(mes))



with col1:
    year = st.selectbox("Seleccione Año", df["Año"].unique(), placeholder="Seleccione el año")
    
with col2:
    month = st.selectbox("Seleccione Mes",meses_ordenados, placeholder="Seleccione el mes")

# Filtrar el DataFrame según el año y mes seleccionados
filtered_df = df[(df["Año"] == year) & (df["Mes"] == month)].copy()
filtered_df_year = df[(df["Año"] == year)].copy()
# Barra lateral para las opciones de filtro
st.sidebar.header("🔍 Elige tu filtro: ")
# Filtro de ciudades usando selección múltiple
ciudad = st.sidebar.multiselect("Seleccione la ciudad", filtered_df["Ciudad"].unique(), placeholder="Selecciones la ciudad")
filtered_df = filtered_df[filtered_df["Ciudad"].isin(ciudad)] if ciudad else filtered_df

# Filtro de sucursales usando selección múltiple
sucursal = st.sidebar.multiselect("Seleccione la Sucursal", filtered_df["Sucursal"].unique(),placeholder="Seleccione la sucursal")
filtered_df = filtered_df[filtered_df["Sucursal"].isin(sucursal)] if sucursal else filtered_df
    
# Filtro de categoría usando selección múltiple
categoria = st.sidebar.multiselect("Seleccione la Categoría", filtered_df["Categoria del Producto"].unique(),placeholder="Seleccione la Categoría")
filtered_df = filtered_df[filtered_df["Categoria del Producto"].isin(categoria)] if categoria else filtered_df

# Agrupar los datos filtrados por categoría y sumar los ingresos
categoria_df = filtered_df.groupby(by=["Categoria del Producto"], as_index=False)["Ingresos"].sum()
    
def metric_with_style(label, value, background_color="#FFF8DC"):
    st.markdown(
        f"""
        <div style="
            background-color: {background_color};
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #E0E0E0;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            text-align: center;
        ">
            <label style="color: #333; margin-bottom: 5px;">{label}</label>
            <p style="color: #333; font-size: 24px; font-weight: bold; margin: 0;">{value}</p>
        </div>
        """, unsafe_allow_html=True
    )

cola, colb, colc = st.columns((3))
with cola:
# Crear las métricas
    ingresos_totales = filtered_df["Ingresos"].sum()
    st.metric(" Ingresos Totales", f"Bs{ingresos_totales:,.2f}")
with colb:
    # Agrupar por Subcategoría y sumar la cantidad de productos vendidos
    subcategoria_df = filtered_df.groupby("Producto", as_index=False)["Cantidad"].sum()

    # Ordenar de forma descendente para encontrar la subcategoría más vendida
    subcategoria_df = subcategoria_df.sort_values(by="Cantidad", ascending=False)
    subcategoria_mas_vendida = subcategoria_df.iloc[0]
    # Mostrar la métrica personalizada
    metric_with_style(
        f"Producto más Vendido: {subcategoria_mas_vendida['Producto']}",
        f"Unidades: {subcategoria_mas_vendida['Cantidad']}",
        background_color="#FFFACD"  # Fondo amarillo suave
)
with colc:
    costo_total = filtered_df["Costo"].sum()
    st.metric("Costo Total", f"Bs{costo_total:,.2f}")
# Mostrar las métricas
col1, col2, = st.columns((2))
# Gráfico de barras para ingresos por categoría
with col1:
    st.subheader("💹Ingresos por Categoría")
    fig = px.bar(categoria_df, x="Categoria del Producto", y="Ingresos", 
                      text=['Bs{:,.2f}'.format(x) for x in categoria_df["Ingresos"]],
                      template="seaborn")
    ##fig.update_layout(width=400)
    st.plotly_chart(fig, use_container_width=True)
# Gráfico de pastel para ingresos por ciudad
with col2:
    st.subheader("📈Ingresos por Ciudad")
    ciudad_df = filtered_df.groupby(by=["Ciudad"], as_index=False)["Ingresos"].sum()
    fig = px.pie(ciudad_df, values="Ingresos", names="Ciudad", hole=0.5)
    fig.update_traces(text=ciudad_df["Ciudad"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

# Definir columnas para mostrar datos
cl1, cl2 = st.columns((2))
    
# Sección expandible para ver datos por categoría
with cl1:
    with st.expander("Ver Datos por Categoría"):
        st.write(categoria_df.style.background_gradient(cmap="Blues"))
        csv = categoria_df.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar Datos", data=csv, file_name="Categoria.csv", mime="text/csv",
                                help='Haz clic aquí para descargar los datos como un archivo CSV')
    
# Sección expandible para ver datos por ciudad
with cl2:
    with st.expander("Ver Datos por Ciudad"):
        ciudad_df = filtered_df.groupby(by="Ciudad", as_index=False)["Ingresos"].sum()
        st.write(ciudad_df.style.background_gradient(cmap="Oranges"))
        csv = ciudad_df.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar Datos", data=csv, file_name="Ciudad.csv", mime="text/csv", help='Haz clic aquí para descargar los datos como un archivo CSV')

# Crear columna 'month_year' para análisis de series temporales
##filtered_df_year["month_year"] = filtered_df_year["Año"].astype(str) + " " + filtered_df_year["Mes"]

# Crear la columna 'month_year' para análisis de series temporales
filtered_df_year["month_year"] = pd.to_datetime(
    filtered_df_year["Año"].astype(str) + "-" + 
    filtered_df_year["Mes"].apply(lambda x: orden_meses.index(x) + 1).astype(str) + "-01"
)



filtered_df_year = filtered_df_year[filtered_df_year['Año'] == year]

st.subheader('💰 Análisis de Series Temporales')
# Crear un DataFrame para ingresos mensuales
linechart = pd.DataFrame(filtered_df_year.groupby("month_year")["Ingresos"].sum()).reset_index()


# Gráfico de líneas para ingresos mensuales
fig2 = px.line(linechart, x="month_year", y="Ingresos", labels={"Ingresos": "Monto"}, height=500, width=1000, template="gridon")
st.plotly_chart(fig2, use_container_width=True)


# Convertir la columna 'Fecha' a formato datetime

filtered_df["Fecha"] = pd.to_datetime(filtered_df[" Fecha"])

# Filtrar solo las columnas 'Fecha' e 'Ingresos' y hacer una copia
filter_day = filtered_df[["Fecha", "Ingresos"]].copy()
filter_day = filter_day.groupby("Fecha")["Ingresos"].sum().reset_index()
print(filter_day)
fig2 = px.line(filter_day, x="Fecha", y="Ingresos", labels={"Ingresos": "Monto"}, height=500, width=1000, template="gridon")
st.plotly_chart(fig2, use_container_width=True)

# Sección expandible para ver los datos de series temporales
with st.expander("Ver Datos de Series Temporales"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Descargar Datos', data=csv, file_name="TimeSeries.csv", mime='text/csv')
    
# Crear dos columnas para los gráficos de pastel de género y categoría
chart1, chart2 = st.columns((2))

# Gráfico de pastel para ingresos por género
with chart1:
    st.subheader('🏦 Ingresos por Género')
    genero_df = filtered_df.groupby(by=["Genero del Cliente"], as_index=False)["Ingresos"].sum()
    fig = px.pie(genero_df, values="Ingresos", names="Genero del Cliente", template="plotly_dark")
    fig.update_traces(text=genero_df["Genero del Cliente"], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)
    
# Gráfico de pastel para ingresos por categoría
with chart2:
    st.subheader('💳 Ingresos por Categoría')
    fig = px.pie(categoria_df, values="Ingresos", names="Categoria del Producto", template="gridon")
    fig.update_traces(text=categoria_df["Categoria del Producto"], textposition="inside")
    st.plotly_chart(fig, use_container_width=True)

# Mostrar una tabla resumen de muestra de los datos filtrados
st.subheader(":point_right: Muestra de Resumen de Datos")
with st.expander("Tabla Resumen"):
    df_sample = filtered_df[0:5][["Sucursal", "Ciudad", "Categoria del Producto", "Ingresos", "Cantidad"]]
    st.write(filtered_df.style.background_gradient(cmap="cividis"))

# Crear un gráfico de dispersión para Ingresos vs. Costo
data1 = px.scatter(filtered_df, x="Ingresos", y="Costo", size="Cantidad", 
                        hover_name="Producto", color="Categoria del Producto")
data1['layout'].update(title="Relación entre Ingresos y Costo usando Gráfico de Dispersión",
                           titlefont=dict(size=20), xaxis=dict(title="Ingresos", titlefont=dict(size=19)),
                           yaxis=dict(title="Costo", titlefont=dict(size=19)))
st.plotly_chart(data1, use_container_width=True)
    
# Sección expandible para ver los datos filtrados detallados
with st.expander("Ver Datos Detallados"):
    st.write(filtered_df.iloc[:500, :].style.background_gradient(cmap="Oranges"))



 
    
# Gráfico de Treemap para vista jerárquica de ventas
st.subheader("🏷️Vista Jerárquica de Ventas usando TreeMap")
fig3 = px.treemap(filtered_df, path=["Ciudad", "Sucursal", "Categoria del Producto"], values="Ingresos", hover_data=["Ingresos"],
                      color="Categoria del Producto")
fig3.update_layout(width=800, height=650)
st.plotly_chart(fig3, use_container_width=True)

# Descargar el conjunto de datos original
csv = df.to_csv(index=False).encode('utf-8')
st.download_button('Descargar Datos', data=csv, file_name="Data.csv", mime="text/csv")
