import streamlit as st
import pandas as pd
import plotly.express as px
import os
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("country_comparison_large_dataset_m.csv")

st.set_page_config(page_title="Dashboard Paises", page_icon="📊", layout="wide")
st.title(":money_with_wings: Dashboard Paises")

st.sidebar.header("Seleccione un pais")
selected_country = st.sidebar.multiselect(
    "Seleccione un pais", df["Country"].unique(), default=df["Country"].unique()
)

selected_year = st.sidebar.selectbox ("Seleccione un año", df["Year"].unique())

selected_variable = st.sidebar.selectbox ("Seleccione una variable", df.columns[2:])

### mostrar la informacion del dataframe
df = df[(df['Country'].isin(selected_country)) & (df['Year']>=selected_year)]
if st.checkbox("🥇 Mostrar información del dataframe"):
    with st.expander("Información del dataframe"):
        st.subheader("Información del dataframe")
        st.write(df)
    with st.expander("Descripción del dataframe"):
        st.subheader("Estadísticas generales")
        st.write(df.describe())
col1, col2 = st.columns(2)
with col1:
    st.subheader(":1234: Distribución del PIB")
    st.write("Este gráfico muestra la distribución del Producto Interno Bruto (PIB) en trillones de USD entre los países.")
    fig_gdp = px.histogram(df, x=selected_variable, nbins=30, 
                           title='Distribución del PIB', 
                           color_discrete_sequence=["blue","red"])
  
    st.plotly_chart(fig_gdp)
    
with col2:
    st.subheader("Distribucion del PIB per Capita")
    fig_gdp_per_capita= px.box(df, x='Country', y=selected_variable, title=f"Distribución del PIB per Capita {selected_variable}", color="Country", hover_name="Country")
    st.plotly_chart(fig_gdp_per_capita)

with st.expander("Histograma de Indicadores economicos"):
    st.subheader("Histograma de Indicadores economicos")
    fig_economic_indicators = px.bar(df, x="Country", y=selected_variable, color="Country", 
        hover_name="Country", barmode="overlay", title=f"Histograma de Indicadores economicos {selected_variable}")
    st.plotly_chart(fig_economic_indicators)

st.subheader(f"{selected_variable} vs. Esperanza de vida")
fig_scatter = px.scatter(df,x=selected_variable, y="Life Expectancy (Years)", color="Country", hover_name="Country",
    color_discrete_sequence=px.colors.qualitative.Dark24)

st.plotly_chart(fig_scatter)

st.subheader("Crecimiento del PIB a lo largo del tiempo")
fig_line = px.line(df, x="Year", y=selected_variable, color="Country", hover_name="Country",
 title=f"Crecimiento del PIB a lo largo del tiempo {selected_variable}")
st.plotly_chart(fig_line)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
# Generar WordCloud de países basados en el número de aeropuertos
st.subheader(f"Nube de Palabras de Países según {selected_variable}")
country_airports = dict(zip(df['Country'], df[selected_variable]))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(country_airports)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)
#########
st.subheader(f"Grafico Pie de países  {selected_variable}")
fig_pie= px.pie(df, values=selected_variable, names="Country", 
title=f"Distribución de {selected_variable}", hole=0.4)

# Agregar personalización
fig_pie.update_traces(
    textinfo="percent+label",  # Mostrar porcentaje y nombre del país
    pull=[0.05] * len(df),  # Separar todas las porciones un poco
    marker=dict(line=dict(color="#000000", width=1))  # Bordes negros para mayor contraste
)

fig_pie.update_layout(
    title_font_size=20,
    title_x=0.5,  # Centrar título
    showlegend=True, 
    legend_title="Países",
    height=500, width=600,
    paper_bgcolor="rgba(0,0,0,0)",  # Fondo transparente
)

st.plotly_chart(fig_pie)


  
st.subheader("Analisis de Variables con respecto al Pais")
selected_variabley = st.selectbox("Seleccione una variable para realizar la comparación", 
                                         df.columns[2:])
with st.expander('Datos Agrupados por Pais'):
    df_grouped = df.groupby('Country').mean().reset_index()
    st.write(df_grouped)
# Primera Forma
df_grouped[[selected_variable, selected_variabley]].plot(kind='bar', stacked=True, figsize=(15, 8))
##plt.title('Cuota de Energía Renovable y Terreno Agrícola por País')
plt.xlabel(selected_variable)
plt.ylabel(selected_variabley)
plt.xticks(rotation=45)
st.pyplot(plt)


#Segunda Forma
fig = px.bar(
    df_grouped,
    x='Country',
    y= [selected_variable, selected_variabley],
       
    title=f'{selected_variable} y {selected_variabley} por País',
       ## barmode='stack',  # Esto apila las barras
    color_discrete_sequence=px.colors.qualitative.Set1  # Cambiar la paleta de colores si se desea
)
st.plotly_chart(fig)
