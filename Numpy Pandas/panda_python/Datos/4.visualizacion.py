#%%
"""
Explicación:
Generación de gráficos con pandas y matplotlib:
Se crean series temporales y DataFrames con valores aleatorios.
Luego, se realizan operaciones como la suma acumulada y se grafican los resultados con la función .plot() de pandas, que utiliza internamente matplotlib.
Gráficos de barras:
Se muestra cómo crear gráficos de barras apiladas con .plot.bar().
También se puede crear gráficos de barras horizontales con .plot.barh().
Gráficos de dispersión:
Se utiliza .plot.scatter() para generar gráficos de dispersión entre las columnas de un DataFrame.
Puedes superponer múltiples gráficos de dispersión sobre el mismo gráfico utilizando el parámetro ax.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1024)

#%%

# Graficar una serie temporal simple
ts = pd.Series(np.random.randn(1000),  # Generar 1000 valores aleatorios
               index=pd.date_range('1/1/2020', periods=1000))  # Crear un índice de fechas

part_sum = ts.cumsum()  # Sumar acumuladamente los valores de la serie
part_sum.plot()  # Graficar la serie
plt.show()  # Mostrar el gráfico

#%%

# Graficar 4 gráficos, cada uno para una columna de un DataFrame
df = pd.DataFrame(
    np.random.randn(1000, 4),  # 1000 filas y 4 columnas con valores aleatorios
    index=pd.date_range('1/1/2020', periods=1000, freq='30min'),  # Índice de fechas cada 30 minutos
    columns=list('ABCD'))  # Asignar nombres de columnas A, B, C, D
df.head()  # Mostrar las primeras filas del DataFrame

#%%

# Realizar la suma acumulada de las columnas y graficar
df_cum = df.cumsum()  # Calcular la suma acumulada
print(df.head())  # Mostrar las primeras filas
df_cum.plot()  # Graficar la suma acumulada

#%%

# Otros tipos de gráficos

# Seleccionar una fila específica y un subconjunto de filas
row1 = df.iloc[0]  # Primera fila
row2_6 = df.iloc[1:6]  # Filas 1 a 5
print(row2_6)

# Crear un gráfico de barras para una fila
# row1.plot(kind='bar')  # Gráfico de barras de la primera fila

# Crear un gráfico de barras para las filas 1 a 5
# row2_6.plot(kind='bar')
# plt.axhline(0, color='k')  # Línea horizontal en 0
# plt.show()

#%%

# Gráfico de barras apiladas
bar_stacked = pd.DataFrame(np.random.rand(6, 4),  # 6 filas, 4 columnas con valores aleatorios
                    columns=['a', 'b', 'c', 'd'])  # Nombres de columnas
bar_stacked.plot.bar(stacked=True,  # Crear gráfico de barras apiladas
                    title="Bar stacked plot")

bar_stacked.plot.barh(stacked=True)  # Gráfico de barras apiladas horizontal
plt.show()

#%%



# Generar un DataFrame con datos aleatorios
df_part = pd.DataFrame(
    np.random.randn(1000, 4),  # 30 filas, 4 columnas con valores aleatorios
    ##index=pd.date_range('1/1/2020', periods=1000, freq='30min'),  # 30 fechas con intervalo de 30 minutos
    columns=list('ABCD')  # Nombres de columnas A, B, C, D
)
print (df_part.head)
df_part[['A', 'B']] += 5  # Modificar los valores de las columnas A y B

# Graficar el gráfico de dispersión de 'A' vs 'B'
group1 = df_part.plot.scatter(x='A', y='B', color="blue", label='grupo 1')

# Graficar el gráfico de dispersión de 'C' vs 'D' en el mismo gráfico
df_part.plot.scatter(x='C', y='D', color="red", label='grupo 2', ax=group1)

# %%
