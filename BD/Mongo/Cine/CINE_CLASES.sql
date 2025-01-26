CREATE TABLE sucursal (
    IDSucursal SERIAL PRIMARY KEY,
    direccion VARCHAR(45) NOT NULL,
    numeroSucursal INT NOT NULL,
    nit VARCHAR(45) NOT NULL UNIQUE
);

CREATE TABLE clasificacion (
    IDClasificacion SERIAL PRIMARY KEY,
    nombreClasificacion VARCHAR(45) NOT NULL
);

CREATE TABLE pelicula (
    IDPelicula SERIAL PRIMARY KEY,
    duracion INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    sinopsis TEXT NOT NULL,
    IDClasificacion INT,
    FOREIGN KEY (IDClasificacion) REFERENCES clasificacion(IDClasificacion)
);

CREATE TABLE sucursalpelicula (
    IDPSucursalPelicula SERIAL PRIMARY KEY,
    IDSucursal INT,
    IDPelicula INT,
    fechaDebut DATE NOT NULL,
    FOREIGN KEY (IDSucursal) REFERENCES sucursal(IDSucursal),
    FOREIGN KEY (IDPelicula) REFERENCES pelicula(IDPelicula)
);

CREATE TABLE genero (
    IDGenero SERIAL PRIMARY KEY,
    nombreGenero VARCHAR(45) NOT NULL
);

CREATE TABLE generoPelicula (
    IDGeneroPelicula SERIAL PRIMARY KEY,
    IDGenero INT,
    IDPelicula INT,
    FOREIGN KEY (IDGenero) REFERENCES genero(IDGenero),
    FOREIGN KEY (IDPelicula) REFERENCES pelicula(IDPelicula)
);

CREATE TABLE funcion (
    IDFuncion SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    precio DECIMAL(18,2) NOT NULL,
    disponibilidad BOOLEAN NOT NULL,
    IDPelicula INT NOT NULL,
    FOREIGN KEY (IDPelicula) REFERENCES pelicula(IDPelicula)
);

CREATE TABLE sala (
    IDSala SERIAL PRIMARY KEY,
    numeroSala INT NOT NULL,
    capacidad INT NOT NULL,
    tipoPantalla VARCHAR(10),
    sonido VARCHAR(10),
    IDFuncion INT NOT NULL,
    FOREIGN KEY (IDFuncion) REFERENCES funcion(IDFuncion)
);

CREATE TABLE cliente (
    IDCliente SERIAL PRIMARY KEY,
    nombre VARCHAR(45),
    apellidoPaterno VARCHAR(45),
    apellidoMaterno VARCHAR(45),
    email VARCHAR(45) UNIQUE,
    ci BIGINT NOT NULL UNIQUE,
    fechaNacimiento DATE NOT NULL
);

CREATE TABLE direccion (
    IDDireccion SERIAL PRIMARY KEY,
    numero INT NOT NULL,
    calle VARCHAR(45) NOT NULL,
    latitud DECIMAL(10,5) NOT NULL,
    longitud DECIMAL(10,5) NOT NULL,
    edificio VARCHAR(45),
    piso VARCHAR(45),
    IDCliente INT NOT NULL,
    FOREIGN KEY (IDCliente) REFERENCES cliente(IDCliente)
);

CREATE TABLE reserva (
    IDReserva SERIAL PRIMARY KEY,
    codigoReserva VARCHAR(45) NOT NULL,
    fechaReserva TIMESTAMP NOT NULL,
    estadoReserva VARCHAR(10) NOT NULL,
    totalReserva DECIMAL(18,2),
    IDCliente INT NOT NULL,
    IDFuncion INT NOT NULL,
    FOREIGN KEY (IDCliente) REFERENCES cliente(IDCliente),
    FOREIGN KEY (IDFuncion) REFERENCES funcion(IDFuncion)
);

CREATE TABLE usuario (
    IDUsuario SERIAL PRIMARY KEY,
    nombreUsuario VARCHAR(45) NOT NULL,
    IDCliente INT,
    FOREIGN KEY (IDCliente) REFERENCES cliente(IDCliente)
);

CREATE TABLE passwords (
    IDPassword SERIAL PRIMARY KEY,
    clave VARCHAR(45),
    idUsuario INT NOT NULL,
    fechaRegistroPassword DATE,
    fechaModifPassword DATE,
    estado INT,
    FOREIGN KEY (idUsuario) REFERENCES usuario(IDUsuario)
);

CREATE TABLE telefono (
    IDTelefono SERIAL PRIMARY KEY,
    numeroTelefono BIGINT NOT NULL,
    IDCliente INT,
    FOREIGN KEY (IDCliente) REFERENCES cliente(IDCliente)
);

CREATE TABLE asiento (
    IDAsiento SERIAL PRIMARY KEY,
    numeroAsiento INT NOT NULL,
    fila VARCHAR(5) NOT NULL,
    estado VARCHAR(10),
    IDReserva INT,
    FOREIGN KEY (IDReserva) REFERENCES reserva(IDReserva)
);

CREATE TABLE pago (
    IDPago SERIAL PRIMARY KEY,
    fechaPago DATE NOT NULL,
    metodoPago VARCHAR(25) NOT NULL,
    montoPago DECIMAL(18,2) NOT NULL,
    estadoPago VARCHAR(10) NOT NULL,
    IDReserva INT,
    FOREIGN KEY (IDReserva) REFERENCES reserva(IDReserva)
);

CREATE TABLE facturacion (
    IDFacturacion SERIAL PRIMARY KEY,
    numeroFacturacion BIGINT NOT NULL,
    monto DECIMAL(18,2) NOT NULL,
    codigoCUF VARCHAR(100) NOT NULL,
    fechaFacturacion DATE NOT NULL,
    IDPago INT,
    FOREIGN KEY (IDPago) REFERENCES pago(IDPago)
);

CREATE TABLE tipoPago (
    IDTipoPago SERIAL PRIMARY KEY,
    tokenSeguridad VARCHAR(45) UNIQUE,
    codigoComprobante VARCHAR(45) UNIQUE,
    IDpago INT NOT NULL,
    FOREIGN KEY (IDPago) REFERENCES pago(IDPago)
);

CREATE TABLE tarjeta (
    IDTarjeta SERIAL PRIMARY KEY,
    numeroTarjeta VARCHAR(45),
    IDTipoPago INT NOT NULL,
    FOREIGN KEY (IDTipoPago) REFERENCES tipopago(IDTipoPago)
);

CREATE TABLE efectivo (
    IDEfectivo SERIAL PRIMARY KEY,
    tc DECIMAL(18,2),
    montoCambio DECIMAL(18,2),
    IDTipoPago INT NOT NULL,
    FOREIGN KEY (IDTipoPago) REFERENCES tipopago(IDTipoPago)
);

CREATE TABLE QR (
    IDQR SERIAL PRIMARY KEY,
    codigoQR BYTEA,
    estadoQR VARCHAR(10),
    fechaGeneracion DATE,
    fechaExpiracionQR DATE,
    QRcol VARCHAR(45),
    IDTipoPago INT,
    FOREIGN KEY (IDTipoPago) REFERENCES tipopago(IDTipoPago)
);
