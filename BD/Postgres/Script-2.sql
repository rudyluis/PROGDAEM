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


select * from cliente c;


create or replace function obtener_oficinas()
returns int as $$
declare
	contar_oficinas int;
begin		
	select count(*) into contar_oficinas
	from oficina;
	return contar_oficinas ; 
end;
$$ language plpgsql;

select * from oficina;

select obtener_oficinas();

select count(*) into contar_oficinas
	from oficina;

-----------------------------------
create or replace function cantidad_empleados(codigooficina_v varchar)
returns int as $$
declare
	contador_empleados int;
begin
	select COUNT(e.idempleado) into contador_empleados 
	from oficina o
	inner join empleado e on e.idoficina=o.idoficina
	where codigooficina=codigooficina_v;

	return contador_empleados;
end;
$$ language plpgsql;
 
select cantidad_empleados('BCN-ES');

-------------------------

create or replace function obtener_nombre_cliente_registro(pm_idcliente int)
returns RECORD as $$
declare
	datos_cliente RECORD;
begin		
	select 
	codigocliente,
	nombrecliente, 
	nombrecontacto,
	telefono,
	ciudad
	into datos_cliente
	from 
	cliente 
	where idcliente=pm_idcliente;
	return datos_cliente; 
end;
$$ language plpgsql;
-------

select obtener_nombre_cliente_registro(35);

select * from obtener_nombre_cliente_registro(35) as
(
	codigocliente int,
	nombrecliente varchar, 
	nombrecontacto varchar,
	telefono varchar,
	ciudad varchar
)

------------------------------------

create or replace function obtener_precio_gama_producto(pm_codigo_producto varchar)
returns setof RECORD as $$
begin		
	return query(
		select p.precioventa, gp.gama 
		from
		producto p
		inner join gamaproducto gp on gp.idgamaproducto =p.idgamaproducto 
		where p.codigo_producto =pm_codigo_producto
	);
end;
$$ language plpgsql;

select * from obtener_precio_gama_producto ('AR-003') 
as (precioVenta numeric, gama varchar);





select * from gamaproducto g ;
select * from producto p ;


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




select e.nombre, coalesce(sum(dp.cantidad *dp.preciounidad),0):: numeric as monto_total   from 
empleado e 
left join cliente c on c.idcodigoempleadoventas =e.idempleado 
left join pedido p on p.idcliente = c.idcliente 
left join detallepedido dp on dp.idpedido =p.idpedido 
group by e.nombre 
order by monto_total ASC
limit 2



CREATE OR REPLACE FUNCTION empleados_menos_pagados2() 
returns setof RECORD as $$

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
    r_record RECORD;
BEGIN
    OPEN empleado;
	    LOOP
	        -- Recupera la siguiente fila del cursor 'empleado' y la coloca en las variables 'nombre_empleado' y 'monto_ventas'
	        FETCH  empleado into r_record;
	        -- Si no se encuentra ninguna fila o si el contador es igual a 2, sale del bucle LOOP
	        	EXIT WHEN NOT FOUND ;
	         
	        RETURN next r_record;
	    END LOOP;
    CLOSE empleado;
END;
$$ LANGUAGE plpgsql;

select * from empleados_menos_pagados2() as 
	 (
	 	nombre_empleado VARCHAR, 
	 	monto_ventas numeric
	 );



	
select * from oficina;	


CREATE OR REPLACE FUNCTION listadoOficinas() 
returns setof RECORD as $$
DECLARE
    -- Declara un cursor llamado 'empleado' que selecciona todos los empleados ordenados por 'monto_ventas' en orden ascendente
    oficina cursor for 
    	select  o.codigooficina, o.ciudad, o.pais
    	from oficina o;
    		
    r_record RECORD;
BEGIN
   	open oficina;
   		loop
   			fetch oficina into r_record;
   				exit when not found;
   			return next r_record;	
   		end loop;   		
   	close oficina;
END;
$$ LANGUAGE plpgsql;


select * from listadooficinas() as  (codigo_oficina varchar, ciudad varchar, pais varchar); 

select * from empleado;



	
	





