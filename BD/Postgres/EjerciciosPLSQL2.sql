---11. Realizar un método o procedimiento que muestre el total en euros de un pedido, pasale el codigo por parametro.


CREATE OR REPLACE FUNCTION calcular_total_euros_pedido(IN codigo_pedido INTEGER)
RETURNS NUMERIC AS $$
DECLARE
    total_euros NUMERIC := 0;
BEGIN
    SELECT SUM(p.precioVenta) INTO total_euros
    FROM pedido pe
    INNER JOIN detallePedido dp ON pe.IDPedido = dp.IDPedido
    INNER JOIN producto p ON dp.IDProducto = p.IDProducto
    WHERE pe.codigoPedido = codigo_pedido;

    RETURN total_euros;
END;
$$ LANGUAGE plpgsql;


---12. Mostrar el nombre de un cliente dado su codigo. Controla en caso de que no se encuentre, mostrando un mensaje por ejemplo. "No se encontro el Cliente"
CREATE OR REPLACE FUNCTION obtener_nombre_cliente(IN codigo_cliente INTEGER)
RETURNS VARCHAR(50) AS $$
DECLARE
    nombre_cliente VARCHAR(50);
BEGIN
    SELECT nombreCliente INTO nombre_cliente
    FROM cliente
    WHERE codigoCliente = codigo_cliente;

    IF nombre_cliente IS NOT NULL THEN
        RETURN nombre_cliente;
    ELSE
        RETURN 'No se encontró el Cliente';
    END IF;
END;
$$ LANGUAGE plpgsql;


SELECT obtener_nombre_cliente(1);




SELECT calcular_total_euros_pedido(116);


----13. Realizar una función que me devuelva la suma de pagos que ha realizado. Pasa el codigo por parametro. Controla en caso de que no se encuentre, en ese caso devuelve un -1.


CREATE OR REPLACE FUNCTION obtener_suma_pagos(IN codigo_cliente INTEGER)
RETURNS NUMERIC AS $$
DECLARE
    total_pagos NUMERIC := 0;
BEGIN
    SELECT SUM(total) INTO total_pagos
    FROM pago
    WHERE IDCliente = codigo_cliente;

    IF total_pagos IS NOT NULL THEN
        RETURN total_pagos;
    ELSE
        RETURN -1;
    END IF;
END;
$$ LANGUAGE plpgsql;



SELECT obtener_suma_pagos(115);
----
Realizar una función que devuelva el total en euros de un pedido, pasale el codigo por parametro. Controla en caso de que no se encuentre, en ese caso devuelve un 0. Pasale otro parametro, si supera ese limite, lanzaremos una excepcion propia y devolveremos un 0.

CREATE OR REPLACE FUNCTION obtener_total_pedido_en_euros(
    IN codigo_pedido INTEGER,
    IN limite_euros NUMERIC
)
RETURNS NUMERIC AS $$
DECLARE
    total_pedido NUMERIC := 0;
BEGIN
    -- Obtener el total en euros del pedido
    SELECT SUM(dp.cantidad * p.precioVenta) INTO total_pedido
    FROM pedido pe
    INNER JOIN detallepedido dp ON pe.IDPedido = dp.IDPedido
    INNER JOIN producto p ON dp.IDProducto = p.IDProducto
    WHERE pe.IDPedido = codigo_pedido;

    -- Controlar si el pedido no existe o el total supera el límite especificado
    IF total_pedido IS NULL THEN
        RETURN 0;
    ELSIF total_pedido > limite_euros THEN
        RAISE EXCEPTION 'El total del pedido supera el límite especificado';
    ELSE
        RETURN total_pedido;
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT obtener_total_pedido_en_euros(1, 5);


CREATE OR REPLACE FUNCTION clientes_sin_pagos() RETURNS  SETOF RECORD AS $$
DECLARE
    cliente_cursor CURSOR FOR
        SELECT c.nombreCliente
        FROM cliente c
        LEFT JOIN pago p ON c.IDCliente = p.IDCliente
        WHERE p.IDPago IS NULL; -- Clientes que no tienen pagos
    cliente_record RECORD; -- Registro para almacenar cada cliente sin pagos
BEGIN
    -- Abrir el cursor
    OPEN cliente_cursor;

    -- Recorrer el cursor utilizando un bucle WHILE
    LOOP
        FETCH cliente_cursor INTO cliente_record;
        EXIT WHEN NOT FOUND; -- Salir del bucle cuando no hay más registros por procesar

        -- Mostrar el nombre del cliente
        RAISE NOTICE 'Cliente sin pagos: %', cliente_record.nombreCliente;
        return next cliente_record;
    END LOOP;

    -- Cerrar el cursor
    CLOSE cliente_cursor;

    -- Si no se encontraron clientes sin pagos, mostrar un mensaje de aviso
    IF NOT FOUND THEN
        RAISE NOTICE 'No se encontraron clientes sin pagos.';
    END IF;
END;
$$ LANGUAGE plpgsql;


----Crear un cursor para ver todos los clientes que no hayan hecho pagos. Hazlo con un for.

-- Llamar a la función para mostrar los clientes sin pagos
SELECT * from clientes_sin_pagos() as (clientes_sin_pagos varchar);
---Crear un cursor para ver todos los clientes que no hayan hecho pagos. Hazlo con un for.

CREATE OR REPLACE FUNCTION clientes_sin_pagos_confor() RETURNS SETOF record AS
$$
DECLARE
    cliente_record record;  -- Variable para almacenar el registro del cliente
BEGIN
    -- Abre un cursor para seleccionar los clientes que no han realizado pagos
    FOR cliente_record IN SELECT c.nombrecliente, c.telefono FROM cliente c WHERE NOT EXISTS (SELECT 1 FROM pago p WHERE p.IDCliente = c.IDCliente) LOOP
        -- Retorna el registro del clente actual
        RETURN NEXT cliente_record;
    END LOOP;

    -- Cierra el cursor
   

    -- Si no se encontraron clientes sin pagos, devuelve un mensaje de aviso
    IF NOT FOUND THEN
        RETURN QUERY VALUES ('No se encontraron clientes sin pagos.');
    END IF;
END;
$$ LANGUAGE plpgsql;


SELECT * from clientes_sin_pagos_confor() as (clientes_sin_pagos varchar, telefono varchar);



---- Gestion CRUD Cliente
CREATE OR REPLACE FUNCTION gestionar_cliente_iud(
    IN p_operacion VARCHAR(10),
    IN p_id_cliente INT,
    IN p_codigo_cliente INT,
    IN p_nombre_cliente VARCHAR(50),
    IN p_nombre_contacto VARCHAR(30),
    IN p_apellido_contacto VARCHAR(30),
    IN p_telefono VARCHAR(15),
    IN p_fax VARCHAR(15),
    IN p_direccion1 VARCHAR(50),
    IN p_direccion2 VARCHAR(50),
    IN p_ciudad VARCHAR(50),
    IN p_region VARCHAR(50),
    IN p_pais VARCHAR(50),
    IN p_codigo_postal VARCHAR(10),
    IN p_id_empleado_ventas INT,
    IN p_limite_credito NUMERIC(15,2)
) 
RETURNS varchar AS $$
DECLARE
    p_mensaje VARCHAR;
begin
	BEGIN
	    IF p_operacion = 'INSERT' THEN
	        INSERT INTO cliente (codigoCliente, nombreCliente, nombreContacto, apellidoContacto, telefono, fax, lineaDireccion1, lineaDireccion2, ciudad, region, pais, codigoPostal, IDcodigoEmpleadoVentas, limite_credito)
	        VALUES (p_codigo_cliente, p_nombre_cliente, p_nombre_contacto, p_apellido_contacto, p_telefono, p_fax, p_direccion1, p_direccion2, p_ciudad, p_region, p_pais, p_codigo_postal, p_id_empleado_ventas, p_limite_credito);
	        p_mensaje := 'Se ha insertado el cliente con éxito.';
	    ELSIF p_operacion = 'UPDATE' THEN
	        UPDATE cliente
	        SET codigoCliente = p_codigo_cliente,
	            nombreCliente = p_nombre_cliente,
	            nombreContacto = p_nombre_contacto,
	            apellidoContacto = p_apellido_contacto,
	            telefono = p_telefono,
	            fax = p_fax,
	            lineaDireccion1 = p_direccion1,
	            lineaDireccion2 = p_direccion2,
	            ciudad = p_ciudad,
	            region = p_region,
	            pais = p_pais,
	            codigoPostal = p_codigo_postal,
	            IDcodigoEmpleadoVentas = p_id_empleado_ventas,
	            limite_credito = p_limite_credito
	        WHERE IDCliente = p_id_cliente;
	        p_mensaje := 'Se ha actualizado el cliente con éxito.';
	    ELSIF p_operacion = 'DELETE' THEN
	        DELETE FROM cliente WHERE IDCliente = p_id_cliente;
	        p_mensaje := 'Se ha eliminado el cliente con éxito.';
	    ELSE
	        RAISE EXCEPTION 'Operación no válida: %', p_operacion;
	    END IF;
	EXCEPTION
	    WHEN others THEN
	            -- Capturar excepciones
	            p_mensaje := SQLERRM;
	    END;
    -- Devolver el registro con la operación, ID del cliente y el mensaje
    RETURN (p_operacion||'|'|| p_mensaje);
END;
$$ LANGUAGE plpgsql;


-- Llamar a la función para insertar un nuevo cliente
SELECT * FROM gestionar_cliente_iud('INSERT', NULL, 123, 'Nombre Cliente', 'Nombre Contacto', 'Apellido Contacto', '123456789', '987654321', 'Direccion 1', 'Direccion 2', 'Ciudad', 'Region', 'Pais', '12345', 1, 1000.00) ;
-- Llamar a la función para actualizar un cliente existente
SELECT * FROM gestionar_cliente_iud('UPDATE', 37, 123, 'Nuevo Nombre', 'Nuevo Contacto', 'Nuevo Apellido', '987654321', '123456789', 'Nueva Dirección 1', 'Nueva Dirección 2', 'Nueva Ciudad', 'Nueva Región', 'Nuevo País', '54321', 2, 2000.00);

-- Llamar a la función para eliminar un cliente existente
SELECT * FROM gestionar_cliente_iud('DELETE', 47, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-----------------------


CREATE OR REPLACE FUNCTION calcular_total_ventas_temp()
RETURNS TABLE (
    cliente_id INTEGER,
    cliente_nombre VARCHAR(50),
    pedido_id INTEGER,
    fecha_pedido DATE,
    total_venta NUMERIC(15, 2)
) AS $$
BEGIN
    -- Crear una tabla temporal para almacenar los resultados temporales
    CREATE TEMP TABLE ventas_temporales (
        cliente_id INTEGER,
        cliente_nombre VARCHAR(50),
        pedido_id INTEGER,
        fecha_pedido DATE,
        total_venta NUMERIC(15, 2)
    );

    -- Insertar datos en la tabla temporal utilizando una consulta
    INSERT INTO ventas_temporales (cliente_id, cliente_nombre, pedido_id, fecha_pedido, total_venta)
    SELECT c.IDCliente, c.nombreCliente, p.IDPedido, p.fechaPedido, SUM(dp.cantidad * pr.precioVenta) AS total_venta
    FROM cliente c
    JOIN pedido p ON c.IDCliente = p.IDCliente
    JOIN detallepedido dp ON p.IDPedido = dp.IDPedido
    JOIN producto pr ON dp.IDProducto = pr.IDProducto
    GROUP BY c.IDCliente, c.nombreCliente, p.IDPedido, p.fechaPedido
    order by c.nombreCliente;

    -- Devolver los resultados de la tabla temporal
    RETURN QUERY SELECT * FROM ventas_temporales;

    -- Limpiar la tabla temporal al finalizar
    DROP TABLE ventas_temporales;
END;
$$ LANGUAGE plpgsql;



SELECT * FROM calcular_total_ventas_temp();


-----
---Desarrollar una función que devuelva el número de años completos que hay entre
dos fechas que se pasan como argumentos.


CREATE OR REPLACE FUNCTION meses_dif(
    fecha1 DATE,
    fecha2 DATE)
RETURNS INTEGER
AS $$
DECLARE
    v_meses_dif INTEGER;
BEGIN
    v_meses_dif := EXTRACT(YEAR FROM age(fecha2, fecha1)) * 12 + EXTRACT(MONTH FROM age(fecha2, fecha1));
    RETURN v_meses_dif;
END;
$$ LANGUAGE plpgsql;


select meses_dif('2020-01-15','2024-01-01')
------- emeplados por oficna

CREATE OR REPLACE FUNCTION obtener_numero_empleados_por_oficina()
RETURNS TABLE (nombre_oficina TEXT, numero_empleados INTEGER) AS $$
BEGIN
    RETURN QUERY 
    SELECT o.codigooficina||'-'||o.ciudad as nombre_oficina, COUNT(e.idempleado)::integer AS numero_empleados
    FROM oficina o
    LEFT JOIN empleado e ON o.idoficina = e.idoficina
    GROUP BY o.codigooficina, o.ciudad ;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM obtener_numero_empleados_por_oficina();

-------Codificar un programa que visualice los dos empleados que ganan menos de cada oficio.

CREATE OR REPLACE FUNCTION obtener_dos_empleados_menos_pagados()
---RETURNS TABLE (nombre_empleado VARCHAR, salario NUMERIC, nombre_oficina VARCHAR) AS $$
RETURNS SETOF RECORD AS $$
DECLARE
    r_record RECORD;
    c_cursor CURSOR FOR
     SELECT DISTINCT e.nombre, COALESCE(SUM(dp.cantidad * dp.preciounidad), 0)::INT AS total_ventas
		FROM empleado e
		LEFT JOIN cliente c ON c.idcodigoempleadoventas = e.idempleado 
		LEFT JOIN pedido p ON p.idcliente = c.idcliente 
		LEFT JOIN detallepedido dp ON dp.idpedido = p.idpedido 
		WHERE p.estado = 'Entregado'
		GROUP BY e.idempleado, e.nombre
		ORDER BY total_ventas ASC
		LIMIT 2;
       
    contador INT := 0;
BEGIN
    OPEN c_cursor;
    LOOP
        FETCH c_cursor INTO r_record;
        EXIT WHEN NOT FOUND;
      	RETURN NEXT r_record;
    END LOOP;
    CLOSE c_cursor;
END;
$$ LANGUAGE plpgsql;



SELECT * FROM obtener_dos_empleados_menos_pagados() as (nombre_empleado VARCHAR, monto_ventas int);


----------