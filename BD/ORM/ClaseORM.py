from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ORM import Oficina, Empleado

engine= create_engine('postgresql://postgres:123456@localhost/jardineria')

#Crea una sesion
Session= sessionmaker(bind=engine)
session= Session()
# Consutar la tabla oficina
"""
oficinas= session.query(Oficina).all()

for oficina in oficinas:
    print(oficina.ciudad, oficina.region)

oficina= Oficina(codigooficina='0006', ciudad='Madrid', pais='Bolivia',
                 region='Cochabamba', codigopostal='591', telefono='12345678', 
                 lineadireccion1='Calle por ahi cerca de un poste', lineadireccion2='otro lugar'
                 ) 
session.add(oficina)
session.commit()

"""
empleados= session.query(Empleado).all()
for empleado in empleados:
    if(empleado.jefe):
        print(empleado.nombre, empleado.apellido1, empleado.oficina.ciudad, empleado.jefe.nombre)

Empleado.empleadoInfo(session)


Oficina.mostrar_todas_las_oficinas(session)

Oficina.mostrar_oficina_por_id(session, 5)










