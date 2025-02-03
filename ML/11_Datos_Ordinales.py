import pandas as pd
import numpy as np

categorias_servicio = ["Muy insatisfecho", "Insatisfecho", 
                       "Neutral", "Satisfecho", "Muy satisfecho"]

categorias_calidad = ["Mala", "Buena", "Muy buena", "Excelente"]

encuesta = {"servicio" : ["Muy insatisfecho", "Insatisfecho",
                          "Neutral", "Satisfecho", "Muy satisfecho",
                          "Muy insatisfecho"],
            
            "alimentos" : ["Mala", "Buena", "Muy buena",
                           "Excelente", "Mala", "Buena"]}

# 0: cliente esporádico       1: cliente frecuente
tipo_cliente = [0, 0, 1, 1, 0, 1] 

pd.DataFrame(encuesta)

print(encuesta)

from sklearn.preprocessing import OrdinalEncoder

datos_ord = pd.DataFrame(encuesta)

codificador = OrdinalEncoder(categories=[categorias_servicio,
                                        categorias_calidad])

datos_ord = pd.DataFrame(codificador.fit_transform(datos_ord),
                         columns=["servicio", "alimentacion"])

print(datos_ord)
print(codificador.categories_)


from sklearn.preprocessing import OneHotEncoder

datos_one = pd.DataFrame(encuesta)

codificador = OneHotEncoder()

datos_one = pd.DataFrame(codificador.fit_transform(datos_one).toarray(),
                         columns=np.concatenate(codificador.categories_))

print(datos_one)

### comparacion
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler

print("\n*** Datos Escalados de la Codificación Ordinal")
escalador = MinMaxScaler()
print(datos_ord)
datos_ord = escalador.fit_transform(datos_ord)
print(datos_ord)

print("\n*** Clasificación con Datos codificados con OrdinalEncoder")
modelo = LogisticRegression().fit(datos_ord, tipo_cliente)
print("Predicciones:", modelo.predict(datos_ord))
print("Clases correctas:", tipo_cliente)
print(modelo.predict_proba(datos_ord))

print("\n*** Clasificación con Datos codificados con OneHotEncoder")
modelo = LogisticRegression().fit(datos_one, tipo_cliente)
print("Predicciones:", modelo.predict(datos_one))
print("Clases correctas:", tipo_cliente)
print(modelo.predict_proba(datos_one))