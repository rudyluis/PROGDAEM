# Generación de datos adicionales para frecuencias cardíacas
import numpy as np

# Frecuencia cardíaca normal (60 a 100 bpm)
frecuencias_normal = np.random.randint(60, 101, size=150)  # 150 registros de personas con frecuencia normal
clase_normal = [0] * len(frecuencias_normal)

# Frecuencia cardíaca con taquicardia (101 a 220 bpm)
frecuencias_taquicardia = np.random.randint(101, 221, size=100)  # 100 registros de personas con taquicardia
clase_taquicardia = [1] * len(frecuencias_taquicardia)

# Concatenar los datos para tener el conjunto final
frecuencias_cardiacas = np.concatenate([frecuencias_normal, frecuencias_taquicardia]).reshape(-1, 1)
clase = np.concatenate([clase_normal, clase_taquicardia])

import pandas as pd

# Crear DataFrame con las frecuencias y clases
data = pd.DataFrame({
    'frecuencia': np.concatenate([frecuencias_normal, frecuencias_taquicardia]),
    'clase': np.concatenate([clase_normal, clase_taquicardia])
})

# Guardar en un archivo CSV
data.to_csv('frecuencias_cardiacas_ampliadas.csv', index=False)
S