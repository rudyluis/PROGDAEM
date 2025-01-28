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

#AgregarOficina
oficinas = session.query(Oficina).all()
print(oficinas)

# %%
oficinas = session.query(Oficina).all()

for oficina in oficinas:
    print(oficina.ciudad)

empleados = session.query(Empleado).all()
# %%
# buscar todas las oficinas 
oficinas= session.query(Oficina).filter(Oficina.region=='Barcelona').all()
for oficina in oficinas:
    print(oficina.ciudad)
# %%
from ORM import Oficina, Producto, Empleado, Cliente
from sqlalchemy import or_, and_, func
result= session.query(Producto.nombre, func.count(Producto.idproducto)).\
        group_by(Producto.nombre).\
        having(func.count(Producto.idproducto)>5).all()

for nombre_producto, contar in result:
    print(f"Producto:{nombre_producto}  Cantidad:{contar}")
# %%
