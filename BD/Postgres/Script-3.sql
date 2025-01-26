create or replace function producto_sin_pedido()
returns table (nombre_producto VARCHAR(50))as $$
begin
    return query(
    select pr.nombre from producto pr
    left join detallepedido dp on pr.idproducto = dp.idproducto
    where dp.iddetallepedido is null
   );
end;
$$ language plpgsql;
 
select * from producto_sin_pedido();


create or replace function producto_sin_pedidov2()
returns setof RECORD as $$
begin
    return query(
    select pr.nombre from producto pr
    left join detallepedido dp on pr.idproducto = dp.idproducto
    where dp.iddetallepedido is null
   );
end;
$$ language plpgsql;


select * from producto_sin_pedidov2() as (nombre_producto varchar);


create or replace function ciudad_y_empleados(v_idoficina bigint)
returns setof record as $$
begin
    return query(
    select o.ciudad, COUNT(e.idempleado)::numeric
    from oficina o
    inner join empleado e on o.idoficina=e.idoficina
   	where o.idoficina=v_idoficina
    group by o.ciudad
   );
end;
$$ language plpgsql;
 
select * from ciudad_y_empleados (5::bigint)
as (ciudad varchar, empleados numeric);



create or replace function obtener_informacion_pedido(pm_codigo_pedido int)
returns table(
			fecha_pedido date,
    		fecha_entrega date,
    		fecha_esperada date,
    		estado varchar,
    		comentarios text
)as $$
begin
    return query(
    	select 
    		p.fechapedido,
    		p.fechaentrega,
    		p.fechaesperada,
    		p.estado,
    		p.comentarios
    	from pedido p 
    	where p.codigopedido=pm_codigo_pedido
   );
end;
$$ language plpgsql;


select * from obtener_informacion_pedido(1);




create or replace function obtener_informacion_pedido2(pm_codigo_pedido int)
returns setof RECORD as $$
declare 
	g_registros RECORD;
	query  varchar;
begin
	 if(pm_codigo_pedido=0) then
	 
			 query:='select 
		    		p.fechapedido,
		    		p.fechaentrega,
		    		p.fechaesperada,
		    		p.estado,
		    		p.comentarios
		    	from pedido p';
    
	 else
		 	query:='select 
	    		p.fechapedido,
	    		p.fechaentrega,
	    		p.fechaesperada,
	    		p.estado,
	    		p.comentarios
	    	from pedido p 
	    	where p.codigopedido='||pm_codigo_pedido;
    
	 end if;
   	  for g_registros in execute query loop
   	  	return next g_registros;
   	  end loop;
end;
$$ language plpgsql;

select * from obtener_informacion_pedido2(3)
as (
			fecha_pedido date,
    		fecha_entrega date,
    		fecha_esperada date,
    		estado varchar,
    		comentarios text
); 




create or replace function obtener_informacion_pedido2(pm_codigo_pedido int)
returns setof RECORD as $$
declare 
	g_registros RECORD;
	query  varchar;
	query_e varchar;
begin
	query_e:='';
	 if(pm_codigo_pedido>0) then
	 
			 query_e:=' where p.codigopedido='||pm_codigo_pedido;
	 end if;
	 	query:='select 
	    		p.fechapedido,
	    		p.fechaentrega,
	    		p.fechaesperada,
	    		p.estado,
	    		p.comentarios
	    	from pedido p '||query_e;
	    	
   	  for g_registros in execute query loop
   	  	return next g_registros;
   	  end loop;
end;
$$ language plpgsql;

select * from obtener_informacion_pedido2(0)
as (
			fecha_pedido date,
    		fecha_entrega date,
    		fecha_esperada date,
    		estado varchar,
    		comentarios text
); 

--------------------------------------------------------

create or replace function obtener_suma_pagos2(pm_codigo_cliente int)
returns setof RECORD as $$
declare 
	g_registros RECORD;
	query  varchar;
	
begin
	  query:='
		select coalesce(SUM(p.total),0)::numeric  as total
		from pago p 
		inner join cliente c  on c.idcliente =p.idcliente 
		where codigocliente ='||pm_codigo_cliente;
		
	   
   	  for g_registros in execute query loop
	   	raise notice '%', g_registros;
   	  	return next g_registros;
   	  end loop;
end;
$$ language plpgsql;




create or replace function obtener_suma_pagos2(pm_codigo_cliente int default 0)
returns setof RECORD as $$
declare 
	g_registros RECORD;
	query  varchar;
begin
	if(pm_codigo_cliente=0) then
			query:='
				select 
				''TOTAL GENERAL'' ::varchar,
				coalesce(SUM(p.total),0)::numeric  as total
				from pago p 
				inner join cliente c  on c.idcliente =p.idcliente ';
		else
				 query:='
				select
				codigocliente::varchar as cliente,
				coalesce(SUM(p.total),0)::numeric  as total
				from pago p 
				inner join cliente c  on c.idcliente =p.idcliente 
				where codigocliente ='||pm_codigo_cliente||
				' group by codigocliente';
	end if;
   	  for g_registros in execute query loop
	   	raise notice '%', g_registros;
   	  	return next g_registros;
   	  end loop;
end;
$$ language plpgsql;

select * from obtener_suma_pagos2(1) as (mensaje varchar,total_pago numeric);


SELECT usename
FROM pg_user;


CREATE 'rudy.manzaneda' LOGIN PASSWORD '123456';


CREATE ROLE "rudy.manzaneda" LOGIN PASSWORD '123456';

CREATE ROLE "claudia.sullcani" WITH
  LOGIN
  PASSWORD '123456'
  NOSUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  NOREPLICATION
  VALID UNTIL '2024-03-03';

GRANT rol_super TO nuevo_usuario;

SELECT usename AS username, valuntil AS expiration_date
FROM pg_user
WHERE usename = 'claudia.sullcani';


SELECT usename
FROM pg_user;


DROP USER "rudy.manzaneda";


SELECT grantee, table_schema, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee = 'rudy.manzaneda';

CREATE ROLE "rudy.manzaneda" WITH
  LOGIN
  PASSWORD '123456'
  SUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  NOREPLICATION
  VALID UNTIL 'infinity';

SELECT rolname FROM pg_roles;


CREATE ROLE prueba_select;


GRANT SELECT ON oficina TO prueba_select;


GRANT prueba_select TO "rudy.manzaneda";

SELECT r.rolname AS rol_nombre,
       r.rolsuper AS es_superusuario,
       r.rolcreaterole AS puede_crear_roles,
       r.rolcreatedb AS puede_crear_bd,
       r.rolinherit AS hereda_roles,
       r.rolcanlogin AS puede_iniciar_sesion
FROM pg_catalog.pg_roles r
JOIN pg_catalog.pg_auth_members m ON (m.roleid = r.oid)
JOIN pg_catalog.pg_roles g ON (m.member = g.oid)
WHERE g.rolname = 'prueba_select';


SELECT r.rolname AS rol_nombre
FROM pg_catalog.pg_roles r
JOIN pg_catalog.pg_auth_members m ON m.roleid = r.oid
JOIN pg_catalog.pg_roles u ON m.member = u.oid
WHERE u.rolname = 'claudia.sullcani';


REVOKE prueba_select FROM "rudy.manzaneda";


ALTER USER "claudia.sullcani" WITH SUPERUSER;


GRANT ALL ON oficina TO "claudia.sullcani";
grant all on empleado to "rudy.manzaneda";

SELECT rolname FROM pg_roles WHERE rolsuper = TRUE;


GRANT SELECT, INSERT, UPDATE ON tabla TO rol;


GRANT ALL PRIVILEGES ON TABLE oficina TO "claudia.sullcani";



SELECT table_name, privilege_type, grantee 
FROM information_schema.table_privileges
WHERE grantee = 'rudy.manzaneda';



REVOKE ALL PRIVILEGES ON TABLE empleado  FROM "rudy.manzaneda";




GRANT SELECT (columna1, columna2, ...) ON nombre_tabla TO usuario;
GRANT INSERT (columna1, columna2, ...) ON nombre_tabla TO usuario;
GRANT UPDATE (columna1, columna2, ...) ON nombre_tabla TO usuario;
