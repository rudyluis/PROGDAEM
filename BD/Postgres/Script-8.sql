CREATE OR REPLACE FUNCTION calcular_ventas_totales_producto()
RETURNS TABLE (id int, producto varchar, total_ventas numeric(18,2)) AS $$
DECLARE
    -- Declaración de variables locales
    temp_table_name TEXT := 'temp_ventas_totales' ; -- Nombre de tabla temporal aleatorio
begin
	 raise notice 'tabla---> %',temp_table_name;
    -- Crear tabla temporal para almacenar resultados
    EXECUTE 'CREATE TEMP TABLE ' || temp_table_name || ' (id serial not null, producto varchar, total_ventas NUMERIC(18,2))';
 	EXECUTE format('
        INSERT INTO %I (producto, total_ventas)
        select 
			p.nombre, 
			sum(coalesce((d.cantidad*d.preciounidad),0))::numeric(18,2) as total_ventas 
			from detallepedido d 
			inner join producto p on p.idproducto =d.idpedido 
			group by p.nombre
			order by p.nombre;', temp_table_name);
    ---
  
    -- Devolver resultados de la tabla temporal
    RETURN QUERY EXECUTE format('SELECT * FROM %s', temp_table_name);
    -- Eliminar tabla temporal al finalizar
    EXECUTE 'DROP TABLE IF EXISTS ' || temp_table_name;
END;
$$ LANGUAGE plpgsql;



SELECT * FROM calcular_ventas_totales_producto();


select 
	p.nombre, 
	sum(coalesce((d.cantidad* d.preciounidad),0))::numeric(18,2) as total_ventas 
from detallepedido d 
inner join producto p on p.idproducto =d.idpedido 
group by p.nombre
order by p.nombre;

        
        
        
        
SELECT table_name 
FROM information_schema.tables
WHERE table_catalog= 'jardineria'  -- Cambia 'public' al esquema que desees consultar, si es diferente
      AND table_type = 'BASE TABLE' and table_schema ='public';   
     
 select * from pedido p ;
