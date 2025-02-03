import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import graphviz

# Cargar el dataset
dataset = pd.read_csv('df/Social_Network_Ads.csv')

# Análisis de los datos
st.title("Análisis de Datos de Compras en Redes Sociales")
with st.expander("Descripción del dataset:"):
    st.write(dataset.describe())

# Preprocesar el dataset
# Convertir Gender a variable numérica: Male = 1, Female = 0
##dataset['Gender'] = dataset['Gender'].map({'Male': 1, 'Female': 0})
# Crear una instancia de LabelEncoder
labelencoder = LabelEncoder()
dataset['Gender'] = labelencoder.fit_transform(dataset['Gender'])
X = dataset.iloc[:, [1, 2, 3]].values  # Usamos Gender, Age y Estimated Salary
y = dataset.iloc[:, 4].values            # Variable objetivo: Purchased

# Dividir el dataset en conjunto de entrenamiento y conjunto de testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Ajustar el clasificador de Árbol de Decisión en el Conjunto de Entrenamiento
"""
Principales Parámetros de DecisionTreeClassifier
criterion:

Especifica la función a utilizar para medir la calidad de una división.
Opciones:
'gini': (default) índice de Gini.
'entropy': ganancia de información.
max_depth:
Limita la profundidad del árbol. Esto ayuda a evitar el sobreajuste (overfitting).
min_samples_split:

El número mínimo de muestras necesarias para dividir un nodo. Puede ser un entero (número mínimo de muestras) o un flotante (proporción de muestras).
min_samples_leaf:

El número mínimo de muestras que debe estar presente en un nodo hoja. También puede ser un entero o un flotante.
max_features:

Número máximo de características a considerar para la mejor división. Opciones:
None: todas las características.
Un entero: número fijo de características.
Un flotante: porcentaje de características.
'sqrt': raíz cuadrada del número de características.
'log2': logaritmo en base 2 del número de características.
max_leaf_nodes:

Si se establece, limita el número de nodos hoja en el árbol. Esto puede ayudar a controlar el tamaño del árbol.
min_weight_fraction_leaf:

El peso mínimo de fracción de las muestras requeridas para estar en un nodo hoja. Útil para conjuntos de datos desbalanceados.
class_weight:

Permite ajustar los pesos de las clases. Puede ser:
None: sin ajuste (default).
Un diccionario con pesos específicos para cada clase.
'balanced': ajusta automáticamente los pesos inversamente proporcionales a las frecuencias de clase en el conjunto de datos.
random_state:

Controla la aleatoriedad del modelo. Al establecer un número, puedes asegurar que tus resultados sean reproducibles.
splitter:

El método utilizado para dividir en los nodos. Puede ser 'best' (mejor división) o 'random' (división aleatoria).

"""

##classifier = DecisionTreeClassifier(criterion="entropy", random_state=0)
classifier = DecisionTreeClassifier(criterion='entropy', 
                                     max_depth=5, 
                                     min_samples_split=10, 
                                     min_samples_leaf=5, 
                                     random_state=42)
classifier.fit(X_train, y_train)

# Predicción de los resultados con el Conjunto de Testing
y_pred = classifier.predict(X_test)

# Crear la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Mostrar la matriz de confusión
st.title("Matriz de Confusión") 
st.write(cm)

labels = np.array([[str(cm[0][0])+' (VN)', str(cm[0][1])+' (FP)'], [str(cm[1][0])+' (FN) ', str(cm[1][1])+ ' (VP)']])

fig = ff.create_annotated_heatmap(z=cm, colorscale='Blues', 
                                    x=['Predicho 0', 'Predicho 1'], 
                                    y=['Real 0', 'Real 1'],
                                    annotation_text=labels, )

# Mostrar la figura
fig.update_layout(
  
    xaxis_title="Predicción",
    yaxis_title="Real"
)                                    
st.plotly_chart(fig)

# Reporte de clasificación
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
with st.expander("Reporte de Clasificación"):
    st.dataframe(report_df)

# Visualización de los resultados del algoritmo en el Conjunto de Entrenamiento
fig_train = px.scatter(x=X_train[:, 1], y=X_train[:, 2], color=y_train.astype(str),
                       labels={'x': 'Edad', 'y': 'Sueldo Estimado'},
                       title='Árbol de Decisión (Conjunto de Entrenamiento)',
                       color_continuous_scale=['red', 'green'])
st.plotly_chart(fig_train)

# Visualización de los resultados del algoritmo en el Conjunto de Testing
fig_test = px.scatter(x=X_test[:, 1], y=X_test[:, 2], color=y_test.astype(str),
                      labels={'x': 'Edad', 'y': 'Sueldo Estimado'},
                      title='Árbol de Decisión (Conjunto de Test)',
                      color_continuous_scale=['red', 'green'])
st.plotly_chart(fig_test)

# Curva ROC usando Matplotlib
fpr, tpr, thresholds = roc_curve(y_test, classifier.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr, tpr)
st.write(roc_auc)
# Mostrar la curva ROC con Matplotlib
st.title("Curva ROC (Matplotlib)")
plt.figure()
plt.plot(fpr, tpr, color='blue', label='Curva ROC (AUC = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='red', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Tasa de Falsos Positivos')
plt.ylabel('Tasa de Verdaderos Positivos')
plt.title('Curva ROC')
plt.legend(loc='lower right')
st.pyplot(plt)

# Curva de Precisión-Recall usando Matplotlib
precision, recall, _ = precision_recall_curve(y_test, classifier.predict_proba(X_test)[:, 1])
st.title("Curva de Precisión-Recall (Matplotlib)")
plt.figure()
plt.plot(recall, precision, color='blue')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Curva de Precisión-Recall')
plt.grid()
st.pyplot(plt)

# Gráfico de Importancia de Características
importances = classifier.feature_importances_

features = ['Gender', 'Age', 'Estimated Salary']
fig_importance = px.bar(x=features, y=importances, title='Importancia de Características')
st.plotly_chart(fig_importance)

# Validación Cruzada
cv_scores = cross_val_score(classifier, X, y, cv=5)
st.title("Validación Cruzada")
st.write(f"Precisión promedio de la validación cruzada: {np.mean(cv_scores):.2f}")

# Interfaz para introducir valores de usuario
st.sidebar.header("Introducir Datos de Usuario")

gender = st.sidebar.selectbox("Género", ("Male", "Female"))
age = st.sidebar.number_input("Edad", min_value=0, max_value=100, value=30)
estimated_salary = st.sidebar.number_input("Sueldo Estimado", min_value=0, max_value=200000, value=50000)

# Codificación del género
gender_encoded = 1 if gender == "Male" else 0  # Codificación del género
user_input = np.array([[gender_encoded, age, estimated_salary]])

# Visualizar el árbol de decisión
st.title("Árbol de Decisión")
dot_data = export_graphviz(classifier, out_file=None, 
                           feature_names=['Gender', 'Age', 'Estimated Salary'],  
                           class_names=['No', 'Yes'],  
                           filled=True, rounded=True,  
                           special_characters=True)  
graph = graphviz.Source(dot_data)  
st.graphviz_chart(graph)

# Botón para realizar la predicción
if st.sidebar.button("Predecir"):
    prediction = classifier.predict(user_input)
    st.sidebar.subheader("Predicción para el Usuario")
    st.sidebar.write("El usuario con ID **{}** es predecido a comprar (1) o no comprar (0): **{}**".format(user_id, prediction[0]))
