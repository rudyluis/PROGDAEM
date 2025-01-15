#%%

import pandas as pd
import numpy as np

# Crear un DataFrame pasando una matriz numpy, con un índice y columnas etiquetadas
dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

#%%

## Selección
# Seleccionar la columna 'A'
df['A']

# Seleccionar las primeras tres filas
df[0:3]

# Selección por etiqueta
# Seleccionar la primera fila usando la etiqueta del índice
df.loc[dates[0]]

# Seleccionar todas las filas y solo las columnas 'A' y 'B'
df.loc[:, ['A', 'B']]

# Selección con un rango de fechas en el índice
df.loc['20200102':'20200104', ['A', 'B']]

# Seleccionar un valor específico de la columna 'A' en la primera fila
df.loc[dates[0], 'A']

#%% Selección por posición

# Elegir la tercera fila
df.iloc[3]

# Actuar de manera similar a cómo se haría en numpy o Python (slicing)
df.iloc[3:5, 0:2]

# Seleccionar filas específicas y columnas específicas
df.iloc[[1, 2, 4], [0, 2]]

# Seleccionar un rango de filas y todas las columnas
df.iloc[1:3, :]

# Indexación booleana
# Seleccionar las filas donde los valores de la columna 'A' son mayores que 0
df[df.A > 0]

# Crear una copia del DataFrame
df2 = df.copy()

# Agregar fácilmente una nueva columna
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

# Filtrar usando un conjunto de valores en la columna 'E'
df2[df2['E'].isin(['two', 'four'])]
