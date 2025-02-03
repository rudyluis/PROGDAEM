import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, SVR
from sklearn.metrics import confusion_matrix, accuracy_score, mean_squared_error
import seaborn as sns

# Títulos de la aplicación
st.title("Ejemplo de SVM: Clasificación y Regresión")
st.markdown("""
Este ejemplo demuestra el uso de SVM tanto para clasificación como para regresión. 
Usaremos un conjunto de datos ficticio generado aleatoriamente.
""")

# Opción para elegir entre Clasificación y Regresión
option = st.sidebar.selectbox("Selecciona el modelo", ("Clasificación", "Regresión"))

if option == "Clasificación":
  # Generación de datos ficticios para clasificación
    st.header("Clasificación con SVM")
    n_samples = 100
    X_class, y_class = datasets.make_classification(n_samples=n_samples, n_features=2, n_classes=2, n_informative=2, n_redundant=0, random_state=42)
    X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.3, random_state=42)

    # Entrenamiento del modelo SVM para clasificación
    model_class = SVC(kernel='linear', random_state=42)
    model_class.fit(X_train_class, y_train_class)
    y_pred_class = model_class.predict(X_test_class)

    # Visualización de los datos de clasificación
    fig, ax = plt.subplots()
    scatter = ax.scatter(X_class[:, 0], X_class[:, 1], c=y_class, cmap='coolwarm', edgecolors='k', s=50)
    legend1 = ax.legend(*scatter.legend_elements(), title="Clases")
    ax.add_artist(legend1)
    ax.set_title("Datos de Clasificación")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    st.pyplot(fig)

    # Evaluación del modelo de clasificación
    accuracy = accuracy_score(y_test_class, y_pred_class)
    cm_class = confusion_matrix(y_test_class, y_pred_class)
        # Mostrar matriz de confusión
    st.subheader("Resultados de Clasificación")
    st.write(f"Accuracy: {accuracy:.2f}")

    with st.expander("Matriz de Confusión", expanded=True):
        fig_cm_class, ax_cm_class = plt.subplots()
        sns.heatmap(cm_class, annot=True, fmt='d', ax=ax_cm_class, cmap='Blues', 
                    xticklabels=['Clase 0', 'Clase 1'], yticklabels=['Clase 0', 'Clase 1'])
        ax_cm_class.set_xlabel('Predicciones')
        ax_cm_class.set_ylabel('Reales')
        ax_cm_class.set_title('Matriz de Confusión')
        st.pyplot(fig_cm_class)
elif option == "Regresión":


    # Generación de datos ficticios para regresión
    st.header("Regresión con SVM")
    X_reg = np.sort(5 * np.random.rand(80, 1), axis=0)
    y_reg = np.sin(X_reg).ravel() + np.random.normal(0, 0.1, X_reg.shape[0])

    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

    # Entrenamiento del modelo SVM para regresión
    model_reg = SVR(kernel='linear')
    model_reg.fit(X_train_reg, y_train_reg)
    y_pred_reg = model_reg.predict(X_test_reg)

    # Visualización de los datos de regresión
    # Visualización de los datos de regresión
    st.subheader("Resultados de Regresión")
    fig_reg, ax_reg = plt.subplots(figsize=(10, 6))
    ax_reg.scatter(X_train_reg, y_train_reg, color='blue', label='Datos de Entrenamiento')
    ax_reg.scatter(X_test_reg, y_test_reg, color='green', label='Datos de Prueba')
    ax_reg.scatter(X_test_reg, y_pred_reg, color='red', label='Predicciones')
    ax_reg.plot(X_test_reg, y_pred_reg, color='orange', lw=2)
    ax_reg.set_title("Regresión SVM")
    ax_reg.set_xlabel("Feature")
    ax_reg.set_ylabel("Target")
    ax_reg.legend()
    st.pyplot(fig_reg)

    # Evaluación del modelo de regresión
    mse = mean_squared_error(y_test_reg, y_pred_reg)
    st.write(f"MSE: {mse:.2f}")

    # Mostrar los datos reales y predicciones en una tabla
    with st.expander("Datos Reales y Predicciones", expanded=True):
        df_results_reg = pd.DataFrame({'Reales': y_test_reg, 'Predicciones': y_pred_reg})
        st.write(df_results_reg)

st.markdown("""
### Conclusiones
En esta aplicación, hemos visto cómo implementar SVM tanto para tareas de clasificación como de regresión. 
Hemos evaluado el rendimiento de los modelos utilizando métricas como accuracy para clasificación y MSE para regresión.
""")


