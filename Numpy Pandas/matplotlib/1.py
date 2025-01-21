import matplotlib.pyplot as plt 

def diagrama_barras_notas(notas, color):
    '''Función que construye un diagrama de barras con las notas de las asignaturas de un curso.
    
    Parámetros:
        - notas: Es un diccionario formado por pares con clave el nombre de la asignaturay valor la nota.
        - color: Es una cadena con el color de las barras.
    
    Salida:
        - Un diagrama de barras con las notas del diccionario dado en el color dado.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las barras con las notas a partir del diccionario
    ax.bar(notas.keys(), notas.values(), color = color)
    # Devolvemos un objeto con los ejes y las barras que contienen
    return ax

notas = {'Programación':9, 'Mates':6.5, 'Economía':4, 'Historia': 8}
diagrama_barras_notas(notas, 'orange')
plt.show()

#%%
import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_sectores_ventas(ventas, titulo):
    '''Función que construye un diagrama de sectores con las ventas de un trimestre y lo guarda con un nombre dado. 
    
    Parámetros:
        - ventas: Es una serie de Pandas con las ventas del trimestre, siendo el índice los meses.
        - titulo: Es una cadena con el título.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos los sectores con las verntas a partir de la serie
    ventas.plot(kind = 'pie', ax = ax)
    # Eliminamos el título del eje y
    plt.ylabel('')
    # Añadimos el título
    plt.title(titulo)
    # Guardamos el gráfico con el nombre dado en formato png
    plt.savefig(titulo + '.png')
    return 

ventas = {'Enero':200, 'Febrero':240, 'Marzo':310}
s_ventas = pd.Series(ventas)
diagrama_sectores_ventas(s_ventas, 'Ventas primer trimestre')
# %%
###3

import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_lineas_ingresos_gastos(datos):
    '''Función que construye un diagrama de lineas con los ingresos y gastos de un cuatrimestre.
    
    Parámetros:
        - datos: Es un dataframe de Pandas con dos columnas, una para los ingresos y otra para los gastos, y como índice los meses.

    Salida:
        Un gráfico de líneas con los ingresos y los gastos dados.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las series de líneas con los ingresos y los gastos
    datos.plot(ax = ax)
    # Añadimos la escala del eje y
    ax.set_ylim([0, max(datos.Ingresos.max(), datos.Gastos.max()) + 500])
    # Añadimos el título
    plt.title('Evolución de ingresos y gastos')
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax

datos = {'Mes':['Ene', 'Feb', 'Mar', 'Abr'], 'Ingresos':[4500, 5200, 4800, 5300], 'Gastos':[2300, 2450, 2000, 2200]}
df_datos = pd.DataFrame(datos).set_index('Mes')
diagrama_lineas_ingresos_gastos(df_datos)
plt.show()
# %%
