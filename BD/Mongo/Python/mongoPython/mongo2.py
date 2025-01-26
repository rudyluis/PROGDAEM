from pymongo import MongoClient
from datetime import datetime
# Conexión al servidor MongoDB (en este caso, el servidor local)
client = MongoClient('localhost', 27017)
##client = MongoClient('mongodb+srv://rmanzaneda001:VaY0atGZkZ3TFnoY@cluster0.2eo714p.mongodb.net/')
#client = MongoClient('mongodb://localhost:27017/')
# Acceder a una base de datos
db = client['jardineria2']

estado_pedido=db.pedido.distinct("estado")


[
    {
        '$lookup': {
            'from': 'detallepedido', 
            'localField': 'idproducto', 
            'foreignField': 'idproducto', 
            'as': 'detallepedidos'
        }
    }, {
        '$unwind': {
            'path': '$detallepedidos'
        }
    }, {
        '$lookup': {
            'from': 'pedido', 
            'localField': 'detallepedidos.idpedido', 
            'foreignField': 'idpedido', 
            'as': 'pedidos_info'
        }
    }, {
        '$unwind': {
            'path': '$pedidos_info'
        }
    }, {
        '$lookup': {
            'from': 'cliente', 
            'localField': 'pedidos_info.idcliente', 
            'foreignField': 'idcliente', 
            'as': 'clientes'
        }
    }, {
        '$unwind': {
            'path': '$clientes'
        }
    }, {
        '$lookup': {
            'from': 'pago', 
            'localField': 'clientes.idcliente', 
            'foreignField': 'idcliente', 
            'as': 'pagos_info'
        }
    }, {
        '$unwind': {
            'path': '$pagos_info'
        }
    }, {
        '$group': {
            '_id': {
                'codigo_producto': '$codigoProducto', 
                'cantidad': '$detallepedidos.cantidad'
            }, 
            'Total': {
                '$sum': {
                    '$multiply': [
                        '$detallepedidos.preciounidad', '$detallepedidos.cantidad'
                    ]
                }
            }, 
            'Impuestos': {
                '$sum': {
                    '$add': [
                        {
                            '$multiply': [
                                '$detallepedidos.preciounidad', '$detallepedidos.cantidad'
                            ], 
                            '$multiply': [
                                '$detallepedidos.preciounidad', '$detallepedidos.cantidad', 0.13
                            ]
                        }
                    ]
                }
            }
        }
    }, {
        '$match': {
            'Total': {
                '$gt': 3000
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'Total': 1, 
            'Impuestos': 1, 
            'codigo_producto': '$_id.codigo_producto', 
            'unidades_vendidas': '$_id.cantidad'
        }
    }
]


print(estado_pedido)

estado_pedido=db.pedido.find({
  "estado": "Rechazado",
  "$expr": {
    "$eq": [{ "$year": "$fechapedido" }, 2009] ## Filtra por año (en este caso, 2009)
  }
})
for estado in estado_pedido:
  print(estado)
  
  
  
empleados=db.empleado.find(
  { "puesto": { "$ne": 'Representante Ventas' } },
  { "nombre": 1, "apellido1": 1, "apellido2": 1, "puesto": 1, "_id": 0 }
);

for empleado in empleados:
  print(empleado['apellido1'])

# Definir la fecha de inicio y fin del año 2009
inicio_2009 = datetime(2009, 1, 1)
fin_2009 = datetime(2010, 1, 1)

# Consulta de agregación
resultado = db.pago.aggregate([
    {
        "$match": {
            "fechapago": {
                "$gte": inicio_2009,
                "$lt": fin_2009
            }
        }
    },
    {
        "$group": {
            "_id": None,
            "Promedio de pago en 2009": { "$avg": "$total" }
        }
    }
])


# Mostrar el resultado
for pago in resultado:
    print(pago)
    
pagos=db.pago.find()
for pago in pagos:
  print(pago)    

resultado = db.cliente.aggregate([
    {
        "$match": {
            "ciudad": 'Fuenlabrada'
        }
    },
    {
        "$lookup": {
            "from": "pago",
            "localField": "idcliente",
            "foreignField": "idcliente",
            "as": "pagos"
        }
    },
    {
        "$unwind": "$pagos"
    },
    {
        "$lookup": {
            "from": "empleado",
            "localField": "pagos.idcodigoempleadoventas",
            "foreignField": "idempleado",
            "as": "empleado"
        }
    },
    {
        "$unwind": "$empleado"
    },
    {
        "$lookup": {
            "from": "oficina",
            "localField": "empleado.idoficina",
            "foreignField": "idoficina",
            "as": "oficina"
        }
    },
    {
        "$unwind": "$oficina"
    },
    {
        "$group": {
            "_id": {
                "lineadireccion1": "$oficina.lineadireccion1",
                "lineadireccion2": "$oficina.lineadireccion2"
            }
        }
    },
    {
        "$project": {
            "_id": 0,
            "lineadireccion1": "$_id.lineadireccion1",
            "lineadireccion2": "$_id.lineadireccion2"
        }
    }
])

# Mostrar el resultado
for direccion in resultado:
    print(direccion)