# Coordenadas de algunas ciudades importantes
ubicaciones = {
    "Nueva York": (40.7128, -74.0060),
    "Londres": (51.5074, -0.1278),
    "Tokio": (35.6895, 139.6917)
}

# Acceder a las coordenadas
print("Coordenadas de Londres:", ubicaciones["Londres"])



# Días de la semana
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# Crear un horario de trabajo utilizando los días de la semana
horario_trabajo = {
    "Juan": (dias_semana[0], dias_semana[1], dias_semana[2], dias_semana[3], dias_semana[4]),  # Lunes a Viernes
    "Ana": (dias_semana[1], dias_semana[2], dias_semana[3])  # Martes a Jueves
}

# Verificar el horario de trabajo de Juan
print("Juan trabaja los días:", horario_trabajo["Juan"])