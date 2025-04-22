import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns  # Asegúrate de tener Seaborn importado
import altair as alt
# Configurar layout a 'wide'
st.set_page_config(layout="wide")
# Cargar datos
df = pd.read_csv('country_comparison_large_dataset_m.csv')
# Título
st.title("	:money_with_wings: Análisis Exploratorio de Datos por País")

# Sidebar para seleccionar país y variable
st.sidebar.header(":capital_abcd: Filtros")
# Seleccionar todos los países por defecto
selected_country = st.sidebar.multiselect("Selecciona el/los país(es)", 
                                           df['Country'].unique(), 
                                           default=df['Country'].unique())
selected_year = st.sidebar.selectbox("Selecciona un año", df['Year'].unique())
selected_variable = st.sidebar.selectbox("Selecciona una variable para las gráficas", 
                                         df.columns[2:])

# Mostrar información del DataFrame
df = df[(df['Country'].isin(selected_country)) & (df['Year']>=selected_year)]
if st.checkbox("	🥇 Mostrar información del dataset"):
    
    with st.expander("Estadísticas Descriptivas del Dataset"):
        st.subheader("Estadísticas Descriptivas del Dataset")
        st.write(df.describe())
    with st.expander("Datos Originales del Dataset"):
        st.subheader("Datos Originales del Dataset")
        st.dataframe(df)

# Gráfico de distribución de GDP y PIB per Cápita en columnas
col1, col2 = st.columns(2)

with col1:
    st.subheader(":1234: Distribución del PIB")
    st.write("Este gráfico muestra la distribución del Producto Interno Bruto (PIB) en trillones de USD entre los países.")
    fig_gdp = px.histogram(df, x=selected_variable, nbins=30, 
                           title='Distribución del PIB', 
                           color_discrete_sequence=["blue","red"])
  
    st.plotly_chart(fig_gdp)

with col2:
    st.subheader("	:white_check_mark:  Distribución del PIB per Cápita")
    st.write(f"Este gráfico representa la distribución {selected_variable} en USD entre los países.")
    fig_gdp_per_capita = px.box(df, x='Country', y=selected_variable ,
                                 title=f'Distribución del {selected_variable}', 
                                 color= 'Country'
                                )
    st.plotly_chart(fig_gdp_per_capita)

# Sección para histogramas de indicadores económicos
with st.expander(" 💯 Ver histogramas de indicadores económicos"):
    st.subheader("Histogramas de Indicadores Económicos")
    fig_gdp2 = px.bar(df, x="Country", y=selected_variable, color="Country", barmode="overlay",  ##stacl,overlay, relative 
                       title=f'Barras  de  Pais vs {selected_variable}')
    st.plotly_chart(fig_gdp2)
    fig_hist = px.histogram(df, x=selected_variable, nbins=20, 
                                 title=f'Histograma de {selected_variable}', 
                                 color_discrete_sequence=["green"])
    st.plotly_chart(fig_hist)


# Gráfico de dispersión de PIB per Cápita vs Esperanza de Vida
st.subheader(f":sparkles: {selected_variable} vs Esperanza de Vida")
fig_scatter_gdp_life_expectancy = px.scatter(df, x=selected_variable, 
                                              y='Life Expectancy (Years)',
                                              title=f'{selected_variable} vs Esperanza de Vida', 
                                              color='Country', 
                                              color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig_scatter_gdp_life_expectancy)

# Gráfico de líneas de PIB a lo largo del tiempo
st.subheader("	:anchor: Crecimiento del PIB a lo largo del tiempo")
fig_gdp_growth = px.line(df, x='Year', y='GDP (in Trillions USD)', 
                          color='Country', 
                          title='Crecimiento del PIB a lo largo del tiempo', 
                          color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig_gdp_growth)


# Gráfico de violín por pais
st.subheader(f":pencil: Cuota de {selected_variable} por País")
fig_renewable_energy = px.violin(df, x='Country', 
                                  y=selected_variable, 
                                  title=f'{selected_variable} por País', 
                                  color='Country', 
                                  color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig_renewable_energy)

# Generar WordCloud de países basados en el número de aeropuertos
st.subheader(f"🌧️ Nube de Palabras de Países según {selected_variable}")
country_airports = dict(zip(df['Country'], df[selected_variable]))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(country_airports)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)
#########
# Gráfico de barras para la Penetración de Internet por País usando Streamlit
st.subheader("💻 Penetración de Internet por País")
# Agrupar los datos para obtener la media si es necesario
internet_data = df.groupby('Country')['Internet Penetration (%)'].mean().reset_index()
st.bar_chart(internet_data.set_index('Country')['Internet Penetration (%)'])
st.subheader(f"💻 Grafico de Barras {selected_variable} por País")
internet_data = df.groupby('Country')[selected_variable].mean().reset_index()
st.bar_chart(internet_data.set_index('Country')[selected_variable])

# Gráfico de CO2 Emisiones a lo largo del tiempo para países específicos
st.subheader("🗺️ Emisiones de CO2 a lo largo del tiempo")
if selected_country:
    df_filtered = df[(df['Country'].isin(selected_country)) & (df['Year'] >= selected_year)]
    fig_co2_emissions = px.line(df_filtered, x='Year', 
                                 y='CO2 Emissions (Million Metric Tons)', 
                                 color='Country', 
                                 title='Emisiones de CO2 a lo largo del tiempo para países seleccionados',
                                 color_discrete_sequence=px.colors.qualitative.Plotly)
    st.plotly_chart(fig_co2_emissions)
else:
    st.write("Selecciona al menos un país para visualizar las emisiones de CO2.")

# Gráfico de barras apiladas para Renewable Energy Share y Agricultural Land por País

st.subheader("🚈 Analisis de Variables con respecto al Pais")
selected_variabley = st.selectbox("Seleccione una variable para realizar la comparación", 
                                         df.columns[2:])
with st.expander('Datos Agrupados por Pais'):
    df_grouped = df.groupby('Country').mean().reset_index()
    st.write(df_grouped)
# Primera Forma
df_grouped[[selected_variable, selected_variabley]].plot(kind='bar', stacked=True, figsize=(15, 8))
plt.title('Cuota de Energía Renovable y Terreno Agrícola por País')
plt.xlabel('País')
plt.ylabel('Porcentaje')
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




st.write('https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/')
