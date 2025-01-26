create or replace function meses_dif(fecha1 date , fecha2 date)
returns INTEGER as $$
declare 
	v_meses_dif int;
begin
    v_meses_dif:=EXTRACT(year  from age(fecha1,fecha2))*12 +extract(month from age(fecha1,fecha2)) ;
	return v_meses_dif;
end;
$$ language plpgsql;


select meses_dif('2024-03-04'::date,'2021-12-24'::date);


select age('2023-12-25'::date);
 
select extract(dayfrom now()) ;


------ cliente sin pagos




CREATE OR REPLACE FUNCTION cliente_sin_pagos()
RETURNS setof RECORD AS $$
declare
    cliente_cursor cursor for 
						   	select c.nombrecliente 
						   	from cliente c
						   	left join pago p on c.idcliente=p.idcliente
						   	where p.idpago is null;
   	cliente_record record;
BEGIN
   open cliente_cursor;
  		loop
  			fetch cliente_cursor into cliente_record;
  			exit when not found;
  			return next cliente_record;
  		end loop;

   close cliente_cursor; 
   if not found then
  		raise notice 'No se encontraron clientes sin pagos';
   end if;
END;
$$ LANGUAGE plpgsql;


select * from cliente_sin_pagos () as (cliente_sin_pagos varchar);



CREATE OR REPLACE FUNCTION cliente_sin_pagos_cursor_for()
RETURNS setof RECORD AS $$
declare
   	cliente_record record;
BEGIN
 	for cliente_record in (
 			select c.nombrecliente 
				from cliente c
				left join pago p on c.idcliente=p.idcliente
			    where p.idpago is null
 	)  loop
 		return next cliente_record;
 	end loop;
 	if not found then
 		return query values('No se encontraron clientes sin pagos'::varchar);
 	end if;
END;
$$ LANGUAGE plpgsql;


select * from cliente_sin_pagos_cursor_for () as (cliente_sin_pagos varchar);


------------------ tablas temporales--------------



