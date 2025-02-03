import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.figure_factory as ff
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler, LabelEncoder
import graphviz
# Cargar el dataset
dataset = pd.read_csv('df/Social_Network_Ads.csv')
st.set_page_config(page_title="Random Forest")
# Análisis de los datos
st.title("Análisis de Datos de Compras en Redes Sociales")
with st.expander("Descripción del dataset:"):
    st.write(dataset.describe())

# Preprocesar el dataset
# Convertir la variable "Gender" en una variable numérica
labelencoder_gender = LabelEncoder()
dataset['Gender'] = labelencoder_gender.fit_transform(dataset['Gender'])

# Separar características y variable objetivo
X = dataset.iloc[:, [1, 2, 3]].values  # Usamos Gender, Age y Estimated Salary
y = dataset.iloc[:, 4].values          # Variable objetivo: Purchased

# Dividir el dataset en conjunto de entrenamiento y conjunto de testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Escalar las variables
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)

# Ajustar el clasificador Random Forest en el Conjunto de Entrenamiento
classifier = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state=0)
classifier.fit(X_train, y_train)

# Predicción de los resultados con el Conjunto de Testing
y_pred = classifier.predict(X_test)

# Matriz de Confusión
cm = confusion_matrix(y_test, y_pred)
st.title("Matriz de Confusión")
st.write("La Matriz de Confusión muestra el desempeño del modelo:")
st.write(cm)

st.title("Matriz de Confusión")
fig = ff.create_annotated_heatmap(z=cm, colorscale='Blues', 
                                    x=['Predicho 0', 'Predicho 1'], 
                                    y=['Real 0', 'Real 1'])
st.plotly_chart(fig)


# Reporte de clasificación
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
st.title("Reporte de Clasificación")
st.dataframe(report_df)

# Visualización de los resultados del algoritmo en el Conjunto de Entrenamiento
def plot_decision_boundary(X_set, y_set, title):
    X1, X2 = np.meshgrid(np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
                         np.arange(start=X_set[:, 2].min() - 1, stop=X_set[:, 2].max() + 1, step=0.01))
    plt.contourf(X1, X2, classifier.predict(np.array([np.zeros(X1.shape).ravel(), X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha=0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 1], X_set[y_set == j, 2],
                    c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title(title)
    plt.xlabel('Edad')
    plt.ylabel('Sueldo Estimado')
    plt.legend()
    st.pyplot(plt)

##st.title("Árbol de Decisión - Conjunto de Entrenamiento")
##plot_decision_boundary(X_train, y_train, 'Random Forest (Conjunto de Entrenamiento)')

##st.title("Árbol de Decisión - Conjunto de Test")
##plot_decision_boundary(X_test, y_test, 'Random Forest (Conjunto de Test)')

# Curva ROC
fpr, tpr, thresholds = roc_curve(y_test, classifier.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr, tpr)

# Mostrar la curva ROC con Matplotlib
st.title("Curva ROC")
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

# Interfaz para introducir valores de usuario
st.sidebar.header("Introducir Datos de Usuario")
gender = st.sidebar.selectbox("Género", options=["Femenino", "Masculino"])
gender_encoded = 0 if gender == "Femenino" else 1  # Convertir género a número (0: Femenino, 1: Masculino)
age = st.sidebar.number_input("Edad", min_value=0, max_value=100, value=30)
estimated_salary = st.sidebar.number_input("Sueldo Estimado", min_value=0, max_value=200000, value=50000)

#user_input = sc_X.transform(np.array([[gender_encoded, age, estimated_salary]]))
user_input = np.array([[gender_encoded, age, estimated_salary]])

# Botón para realizar la predicción
if st.sidebar.button("Predecir"):
    prediction = classifier.predict(user_input)
    st.sidebar.subheader("Predicción para el Usuario")
    st.sidebar.write(f"Género: {gender}, Edad: {age} años, Sueldo Estimado: {estimated_salary}")
    st.sidebar.write(f"Predicción: {'Comprará' if prediction[0] == 1 else 'No Comprará'}")


# Visualizar el árbol de decisión
# Visualizar uno de los árboles del Random Forest
st.title("Visualización de un Árbol de Decisión en el Random Forest")
st.write("Selecciona el índice del árbol que deseas visualizar:")

# Selección del índice del árbol a visualizar
tree_index = st.number_input("Índice del árbol", min_value=0, max_value=len(classifier.estimators_)-1, value=0)

# Exportar y visualizar el árbol seleccionado
from sklearn.tree import export_graphviz
dot_data = export_graphviz(
    classifier.estimators_[tree_index],
    out_file=None, 
    feature_names=['Gender', 'Age', 'Estimated Salary'],
    class_names=['No', 'Yes'],
    filled=True, rounded=True,
    special_characters=True
)
graph = graphviz.Source(dot_data)
st.graphviz_chart(graph)


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


from sklearn.model_selection import cross_val_score
# Validación Cruzada

scores = cross_val_score(classifier, X, y, cv=5)  ###cantidad de CV que se dividiran para la validacion
st.write(f"Scores de la validación cruzada: {scores}")
st.write(f"Media de los scores: {round(np.mean(scores),2)}")
st.write(f"Desviación estándar de los scores: {round(np.std(scores),2)}")

# Gráfico de Importancia de Características
importances = classifier.feature_importances_
features = ['Gender', 'Age', 'Estimated Salary']
fig_importance = px.bar(x=features, y=importances, title='Importancia de Características')
st.plotly_chart(fig_importance)


