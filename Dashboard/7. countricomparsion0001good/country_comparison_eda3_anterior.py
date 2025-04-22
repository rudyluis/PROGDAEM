import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns  # Asegúrate de tener Seaborn importado
# Configurar layout a 'wide'
st.set_page_config(layout="wide")
# Cargar datos
df = pd.read_csv('country_comparison_large_dataset.csv')
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
                                          ['GDP (in Trillions USD)', 
                                           'GDP per Capita (in USD)', 
                                           'CO2 Emissions (Million Metric Tons)', 
                                           'Military Expenditure (in Billion USD)', 
                                           'Renewable Energy Share (%)'])

# Mostrar información del DataFrame
df = df[df['Country'].isin(selected_country)]
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
    fig_gdp = px.histogram(df, x='GDP (in Trillions USD)', nbins=30, 
                           title='Distribución del PIB', 
                           color_discrete_sequence=["blue"])
    st.plotly_chart(fig_gdp)

with col2:
    st.subheader("	:white_check_mark:  Distribución del PIB per Cápita")
    st.write("Este gráfico representa la distribución del PIB per cápita en USD entre los países.")
    fig_gdp_per_capita = px.box(df, x='GDP per Capita (in USD)', 
                                 title='Distribución del PIB per Cápita', 
                                 color_discrete_sequence=["orange"])
    st.plotly_chart(fig_gdp_per_capita)

# Sección para histogramas de indicadores económicos
with st.expander(" 💯 Ver histogramas de indicadores económicos"):
    st.subheader("Histogramas de Indicadores Económicos")
    for var in ['Inflation Rate (%)', 'Population Growth Rate (%)', 'Unemployment Rate (%)']:
        fig_hist = px.histogram(df, x=var, nbins=20, 
                                 title=f'Histograma de {var}', 
                                 color_discrete_sequence=["green"])
        st.plotly_chart(fig_hist)

# Gráfico de dispersión de PIB per Cápita vs Esperanza de Vida
st.subheader(":sparkles: PIB per Cápita vs Esperanza de Vida")
fig_scatter_gdp_life_expectancy = px.scatter(df, x='GDP per Capita (in USD)', 
                                              y='Life Expectancy (Years)',
                                              title='PIB per Cápita vs Esperanza de Vida', 
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

# Gráfico de barras para el gasto militar por país
st.subheader(":book: Gasto Militar por País")
if selected_country:
    filtered_df = df[df['Country'].isin(selected_country)]
else:
    filtered_df = df

fig_military_expenditure = px.bar(filtered_df, x='Country', 
                                   y='Military Expenditure (in Billion USD)', 
                                   title='Gasto Militar por País', 
                                   color='Country', 
                                   color_discrete_sequence=px.colors.qualitative.Dark2)
st.plotly_chart(fig_military_expenditure)

# Gráfico de violín para la cuota de energía renovable
st.subheader("	:pencil: Cuota de Energía Renovable por País")
fig_renewable_energy = px.violin(filtered_df, x='Country', 
                                  y='Renewable Energy Share (%)', 
                                  title='Cuota de Energía Renovable por País', 
                                  color='Country', 
                                  color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig_renewable_energy)

# Generar WordCloud de países basados en el número de aeropuertos
st.subheader("🌧️ Nube de Palabras de Países según Número de Aeropuertos")
country_airports = dict(zip(df['Country'], df['Number of Airports']))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(country_airports)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

# Gráfico de barras para la Penetración de Internet por País usando Streamlit
st.subheader("💻 Penetración de Internet por País")
# Agrupar los datos para obtener la media si es necesario
internet_data = df.groupby('Country')['Internet Penetration (%)'].mean().reset_index()
st.bar_chart(internet_data.set_index('Country')['Internet Penetration (%)'])



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
st.subheader("🚈 Cuota de Energía Renovable y Terreno Agrícola por País")
df_grouped = df.groupby('Country').mean()

# Asegúrate de que 'Agricultural Land (%)' está en el DataFrame
if 'Agricultural Land (%)' in df_grouped.columns:
    df_grouped[['Renewable Energy Share (%)', 'Agricultural Land (%)']].plot(kind='bar', stacked=True, figsize=(15, 8))
    plt.title('Cuota de Energía Renovable y Terreno Agrícola por País')
    plt.xlabel('País')
    plt.ylabel('Porcentaje')
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write("La columna 'Agricultural Land (%)' no está presente en el dataset.")


# Gráfico de barras para la Penetración de Internet por País (añadido al final)
#3st.subheader("Penetración de Internet por País")
##plt.figure(figsize=(12, 8))
##sns.barplot(x='Country', y='Internet Penetration (%)', data=df)
#3plt.xticks(rotation=90)
##plt.title('Penetración de Internet por País')
##st.pyplot(plt)

# Gráfico de barras para la Penetración de Internet por País

# Supongamos que 'df' es tu DataFrame que ya contiene los datos
columnas = df.columns.tolist()

# Combos para seleccionar las variables
st.sidebar.header("	🚟 Selecciona las variables para el boxplot")
x_variable = st.sidebar.selectbox("Selecciona la variable para el eje X", columnas)
y_variable = st.sidebar.selectbox("Selecciona la variable para el eje Y", columnas)

# Asegúrate de que las variables seleccionadas son adecuadas
if x_variable and y_variable:
    # Crear el gráfico de cajas
    fig = px.box(df, 
                  x=x_variable,
                  y=y_variable,
                  title=f"Boxplot de {y_variable} por {x_variable}")

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)
else:
    st.write("Por favor, selecciona ambas variables.")



