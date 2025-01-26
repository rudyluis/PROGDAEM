--EXAMEN

--ejercicio 1-
create or replace function listar_sucursal_pelicula(
    titulo_pelicula varchar default null
)
returns setof RECORD as $$
begin
        return QUERY
        select p.titulo, s.direccion
        from pelicula p
        join sucursalpelicula sp on p.IDPelicula = sp.IDPelicula
        join sucursal s on sp.IDSucursal = s.IDSucursal
        where p.titulo = titulo_pelicula OR
        titulo_pelicula IS NULL;
end;
$$ language plpgsql;
select * from listar_sucursal_pelicula('Comedia Loca') as (nombre_pelicula varchar, sucursal varchar);
select * from listar_sucursal_pelicula() as (nombre_pelicula varchar, sucursal varchar);


--ejercicio 2--
create or replace function  buscar_genero_pelicula(
    titulo_parametro VARCHAR default null
) 
returns table  (
    titulo VARCHAR,
    nombre_clasificacion VARCHAR
) as $$
begin
    return QUERY 
    select p.titulo,  g.nombregenero 
    from pelicula p
    left join generopelicula gp on p.idpelicula = gp.idpelicula 
    left join genero g on gp.idgenero = g.idgenero 
    where  
        p.titulo = titulo_parametro  OR
        titulo_parametro IS NULL;
end;
$$ language plpgsql;
select * from buscar_genero_pelicula('La Aventura Épica');
select * from buscar_genero_pelicula();

-- Ejercicio 3--

select p.idpago as id_pago, p.fechapago as fecha_pago , p.metodopago as metodo_pago ,p.montopago as monto_pago ,p.estadopago as estado_pago ,t.tokenseguridad as tipo_pago
from pago p 
inner join tipopago t ON p.idpago = t.idpago 


create or replace function  obtener_info_pago()
returns table (
    id_pago INT,
    fecha_pago DATE,
    metodo_pago VARCHAR,
    monto_pago NUMERIC(18,2),
    estado_pago VARCHAR,
    tipo_pago VARCHAR
) as $$
begin
    create temp table pagos_temporales(
        id_pago INT,
        fecha_pago DATE,
        metodo_pago VARCHAR(50),
        monto_pago NUMERIC(18,2),
        estado_pago VARCHAR(50),
        tipo_pago VARCHAR(50)
    );

    insert into pagos_temporales(id_pago, fecha_pago, metodo_pago, monto_pago, estado_pago, tipo_pago)
    select p.idpago, p.fechapago, p.metodopago, p.montopago, p.estadopago, t.tokenseguridad
    from pago p 
    inner join tipopago t ON p.idpago = t.idpago;

    return QUERY select * from pagos_temporales;

    drop table if exists pagos_temporales;
end;
$$ language plpgsql;

select * from obtener_info_pago();

-- ejericio 4 CRUD--
create or replace function  gestionar_funcion_iud(
    p_operacion varchar(10),
    p_id_funcion int,
    p_fecha date,
    p_hora time without time zone,
    p_precio numeric,
    p_disponibilidad boolean,
    p_id_pelicula int
)
returns varchar AS $$
declare
    p_mensaje varchar;
begin
    if p_operacion = 'INSERT' then
        insert into funcion (
            fecha,
            hora,
            precio,
            disponibilidad,
            idpelicula
        )
        values (
            p_fecha,
            p_hora,
            p_precio,
            p_disponibilidad,
            p_id_pelicula
        );
        p_mensaje := 'Se ha insertado el registro correctamente.';
    elsif p_operacion = 'UPDATE' then
        update funcion
        set fecha = p_fecha,
            hora = p_hora,
            precio = p_precio,
            disponibilidad = p_disponibilidad,
            idpelicula = p_id_pelicula
        where idfuncion = p_id_funcion;
        p_mensaje := 'Se ha actualizado el registro correctamente.';
    elseif p_operacion = 'DELETE' then
        delete from funcion
        where idfuncion = p_id_funcion;
        p_mensaje := 'Se ha eliminado el registro correctamente.';
    else			
        raise exception	'Operación no válida: %', p_operacion;
    end if;

    return p_mensaje;
end;
$$ language	plpgsql;

SELECT gestionar_funcion_iud(
    'INSERT',
    null, -- id
    '2024-03-18', -- fecha anio,mes,dia
    '15:30:00', -- hora
    10.50, -- orecio
    true, -- disponibilidad
    11 -- id película de 1 a 15 menos 13
);
select * from funcion f ;
SELECT gestionar_funcion_iud(
    'UPDATE',
    7, -- id
    '2024-03-18', -- fecha anio,mes,dia
    '14:30:00', -- hora
    15.50, -- orecio
    true, -- disponibilidad
    10 -- id película de 1 a 15 menos 13
);
select * from funcion f ;

SELECT gestionar_funcion_iud(
    'DELETE',
    8, -- id
    null, 
    null,
    null,
    null,
    null
);

select * from funcion f ;

