--1

--2
create or replace function buscar_pelicula1(nombre_pelicula VARCHAR)
returns table (titulo VARCHAR,
               genero VARCHAR)
as $$
begin
    if nombre_pelicula is null then
        return QUERY select p.titulo, g.nombreGenero
                     from pelicula p
                     join generoPelicula gp on p.IDPelicula = gp.IDPelicula
                     join genero g on gp.IDGenero = g.IDGenero;
    else
        return QUERY select p.titulo, g.nombreGenero
                     from pelicula p
                     join generoPelicula gp on p.IDPelicula = gp.IDPelicula
                     join genero g on gp.IDGenero = g.IDGenero
                     where p.titulo ilike '%' || nombre_pelicula || '%';
    end if;
end;
$$ language plpgsql;

select * from buscar_pelicula1();

--3
create or replace function listar_pagos_tipo_pago()
returns table (fecha_pago DATE,
               monto_pago DECIMAL(18,2),
               metodo_pago VARCHAR(25)) AS
$$
begin
    create temp table PagosTipoPago as
    select p.fechaPago, p.montoPago, tp.metodoPago
    from pago p
    join tipoPago tp on p.IDTipoPago = tp.IDTipoPago;

    return QUERY select * from PagosTipoPago;
end;
$$ language plpgsql;

select * from listar_pagos_tipo_pago();

