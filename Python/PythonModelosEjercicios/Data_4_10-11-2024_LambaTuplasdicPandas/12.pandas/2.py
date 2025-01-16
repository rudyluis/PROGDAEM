import pandas as pd

df=pd.read_csv('dataframe2.csv', delimiter=',' )
##df = pd.DataFrame(data)


# Seleccionar registros donde el Departamento sea "Ventas"
ventas = df[df["Departamento"] == "Legal"]
print("\nEmpleados del Departamento 'Ventas':")
print(ventas)

# Seleccionar solo las columnas "Nombre" y "Salario"
nombre_salario = df[["Nombre", "Salario"]]
print("\nColumnas 'Nombre' y 'Salario':")
print(nombre_salario)


# Añadir una columna "Bono"
df["Bono"] = df["Salario"] * 0.10
print("\nDataFrame con columna 'Bono':")
print(df)

# Filtrar empleados con salario > 50000 y en "Marketing"
filtro = df[(df["Salario"] > 50000) & (df["Departamento"] == "Marketing")]
print("\nEmpleados con Salario > 50,000 en 'Marketing':")
print(filtro)

# Ordenar por Salario de forma descendente
df_ordenado = df.sort_values(by="Salario", ascending=False)
print("\nDataFrame ordenado por 'Salario' (descendente):")
print(df_ordenado)

# Agrupar por Departamento y calcular el promedio de Salario
promedio_salario = df.groupby("Departamento")["Salario"].mean()
print("\nPromedio de Salarios por Departamento:")
print(promedio_salario)