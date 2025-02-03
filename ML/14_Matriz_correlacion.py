import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Título y descripción de la app
st.title("Visualización de la Matriz de Correlación con Gráfica de Dispersión")
st.markdown("""
Esta aplicación muestra cómo visualizar y analizar la matriz de correlación entre variables.
Usaremos el conjunto de datos de Iris como ejemplo.
""")

# Cargar y mostrar datos
iris_data = load_iris(as_frame=True)
df = iris_data.frame

# Mostrar los datos
with st.expander("Ver Datos de Ejemplo"):
    st.write(df)

# Cálculo de la matriz de correlación
correlation_matrix = df.corr()

# Visualización de la matriz de correlación
st.header("Matriz de Correlación")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=ax,
            xticklabels=correlation_matrix.columns, yticklabels=correlation_matrix.columns)
plt.title("Matriz de Correlación de Variables en el Conjunto de Datos Iris")
st.pyplot(fig)

# Selección de variables para gráfica de dispersión
st.header("Análisis de Relación entre Variables")
st.markdown("Selecciona dos variables para visualizar su relación en una gráfica de dispersión.")

# Crear selectboxes para elegir variables
col1, col2 = st.columns(2)
with col1:
    variable_x = st.selectbox("Variable en el Eje X", options=df.columns)
with col2:
    variable_y = st.selectbox("Variable en el Eje Y", options=df.columns)

# Generar gráfico de dispersión entre las variables seleccionadas
st.subheader(f"Gráfica de Dispersión entre {variable_x} y {variable_y}")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x=variable_x, y=variable_y, hue="target", palette="viridis", s=60, ax=ax)
ax.set_title(f"Dispersión de {variable_x} vs {variable_y}")
st.pyplot(fig)

# Interpretación
st.markdown("""
### Interpretación de la Matriz de Correlación
- Los valores altos positivos o negativos (cercanos a 1 o -1) indican una fuerte correlación entre las variables.
- En este ejemplo, podemos observar que:
  - **Longitud y Anchura del Sépalo** están moderadamente correlacionadas.
  - **Longitud del Pétalo y Longitud del Sépalo** tienen una correlación fuerte.
  
Estas correlaciones ayudan a identificar las relaciones entre variables y a decidir si algunas pueden ser redundantes para un análisis o modelo.
""")
