from pymongo import MongoClient
from datetime import datetime
# Conexión al servidor MongoDB (en este caso, el servidor local)
client = MongoClient('localhost', 27017)
client = MongoClient("mongodb+srv://rmanzanedav0001:lGSisb4y4HEoLWTa@cluster0.2eo714p.mongodb.net/")


db =client['jardineria_clases01']
print(client.list_database_names())



# Agregación
pipeline = [
    {
        "$lookup": {
            "from": "empleado",
            "localField": "idoficina",
            "foreignField": "idoficina",
            "as": "empleados"
        }
    },
    {
        "$unwind": "$empleados"
    },
    {
        "$group": {
            "_id": "$ciudad",
            "cantidadEmpleados": {"$sum": 1}
        }
    },
    {
        "$project": {
            "_id": 0,
            "ciudad": "$_id",
            "cantidadEmpleados": 1
        }
    }
]

# Ejecutar agregación
resultado = db.oficina.aggregate(pipeline)

# Mostrar resultados
for doc in resultado:
    print(doc)