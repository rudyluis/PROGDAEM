import streamlit as  st
import pandas as pd

st.title('Analisis de Datos')

uploaded_file=st.file_uploader('Subir Archivo CSV', type=['csv'])

if(uploaded_file is not None):
    df= pd.read_csv(uploaded_file, encoding='latin-1', delimiter=',')
    st.subheader('Primeras Filas del Dataset')
    st.dataframe(df.head())
    
    st.subheader('Resumen Estadistico')
    st.write(df.describe())
    
    st.subheader('Nombres de las Columnas')
    st.write(df.columns)
    
    st.subheader('Tipos de Datos')
    st.write(df.dtypes)
    
    st.subheader("Tamaño del Dataset")
    st.write(df.shape)
    
    st.subheader("Valores Nulos en el DataSet")
    st.write(df.isnull().sum())
    
    st.subheader("Filas duplicadas")
    st.write(df.duplicated().sum())
    
    
else: 
    st.write('Por favor, sube un archivo CSV')
