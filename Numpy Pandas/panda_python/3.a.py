""""
# Ejercicio 

El fichero [titanic.csv](https://raw.githubusercontent.com/asalber/asalber.github.io/master/python/ejercicios/soluciones/pandas/titanic.csv) contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:

1. Generar un DataFrame con los datos del fichero.
2. Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
3. Mostrar por pantalla los datos del pasajero con identificador 148.
3. Mostrar por pantalla las filas pares del DataFrame.
4. Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
5. Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
5. Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
6. Eliminar del DataFrame los pasajeros con edad desconocida.
7. Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
8.  Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
"""
#%%
import pandas as pd

# Generar un DataFrame con los datos del fichero.
titanic = pd.read_csv('titanic.csv', index_col=0)

print(titanic)
print(titanic.head)
# %%
# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
print('Dimensiones:', titanic.shape)
print('Número de elemntos:', titanic.size)
print('Nombres de columnas:', titanic.columns)
print('Nombres de filas:', titanic.index)
print('Tipos de datos:\n', titanic.dtypes)
print('Primeras 10 filas:\n', titanic.head(10))
print('Últimas 10 filas:\n', titanic.tail(10))
# %%
# Mostrar por pantalla los datos del pasajero con identificador 148
print(titanic.loc[148])
# %%
# Mostrar por pantalla las filas pares del DataFrame.
print(titanic.iloc[range(0,titanic.shape[0],2)])
# %%
# Mostrar los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(titanic[titanic["Pclass"]==1]['Name'].sort_values())
# %%
# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron
print(titanic['Survived'].value_counts()/titanic['Survived'].count() * 100)

# Alternativa
print(titanic['Survived'].value_counts(normalize=True) * 100)
# %%
#Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase
print(titanic.groupby('Pclass')['Survived'].value_counts(normalize=True))
# %%
# Eliminar del DataFrame los pasajeros con edad desconocida.
titanic.dropna(subset=['Age'])

# Alternativa 
# titanic = titanic[titanic['Age'].notna()]

# %%
# Mostrar la edad media de las mujeres que viajaban en cada clase.
print(titanic.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])

# %%
# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
titanic['Young'] = titanic['Age'] < 18
print(titanic['Young'])

# %%
# Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print(titanic.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100)
# %%
