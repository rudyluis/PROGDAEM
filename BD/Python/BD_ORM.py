from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import Base
if __name__=='__main__':
    engine = create_engine('postgresql://postgres:123456@localhost/jardineria_bkp')

    # Llamar a create_all en Base.metadata
    Base.metadata.create_all(engine)


#%%
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ORM import Oficina, Empleado

engine= create_engine('postgresql://postgres:123456@localhost/jardineria')

#Crea una sesion
Session= sessionmaker(bind=engine)
session= Session()
#%%
#Agregar Registro
nueva_oficina = Oficina(
    codigooficina="OF001-01",
    ciudad="Lima",
    pais="Perú",
    region="Lima Metropolitana",
    codigopostal="15001",
    telefono="123456789",
    lineadireccion1="Av. Principal 123",
    lineadireccion2=None
)
session.add(nueva_oficina)
session.commit()
print("Oficina insertada con éxito.")

#%%
## Busque da de registro 
oficina = session.query(Oficina).filter_by(codigooficina="OF001-01").first()
if oficina:
    oficina.telefono = "987654321"
    session.commit()
    print("Teléfono actualizado.")
#%%
## Transacciones controladas
from sqlalchemy.exc import SQLAlchemyError

try:
    ##session.begin()
    
    # Crear una nueva oficina
    nueva_oficina = Oficina(
        codigooficina="OF002",
        ciudad="Bogotá",
        pais="Colombia",
        codigopostal="11001",
        telefono="555123456",
        lineadireccion1="Calle 45 #12-30"
    )
    session.add(nueva_oficina)

    # Insertar un empleado asociado a la oficina
    nuevo_empleado = Empleado(
        codigo_empleado=1002,
        nombre="Carlos",
        apellido1="Ramírez",
        extension="x200",
        email="carlos.ramirez@empresa.com",
        idoficina=2,
        puesto="Analista"
    )
    session.add(nuevo_empleado)

    session.commit()
    print("Transacción exitosa.")
except SQLAlchemyError as e:
    session.rollback()
    print("Error en la transacción:", str(e))

#%%
## Eliminar un registro
empleado = session.query(Empleado).filter_by(codigo_empleado=1002).first()
if empleado:
    session.delete(empleado)
    session.commit()
    print("Empleado eliminado.")

#%%
#Listar Oficina
oficinas = session.query(Oficina).all()
print(oficinas)

# %%
oficinas = session.query(Oficina).all()

for oficina in oficinas:
    print(oficina.ciudad)

#%%
##buscar todas las oficinas 
oficinas= session.query(Oficina).filter(Oficina.region=='Barcelona').all()
for oficina in oficinas:
    print(oficina.ciudad)

#%%
oficinas = session.query(Oficina).all()
for oficina in oficinas:
    print(oficina.ciudad, oficina.pais)
#%%
## Relaciones y Joins
empleados = session.query(Empleado).join(Oficina).all()
for emp in empleados:
    print(f"Empleado: {emp.nombre} {emp.apellido1} - Oficina: {emp.oficina.ciudad}")
 
#%%
## Join con filter
empleados_lima = session.query(Empleado).join(Oficina).filter(Oficina.ciudad == "Barcelona").all()
for emp in empleados_lima:
    print(emp.nombre, emp.apellido1)


# %%
from ORM import Oficina, Producto, Empleado, Cliente, Pago
from sqlalchemy import or_, and_, func
result= session.query(Producto.nombre, func.count(Producto.idproducto)).\
        group_by(Producto.nombre).\
        having(func.count(Producto.idproducto)>5).all()

for nombre_producto, contar in result:
    print(f"Producto:{nombre_producto}  Cantidad:{contar}")
# %%
## Funciones especiales 
from sqlalchemy import func
"""
En SQLAlchemy, .scalar() se usa para obtener un único valor en lugar de una tupla o lista. 
Es útil cuando esperamos un solo resultado de una consulta que usa funciones agregadas como COUNT(), SUM(), AVG(), etc.

"""
cantidad_empleados = session.query(func.count(Empleado.idempleado)).filter(Empleado.idoficina == 1).scalar()
print(f"Empleados en la oficina 1: {cantidad_empleados}")

#%%
total_pagos = session.query(func.sum(Pago.total)).filter(Pago.idcliente == 1).scalar()
print(f"Total pagado por el cliente 1: {total_pagos}")

# %%
