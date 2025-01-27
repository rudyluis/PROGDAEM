from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session,relationship

# Conectar a la base de datos
engine = create_engine('postgresql://postgres:123456@localhost/jardineria2')
# Crear una instancia de AutomapBase
Base = automap_base()

# Reflejar las tablas de la base de datos
Base.prepare(engine, reflect=True)

# Acceder a las clases generadas automáticamente
Oficina = Base.classes.oficina
Empleado = Base.classes.empleado
GamaProducto = Base.classes.gamaproducto
Cliente = Base.classes.cliente
Pedido = Base.classes.pedido
Producto = Base.classes.producto
DetallePedido = Base.classes.detallepedido
Pago = Base.classes.pago



# Crear una sesión de SQLAlchemy
session = Session(engine)

# Consultar datos utilizando las clases ORM generadas automáticamente
oficinas = session.query(Oficina).all()

for oficina in oficinas:
    print(oficina.ciudad)

empleados = session.query(Empleado).all()
