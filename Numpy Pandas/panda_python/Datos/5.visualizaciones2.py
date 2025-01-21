#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generar un DataFrame con datos aleatorios
df = pd.DataFrame(
    np.random.randn(30, 4),
    ##index=pd.date_range('1/1/2020', periods=1000),
    columns=list('ABCD')
)
print(df.head)
# Calcular la suma acumulada de cada columna
df_cum = df.cumsum()
print(df_cum)
# Graficar los datos acumulados
df_cum.plot()
plt.title('Gráfico de Líneas: Suma Acumulada de las Columnas')
plt.xlabel('Fecha')
plt.ylabel('Valor Acumulado')
plt.show()

# %% 
#grafico de dispersion
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame con datos aleatorios
df = pd.DataFrame(
    np.random.randn(30, 4),  # 30 filas, 4 columnas con valores aleatorios
    index=pd.date_range('1/1/2020', periods=30, freq='30min'),
    columns=list('ABCD')
)

# Graficar un gráfico de dispersión entre las columnas 'A' y 'B'
df.plot.scatter(x='A', y='B', color='red', label='A vs B')

# Mostrar el gráfico
plt.title('Gráfico de Dispersión: A vs B')
plt.show()

# %%
import pandas as pd
import numpy as np

# Crear un DataFrame con datos aleatorios
df = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['col1', 'col2', 'col3']
)

# Estadísticas descriptivas
print(df.describe())

# %%
import numpy as np

# Crear una matriz 3x3 con valores aleatorios
matrix = np.random.rand(3, 3 )
# Numeros Aletorios enteros 

matrix = np.random.randint(0, 10, size=(3, 3))
print("Matriz original:")
print(matrix)

# Multiplicación de matrices
matrix_mult = np.dot(matrix, matrix)
print("\nMatriz multiplicada por sí misma:")
print(matrix_mult)

# Inversión de la matriz
if np.linalg.det(matrix) != 0:  # Verificamos si la matriz es invertible
    matrix_inv = np.linalg.inv(matrix)
    print("\nMatriz inversa:")
    print(matrix_inv)
else:
    print("\nLa matriz no es invertible.")

# %%
import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios
data = np.random.randint(0,100, size=1000)
#data =np.random.rand(1000)
#data =np.random.randn() 
##data = np.random.uniform(0, 20, size=1000)
print(data)
# Crear un histograma
plt.hist(data, bins=30, edgecolor='black')

# Añadir título y etiquetas
plt.title('Histograma de Datos Aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()

# %%
