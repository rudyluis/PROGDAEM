#%%
# Importar bibliotecas necesarias
import numpy as np
import pandas as pd

# Crear una Serie
s = pd.Series([1, 2, 3, 'foo', 4, np.nan, 'bar'])
print(s)

#%%
# Crear un rango de fechas (índice para el DataFrame)
dates = pd.date_range('20200101', periods=6, freq="D")

# Crear un DataFrame usando un array de numpy con índices y columnas etiquetadas
df = pd.DataFrame(np.random.randn(6, 4), 
                  index=dates, 
                  columns=['A', 'B', 'C', 'D'])
print(df)
""""
np.random.randn:

Proviene del módulo numpy.random y genera valores aleatorios que siguen una distribución normal estándar.
Es útil para simulaciones estadísticas o inicialización aleatoria en algoritmos como redes neuronales.
Parámetros (6, 4):

El primer argumento (6) representa el número de filas.
El segundo argumento (4) representa el número de columnas.
Por lo tanto, el resultado será un array de forma (6, 4).
Distribución:

La distribución normal estándar implica que los valores generados tienen:
Una media cercana a 0.
Una desviación estándar cercana a 1.
"""




#%%
# Crear un DataFrame utilizando un diccionario de objetos que pueden convertirse en series
df2 = pd.DataFrame({
    'A': 1.0,
    'B': pd.Timestamp('20201126'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})
print (df2)


#%%

# Crear un DataFrame con valores generados
n = 5  # Número de filas
df = pd.DataFrame(np.arange(1, n * 4 + 1).reshape(n, 4), columns=['A', 'B', 'C', 'D'])

print(df)
#%%
# Mostrar tipos de columnas del DataFrame df2
print("Tipos de columnas en df2:")
print(df2.dtypes)
#%%
# Visualizar datos en el DataFrame df
print("Primeras filas de df:")
print(df.head())
#%%
print("Últimas 5 filas de df:")
print(df.tail(5))
#%%
# Mostrar el índice, las columnas y los valores subyacentes
print("Índice de df:")
print(df.index)
#%%
print("Columnas de df:")
print(df.columns)
#%%
print("Valores subyacentes de df:")
print(df.values)
#%%
# Mostrar un resumen estadístico rápido del DataFrame
print("Resumen estadístico de df:")
print(df.describe())
#%%
# Transposición del DataFrame
print("Transposición de df:")
print(df.T)
#%%
# Ordenar por índice en orden descendente a lo largo de las columnas (axis=1)
print("Ordenar por índice (columnas) en orden descendente:")
print(df.sort_index(axis=1, ascending=False))
#%%
# Ordenar por valores en la columna 'B' (en df2, si aplica)
if 'B' in df2.columns:
    print("Ordenar df2 por la columna 'B':")
    print(df2.sort_values(by='B'))
else:
    print("La columna 'B' no existe en df2.")


