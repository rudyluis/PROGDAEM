Devuelve un listado de los 20 productos más vendidos y su codigo de Producto y el número total de unidades que se han vendido de cada uno. 
El listado deberá estar ordenado por el número total de unidades vendidas.
SELECT p.nombre , p.codigo_producto , SUM(dv.cantidad) AS total_unidades_vendidas
FROM detallepedido dv
inner JOIN producto p ON dv.idproducto = p.idproducto
GROUP BY p.nombre,p.codigo_producto
ORDER BY total_unidades_vendidas DESC
LIMIT 20;


Mostrar la fecha del primer y el último pago realizado por cada uno de los clientes. El listado deberá mostrar el nombre y los apellidos de cada cliente.
SELECT cliente.nombrecliente , cliente.nombrecontacto ,cliente.apellidocontacto , MIN(pago.fechapago) AS primer_pago, MAX(pago.fechapago) AS ultimo_pago
FROM cliente
LEFT JOIN pago ON cliente.idcliente  = pago.idcliente 
GROUP BY cliente.nombrecliente,cliente.nombrecontacto, cliente.apellidocontacto;




CREATE OR REPLACE FUNCTION obtener_empleado_oficina(pm_codigo_oficina varchar)
RETURNS TABLE (
    codigo_empleado INTEGER,
    empleado  TEXT
) AS $$
BEGIN
    RETURN QUERY 
    SELECT e.codigo_empleado ,(e.nombre||' '||e.apellido1||' '||e.apellido2)::TEXT as empleado
    FROM empleado e
    INNER JOIN oficina o  ON o.idoficina =e.idoficina 
    WHERE o.codigooficina = pm_codigo_oficina;
END;
$$ LANGUAGE plpgsql;


select * from oficina o ;
where o.
SELECT * FROM obtener_empleado_oficina('TOK-JP');


SELECT e.codigo_empleado ,e.nombre||' '||e.apellido1||' '||e.apellido2 as empleado
    FROM empleado e
    INNER JOIN oficina o  ON o.idoficina =e.idoficina 
    WHERE o.codigooficina ='TOK-JP';

