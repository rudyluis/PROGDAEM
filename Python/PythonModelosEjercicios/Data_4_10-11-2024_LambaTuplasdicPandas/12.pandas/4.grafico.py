import matplotlib.pyplot as plt
import pandas as pd
# Crear DataFrame ficticio
data_estudiantes = {
    "Estudiante": ["Juan", "Ana", "Pedro", "Lucía", "Carlos"],
    "Calificación": [45, 80, 60, 72, 38]
}
df_estudiantes = pd.DataFrame(data_estudiantes)

# Calcular estadísticas descriptivas
print("\nEstadísticas descriptivas de las calificaciones:")
print(df_estudiantes["Calificación"].describe())

# Clasificar por rango de calificación
def clasificar_calificacion(calif):
    if calif < 50:
        return "Menor a 50"
    elif 50 <= calif <= 70:
        return "50 a 70"
    else:
        return "Mayor a 70"

df_estudiantes["Rango"] = df_estudiantes["Calificación"].apply(clasificar_calificacion)

# Contar estudiantes por rango
conteo_rangos = df_estudiantes["Rango"].value_counts()

# Gráfico de barras
conteo_rangos.plot(kind="bar", color="skyblue", title="Cantidad de estudiantes por rango de calificación")
plt.xlabel("Rango de calificación")
plt.ylabel("Cantidad de estudiantes")
plt.show()
