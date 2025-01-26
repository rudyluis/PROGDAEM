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

