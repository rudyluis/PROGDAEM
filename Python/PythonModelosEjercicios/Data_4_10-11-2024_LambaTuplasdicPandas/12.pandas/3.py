import pandas as pd

# Crear un DataFrame ficticio
df_financiera=pd.read_csv('dataframe2.csv', delimiter=',')
##df = pd.DataFrame(data)



# Clasificar ingresos
def clasificar_ingreso(salario):
    if salario < 20000:
        return "Bajo"
    elif 20000 <= salario <= 50000:
        return "Medio"
    else:
        return "Alto"

df_financiera["Categoría"] = df_financiera["Salario"].apply(clasificar_ingreso)
print("\nDataFrame con Categorías:")
print(df_financiera)

# Reemplazar valores nulos con el promedio
promedio_ingreso = df_financiera["Salario"].mean(skipna=True)
df_financiera["Salario"].fillna(promedio_ingreso, inplace=True)
print("\nDataFrame con valores nulos reemplazados:")
print(df_financiera)