from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conectar a la base de datos
engine = create_engine('postgresql://postgres:123456@localhost/jardineria2')

connection= engine.connect()


query= text("SELECT * FROM v_vista_clientes")

result= connection.execute(query)

for row in result:
    print(row)



query_f= text('SELECT * from cliente_sin_pagos() as (clientes_sin_pagos varchar)')

result_f= connection.execute(query_f)

connection.close()


for row in result_f:
    print(row)


