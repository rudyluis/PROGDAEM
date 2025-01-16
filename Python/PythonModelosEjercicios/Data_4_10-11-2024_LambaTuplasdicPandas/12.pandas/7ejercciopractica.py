import pandas as pd

# Crear un DataFrame con la información de 5 personas
data = {
    'Nombre': ['Carlos', 'Ana', 'Luis', 'Maria', 'Pedro'],
    'Edad': [25, 35, 28, 40, 32],
    'Ciudad': ['Madrid', 'Madrid', 'Barcelona', 'Madrid', 'Sevilla'],
    'Profesión': ['Ingeniero', 'Médico', 'Abogado', 'Diseñadora', 'Arquitecto']
}

# Listas vacías para almacenar los datos
nombres = []
edades = []
ciudades = []
profesiones = [] 
# Número de registros que el usuario quiere ingresar
num_personas = int(input("¿Cuántas personas quieres ingresar? "))

# Captura de datos desde teclado
for i in range(num_personas):
    print(f"\nIngrese los datos para la persona {i+1}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")
    profesion = input("Profesión: ")

    # Agregar los datos a las listas correspondientes
    nombres.append(nombre)
    edades.append(edad)
    ciudades.append(ciudad)
    profesiones.append(profesion)

# Crear el DataFrame
data = {
    'Nombre': nombres,
    'Edad': edades,
    'Ciudad': ciudades,
    'Profesión': profesiones
}




df = pd.DataFrame(data)

# 1. Filtrar las personas cuya edad sea mayor de 30 años
mayores_30 = df[df['Edad'] > 30]

# 2. Encontrar el promedio de edad de las personas que viven en Madrid
promedio_madrid = df[df['Ciudad'] == 'Madrid']['Edad'].mean()

# 3. Ordenar el DataFrame por edad de forma descendente
df_ordenado = df.sort_values(by='Edad', ascending=False)

# Mostrar los resultados
print("Personas mayores de 30 años:")
print(mayores_30)

print("\nPromedio de edad de las personas que viven en Madrid:", promedio_madrid)

print("\nDataFrame ordenado por edad de forma descendente:")
print(df_ordenado)