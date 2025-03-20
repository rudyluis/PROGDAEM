import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import plotly.express as px

# Configurar layout de página a 'wide'
st.set_page_config(layout="wide")

# Cargar datos
df = pd.read_csv('country_comparison_large_dataset.csv')

# Título de la app
st.title("Análisis Exploratorio de Datos (EDA) con Visualizaciones")

# Sidebar para seleccionar el país
st.sidebar.header("Filtros")
selected_country = st.sidebar.multiselect("Selecciona el/los país(es)", 
                                           df['Country'].unique(), 
                                           default=df['Country'].unique())

# Filtrar el DataFrame por los países seleccionados
df_filtered = df[df['Country'].isin(selected_country)]

# Mostrar información del DataFrame
if st.checkbox("Mostrar información del dataset"):
    with st.expander("Estadísticas Descriptivas"):
        st.subheader("Estadísticas Descriptivas")
        st.write(df_filtered.describe())
    with st.expander("Datos Originales"):
        st.subheader("Datos Originales del Dataset")
        st.dataframe(df_filtered)

# Análisis Univariante
st.subheader("Análisis Univariante")
selected_univariate_variable = st.selectbox("Selecciona una variable para el análisis univariante", 
                                             ['GDP (in Trillions USD)', 
                                              'GDP per Capita (in USD)', 
                                              'Life Expectancy (Years)', 
                                              'Internet Penetration (%)',
                                              'CO2 Emissions (Million Metric Tons)',
                                              'Population Growth Rate (%)'])

# Histograma para la variable seleccionada
st.write(f"Distribución de la variable: {selected_univariate_variable}")
# Crear la figura con un tamaño reducido (70% del tamaño original)
fig, ax = plt.subplots()
##fig.set_size_inches(5 * 0.5, 5* 0.5)  # El tamaño original es 7x5 pulgadas, lo reducimos un 30%

sns.histplot(df_filtered[selected_univariate_variable], bins=20, kde=True, ax=ax)
ax.set_title(f"Distribución de {selected_univariate_variable}")
st.pyplot(fig)




# Análisis Bivariante
st.subheader("Análisis Bivariante")
col1, col2 = st.columns(2)

# Selección de variables para el análisis bivariante
with col1:
    selected_bivariate_x = st.selectbox("Selecciona la variable en el eje X", 
                                         ['GDP (in Trillions USD)', 
                                          'GDP per Capita (in USD)', 
                                          'Life Expectancy (Years)', 
                                          'Internet Penetration (%)',
                                          'CO2 Emissions (Million Metric Tons)',
                                          'Population Growth Rate (%)'])
    
with col2:
    selected_bivariate_y = st.selectbox("Selecciona la variable en el eje Y", 
                                         ['GDP (in Trillions USD)', 
                                          'GDP per Capita (in USD)', 
                                          'Life Expectancy (Years)', 
                                          'Internet Penetration (%)',
                                          'CO2 Emissions (Million Metric Tons)',
                                          'Population Growth Rate (%)'])

# Gráfico de dispersión para las variables seleccionadas
##st.write(f"Relación entre {selected_bivariate_x} y {selected_bivariate_y}")
##fig_bivar, ax_bivar = plt.subplots()
##sns.scatterplot(x=selected_bivariate_x, y=selected_bivariate_y, data=df_filtered, hue='Country', ax=ax_bivar)
##ax_bivar.set_title(f"{selected_bivariate_x} vs {selected_bivariate_y}")
##st.pyplot(fig_bivar)

# Gráfico de dispersión para las variables seleccionadas usando Plotly Express
st.write(f"Relación entre {selected_bivariate_x} y {selected_bivariate_y}")

# Crear el gráfico de dispersión
fig_bivar = px.scatter(df_filtered, 
                       x=selected_bivariate_x, 
                       y=selected_bivariate_y, 
                       color='Country',  # Color según el país
                       title=f"{selected_bivariate_x} vs {selected_bivariate_y}",
                       labels={selected_bivariate_x: selected_bivariate_x, 
                               selected_bivariate_y: selected_bivariate_y})  # Etiquetas para ejes

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_bivar)



# Gráfico de regresión lineal para el análisis bivariante

#### ocn regresion lineal
import numpy as np
import statsmodels.api as sm

# Calcular la regresión lineal
X = df_filtered[selected_bivariate_x]
y = df_filtered[selected_bivariate_y]

# Añadir una constante (intercepto)
X = sm.add_constant(X)

# Crear el modelo
model = sm.OLS(y, X).fit()

# Obtener las predicciones
df_filtered['predicted'] = model.predict(X)

# Gráfico de dispersión y línea de regresión usando Plotly Express
st.write("Gráfico de Regresión Lineal")
fig_reg = px.scatter(df_filtered, 
                     x=selected_bivariate_x, 
                     y=selected_bivariate_y, 
                     color='Country', 
                     title=f"Regresión Lineal: {selected_bivariate_x} vs {selected_bivariate_y}",
                     labels={selected_bivariate_x: selected_bivariate_x, 
                             selected_bivariate_y: selected_bivariate_y})  # Etiquetas para los ejes

# Añadir la línea de regresión
fig_reg.add_scatter(x=df_filtered[selected_bivariate_x], 
                    y=df_filtered['predicted'], 
                    mode='lines', 
                    name='Línea de Regresión', 
                    line=dict(color='red', width=2))

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_reg)


# Gráfico de cajas (Boxplot) para las variables seleccionadas
st.write("Boxplot para las variables seleccionadas")
fig_box = px.box(df_filtered, 
                 x=selected_bivariate_x, 
                 y=selected_bivariate_y, 
                 title=f"Boxplot de {selected_bivariate_x} vs {selected_bivariate_y}",
                 labels={selected_bivariate_x: selected_bivariate_x, 
                         selected_bivariate_y: selected_bivariate_y})  # Etiquetas para los ejes

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_box)

# Matriz de Correlación
st.subheader("Matriz de Correlación")
corr_matrix = df_filtered[['GDP (in Trillions USD)', 
                           'GDP per Capita (in USD)', 
                           'Life Expectancy (Years)', 
                           'Internet Penetration (%)',
                           'CO2 Emissions (Million Metric Tons)',
                           'Population Growth Rate (%)']].corr()

# Mostrar la matriz de correlación
st.write("Matriz de correlación entre variables seleccionadas:")
st.dataframe(corr_matrix)

# Heatmap de la matriz de correlación
fig_corr, ax_corr = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax_corr)
ax_corr.set_title('Heatmap de Matriz de Correlación')
st.pyplot(fig_corr)

# Análisis Multivariante (PCA)
st.subheader("Análisis Multivariante: Análisis de Componentes Principales (PCA)")

# Normalizar las variables seleccionadas
variables_pca = ['GDP (in Trillions USD)', 
                 'GDP per Capita (in USD)', 
                 'Life Expectancy (Years)', 
                 'Internet Penetration (%)',
                 'CO2 Emissions (Million Metric Tons)',
                 'Population Growth Rate (%)']

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_filtered[variables_pca])

# Aplicar PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_scaled)

# Convertir resultado a DataFrame
df_pca = pd.DataFrame(data=pca_result, columns=['Componente 1', 'Componente 2'])
df_pca['Country'] = df_filtered['Country'].values

# Gráfico PCA usando Plotly Express
st.write("Análisis de Componentes Principales (PCA)")
fig_pca = px.scatter(df_pca, 
                     x='Componente 1', 
                     y='Componente 2', 
                     color='Country', 
                    ## title='Análisis de Componentes Principales (PCA)',
                     labels={'Componente 1': 'Componente 1', 'Componente 2': 'Componente 2'})

st.plotly_chart(fig_pca)

# Mostrar la varianza explicada por los componentes principales
explained_variance = pca.explained_variance_ratio_
st.write(f"Varianza explicada por el componente 1: {explained_variance[0]:.2f}")
st.write(f"Varianza explicada por el componente 2: {explained_variance[1]:.2f}")
