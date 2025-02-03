import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt


# Función para detectar valores atípicos usando el rango intercuartil (IQR)
def eliminar_valores_atipicos(df, column):
    # Calcular el cuartil 1 (Q1) y cuartil 3 (Q3)
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    # Definir límites para detectar los outliers
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    
    # Filtrar los datos que están dentro de los límites
    df_sin_atipicos = df[(df[column] >= lower_limit) & (df[column] <= upper_limit)]
    
    return df_sin_atipicos

# Cargar los datos desde un archivo Excel
data = pd.read_excel('df/copia.xlsx')

# Crear el DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame en Streamlit
st.write("Datos Originales")
st.write(df)

# Convertir la columna 'año_mes' a formato de fecha para facilitar la manipulación


# Filtrar el DataFrame por los valores seleccionados por el usuario
st.sidebar.header("Filtrar datos")
nombre_tipo_input = st.sidebar.selectbox("Seleccione Nombre Tipo", df['nombre_tipo'].unique())
nombre_categoria_input = st.sidebar.selectbox("Seleccione Nombre Categoria", df['nombre_categoria'].unique())

# Filtrar los datos según la entrada del usuario
filtered_df = df[
                 (df['nombre_tipo'] == nombre_tipo_input) &
                 (df['nombre_categoria'] == nombre_categoria_input)]

# Mostrar el DataFrame filtrado
st.write(f"Datos filtrados por Tipo: {nombre_tipo_input}, Categoria: {nombre_categoria_input}")
st.write(filtered_df)

# Verificar si el DataFrame filtrado tiene suficientes datos para el modelo
if len(filtered_df) >= 2:  # Para que se pueda realizar una regresión polinómica
    # Definir las variables independientes (X) y la dependiente (y)
    # Convertir 'año_mes' a una variable numérica que el modelo pueda usar (por ejemplo, convertirla a número de mes)
    filtered_df['año_mes_num'] = filtered_df['año_mes'].dt.month + 12 * (filtered_df['año_mes'].dt.year - filtered_df['año_mes'].dt.year.min())
    filtered_df = filtered_df.sort_values(by='año_mes_num', ascending=False)
    
    # Eliminar outliers usando el rango intercuartílico (IQR)
    Q1 = filtered_df['cantidad_comprada'].quantile(0.25)
    Q3 = filtered_df['cantidad_comprada'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filtrar los outliers en la variable dependiente
    filtered_df = filtered_df[(filtered_df['cantidad_comprada'] >= lower_bound) & (filtered_df['cantidad_comprada'] <= upper_bound)]
    
    st.write(f"Datos después de eliminar outliers")
    st.write(filtered_df)

    X = filtered_df[['año_mes_num']]  # Año-Mes convertido a variable numérica
    y = filtered_df['cantidad_comprada']  # Cantidad comprada

    # Crear la transformación polinómica
    poly = PolynomialFeatures(degree=9)  # Puedes cambiar el grado según sea necesario
    X_poly = poly.fit_transform(X)

    # Crear el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_poly, y)

    # Realizar las predicciones
    y_pred = model.predict(X_poly)

    # Graficar los resultados
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X, y, color='blue', label='Datos reales')
    ax.plot(X, y_pred, color='red', label='Regresión Polinómica')

    # Etiquetas
    ax.set_title('Relación entre Año-Mes Numérico y Cantidad Comprada con Ajuste Polinómico')
    ax.set_xlabel('Año-Mes Numérico')
    ax.set_ylabel('Cantidad Comprada')
    ax.legend()

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)

    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

    # Realizar las predicciones
    y_pred_test = model.predict(X_test)

    # Calcular las métricas de evaluación
    mae = mean_absolute_error(y_test, y_pred_test)  # Error absoluto medio
    mse = mean_squared_error(y_test, y_pred_test)  # Error cuadrático medio
    rmse = np.sqrt(mse)  # Raíz del error cuadrático medio
    r2 = r2_score(y_test, y_pred_test)  # Coeficiente de determinación (R²)

    # Mostrar las métricas en Streamlit
    st.write("Evaluación del Modelo")
    st.write(f"Error Absoluto Medio (MAE): {mae}")
    st.write(f"Error Cuadrático Medio (MSE): {mse}")
    st.write(f"Raíz del Error Cuadrático Medio (RMSE): {rmse}")
    st.write(f"Coeficiente de Determinación (R²): {r2}")

    # Gráfico de Predicción vs Real
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(y_test, y_pred_test)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    ax.set_xlabel('Cantidad Real')
    ax.set_ylabel('Predicción')
    ax.set_title('Predicción vs Real')

    st.pyplot(fig)

    # Realizar validación cruzada en el modelo
    from sklearn.model_selection import cross_val_score

    cv_scores = cross_val_score(model, X_poly, y, cv=5, scoring='neg_mean_absolute_error')

    # Mostrar los resultados de la validación cruzada
    st.write("Validación Cruzada - Resultados (Error Absoluto Medio):")
    st.write(cv_scores)

    # Promedio del Error Absoluto Medio (MAE) de la validación cruzada
    mae_cv = -cv_scores.mean()  # Negativo porque cross_val_score devuelve valores negativos para MAE
    st.write(f"Promedio del Error Absoluto Medio (MAE) con validación cruzada: {mae_cv:.2f}")

    # Predicción con los datos del usuario
    prediction_input = np.array([[filtered_df['año_mes_num'].iloc[0]]])
    prediction_input_poly = poly.transform(prediction_input)
    prediction = model.predict(prediction_input_poly)

    # Mostrar la predicción
    st.write(f"Predicción de cantidad comprada para el mes seleccionado: {prediction[0]:.2f}")
else:
    st.write("No hay suficientes datos para entrenar el modelo con los filtros seleccionados.")
