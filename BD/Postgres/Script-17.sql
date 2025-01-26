---1
create or replace function listar_sucursal_pelicula(nombre_peli varchar )
returns setof record as $$
begin
	if nombre_peli='' then 
		return query(select p.titulo , s.direccion from pelicula p 
		inner join sucursalpelicula sp on p.idpelicula=sp.idpelicula
		inner join sucursal s on s.idsucursal=sp.idsucursal);
	else 
		return query(select p.titulo , s.direccion from pelicula p 
		inner join sucursalpelicula sp on p.idpelicula=sp.idpelicula
		inner join sucursal s on s.idsucursal=sp.idsucursal
		where p.titulo=nombre_peli);
	end if;
end;
$$ language plpgsql;
select * from listar_sucursal_pelicula('Comedia Loca') as (nombre_pelicula varchar,sucursal varchar);
select * from listar_sucursal_pelicula('') as (nombre_pelicula varchar,sucursal varchar);
---2
create or replace function buscar_generos_pelicula(nombre_peli varchar)
returns table(
	titulo varchar,
	gene varchar) as $$
begin
	if nombre_peli='' then 
	return query(select p.titulo , g.nombregenero from pelicula p 
		inner join generopelicula gp on p.idpelicula=gp.idpelicula
		inner join genero g on g.idgenero=gp.idgenero);
	else 
		return query(select p.titulo , g.nombregenero from pelicula p 
		inner join generopelicula gp on p.idpelicula=gp.idpelicula
		inner join genero g on g.idgenero=gp.idgenero
		where p.titulo=nombre_peli);
	end if;
end;
$$ language plpgsql;
select * from buscar_generos_pelicula('La Aventura Épica');
select * from buscar_generos_pelicula('');
--3
create or replace function listar_tipos_pagos()
returns table(id_pago int,
	fecha_pago date,
	metodo_pago varchar,
	monto_pago numeric,
	estado_pago varchar, 
	token_seguridad varchar)as $$
begin
	create temp table pagos(
		pago_id int,
		pago_fecha date,
		pago_metodo varchar,
		pago_monto numeric,
		pago_estado varchar,
		tokenseg varchar);
	insert into pagos(pago_id,pago_fecha,	pago_metodo,pago_monto,pago_estado,tokenseg)
		select p.idpago,p.fechapago,p.metodopago,p.montopago,p.estadopago, tp.tokenseguridad from pago p
		inner join tipopago tp on p.idpago=tp.idpago;
	return query select * from pagos;
	drop table pagos;
end;
$$ language plpgsql;
select * from listar_tipos_pagos();

---4
create or replace function gestionar_funcion(
	f_operacion varchar,
	f_idfuncion int,
	f_fecha date,
	f_hora time,
	f_precio numeric,
	f_disponibilidad boolean,
	f_idpelicula int)
returns varchar as $$
declare 
	f_mensaje varchar;
begin
	if f_operacion= 'INSERT' then 
		insert into funcion(
		idfuncion,
		fecha,
		hora,
		precio,
		disponibilidad,
		idpelicula
	)
	values(
	f_operacion,
	f_idfuncion,
	f_fecha,
	f_hora,
	f_precio,
	f_disponibilidad,
	f_idpelicula);
	f_mensaje:='Se ha insertado el registro correctamente';
		raise notice 'Agregar';
	elseif p_operacion ='UPDATE' then 
		update cliente set
		fecha=f_fecha,
		hora=f_hora,
		precio=f_precio,
		disponibilidad=f_disponibilidad,
		idpelicula=f_idpelicula
		where idfuncion=f_idfuncion;
	f_mensaje:='Se ha modificado el registro correctamente';
	raise notice 'Modificar';
	elseif f_operacion ='DELETE' then 
	delete from funcion where idfuncion=f_idfuncion;
	f_mensaje:='Se ha eliminado el registro correctamente';
	raise notice 'Eliminar';
	else 
		raise exception 'Operación no valida: %',f_operacion;
	end if;
	return(f_operacion||'|'||f_mensaje);
end;
$$ language plpgsql;


