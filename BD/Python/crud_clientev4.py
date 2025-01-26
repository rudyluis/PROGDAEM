from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir el motor y crear la sesión
engine = create_engine('postgresql://user:password@localhost:5432/database')
Session = sessionmaker(bind=engine)
session = Session()

# Definir la clase de la tabla Cliente
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    codigoCliente = Column(Integer)
    nombreCliente = Column(String)
    nombreContacto = Column(String)
    apellidoContacto = Column(String)
    telefono = Column(String)
    fax = Column(String)
    lineaDireccion1 = Column(String)
    lineaDireccion2 = Column(String)
    ciudad = Column(String)
    region = Column(String)
    pais = Column(String)
    codigoPostal = Column(String)
    IDcodigoEmpleadoVentas = Column(Integer)
    limiteCredito = Column(Numeric)

# Función para insertar un nuevo cliente
def insertar_cliente(codigoCliente, nombreCliente, nombreContacto, apellidoContacto, telefono, fax, lineaDireccion1, lineaDireccion2, ciudad, region, pais, codigoPostal, IDcodigoEmpleadoVentas, limiteCredito):
    cliente = Cliente(codigoCliente=codigoCliente, nombreCliente=nombreCliente, nombreContacto=nombreContacto, apellidoContacto=apellidoContacto, telefono=telefono, fax=fax, lineaDireccion1=lineaDireccion1, lineaDireccion2=lineaDireccion2, ciudad=ciudad, region=region, pais=pais, codigoPostal=codigoPostal, IDcodigoEmpleadoVentas=IDcodigoEmpleadoVentas, limiteCredito=limiteCredito)
    session.add(cliente)
    session.commit()

# Función para actualizar un cliente existente
def actualizar_cliente(id_cliente, **kwargs):
    cliente = session.query(Cliente).get(id_cliente)
    if cliente:
        for key, value in kwargs.items():
            setattr(cliente, key, value)
        session.commit()
    else:
        print("Cliente no encontrado.")

# Función para eliminar un cliente existente
def eliminar_cliente(id_cliente):
    cliente = session.query(Cliente).get(id_cliente)
    if cliente:
        session.delete(cliente)
        session.commit()
    else:
        print("Cliente no encontrado.")

# Ejemplo de uso
if __name__ == '__main__':
    # Insertar un nuevo cliente
    insertar_cliente(codigoCliente=1, nombreCliente='Cliente 1', nombreContacto='Contacto 1', apellidoContacto='Apellido 1', telefono='123456789', fax='', lineaDireccion1='Dirección 1', lineaDireccion2='', ciudad='Ciudad 1', region='Región 1', pais='País 1', codigoPostal='12345', IDcodigoEmpleadoVentas=1, limiteCredito=1000.00)

    # Actualizar el nombre de un cliente existente
    actualizar_cliente(id_cliente=1, nombreCliente='Nuevo Nombre')

    # Eliminar un cliente existente
    eliminar_cliente(id_cliente=1)
