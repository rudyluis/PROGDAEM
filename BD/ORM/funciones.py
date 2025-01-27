from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from ORM import Oficina, Producto, Empleado, Cliente,Pedido, filtro_all_generico,filtro_all_generico_combo,filtro_busqueda_generico
from sqlalchemy import or_, and_, func

# Conectar a la base de datos
engine = create_engine('postgresql://postgres:123456@localhost/jardineria2')

connection= engine.connect()

session= Session(engine)

for registro in filtro_busqueda_generico(session,Cliente,'nombrecliente','Jardin de Flores'):
    print(registro)


for registro in filtro_all_generico(session,Oficina):
    print(registro)

for registro in filtro_all_generico_combo(session,Cliente,'nombrecliente'):
    print(registro)