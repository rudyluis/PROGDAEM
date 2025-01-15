import pandas as pd 
def clasificador_salario(salario):
    if salario< 20000:
        return "Bajo"
    elif 2000<=salario<=50000:
        return "Medio"
    else:
        return "Alto"
    
data = {
    "Nombre": ["Ana", "Carlos", "Luis", "María", "Sofía"],
    "Edad": [29, 35, 40, 25, 30],
    "Departamento": ["Ventas", "Marketing", "IT", "Ventas", "Recursos Humanos"],
    "Salario": [45000, 52000, 60000, 48000, 50000]
}

df= pd.DataFrame(data)
print(df)

print("Primeros 5 registros")
print(df.head())

print(df.tail())

print("Informacion del DataFrame:")
print(df.info())

promedio_ingreso=df["Salario"].mean()

print("El promedio de los salarios es:", promedio_ingreso)

df["Categoria"]=df["Salario"].apply(clasificador_salario)

print(df)
df.to_csv('ejemplo_pandas.csv')