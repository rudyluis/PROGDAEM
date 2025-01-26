INSERT INTO sucursal (direccion, numeroSucursal, NIT)
VALUES
    ('Calle Ayoreo, Ciudad Cochabamba', 1, '1234556'),
    ('Calle Ramon Rivero, Ciudad Cochabamba', 2, '4826962015');

INSERT INTO cliente (nombre, apellidoPaterno, apellidoMaterno, email, ci, fechaNacimiento)
VALUES
    ('Juan', 'Pérez', 'González', 'juan.perez@email.com', 1234567890, '1990-05-15'),
    ('María', 'López', 'Fernández', 'maria.lopez@email.com', 9876543210, '1992-08-20'),
    ('Pedro', 'Rodríguez', 'Martínez', 'pedro.rodriguez@email.com', 5555555555, '1985-03-10'),
    ('Laura', 'García', 'Hernández', 'laura.garcia@email.com', 3333333333, '1995-11-30'),
    ('Carlos', 'Martínez', 'Sánchez', 'carlos.martinez@email.com', 6666666666, '1988-02-18');

INSERT INTO direccion (numero, calle, latitud, longitud, edificio, piso, IDCliente)
VALUES
    (123, 'Calle Principal', -12.34567, 45.67890, 'Edificio A', 'Piso 5', 1),
    (456, 'Avenida Secundaria', -12.98765, 67.89012, 'Edificio B', 'Piso 3', 2),
    (789, 'Calle de Ejemplo', -11.11111, 33.33333, NULL, NULL, 3),
    (101, 'Avenida Principal', -9.87654, 21.43210, 'Edificio C', 'Piso 2', 4),
    (202, 'Avenida del Centro', -8.76543, 12.34567, NULL, NULL, 5);

INSERT INTO telefono (numeroTelefono, IDCliente)
VALUES
    (1234567890, 1),
    (9876543210, 2),
    (5555555555, 3),
    (7777777777, 4),
    (9999999999, 5);

INSERT INTO clasificacion (nombreClasificacion)
VALUES
    ('Apta para todos los públicos'),
    ('Mayores de 12 años'),
    ('Mayores de 18 años'),
    ('Mayores de 18 años con restricciones'),
    ('No recomendada para menores de 18 años');

INSERT INTO pelicula (duracion, titulo, sinopsis, IDClasificacion)
VALUES
    (120, 'La Aventura Épica', 'Una emocionante aventura en busca de tesoros perdidos.', 1),
    (105, 'Amor en París', 'Una romántica historia de amor en la ciudad de las luces.', 2),
    (140, 'Atracción Fatal', 'Un thriller psicológico sobre obsesiones peligrosas.', 3),
    (95, 'Comedia Loca', 'Una comedia hilarante llena de situaciones cómicas.', 4),
    (130, 'Misterio en el Abismo', 'Un misterio oscuro en alta mar que desafía la lógica.', 2);

INSERT INTO SucursalPelicula (IDSucursal, IDPelicula, fechaDebut)
VALUES
    (1, 1, '2023-10-01'),
    (2, 2, '2023-10-01'),
    (1, 3, '2023-10-01'),
    (2, 4, '2023-10-01'),
    (1, 5, '2023-10-01');

INSERT INTO funcion (fecha, hora, precio, disponibilidad, IDPelicula)
VALUES
    ('2023-10-10', '18:30:00', 8.50, TRUE, 1),
    ('2023-10-10', '20:45:00', 9.75, TRUE, 2),
    ('2023-10-11', '14:00:00', 7.25, TRUE, 3),
    ('2023-10-11', '16:30:00', 10.00, TRUE, 4),
    ('2023-10-12', '19:15:00', 8.00, TRUE, 5);

INSERT INTO reserva (codigoReserva, fechaReserva, estadoReserva, totalReserva, IDCliente, IDFuncion)
VALUES
    ('ABC123', '2023-10-09 15:30:00', 'PAGADO', 18.75, 1, 1),
    ('DEF456', '2023-10-10 10:45:00', 'RESERVADO', 15.50, 2, 2),
    ('GHI789', '2023-10-11 12:15:00', 'PAGADO', 20.00, 3, 3),
    ('JKL012', '2023-10-12 14:00:00', 'PAGADO', 22.25, 4, 4),
    ('MNO345', '2023-10-12 16:30:00', 'RESERVADO', 19.00, 5, 5);

INSERT INTO genero (nombreGenero)
VALUES
    ('Acción'),
    ('Comedia'),
    ('Drama'),
    ('Ciencia Ficción'),
    ('Romance');

INSERT INTO sala (numeroSala, capacidad, sonido, tipoPantalla, IDFuncion)
VALUES
    (1, 200, 'STEREO', 'Plana', 1),
    (2, 150, 'SURROUND', 'Curva', 2),
    (3, 180, 'STEREO', 'Plana', 3),
    (4, 100, 'MONOAURAL', '3D', 4),
    (5, 220, 'SURROUND', 'Plana', 5);

INSERT INTO GeneroPelicula (IDGenero, IDPelicula)
VALUES
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4);

INSERT INTO asiento (numeroAsiento, fila, estado, IDReserva)
VALUES
    (101, 'A', 'Ocupado', 1),
    (202, 'B', 'Libre', 2),
    (303, 'C', 'Ocupado', 3),
    (404, 'D', 'Ocupado', 4),
    (505, 'E', 'Libre', 5);

INSERT INTO usuario (nombreUsuario, IDCliente)
VALUES
    ('Usuario1', 1),
    ('Usuario2', 2),
    ('Usuario3', 3),
    ('Usuario4', 4),
    ('Usuario5', 5);

INSERT INTO passwords (clave, idUsuario, fechaRegistroPassword, fechaModifPassword, estado)
VALUES
    ('clave1', 1, '2023-10-10', '2023-10-15', 1),
    ('clave2', 2, '2023-10-11', '2023-10-16', 1),
    ('clave3', 3, '2023-10-12', '2023-10-17', 1),
    ('clave4', 4, '2023-10-13', '2023-10-18', 1),
    ('clave5', 5, '2023-10-14', '2023-10-19', 1);

INSERT INTO pago (fechaPago, metodoPago, montoPago, estadoPago, IDReserva)
VALUES
    ('2023-09-01', 'Tarjeta de Crédito', 50.50, 'Pagado', 1),
    ('2023-09-02', 'Efectivo', 30.00, 'Pagado', 2),
    ('2023-09-03', 'PayPal', 25.00, 'Pendiente', 3),
    ('2023-09-04', 'Tarjeta de Débito', 40.00, 'Pagado', 4),
    ('2023-09-05', 'Efectivo', 60.00, 'Pagado', 5);

INSERT INTO tipoPago (tokenSeguridad, codigoComprobante, IDpago)
VALUES
    ('ABC123', 'XYZ789', 1),
    ('DEF456', 'UVW101', 2),
    ('GHI789', 'RST222', 3),
    ('JKL012', 'MNO333', 4),
    ('PQR456', 'STU444', 5);

INSERT INTO facturacion (numeroFacturacion, monto, codigoCUF, fechaFacturacion, IDPago)
VALUES
    (12345, 50.00, 'ABC123', '2023-09-01', 1),
    (67890, 30.00, 'DEF456', '2023-09-02', 2),
    (54321, 25.00, 'GHI789', '2023-09-03', 3),
    (98765, 40.00, 'JKL012', '2023-09-04', 4),
    (23456, 60.00, 'MNO345', '2023-09-05', 5);

INSERT INTO pelicula (duracion, titulo, sinopsis, IDClasificacion) VALUES
(120, 'El Gran Estreno', 'Una emocionante película de acción.', 3),
(105, 'Aventuras en la Selva', 'Una película animada para toda la familia.', 1),
(90, 'El Misterio del Pasado', 'Un thriller de misterio intrigante.', 2),
(135, 'Cazadores del Espacio', 'Ciencia ficción en el espacio profundo.', 3),
(110, 'Comedia Nocturna', 'Una comedia que te hará reír a carcajadas.', 1);

INSERT INTO efectivo (tc, montoCambio, IDTipoPago) VALUES
  (6.86, 70.00, 2),
  (6.86, 105, 5);

INSERT INTO QR (codigoQR, estadoQR, fechaGeneracion, fechaExpiracionQR, IDTipoPago) VALUES
  ('123DEF', 'Expirado', '2023-11-14', '2023-11-19', 3);

INSERT INTO tarjeta (numeroTarjeta,  IDTipoPago) VALUES
  ('1111222233334444',  1),
  ('4444555566667777',  4);
