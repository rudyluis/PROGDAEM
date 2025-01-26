

-- Estructura de tabla para la tabla cliente
CREATE TABLE cliente (
  IDCliente serial PRIMARY KEY,
  CI varchar(45) NOT NULL,
  nombre varchar(45) NOT NULL,
  apellidoPaterno varchar(45) NOT NULL,
  apellidoMaterno varchar(45) NOT NULL,
  ciudad varchar(45),
  categoria int
);

-- Volcado de datos para la tabla cliente
INSERT INTO cliente (CI, nombre, apellidoPaterno, apellidoMaterno, ciudad, categoria) VALUES
('1234567', 'Aarón', 'Rivero', 'Gómez', 'Almería', 100),
('1239876', 'Adela', 'Salas', 'Díaz', 'Granada', 200),
('2345967', 'Adolfo', 'Rubio', 'Flores', 'Sevilla', NULL),
('4356789', 'Adrián', 'Suárez', 'Sanchez', 'Jaén', 300),
('4826965', 'Marcos', 'Loyola', 'Méndez', 'Almería', 200),
('8967453', 'María', 'Santana', 'Moreno', 'Cádiz', 100),
('9876541', 'Pilar', 'Ruiz', 'Lopez', 'Sevilla', 300),
('3456782', 'Pepe', 'Ruiz', 'Santana', 'Huelva', 200),
('4876789', 'Guillermo', 'López', 'Gómez', 'Granada', 225),
('2315678', 'Daniel', 'Santana', 'Loyola', 'Sevilla', 125);


-- Estructura de tabla para la tabla producto
CREATE TABLE producto (
  IDProducto serial PRIMARY KEY,
  codigo_producto varchar(15) NOT NULL,
  nombre varchar(70) NOT NULL,
  descripcion text,
  cantidadStock smallint NOT NULL,
  precioVenta numeric(18,2) NOT NULL
);

-- Volcado de datos para la tabla producto
INSERT INTO producto (codigo_producto, nombre, descripcion, cantidadStock, precioVenta) VALUES
('001', 'Coca Cola 2 Ltrs', 'Coca Cola de 2 Litros', 100, '13.00'),
('002', 'Cerveza', 'Cerveza Tradicional Lata', 50, '10.00'),
('003', 'Galleta', 'Galleta Mabel', 45, '5.50'),
('004', 'Pan', 'Pan Molde Kilo', 25, '10.00'),
('005', 'Carne ', 'Carna Kilo Ahumada', 50, '36.50'),
('006', 'Pesi', 'Pepsi de 3 Litros', 40, '11.00'),
('007', 'Duraznos al Jugo', 'Duraznos al Jugo Enlatado', 23, '16.00');

-- Estructura de tabla para la tabla vendedor
CREATE TABLE vendedor (
  IDVendedor serial PRIMARY KEY,
  nombreVendedor varchar(45),
  apellidoPaterno varchar(45),
  apellidoMaterno varchar(45),
  CI varchar(45),
  ciudad varchar(45),
  comision numeric(10,2)
);

-- Volcado de datos para la tabla vendedor
INSERT INTO vendedor (nombreVendedor, apellidoPaterno, apellidoMaterno, CI, ciudad, comision) VALUES
('Daniel', 'Sáez', 'Vega', '2345678', 'Almería', '0.15'),
('Juan', 'Gómez', 'López', '345678', 'Almería', '0.13'),
('Diego', 'Flores', 'Salas', '2154678', 'Almería', '0.11'),
('Marta', 'Herrera', 'Gil', '4826963', 'Sevilla', '0.14'),
('Antonio', 'Carretero', 'Ortega', '2345668', 'Sevilla', '0.12'),
('Manuel', 'Domínguez', 'Hernández', '2345638', 'Sevilla', '0.13');

-- Estructura de tabla para la tabla pedido
CREATE TABLE pedido (
  IDPedido serial PRIMARY KEY,
  nroPedido varchar(45),
  fecha date,
  estado varchar(45),
  IDcliente int NOT NULL,
  IDVendedor int NOT NULL,
  FOREIGN KEY (IDcliente) REFERENCES cliente (IDCliente),
  FOREIGN KEY (IDVendedor) REFERENCES vendedor (IDVendedor)
);

-- Volcado de datos para la tabla pedido
INSERT INTO pedido (nroPedido, fecha, estado, IDcliente, IDVendedor) VALUES
('001', '2023-12-01', 'Pendiente', 1, 1),
('002', '2023-12-02', 'Entregado', 2, 2),
('003', '2023-12-02', 'Entregado', 3, 3),
('004', '2023-12-03', 'Pendiente', 4, 4),
('005', '2023-12-03', 'Cancelado', 5, 5),
('006', '2023-12-03', 'Entregado', 6, 6),
('007', '2023-12-03', 'Pendiente', 7, 1),
('008', '2023-12-03', 'Entregado', 8, 2),
('009', '2023-12-03', 'Cancelado', 9, 3),
('010', '2023-12-03', 'Entregado', 10, 4);

-- Estructura de tabla para la tabla detallepedido
CREATE TABLE detallepedido (
  IDDetallePedido serial PRIMARY KEY,
  IDPedido int NOT NULL,
  IDProducto int NOT NULL,
  cantidad numeric(18,2) NOT NULL,
  numeroLinea smallint NOT NULL,
  FOREIGN KEY (IDPedido) REFERENCES pedido (IDPedido),
  FOREIGN KEY (IDProducto) REFERENCES producto (IDProducto)
);

-- Volcado de datos para la tabla detallepedido
INSERT INTO detallepedido (IDPedido, IDProducto, cantidad, numeroLinea) VALUES
(1, 1, '2.00', 1),
(1, 2, '1.00', 2),
(1, 1, '2.00', 1),
(1, 2, '1.00', 2),
(2, 3, '3.00', 1),
(3, 4, '2.00', 1),
(4, 5, '2.00', 1),
(5, 6, '3.00', 1),
(6, 7, '5.00', 1),
(7, 1, '2.00', 1),
(7, 6, '3.00', 2),
(8, 4, '2.00', 1),
(8, 5, '1.00', 2),
(9, 6, '2.00', 1),
(9, 7, '2.00', 2),
(10, 1, '5.00', 1),
(10, 5, '10.00', 2),
(10, 7, '10.00', 3),
(10, 4, '3.00', 4);



-- Crear la tabla de registro de cambios
CREATE TABLE registro_cambios (
  id serial PRIMARY KEY,
  producto_id int,
  fecha timestamp DEFAULT current_timestamp,
  stock_anterior int,
  stock_nuevo int
);

-- Crear la función que será llamada por el trigger
CREATE OR REPLACE FUNCTION registrar_cambio()
RETURNS TRIGGER AS $$
BEGIN
  -- Insertar un registro en la tabla de registro_cambios
  INSERT INTO registro_cambios (producto_id, stock_anterior, stock_nuevo)
  VALUES (NEW.idProducto, OLD.cantidadstock, NEW.cantidadstock);

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Crear el trigger que se activará después de una actualización en la tabla de productos
DROP TRIGGER IF EXISTS after_update_stock ON producto;
CREATE TRIGGER after_update_stock
AFTER UPDATE
ON producto
FOR EACH ROW
EXECUTE FUNCTION registrar_cambio();


