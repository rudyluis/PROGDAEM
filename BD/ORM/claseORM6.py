from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from ORM import Oficina, Producto, Empleado, Cliente
from sqlalchemy import or_, and_
from sqlalchemy import func

# Conectar a la base de datos
engine = create_engine('postgresql://postgres:123456@localhost/jardineria2')

connection= engine.connect()

session= Session(engine)

# buscar todas las oficinas 
oficinas= session.query(Oficina).filter(Oficina.region=='Barcelona').all()
# like
oficinas= session.query(Oficina).filter(Oficina.region.like('%d%')).all()
# or
oficinas= session.query(Oficina).filter(or_(Oficina.region.like('%d%'),Oficina.region.like('%ona%'))).all()

# and

oficinas= session.query(Oficina).filter(and_(Oficina.pais=='España',Oficina.region=='Madrid')).all()


oficinas = session.query(Oficina).order_by(Oficina.ciudad.desc()).all()


for oficina in oficinas:
    print(oficina.ciudad, oficina.codigooficina, oficina.region)

productos= session.query(Producto).filter(Producto.cantidadstock.between(10,50)).all()

for producto in productos:
    print(producto.nombre, producto.cantidadstock)

print("QUERY APLICANDO IN")
nombres_producto=['Jardin','Higuera','Peral']

result= session.query(Producto).filter(Producto.nombre.in_(nombres_producto)).all()

codigos_producto=['FR-34','FR-35','FR-36']

result2= session.query(Producto).filter(Producto.codigo_producto.in_(codigos_producto)).all()

for product in result2:
    print(producto.nombre)
session.close()
"""
   select * from 
producto

where nombre in ('Jardin','Olivos','Higuera') 
    """



