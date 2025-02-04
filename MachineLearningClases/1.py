## Prediccion Predicción del Consumo Energético en función de la Temperatura utilizando Regresión Lineal
import numpy as np  # Para operaciones matemáticas y generación de números aleatorios
import pandas as pd  # Para manipulación de datos en estructuras como DataFrame
import matplotlib.pyplot as plt  # Para crear gráficos visuales
import seaborn as sns  # Para visualización avanzada con gráficos estilizados
from sklearn.model_selection import train_test_split  # Para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.linear_model import LinearRegression  # Para el modelo de regresión lineal

from sklearn.metrics import mean_squared_error, r2_score  # Para evaluar el rendimiento del modelo

# Generación de datos sintéticos
np.random.seed(42)  # Fijamos la semilla para que los resultados sean reproducibles
x = np.random.uniform(0, 40, 100)  # Simulamos 100 días de temperatura entre 0 y 40°C
y = 10 + 2.5 * x + np.random.normal(0, 5, 100)  # Relación lineal con ruido (simulamos el consumo de energía)

# Creamos un DataFrame con los datos generados
df = pd.DataFrame({'Temperature': x, 'EnergyConsumption': y})
df.to_csv('DatosTemperatura.csv')
df= pd.read_csv('DatosTemperatura.csv')
# Exploratory Data Analysis (EDA) - Análisis exploratorio de datos
plt.figure(figsize=(10, 5))  # Establecemos el tamaño de la figura para los gráficos
sns.scatterplot(x=df['Temperature'], y=df['EnergyConsumption'])  # Graficamos los datos en un diagrama de dispersión
plt.xlabel('Temperature (°C)')  # Etiqueta para el eje X
plt.ylabel('Energy Consumption (kWh)')  # Etiqueta para el eje Y
plt.title('Temperature vs Energy Consumption')  # Título del gráfico
plt.show()  # Mostramos el gráfico

# Correlación entre las variables
print("Correlación:")
print(df.corr())  # Imprimimos la matriz de correlación entre las variables del DataFrame

# División de los datos en conjunto de entrenamiento y conjunto de prueba
X = df[['Temperature']]  # Seleccionamos la columna 'Temperature' como variable independiente
y = df['EnergyConsumption']  # Seleccionamos la columna 'EnergyConsumption' como variable dependiente
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Dividimos los datos en 80% entrenamiento y 20% prueba

# Entrenamiento del modelo de regresión lineal
model = LinearRegression()  # Creamos un objeto del modelo de regresión lineal
model.fit(X_train, y_train)  # Ajustamos el modelo a los datos de entrenamiento

# Predicciones con los datos de prueba
y_pred = model.predict(X_test)  # Hacemos predicciones sobre el conjunto de prueba

# Evaluación del rendimiento del modelo
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Calculamos la raíz del error cuadrático medio (RMSE)
r2 = r2_score(y_test, y_pred)  # Calculamos el coeficiente de determinación (R²) para evaluar la calidad del modelo
print(f'RMSE: {rmse:.2f}')  # Mostramos el RMSE
print(f'R²: {r2:.2f}')  # Mostramos el R²

# Visualización de resultados: comparando los valores reales y las predicciones
plt.figure(figsize=(10, 5))  # Establecemos el tamaño de la figura para los gráficos
sns.scatterplot(x=X_test['Temperature'], y=y_test, label='Actual')  # Graficamos los valores reales (dispersión)
sns.lineplot(x=X_test['Temperature'], y=y_pred, color='red', label='Predicted')  # Graficamos las predicciones (línea roja)
plt.xlabel('Temperature (°C)')  # Etiqueta para el eje X
plt.ylabel('Energy Consumption (kWh)')  # Etiqueta para el eje Y
plt.title('Regression Model Performance')  # Título del gráfico
plt.legend()  # Mostramos la leyenda
plt.show()  # Mostramos el gráfico
