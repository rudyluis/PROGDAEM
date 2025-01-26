--------------- EJERCICIO 1

CREATE OR REPLACE FUNCTION buscarPeliculaEnSucursales(titulo_pelicula VARCHAR) 
RETURNS TABLE(nombre_pelicula VARCHAR, direccion_sucursal VARCHAR) AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM pelicula WHERE titulo = titulo_pelicula) THEN
        RETURN QUERY
        SELECT p.titulo, s.direccion
        FROM pelicula p
        INNER JOIN sucursalpelicula sp ON p.IDPelicula = sp.IDPelicula
        INNER JOIN sucursal s ON sp.IDSucursal = s.IDSucursal
        WHERE p.titulo = titulo_pelicula;
    ELSE
        RETURN QUERY
        SELECT p.titulo, s.direccion
        FROM pelicula p
        INNER JOIN sucursalpelicula sp ON p.IDPelicula = sp.IDPelicula
        INNER JOIN sucursal s ON sp.IDSucursal = s.IDSucursal;
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM buscarPeliculaEnSucursales('');

------------------------------------------------------------------

CREATE OR REPLACE FUNCTION buscarPeliculaEnSucursales2(titulo_pelicula VARCHAR DEFAULT NULL) 
RETURNS TABLE(nombre_pelicula VARCHAR, direccion_sucursal VARCHAR) AS $$
DECLARE
    info RECORD;
BEGIN
    IF titulo_pelicula IS NOT NULL THEN
        FOR info IN 
            SELECT p.titulo, s.direccion
            FROM pelicula p
            INNER JOIN sucursalpelicula sp ON p.IDPelicula = sp.IDPelicula
            INNER JOIN sucursal s ON sp.IDSucursal = s.IDSucursal
            WHERE p.titulo = titulo_pelicula
        LOOP
            RETURN NEXT info;
        END LOOP;
    ELSE
        FOR info IN 
            SELECT p.titulo, s.direccion
            FROM pelicula p
            INNER JOIN sucursalpelicula sp ON p.IDPelicula = sp.IDPelicula
            INNER JOIN sucursal s ON sp.IDSucursal = s.IDSucursal
        LOOP
            RETURN NEXT info;
        END LOOP;
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM buscarPeliculaEnSucursales(NULL);


------------------ EJERCICIO 2

CREATE OR REPLACE FUNCTION buscarInfoPelicula(nombre_pelicula VARCHAR DEFAULT NULL)
RETURNS TABLE(nombre_pelicula_retorno VARCHAR, generos_pelicula VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT p.titulo, STRING_AGG(g.nombreGenero, ', ' ORDER BY g.nombreGenero) AS generos_pelicula
    FROM pelicula p
    LEFT JOIN generoPelicula gp ON p.IDPelicula = gp.IDPelicula
    LEFT JOIN genero g ON gp.IDGenero = g.IDGenero
    WHERE p.titulo ILIKE '%' || COALESCE(nombre_pelicula, '') || '%'
    GROUP BY p.titulo;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM buscarInfoPelicula();

------ EJERCICIO 3

CREATE OR REPLACE FUNCTION listarPagosConTipoPago()
RETURNS TABLE (
    IDPago INT,
    fechaPago DATE,
    metodoPago VARCHAR(25),
    montoPago DECIMAL(18,2),
    estadoPago VARCHAR(10),
    tipoPago VARCHAR(45)
) AS $$
BEGIN
    CREATE TEMP TABLE PagosTipoPago (
        IDPago INT,
        fechaPago DATE,
        metodoPago VARCHAR(25),
        montoPago DECIMAL(18,2),
        estadoPago VARCHAR(10),
        tipoPago VARCHAR(45)
    );

    INSERT INTO PagosTipoPago (IDPago, fechaPago, metodoPago, montoPago, estadoPago, tipoPago)
    SELECT p.IDPago, p.fechaPago, p.metodoPago, p.montoPago, p.estadoPago, tp.tokenSeguridad
    FROM pago p
    JOIN tipoPago tp ON p.IDPago = tp.IDPago;

    RETURN QUERY SELECT * FROM PagosTipoPago;
   
    DROP TABLE PagosTipoPago;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM listarPagosConTipoPago();

-------- EJERCICIO 4

CREATE OR REPLACE FUNCTION gestionarFuncion(
    operacion VARCHAR,
    id_funcion_param INT DEFAULT NULL,
    fecha_param DATE DEFAULT NULL,
    hora_param TIME DEFAULT NULL,
    precio_param DECIMAL DEFAULT NULL,
    disponibilidad_param BOOLEAN DEFAULT NULL,
    idPelicula_param INT DEFAULT NULL
) 
RETURNS TABLE (
    IDFuncion INT,
    fecha DATE,
    hora TIME,
    precio DECIMAL,
    disponibilidad BOOLEAN,
    IDPelicula INT
) AS $$
BEGIN
    CASE operacion
        WHEN 'CREATE' THEN
            INSERT INTO funcion (fecha, hora, precio, disponibilidad, idPelicula)
            VALUES (fecha_param, hora_param, precio_param, disponibilidad_param, idPelicula_param)
            RETURNING * INTO IDFuncion, fecha, hora, precio, disponibilidad, IDPelicula;
        WHEN 'READ' THEN
            RETURN QUERY 
            SELECT * FROM funcion WHERE IDFuncion = id_funcion_param;
        WHEN 'UPDATE' THEN
            UPDATE funcion 
            SET fecha = fecha_param, hora = hora_param, precio = precio_param, disponibilidad = disponibilidad_param, idPelicula = idPelicula_param
            WHERE IDFuncion = id_funcion_param
            RETURNING * INTO IDFuncion, fecha, hora, precio, disponibilidad, IDPelicula;
        WHEN 'DELETE' THEN
            DELETE FROM funcion WHERE IDFuncion = id_funcion_param
            RETURNING * INTO IDFuncion, fecha, hora, precio, disponibilidad, IDPelicula;
        ELSE
            RAISE EXCEPTION 'Operación no válida. Use CREATE, READ, UPDATE o DELETE.';
    END CASE;
END;
$$ LANGUAGE plpgsql;

SELECT gestionarFuncion('CREATE', NULL, '2024-03-20', '14:00', 10.99, TRUE, 1);
SELECT * FROM gestionarFuncion('READ', 1);
SELECT gestionarFuncion('UPDATE', 1, '2024-03-20', '15:00', 12.99, TRUE, 1);
SELECT gestionarFuncion('DELETE', 1);









