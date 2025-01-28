/*
Un procedimiento almacenado (o stored procedure) es un conjunto de instrucciones SQL 
predefinidas que se almacenan en la base de datos y se pueden ejecutar repetidamente. 
Estos procedimientos permiten realizar tareas específicas, como insertar, 
actualizar o consultar datos, además de incluir lógica de programación, como bucles, condiciones 
y manejo de errores.

Características principales:
Reutilizable: Se puede invocar varias veces, evitando repetir código.
Almacenado en la base de datos: Se guarda directamente en el servidor de base de datos.
Lógica de programación: Permite estructuras como bucles (FOR, WHILE) y condiciones (IF, CASE).
Mejora del rendimiento: Reduce la carga de la red, ya que las operaciones complejas se ejecutan en el servidor.
Seguridad: Puede restringir el acceso a las tablas subyacentes, exponiendo solo el procedimiento.


*/


create or replace function mostrar_hola_mundo_v2() -- Crea o reemplaza una función llamada 'mostrar_hola_mundo_v2'.
returns text as $$ -- Especifica que la función devuelve un valor de tipo 'text'.
begin -- Comienza el bloque de ejecución de la función.
    raise notice 'Bases de Datos II'; -- Muestra un mensaje de nivel NOTICE: 'Bases de Datos II'.
    raise notice 'Hola Mundo'; -- Muestra un mensaje de nivel NOTICE: 'Hola Mundo'.
    RETURN 'Hola mundo todo bien'; -- Devuelve el texto 'Hola mundo todo bien' como resultado de la función.
end; -- Termina el bloque de ejecución de la función.
$$ language plpgsql; -- Finaliza la función y especifica que está escrita en el lenguaje PL/pgSQL.

-- Ejecuta la función creada.
select * from mostrar_hola_mundo_v2(); -- Invoca la función y muestra su resultado ('Hola mundo todo bien').


----

create or replace function comparar_numeros_3(a int, b int, c int)
returns text as $$
begin
	if (a > b and a > c)then --- comparadores no hace falta el doble igual y el distinto es asi != o <> ---
		return 'El mayor es '||a;
	elseif (b > a and b > c) then
		return 'El mayor es '||b;
	else
		return 'El mayor es '||c;
	end if;
end;
$$ language plpgsql;
 
select comparar_numeros_3(100,2999,3);

----


create or replace  function  mostrar_numeros_hasta_n_forv2(n int)
returns setof int as $$
declare 
	contador int :=1;
begin
	for contador in 1..n loop
		---raise notice 'Numero: %', contador;
		return next contador;
	end loop;
	
	
end
$$ language plpgsql;


select mostrar_numeros_hasta_n_forv2(6);
---
create or replace function obtener_nombre_cliente(pm_idcliente int)
returns varchar as $$
declare
	v_nombre_cliente varchar;
	v_nombre_contacto varchar;
begin		
	select nombrecliente, nombrecontacto into v_nombre_cliente, v_nombre_contacto
	from 
	cliente 
	where idcliente=pm_idcliente;
	return v_nombre_cliente||'--->'||v_nombre_contacto; 
end;
$$ language plpgsql;

select obtener_nombre_cliente(35);

----
CREATE OR REPLACE FUNCTION empleados_menos_pagados() 
RETURNS
	TABLE 
	 (
	 	nombre_empleado VARCHAR, 
	 	monto_ventas numeric
	 ) AS $$
DECLARE
    -- Declara un cursor llamado 'empleado' que selecciona todos los empleados ordenados por 'monto_ventas' en orden ascendente
    empleado CURSOR FOR 
		    select e.nombre, coalesce(sum(dp.cantidad *dp.preciounidad),0):: numeric as monto_total   from 
		empleado e 
		left join cliente c on c.idcodigoempleadoventas =e.idempleado 
		left join pedido p on p.idcliente = c.idcliente 
		left join detallepedido dp on dp.idpedido =p.idpedido 
		group by e.nombre 
		order by monto_total ASC
		limit 2;
    -- Declara una variable entera llamada 'contador' e inicialízala en 0
    contador INTEGER := 0;
BEGIN
    OPEN empleado;
    LOOP
        -- Recupera la siguiente fila del cursor 'empleado' y la coloca en las variables 'nombre_empleado' y 'monto_ventas'
        FETCH NEXT FROM empleado INTO nombre_empleado, monto_ventas;
        -- Si no se encuentra ninguna fila o si el contador es igual a 2, sale del bucle LOOP
        EXIT WHEN NOT FOUND OR contador = 2;
        -- Incrementa el contador en 1
        contador := contador + 1;
        -- Devuelve la fila actual como una fila de la tabla de resultados de la función
        RETURN NEXT;
    END LOOP;
    CLOSE empleado;
END;
$$ LANGUAGE plpgsql;
 
select * from empleados_menos_pagados();


-----

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

----

CREATE OR REPLACE FUNCTION obtener_suma_pagos2(pm_codigo_cliente INT)
RETURNS SETOF RECORD AS $$
DECLARE 
	g_registros RECORD;
	query TEXT;
BEGIN
   	query := 'SELECT COALESCE(SUM(p.total), 0)::NUMERIC AS total
   	          FROM pago p
   	          INNER JOIN cliente c ON c.idcliente = p.idcliente
   	          WHERE codigocliente = ' || pm_codigo_cliente;

   	FOR g_registros IN EXECUTE query LOOP
   		RETURN NEXT g_registros;
   	END LOOP;
END;
$$ LANGUAGE plpgsql;