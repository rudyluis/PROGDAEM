import pandas as pd

# Crear el DataFrame
data = {
    "Nombre": ["Ana", "Carlos", "Luis", "María", "Sofía"],
    "Edad": [29, 35, 40, 25, 30],
    "Departamento": ["Ventas", "Marketing", "IT", "Ventas", "Recursos Humanos"],
    "Salario": [45000, 52000, 60000, 48000, 50000]
}
df = pd.DataFrame(data)

# Mostrar primeros 5 registros
print("Primeros 5 registros:")
print(df.head())

# Mostrar últimos 3 registros
print("\nÚltimos 3 registros:")
print(df.tail())

# Ver la estructura del DataFrame
print("\nInformación del DataFrame:")
print(df.info())


df.to_csv('dataframe.csv')

