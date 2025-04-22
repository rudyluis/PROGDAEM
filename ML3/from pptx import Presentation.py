import numpy as np
import pandas as pd

# Datos del préstamo
principal = 306240  # Monto del préstamo en Bs
interes_anual = 0.055  # Tasa de interés anual
seguro_vida = 0.08  # Seguro de vida (8%)
seguro_incendio = 0.02  # Seguro de incendio (2%)
plazo_anos = 20  # Plazo en años
plazo_meses = plazo_anos * 12  # Plazo en meses

# Cuotas especiales
amortizacion_inicial = 49000  # Amortización en la primera cuota
amortizacion_final = 90000  # Amortización en la cuota 103

# Calcular seguros
seguro_total = seguro_vida + seguro_incendio
monto_seguro = principal * seguro_total  # Monto total de seguros

# Calcular la tasa de interés mensual
interes_mensual = interes_anual / 12

# Lista para guardar la tabla de amortización
tabla_amortizacion = []

# Calcular la amortización para cada cuota
saldo_pendiente = principal
for cuota in range(1, plazo_meses + 1):
    if cuota == 1:
        # Primer pago, amortización inicial
        amortizacion = amortizacion_inicial
    elif cuota == 103:
        # Cuota 103, amortización final
        amortizacion = amortizacion_final
    else:
        # Cuotas intermedias, calcular con un pago de amortización igual
        amortizacion = 0

    # Calcular interés sobre saldo pendiente
    interes = saldo_pendiente * interes_mensual
    cuota_total = amortizacion + interes
    
    # Calcular saldo pendiente después del pago
    saldo_pendiente -= amortizacion

    # Guardar datos en la tabla
    tabla_amortizacion.append([cuota, saldo_pendiente, interes, amortizacion, cuota_total])

# Crear DataFrame
df_amortizacion = pd.DataFrame(tabla_amortizacion, columns=["Cuota", "Saldo Pendiente", "Interés", "Amortización", "Cuota Total"])

# Mostrar los primeros 20 registros para ver el inicio de la tabla
print(df_amortizacion.head(20))
