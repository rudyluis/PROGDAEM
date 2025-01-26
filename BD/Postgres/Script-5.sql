
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


select * from obtener_suma_pagos2(1) as (total_pagos numeric);



CREATE OR REPLACE FUNCTION obtener_suma_pagos3(pm_codigo_cliente INT default '0')
RETURNS SETOF RECORD AS $$
DECLARE 
	g_registros RECORD;
	query TEXT;
begin
	if(pm_codigo_cliente =0)then
		query := 'SELECT ''TOTAL GENERAL''::varchar , COALESCE(SUM(p.total), 0)::NUMERIC AS total
   	          FROM pago p
   	          INNER JOIN cliente c ON c.idcliente = p.idcliente
   	          ';
  	else
		query := 'SELECT codigocliente::varchar as cliente, COALESCE(SUM(p.total), 0)::NUMERIC AS total
   	          FROM pago p
   	          INNER JOIN cliente c ON c.idcliente = p.idcliente
   	          WHERE codigocliente = ' || pm_codigo_cliente||'
			  group by codigocliente';
	end if;
   	

   	FOR g_registros IN EXECUTE query loop
	   	raise notice '%',g_registros;
   		RETURN NEXT g_registros;
   	END LOOP;
END;
$$ LANGUAGE plpgsql;


select * from obtener_suma_pagos3() as (cliente varchar , total_pagos numeric);