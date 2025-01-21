#%%
import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))

#%%
import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    return notas.describe()

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))
# %%

import pandas as pd

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 5].sort_values(ascending=False)

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(aprobados(notas))
# %%



import pandas as pd

datos = {
    'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
'Ventas':[30500, 35600, 28300, 33900], 
'Gastos':[22000, 23400, 18100, 20700]
}
contabilidad = pd.DataFrame(datos)
print(contabilidad)
# %%
#Segunda Opcion
import pandas as pd

datos = [['Enero', 30500, 22000], ['Febrero', 35600, 23400], ['Marzo', 28300, 18100], ['Abril', 33900,20700]]
contabilidad = pd.DataFrame(datos, columns=['Mes', 'Ventas', 'Gastos'])
print(contabilidad)
# %%

def balance(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()
print(contabilidad)
print(balance(contabilidad, ['Enero','Marzo']))
# %%
