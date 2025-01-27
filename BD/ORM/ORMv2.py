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
    @staticmethod
    def mostrar_oficina_por_id(session, id_oficina):
        oficina= session.query(Oficina).filter(Oficina.idoficina== id_oficina).first()
        if oficina:
            print('OFICINA ENCONTRADA')
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
        else: 
            print('No existe la Oficina mencionada')
    @staticmethod
    def agregarOficina(session, codigooficina, ciudad, pais, codigopostal, telefono, lineadireccion1, lineadireccion2, region= None):
        nueva_oficina=Oficina(codigooficina=codigooficina, ciudad=ciudad, 
                              pais= pais, codigopostal= codigopostal, telefono= telefono, 
                              lineadireccion1=lineadireccion1, lineadireccion2=lineadireccion2, region=region)
        
        session.add(nueva_oficina)
        session.commit()
        print('Se agregado una nueva oficina')

    @staticmethod
    def modificarOficina(session, id_oficina, **kwargs):
        oficina= session.query(Oficina).filter_by(idoficina=id_oficina).first()
        if oficina:
            for key, value in kwargs.items():
                setattr(oficina, key,value)
            session.commit()
            print('Oficina Actualizada')
        else:
            print('oficina no encontrada')
    
    @staticmethod
    def eliminarOficina(session, id_oficina):
        oficina= session.query(Oficina).filter_by(idoficina=id_oficina).first()
        if oficina:
            session.delete(oficina)
            session.commit()
            print('Oficina Eliminada')
        else:
            print('Oficina no encontrada')

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
    @staticmethod
    def agregarEmpleado(session, codigo_empleado, nombre, apellido1, apellido2, extension, email, id_oficina, id_empleado_jefe, puesto= None):
        nuevoEmpleado= Empleado( codigo_empleado= codigo_empleado, nombre= nombre, apellido1= apellido1,
                                    apellido2=apellido2, extension=extension, email= email, 
                                     idoficina = id_oficina, idempleadojefe= id_empleado_jefe, puesto=puesto                   
                                )
        session.add(nuevoEmpleado)
        session.commit()
        print("Empleado agregado correctamente")
    
    @staticmethod
    def modificarEmpleado(session, id_empleado, **kwargs):
        empleado= session.query(Empleado).filter_by(idempleado=id_empleado).first()
        if empleado:
            for key, value in kwargs.items():
                setattr(empleado, key,value)
            session.commit()
            print('Empleado Actualizado')
        else:
            print('Empleado no encontrado')

    @staticmethod
    def eliminarEmpleado(session, id_empleado):
        empleado= session.query(Empleado).filter_by(idempleado=id_empleado).first()
        if empleado:
            session.delete(empleado)
            session.commit()
            print('Empleado eliminado')
        else:
            print('No existe el empleado')

class GamaProducto(Base):
    __tablename__ = 'gamaproducto'
    idgamaproducto = Column(Integer, primary_key=True)
    gama = Column(String(50), nullable=True)
    descripciontexto = Column(String)  #
    descripcionhtml = Column(String)    #
    imagen = Column(String(256))   #

class Producto(Base):
    __tablename__ = 'producto'
    idproducto = Column(Integer, primary_key=True)
    codigo_producto = Column(String(15), nullable=False, unique=True)
    nombre = Column(String(70), nullable=False)
    idgamaproducto = Column(Integer, ForeignKey('gamaproducto.idgamaproducto'), nullable=False)  ###
    dimensiones = Column(String(25))
    proveedor = Column(String(50))
    descripcion = Column(String)  ####
    cantidad_stock = Column(Integer, nullable=False)
    precio_venta = Column(Numeric(15, 2), nullable=False)
    precio_proveedor = Column(Numeric(15, 2))
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
    limitecredito=Column(Numeric (15,2))   ###

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
    @staticmethod
    def mostrar_todos_los_pedidos(session):
        pedidos = session.query(Pedido).all()
        for pedido in pedidos:
            print("ID de Pedido:", pedido.idpedido)
            print("Código de Pedido:", pedido.codigopedido)
            print("Fecha de Pedido:", pedido.fecha_pedido)
            print("Fecha Esperada:", pedido.fecha_esperada)
            print("Fecha de Entrega:", pedido.fecha_entrega)
            print("Estado:", pedido.estado)
            print("Comentarios:", pedido.comentarios)
            print("ID de Cliente:", pedido.idcliente)
            print("------------------------------------------")

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
    __tablename__ = 'Pago'
    idpago =Column(Integer,primary_key=True)
    idcliente = Column(Integer,ForeignKey('cliente.idcliente'), nullable=False)  ###
    formapago = Column(String(40),nullable=False)
    nrotransaccion = Column(String(50),nullable=False)
    fechapago = Column(Date,nullable=False)
    total = Column(Numeric(15,2),nullable=False)
    cliente=relationship("Cliente")
    

