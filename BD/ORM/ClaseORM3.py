from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ORM import Oficina, Empleado

engine= create_engine('postgresql://postgres:123456@localhost/jardineria')

#Crea una sesion
Session= sessionmaker(bind=engine)
session= Session()

#AgregarOficina
oficinas = session.query(Oficina).all()
##Oficina.agregarOficina(session,codigooficina="1005", ciudad="Venecia", pais="Italia", 
  ##                     codigopostal="1001", telefono="7896541", lineadireccion1="Calle Perfum", 
    ##                   lineadireccion2="Ave Amore", region="Norte")


##Oficina.modificarOficina(session,14, codigooficina="1000",ciudad="Roma",telefono= "1234567")

##Oficina.eliminarOficina(session,14)


##Empleado.agregarEmpleado(session,codigo_empleado="55",nombre="Gustavo",apellido1="Lopez",
                   ##      apellido2="Sanchez",extension="22599",
                    ##    email="gustavolosa@gmail.com",id_oficina="3",
                    ##    id_empleado_jefe="1",puesto="Directo Oficina")

##Empleado.modificarEmpleado(session, 32, nombre="Antonio")
Empleado.eliminarEmpleado(session,32)







