CREATE OR REPLACE FUNCTION mostrar_hola_mundo()
RETURNS VOID AS $$
BEGIN
    RAISE NOTICE 'Hola mundo';
END;
$$ LANGUAGE plpgsql;


select mostrar_hola_mundo();

CREATE OR REPLACE FUNCTION obtener_hola_mundo()
RETURNS TEXT AS $$
BEGIN
    RETURN 'Hola mundo';
END;
$$ LANGUAGE plpgsql;

select obtener_hola_mundo();

CREATE OR REPLACE FUNCTION obtener_mensaje(mensaje_param TEXT)
RETURNS TEXT AS $$
BEGIN
    RETURN mensaje_param;
END;
$$ LANGUAGE plpgsql;

SELECT obtener_mensaje('Hola que tal ');


----2 Verificar si un numero es mayor a 10 

CREATE OR REPLACE FUNCTION verificar_mayor_diez()
RETURNS VOID AS $$
DECLARE
    mi_numero INTEGER := 15; -- Puedes cambiar este valor para probar diferentes casos
BEGIN
    IF mi_numero > 10 THEN
        RAISE NOTICE 'El número % es mayor que 10', mi_numero;
    ELSE
        RAISE NOTICE 'El número % no es mayor que 10', mi_numero;
    END IF;
END;
$$ LANGUAGE plpgsql;

---- Llamada a la función
SELECT verificar_mayor_diez();
----3 mAYOR DE DOS NUMEROS Y SI SON IGUALES

CREATE OR REPLACE FUNCTION comparar_numeros(numero1 INTEGER, numero2 INTEGER)
RETURNS TEXT AS $$
DECLARE
    resultado TEXT;
BEGIN
    IF numero1 > numero2 THEN
        resultado := 'El número ' || numero1 || ' es mayor que ' || numero2;
    ELSIF numero1 < numero2 THEN
        resultado := 'El número ' || numero2 || ' es mayor que ' || numero1;
    ELSE
        resultado := 'Los números ' || numero1 || ' y ' || numero2 || ' son iguales';
    END IF;
    
    RETURN resultado;
END;
$$ LANGUAGE plpgsql;


SELECT comparar_numeros(10, 20);
SELECT comparar_numeros(30, 10);
SELECT comparar_numeros(15, 15);

-------Mostrar los numeros del 1 al N con un while.

CREATE OR REPLACE FUNCTION mostrar_numeros_hasta(n INTEGER)
RETURNS VOID AS $$
DECLARE
    contador INTEGER := 1;
BEGIN
    LOOP
        EXIT WHEN contador > n;
        RAISE NOTICE 'Número: %', contador;
        contador := contador + 1;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT mostrar_numeros_hasta(10); -- Mostrará números del 1 al 10
SELECT mostrar_numeros_hasta(50); -- Mostrará números del 1 al 50


SELECT mostrar_numeros();
----------------------
CREATE OR REPLACE FUNCTION mostrar_numeros_hasta_for(n INTEGER)
RETURNS VOID AS $$
DECLARE
    contador INTEGER := 1;
BEGIN
    FOR contador IN 1..n LOOP
        RAISE NOTICE 'Número: %', contador;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


SELECT mostrar_numeros_hasta(10); -- Mostrará números del 1 al 10
SELECT mostrar_numeros_hasta(50); -- Mostrará números del 1 al 50

------------- aplicando whie


CREATE OR REPLACE FUNCTION mostrar_numeros_hasta_con_while(n INTEGER)
RETURNS VOID AS $$
DECLARE
    contador INTEGER := 1;
BEGIN
    WHILE contador <= n LOOP
        RAISE NOTICE 'Número: %', contador;
        contador := contador + 1;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT mostrar_numeros_hasta(10); -- Mostrará números del 1 al 10
SELECT mostrar_numeros_hasta(50); -- Mostrará números del 1 al 50
--------------------------

--------Mostrar el nombre de un cliente dado su codigo.

CREATE OR REPLACE FUNCTION obtener_nombre_cliente(codigo_cliente INT)
RETURNS VARCHAR AS $$
DECLARE
    nombre_cliente VARCHAR;
BEGIN
    SELECT nombrecliente INTO nombre_cliente
    FROM cliente
    WHERE  codigocliente = codigo_cliente;

    RETURN nombre_cliente;
END;
$$ LANGUAGE plpgsql;


SELECT obtener_nombre_cliente(1);
----


CREATE OR REPLACE FUNCTION obtener_datos_cliente(codigo_cliente int)
RETURNS RECORD AS $$
DECLARE
    datos_cliente RECORD;
BEGIN
    SELECT 
    codigocliente,
    nombrecliente,
    telefono, 
    ciudad
    INTO datos_cliente
    FROM cliente
    WHERE codigocliente = codigo_cliente;

    RETURN datos_cliente;
END;
$$ LANGUAGE plpgsql;

select obtener_datos_cliente(1); 



SELECT * FROM obtener_datos_cliente(1) AS (
    codigocliente int,
    nombrecliente varchar,
    telefono varchar,
    ciudad varchar);


--------------- 
----precio de venta y gama de producto
   
CREATE OR REPLACE FUNCTION obtener_precio_y_gama_producto(pm_codigo_producto VARCHAR) 
RETURNS setof RECORD AS $$
BEGIN
    RETURN QUERY (
        SELECT p.precioventa, gp.gama
        FROM producto p
        inner join gamaproducto gp on gp.idgamaproducto=p.idgamaproducto
        WHERE p.codigo_producto = pm_codigo_producto
    );
END;
$$ LANGUAGE plpgsql;


SELECT * FROM obtener_precio_y_gama_producto('AR-003') as (precioventa numeric, gama varchar);


CREATE OR REPLACE FUNCTION obtener_precio_y_gama_producto_2(pm_codigo_producto VARCHAR)
RETURNS SETOF RECORD AS $$
DECLARE
    g_registros RECORD;
    query VARCHAR;
BEGIN
    query := 'SELECT p.precioventa, gp.gama, nombre, proveedor
              FROM producto p
              INNER JOIN gamaproducto gp ON gp.idgamaproducto = p.idgamaproducto
              WHERE p.codigo_producto = ''' || pm_codigo_producto || '''';

    FOR g_registros IN EXECUTE query LOOP
        RETURN NEXT g_registros;
    END LOOP;
END;
$$ LANGUAGE plpgsql;



SELECT * FROM obtener_precio_y_gama_producto_2('AR-003') as (precioventa numeric, gama varchar,nombreproducto varchar, proveedor varchar);

--------9. Mostrar toda la informacion de un pedido dado su codigo (fechaEsperada, fechaEntrega, fechapedido, estado, comentarios)

CREATE OR REPLACE FUNCTION obtener_informacion_pedido(pm_codigo_pedido INTEGER)
RETURNS TABLE (
    fecha_esperada DATE,
    fecha_entrega DATE,
    fecha_pedido DATE,
    estado VARCHAR(15),
    comentarios TEXT
) AS $$
begin
	
    RETURN QUERY SELECT p.fechapedido, p.fechaentrega, p.fechaesperada, p.estado, p.comentarios
                 FROM pedido p
                 WHERE p.codigopedido = pm_codigo_pedido;
END;
$$ LANGUAGE plpgsql;
SELECT * FROM obtener_informacion_pedido(1);

---- otra version

CREATE OR REPLACE FUNCTION obtener_informacion_pedido2(pm_codigo_pedido INTEGER)
RETURNS SETOF RECORD AS $$
DECLARE
    g_registros RECORD;
    query VARCHAR;
BEGIN
    query := 'SELECT p.fechapedido, p.fechaentrega, p.fechaesperada, p.estado, p.comentarios
                 FROM pedido p
                 WHERE p.codigopedido =''' || pm_codigo_pedido || '''';

    FOR g_registros IN EXECUTE query LOOP
        RETURN NEXT g_registros;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM obtener_informacion_pedido(1);
---10. Realizar una función que me devuelva la suma de pagos que ha realizado. Pasa el codigo por parametro.

CREATE OR REPLACE FUNCTION obtener_suma_pagos(pm_codigo_cliente INTEGER)
RETURNS NUMERIC AS $$
DECLARE
    total_pagos NUMERIC;
BEGIN
    SELECT SUM(total) INTO total_pagos
    FROM pago p
    inner join cliente c on c.idcliente=p.idcliente
    WHERE codigocliente = pm_codigo_cliente;
    RETURN total_pagos;
END;
$$ LANGUAGE plpgsql;


SELECT obtener_suma_pagos(4);

