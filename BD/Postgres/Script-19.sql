--Examen Parcial #1 Base de Datos / Lunes 18 de Marzo 2024 / Andres Aguirre Cortez 

--Ejercicio 1 
create or replace function eje1(p_titulo varchar default null)
returns setof record as $$
declare
    p_registros record;
    query varchar;
begin 
    if (p_titulo is null) then 
        query:= 'select p.titulo as nombre_pelicula, s.direccion from pelicula p
        inner join sucursalpelicula sp on p.idpelicula = sp.idpelicula 
        inner join sucursal s on sp.idsucursal = s.idsucursal';
    else 
        query:= 'select p.titulo as nombre_pelicula, s.direccion from pelicula p
        inner join sucursalpelicula sp on p.idpelicula = sp.idpelicula 
        inner join sucursal s on sp.idsucursal = s.idsucursal
        where p.titulo = ''' || p_titulo || '''';
    end if;
    
    for p_registros in execute query loop
        return next p_registros;
    end loop;

    return;
end;
$$ language plpgsql;

select * from eje1('Comedia Loca') as (nombre_pelicula varchar (100), direccion varchar(45));

--Ejercicio 2 

create or replace function eje2(nombre_pelicula varchar(100))
returns table(
	titulo_pelicula varchar,
	genero_pelicula varchar
) as $$
begin 
	return query (
	select 
	p.fechapedido,
	p.fechaentrega,
	p.fechaesperada,
	p.estado,
	p.comentarios
	from pedido p
	where p.codigopedido = pm_codigo_pedido
	);
	
end;

$$ language plpgsql;

select * from obtener_informacion_pedido (1);

--Ejercicio 3 

--Ejercicio 4 

create or replace function eje4(
f_operacion varchar (10),
id_funcion int,
fecha_funcion date,
hora_funcion time,
precio_funcion numeric(18,2),
disponibilidad_funcion bool,
id_pelicula int
)
returns varchar as $$
declare 

	f_mensaje varchar;

begin 
	if f_operacion = 'INSERT' then 
	insert into funcion(
	fecha,
	hora,
	precio,
	disponibilidad
	)
	values(
	fecha_funcion,
	hora_funcion,
	precio_funcion,
	disponibilidad_funcion
	);
		f_mensaje:= 'Se ha insertado el registro correctamente.';
			raise notice 'Agregar';
		elseif f_operacion ='UPDATE' then 
		update funcion set 
		fecha = fecha_funcion,
		hora = hora_funcion,
		precio= precio_funcion,
		disponibilidad = disponibilidad_funcion
		where idfuncion = id_funcion;
		f_mensaje:= 'Se ha actualizado el registro correctamente.';	
	
	raise notice 'Modificar';

	elseif f_operacion ='DELETE' then 
	
		f_mensaje:= 'Se ha eliminado el registro correctamente.';
		delete from funcion where idfuncion = id_funcion;
	
		raise notice 'Eliminar';
	else 
		raise exception 'Operacion no valida: %', f_operacion;
	end if;
	return (f_operacion||'|'||f_mensaje);
end;

$$ language plpgsql;

select * from eje4('INSERT',null,'2024-10-25','10:10:25',25.00,TRUE);







