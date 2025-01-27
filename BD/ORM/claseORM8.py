from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from ORM import Oficina, Producto, Empleado, Cliente
from sqlalchemy import or_, and_, func


# Conectar a la base de datos
engine = create_engine('postgresql://postgres:123456@localhost/jardineria')

connection= engine.connect()

session= Session(engine)


result= session.query(Oficina,Empleado).join(Empleado).filter(Oficina.pais=='España').all()

for resp in result:
    print(resp)

for oficina,empleado in result:
    print("Oficina:", oficina.region)
    print("Empleado:", empleado.nombre)
    print('-----------------------------')


results= session.query(Oficina.region, Empleado.nombre).select_from(Oficina).join(Empleado, Empleado.idoficina==Oficina.idoficina).filter(Oficina.pais=='España').all()


for oficina_n,empleado_n in results:
    print("Oficina:", oficina_n)
    print("Empleado:", empleado_n)
    print('-----------------------------')


result= session.query(Producto.nombre, func.count(Producto.idproducto)).\
        group_by(Producto.nombre).\
        having(func.count(Producto.idproducto)>5).all()

for nombre_producto, contar in result:
    print(f"Producto:{nombre_producto}  Cantidad:{contar}")


result= session.query(Producto.nombre, func.sum(Producto.cantidadstock).label('Total_inventario')).\
group_by(Producto.nombre,Producto.precioventa).\
having((func.sum(Producto.cantidadstock)>100) & (Producto.precioventa<50)).\
all()
print('-----------------')
for row in result:
    print(f"Nombre Producto: {row.nombre}, Total Inventario:{row.Total_inventario}")

