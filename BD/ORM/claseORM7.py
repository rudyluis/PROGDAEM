from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from ORM import Oficina, Producto, Empleado, Cliente
from sqlalchemy import or_, and_, func


# Conectar a la base de datos
engine = create_engine('postgresql://postgres:123456@localhost/jardineria2')

connection= engine.connect()

session= Session(engine)

count_oficinas = session.query(func.count(Oficina.idoficina)).scalar()

count_oficinas= session.query(Oficina).count()

print("numero total de Oficinas:", count_oficinas)

### AVG promedio
promedio_pedidos= session.query(func.avg(Producto.precioventa)).scalar()
print('El promedio del precio de Venta es de ',promedio_pedidos)

### SUM sumatoria
promedio_pedidos= session.query(func.sum(Producto.precioventa)).scalar()
print('La sumatoria del precio de Venta es de ',promedio_pedidos)


### MAX Maximo
maximo= session.query(func.max(Producto.precioventa)).scalar()
print('El precio maximo de Venta es de ',maximo)

### Minimo
minimo= session.query(func.min(Producto.precioventa)).scalar()
print('El precio minimo de Venta es de ',minimo)









session.close()



