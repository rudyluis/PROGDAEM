import pandas as pd

datos = {"nombre" : ["Mariana", "Ana", "Elsa", "Gustavo",
                     "Pedro", "Raúl", "Carlos", "José", "Luis"],
         
         "saldo" : [10000.00, 8000.00, 9000.00, 2000.00,
                    2100.00, 12000.00, 5000.00, 10000.00, 200.00],
         
         "pais" : ["Argentina", "Bolivia", "Chile", "Colombia",
                   "Costa Rica", "Ecuador", "México", "Perú", "Perú"]}

datos = pd.DataFrame(datos)
datos["pais"] = datos["pais"].astype("category")
print(datos.info())



datos_sesgados = datos.copy()

reemplazos = {"Argentina" : 1,
             "Bolivia" : 2, 
             "Chile" : 3, 
             "Colombia" : 4,                        
             "Costa Rica" : 5,
             "Ecuador" : 6, 
             "México" : 7, 
             "Perú" : 8}

datos_sesgados["pais"].replace(reemplazos, inplace=True)
print(datos_sesgados)

from sklearn.preprocessing import OneHotEncoder

codificador = OneHotEncoder()

codificacion = codificador.fit_transform(datos[["pais"]])

#print(type(codificacion))
#print(codificacion)
#print(codificacion.toarray())

nuevas_cols = pd.DataFrame(codificacion.toarray(),
                           columns=codificador.categories_)
print(nuevas_cols)

datos = pd.concat([datos, nuevas_cols], axis="columns")
print(datos)

datos.drop('pais', axis="columns", inplace=True)
print(datos)

