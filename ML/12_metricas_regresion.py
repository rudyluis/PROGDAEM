import streamlit as st
from sklearn.metrics import max_error, mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Datos verdaderos y predichos
y_verdadero = [1, 2, 3, 4, 5]
y_predicho = [1, 2, 3, 4, -5]

# Cálculo de métricas
max_err = max_error(y_verdadero, y_predicho)
mae = mean_absolute_error(y_verdadero, y_predicho)
mse = mean_squared_error(y_verdadero, y_predicho)
rmse = np.sqrt(mse)  # Calculamos RMSE a partir del MSE
r2 = r2_score(y_verdadero, [1, 2, 3, 4, 2])

# Título de la página
st.title("Cálculo de Métricas de Error")

# Mostrar las métricas y fórmulas en Streamlit
st.write("### Datos")
st.write("Valores verdaderos:", y_verdadero)
st.write("Valores predichos:", y_predicho)

# Descripción y resultado de cada métrica
st.write("### Métricas de Error")

st.write("#### Error Absoluto Máximo (Max Error)")
st.latex(r"M = \max(|y_{\text{true}} - y_{\text{pred}}|)")
st.write(f"Resultado: {max_err}")

st.write("#### Error Absoluto Medio (MAE)")
st.latex(r"MAE = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{true}} - y_{\text{pred}}|")
st.write(f"Resultado: {mae}")

st.write("#### Error Cuadrático Medio (MSE)")
st.latex(r"MSE = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}} - y_{\text{pred}})^2")
st.write(f"Resultado: {mse}")

st.write("#### Raíz Cuadrada del Error Cuadrático Medio (RMSE)")
st.latex(r"RMSE = \sqrt{MSE}")
st.write(f"Resultado: {rmse}")

st.write("#### Coeficiente de Determinación (R²)")
st.latex(r"R^2 = 1 - \frac{\sum_{i=1}^{n} (y_{\text{true}} - y_{\text{pred}})^2}{\sum_{i=1}^{n} (y_{\text{true}} - \overline{y_{\text{true}}})^2}")
st.write(f"Resultado: {r2}")
