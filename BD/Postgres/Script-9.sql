create or replace function info_empleados()
returns setof record as $$
declare
	empleado cursor for
		select (e.nombre ||' '|| e.apellido1 ||' '|| e.apellido2):: varchar as nombre_empleado,
		e.email, e.puesto from empleado e;
	r_record RECORD;
begin
	open empleado;
		loop
			fetch empleado into r_record;
				exit when not found;
			return next r_record;
			
		end loop;
		
	close empleado;
end;
 
$$ language plpgsql;
	
select * from info_empleados() as (nombre_empleado varchar, email varchar, puesto varchar);