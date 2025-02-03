import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from st_aggrid import AgGrid
import plotly.express as px
import calendar

# Conexión a la base de datos
DB_URL = "mysql+pymysql://root:2004@127.0.0.1:3306/veterinariaDatos"

engine = create_engine(DB_URL)

# Configuración de la página
st.set_page_config(page_title="My Vet",
                   layout="wide", page_icon=":paw_prints:")


st.markdown(
    "<h1 style='text-align: center;'>🐾🐾 Dashboard My Vet 🐾🐾</h1>",
    unsafe_allow_html=True,
)

st.markdown("---")

# Carga de datos generales
with engine.connect() as conn:
    query_general = text("""
    SELECT 
        p.id_paciente,
        p.nombre AS paciente_nombre,
        p.especie,
        p.raza,
        CONCAT(a.nombre, ' ', a.apellido) AS apoderado,
        COUNT(DISTINCT vis.id_visita) AS total_visitas,
        COALESCE(SUM(tp.monto), 0) AS total_gastado,
        GROUP_CONCAT(DISTINCT ep.estado_padecimientos SEPARATOR ', ') AS estado_pacientes
    FROM 
        paciente p
    LEFT JOIN 
        visita vis ON p.id_paciente = vis.id_paciente
    LEFT JOIN 
        tipopago tp ON vis.id_visita = tp.id_visita
    LEFT JOIN 
        padecimientos pa ON p.id_paciente = pa.id_padecimientos
    LEFT JOIN 
        estado_padecimientos ep ON pa.id_estado_padecimientos = ep.id_estado_padecimientos
    LEFT JOIN apoderado a ON p.id_apoderado = a.id_apoderado                     
    GROUP BY 
        p.id_paciente, p.nombre, p.especie, p.raza
    ORDER BY 
        total_visitas DESC;
    """)
    result = conn.execute(query_general)
    df = pd.DataFrame(result.fetchall(), columns=result.keys())


# Consulta y filtros dinámicos
with engine.connect() as conn:
    query_visitas = text("""
SELECT
    CONCAT(v.nombre, ' ', v.apellido) AS veterinario,
    p.nombre AS paciente,
    p.especie,
    p.raza,
    CONCAT(a.nombre, ' ', a.apellido) AS apoderado,
    dir.zona AS zona_vivienda,
    YEAR(vis.fecha) AS anio, -- Año de la visita
    DATE_FORMAT(vis.fecha, '%M') AS mes,
    vis.motivo,
    tp.monto AS total_pago,
    tc.tipo_consulta AS tipo_consulta
FROM
    visita vis
INNER JOIN veterinario v ON vis.id_veterinario = v.id_veterinario
INNER JOIN paciente p ON vis.id_paciente = p.id_paciente
LEFT JOIN tipopago tp ON vis.id_visita = tp.id_visita
LEFT JOIN deriva d ON vis.id_visita = d.id_visita
LEFT JOIN tipoconsulta tc ON d.id_tipo_consulta = tc.id_tipo_consulta
LEFT JOIN apoderado a ON p.id_apoderado = a.id_apoderado
LEFT JOIN direccion dir ON a.id_direccion = dir.id_direccion
;
    """)
    result_visitas = conn.execute(query_visitas)
    df_vis = pd.DataFrame(result_visitas.fetchall(),
                          columns=result_visitas.keys())


# Obtener los nombres de los meses en el orden correcto
# ["January", "February", ..., "December"]
month_order = list(calendar.month_name[1:])

# Asegurarnos de que los valores de 'mes' estén en el orden correcto


# Filtros dinámicos
years = sorted(df_vis['anio'].unique())
months = sorted(df_vis['mes'].unique(), key=month_order.index)


# Selectores de año y mes
col1, col2 = st.columns(2)
with col1:
    year = st.selectbox("Seleccione el año", years)
with col2:
    month = st.selectbox("Seleccione el mes", months)

# Consulta filtrada por año y mes
with engine.connect() as conn:
    query_filtered = text("""
SELECT
    CONCAT(v.nombre, ' ', v.apellido) AS veterinario,
    p.nombre AS paciente,
    p.especie,
    p.raza,
    CONCAT(a.nombre, ' ', a.apellido) AS apoderado,
    YEAR(vis.fecha) AS anio, -- Año de la visita
    DATE_FORMAT(vis.fecha, '%M') AS mes,
    vis.motivo,
    tp.monto AS total_pago,
    tc.tipo_consulta AS tipo_consulta
FROM
    visita vis
INNER JOIN veterinario v ON vis.id_veterinario = v.id_veterinario
INNER JOIN paciente p ON vis.id_paciente = p.id_paciente
LEFT JOIN tipopago tp ON vis.id_visita = tp.id_visita
LEFT JOIN deriva d ON vis.id_visita = d.id_visita
LEFT JOIN tipoconsulta tc ON d.id_tipo_consulta = tc.id_tipo_consulta
LEFT JOIN apoderado a ON p.id_apoderado = a.id_apoderado
WHERE
    YEAR(vis.fecha) = :anio AND MONTH(vis.fecha) = :mes;

    """)
    filter_df = pd.read_sql(query_filtered, conn, params={
                            "anio": year, "mes": months.index(month) + 1})


# filtros secundarios
st.sidebar.header("Escoja una opcion")
veterinario_filter = st.sidebar.multiselect(
    "Seleccione el veterinario 🩺", filter_df["veterinario"].unique())
if veterinario_filter:
    filter_df = filter_df[filter_df["veterinario"].isin(veterinario_filter)]
    df_vis = df_vis[df_vis["veterinario"].isin(veterinario_filter)]
especie_filter = st.sidebar.multiselect(
    "Seleccione la especie 🐾", filter_df["especie"].unique())
if especie_filter:
    filter_df = filter_df[filter_df["especie"].isin(especie_filter)]
    df_vis = df_vis[df_vis["especie"].isin(especie_filter)]

raza_filter = st.sidebar.multiselect(
    "Seleccione la raza 📋", filter_df["raza"].unique())

if raza_filter:
    filter_df = filter_df[filter_df["raza"].isin(raza_filter)]
    df_vis = df_vis[df_vis["raza"].isin(raza_filter)]

tipo_consulta_filter = st.sidebar.multiselect(
    "Seleccione el tipo de consulta 💉", filter_df["tipo_consulta"].unique())
if tipo_consulta_filter:
    filter_df = filter_df[filter_df["tipo_consulta"].isin(
        tipo_consulta_filter)]
    df_vis = df_vis[df_vis["tipo_consulta"].isin(tipo_consulta_filter)]

with st.expander("📋 Datos Generales"):
    AgGrid(df)

with st.expander("🔍 Datos Filtrados por Gestión y Mes"):
    AgGrid(filter_df)
st.markdown("---")

col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
    total_gastado = filter_df["total_pago"].sum()
    st.metric("Total Gastado", f"Bs.{total_gastado:,.2f}")
    st.write("Total Gastado")

with col_b:
    total_visitas = filter_df["paciente"].count()
    st.metric("Total Visitas", f"{total_visitas}")
    st.write("Total Visitas")

with col_c:
    total_pacientes = filter_df["paciente"].nunique()
    st.metric("Total Pacientes", f"{total_pacientes}")
    st.write("Total Pacientes")


with col_d:
    especie_mas_frecuente = filter_df["especie"].mode().values[0]
    cantidad_especie = filter_df["especie"].value_counts().max()
    
    st.metric(label="Especie más frecuente", value=f"{especie_mas_frecuente} ({cantidad_especie})")



# grafico visitas por mes
df_vis['mes'] = pd.Categorical(
    df_vis['mes'], categories=month_order, ordered=True)

graf = df_vis.groupby("mes")["paciente"].count(
).reset_index().sort_values(by="mes")

st.subheader("Gráfico de visitas por mes")


fig = px.line(
    graf,
    x="mes",
    y="paciente",
    template="seaborn",
    color_discrete_sequence=["#00f49d"],
    markers=True
)
st.plotly_chart(fig, use_container_width=True)

# distribucion de visitas por especie(grafico de pie)
graf = filter_df.groupby("especie")["paciente"].count(
).reset_index().sort_values(by="paciente", ascending=False)
st.subheader("Distribucion de visitas por especie")
fig = px.pie(graf, values="paciente", names="especie",
             template="seaborn", hole=0.5)
st.plotly_chart(fig, use_container_width=True)

# grafico de visitas por tipo de consulta
graf = filter_df.groupby("tipo_consulta")["paciente"].count(
).reset_index().sort_values(by="paciente", ascending=False)
st.subheader("Grafico de visitas por tipo de consulta")
fig = px.bar(graf, x="tipo_consulta", y="paciente",
             template="seaborn", color="tipo_consulta")
st.plotly_chart(fig, use_container_width=True)

# grafico de visitas por zona
graf = df_vis.groupby("zona_vivienda")["paciente"].count(
).reset_index().sort_values(by="paciente", ascending=False)
st.subheader("Grafico de visitas por zona")
fig = px.bar(graf, x="zona_vivienda", y="paciente",
             template="seaborn", color="zona_vivienda")

st.plotly_chart(fig, use_container_width=True)

# distribucion de estado de lod pacientes
graf = df.groupby("estado_pacientes")["id_paciente"].count(
).reset_index().sort_values(by="id_paciente", ascending=False)
st.subheader("Distribucion de estado de los pacientes 2024")
fig = px.pie(graf, values="id_paciente", names="estado_pacientes",
             template="seaborn", hole=0.5)

st.plotly_chart(fig, use_container_width=True)

# grafico de radar motivo de las visitas
graf = df_vis.groupby("motivo")["paciente"].count(
).reset_index().sort_values(by="paciente", ascending=False)
st.subheader("Grafico de motivo de las visitas")
fig = px.bar_polar(graf, r="paciente", theta="motivo",
                   template="seaborn", color="motivo")

st.plotly_chart(fig, use_container_width=True)
