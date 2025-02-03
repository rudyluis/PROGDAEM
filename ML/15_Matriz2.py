import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo con variables categóricas
data = {
    'Color': np.random.choice(['Rojo', 'Azul', 'Verde'], 100),
    'Forma': np.random.choice(['Círculo', 'Cuadrado', 'Triángulo'], 100),
    'Tamaño': np.random.choice(['Grande', 'Mediano', 'Pequeño'], 100)
}
df = pd.DataFrame(data)

# Función para calcular V de Cramer
def cramers_v(x, y):
    contingency_table = pd.crosstab(x, y)
    chi2 = chi2_contingency(contingency_table)[0]
    n = contingency_table.sum().sum()
    r, k = contingency_table.shape
    return np.sqrt(chi2 / (n * (min(r, k) - 1)))

# Cálculo de matriz de correlación para variables categóricas usando V de Cramer
categorical_columns = df.columns
corr_matrix = pd.DataFrame(index=categorical_columns, columns=categorical_columns)

for col1 in categorical_columns:
    for col2 in categorical_columns:
        corr_matrix.loc[col1, col2] = cramers_v(df[col1], df[col2])

# Visualización
st.title("Matriz de Correlación para Variables Categóricas (V de Cramer)")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix.astype(float), annot=True, cmap='coolwarm', center=0)
st.pyplot(fig)
