##pip install psycopg2
##pip instal sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric, Text, Sequence

from sqlalchemy.orm import relationship, declarative_base

Base= declarative_base()

class Oficina(Base):
    __tablename__='oficina'
    idoficina= Column(Integer, primary_key=True)
    codigooficina=Column(String(10), unique=True, nullable=False)
    ciudad =Column(String(30), nullable=False)
    pais =Column(String(50), nullable=False)
    region =Column(String(50))
    codigopostal=Column(String(50), nullable=False)
    telefono=Column(String(20), nullable=False)
    lineadireccion1=Column(String(50), nullable=False)
    lineadireccion2=Column(String(50))
    empleado= relationship('Empleado', back_populates='oficina')

    @staticmethod
    def mostrar_todas_las_oficinas(session):
        oficinas = session.query(Oficina).all()
        for oficina in oficinas:
            print("ID de Oficina:", oficina.idoficina)
            print("Código de Oficina:", oficina.codigooficina)
            print("Ciudad:", oficina.ciudad)
            print("País:", oficina.pais)
            print("Región:", oficina.region)
            print("Código Postal:", oficina.codigopostal)
            print("Teléfono:", oficina.telefono)
            print("Línea de Dirección 1:", oficina.lineadireccion1)
            print("Línea de Dirección 2:", oficina.lineadireccion2)
            print("-------------------------------------------")
    
class Empleado(Base):
    __tablename__ = 'empleado'
    idempleado = Column(Integer, primary_key=True)
    codigo_empleado = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    apellido1 = Column(String(50), nullable=False)
    apellido2 = Column(String(50))
    extension = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    idoficina= Column(Integer, ForeignKey('oficina.idoficina'), nullable=False)
    idempleadojefe= Column(Integer, ForeignKey('empleado.idempleado'))
    puesto = Column(String(50))
    
    oficina= relationship('Oficina', back_populates='empleado')
    jefe = relationship('Empleado', remote_side=[idempleado])

    @staticmethod
    def empleadoInfo(session):
        empleados = session.query(Empleado).all()
        for empleado in empleados:
            print("ID de Empleado:", empleado.idempleado)
            print("Código de Empleado:", empleado.codigo_empleado)
            print("Nombre:", empleado.nombre)
            print("Apellido 1:", empleado.apellido1)
            print("Apellido 2:", empleado.apellido2)
            print("Extensión:", empleado.extension)
            print("Email:", empleado.email)
            print("ID de Oficina:", empleado.idoficina)
            print("Puesto:", empleado.puesto)
            if empleado.jefe:
                print("ID del Jefe:", empleado.jefe.idempleado)
                print("Nombre del Jefe:", empleado.jefe.nombre)
            else:
                print("JEFE")
            print("--------------------------")
    
class GamaProducto(Base):
    __tablename__ = 'gamaproducto'
    idgamaproducto = Column(Integer, primary_key=True)
    gama = Column(String(50), nullable=True)
    descripciontexto = Column(String)  #
    descripcionhtml = Column(String)    #
    imagen = Column(String(256))   #
    def mostrar_todas_las_gamaProductos(session):
        gamaproductos = session.query(GamaProducto).all()
        for gamaproducto in gamaproductos:
            print("ID de gamaProducto:", gamaproducto.idgamaproducto)
            print("Nombres de la Gama Producto:", gamaproducto.gama)
            print("Descripcion en texto de la Gama Producto:", gamaproducto.descripciontexto)
            print("Descripcion en html de la Gama Producto:", gamaproducto.descripcionhtml)
            print("Imagen la Gama Producto:", gamaproducto.imagen)
            print("-------------------------------------------")

class Producto(Base):
    __tablename__ = 'producto'
    idproducto = Column(Integer, primary_key=True)
    codigo_producto = Column(String(15), nullable=False, unique=True)
    nombre = Column(String(70), nullable=False)
    idgamaproducto = Column(Integer, ForeignKey('gamaproducto.idgamaproducto'), nullable=False)  ###
    dimensiones = Column(String(25))
    proveedor = Column(String(50))
    descripcion = Column(String)  ####
    cantidadstock = Column(Integer, nullable=False)
    precioventa = Column(Numeric(15, 2), nullable=False)
    precioproveedor = Column(Numeric(15, 2))
    gama_producto = relationship('GamaProducto')
    
class Cliente(Base):
    __tablename__='cliente'
    idcliente= Column(Integer, primary_key=True)
    codigocliente=Column(Integer,unique=True, nullable=False)
    nombrecliente=Column(String(50), nullable=False)
    nombrecontacto=Column(String(50), nullable=False)
    apellidocontacto=Column(String(50), nullable=False)
    telefono=Column(String(15), nullable=False)
    fax=Column(String(15))
    lineadireccion1= Column(String(50), nullable=False)
    lineadireccion2= Column(String(50))
    ciudad= Column(String(30), nullable=False)
    region= Column(String(50))
    pais= Column(String(50), nullable=False)
    codigopostal=Column(String(30), nullable=False)
    idcodigoempleadoventas=Column(Integer, ForeignKey('empleado.idempleado'),nullable=False)
    limite_credito=Column(Numeric (15,2))   ###

    ###empleadoventas= relationship('Empleado', backref="cliente")
    empleadoventas= relationship('Empleado')
    

class Pedido(Base):
    __tablename__ = 'pedido'
    idpedido = Column(Integer, primary_key=True)
    codigopedido = Column(String(10), unique=True, nullable=False)
    fechapedido = Column(Date, nullable=False)  ##
    fechaesperada = Column(Date, nullable=False)  ##
    fechaentrega = Column(Date)   ##
    estado = Column(String(15), nullable=False)
    comentarios = Column(String)
    idcliente = Column(Integer, ForeignKey('cliente.idcliente'), nullable=False)
    cliente = relationship("Cliente")   ###
    
class DetallePedido(Base):
    __tablename__ = 'detallepedido'
    iddetallepedido = Column(Integer, primary_key=True, nullable=False)
    idproducto = Column(Integer, ForeignKey('producto.idproducto'),nullable=False)
    idpedido = Column(Integer, ForeignKey('pedido.idpedido'),nullable=False)
    cantidad = Column(Integer,nullable=False)
    preciounidad = Column(Numeric(15,2),nullable=False)
    numerolinea = Column(Integer,nullable=False)
    pedido = relationship("Pedido")
    producto = relationship("Producto")
    
    
class Pago(Base):
    __tablename__ = 'pago'
    idpago =Column(Integer,primary_key=True)
    idcliente = Column(Integer,ForeignKey('cliente.idcliente'), nullable=False)  ###
    formapago = Column(String(40),nullable=False)
    nrotransaccion = Column(String(50),nullable=False)
    fechapago = Column(Date,nullable=False)
    total = Column(Numeric(15,2),nullable=False)
    cliente=relationship("Cliente")

    
