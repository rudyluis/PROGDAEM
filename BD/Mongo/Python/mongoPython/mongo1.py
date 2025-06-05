from pymongo import MongoClient

# Conexión al servidor MongoDB (en este caso, el servidor local)
##client = MongoClient('localhost', 27017)
client = MongoClient("mongodb+srv://rmanzanedav0001:lGSisb4y4HEoLWTa@cluster0.2eo714p.mongodb.net/")
#client = MongoClient('mongodb://localhost:27017/')
# Acceder a una base de datos
db = client['jardineria_clases01']

# Acceder a una colección
oficina = db['oficina']

oficina_doc={

  "idoficina": 19,
  "ciudad": "Barcelona2Rudy",
  "codigooficina": "BCN-ES",
  "codigopostal": "08019",
  "estadoReg": 1,
  "fechaModif": {
    "$date": "2024-03-25T07:32:16.218Z"
  },
  "fechaReg": {
    "$date": "2024-03-25T07:32:16.218Z"
  },
  "lineadireccion1": "Avenida Diagonal, 38",
  "lineadireccion2": "3A escalera Derecha",
  "pais": "España",
  "region": "Barcelona",
  "telefono": "+34 93 3561182",
  "usuarioModif": "postgres",
  "usuarioReg": "postgres",
  "empleados": [
    {
      "idempleado": 11,
      "nombre": "Emmanuel",
      "apellido1": "Magaña",
      "apellido2": "Perez",
      "extension": "2518",
      "email": "manu@jardineria.es",
      "idoficina": 1,
      "idempleadojefe": 3,
      "puesto": "Director Oficina",
      "codigoEmpleado": 11
    },
    {
      "idempleado": 12,
      "nombre": "José Manuel",
      "apellido1": "Martinez",
      "apellido2": "De la Osa",
      "extension": "2519",
      "email": "jmmart@hotmail.es",
      "idoficina": 1,
      "idempleadojefe": 11,
      "puesto": "Representante Ventas",
      "codigoEmpleado": 12
    },
    {
      "idempleado": 13,
      "nombre": "David",
      "apellido1": "Palma",
      "apellido2": "Aceituno",
      "extension": "2519",
      "email": "dpalma@jardineria.es",
      "idoficina": 1,
      "idempleadojefe": 11,
      "puesto": "Representante Ventas",
      "codigoEmpleado": 13
    },
    {
      "idempleado": 14,
      "nombre": "Oscar",
      "apellido1": "Palma",
      "apellido2": "Aceituno",
      "extension": "2519",
      "email": "opalma@jardineria.es",
      "idoficina": 1,
      "idempleadojefe": 11,
      "puesto": "Representante Ventas",
      "codigoEmpleado": 14
    }
  ]
}

##result_oficina= oficina.insert_one(oficina_doc)

##print('ID del documento insertado:', result_oficina.inserted_id)


result_oficina2= db.oficina.insert_one(oficina_doc)
print('ID del documento insertado:', result_oficina2)

oficinas=db.oficina.find()
for oficina in oficinas:
    print(oficina)