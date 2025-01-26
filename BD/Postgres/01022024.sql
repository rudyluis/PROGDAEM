create  table inventario(
	IDinventario serial primary key,
	IDProducto integer not null,
	fechamovimiento date not null,
	tipomovimiento varchar(20) not null,
	cantidad integer not null,
	comentario text,
	foreign key (IDProducto) references producto (idproducto)
);

create or replace function actualizar_stock()
returns trigger as $$
declare
	stock_actual int;
begin 
	
	if new.tipomovimiento='Entrada' then
		update producto 
		set cantidadstock=cantidadstock+new.cantidad
		where idproducto=new.idproducto;
	elseif new.tipomovimiento='Salida' then
		select cantidadstock into stock_actual
		from producto p 
		where idproducto=new.idproducto;
	
		if stock_actual - new.cantidad <0 then
			raise exception 'No hay suficiente cantidad de stock para el producto elegido %',new.idproducto;
		
		else
			update producto 
			set cantidadstock=cantidadstock-new.cantidad
			where idproducto=new.idproducto;
		end if;

	end if;
	return new;
end;
$$ language plpgsql;


create trigger trigger_actualizar_stock
after insert on inventario
for each row 
execute function actualizar_stock();



select * from producto where idproducto =1;





create or replace function registrar_inventario_insert()
returns trigger as $$
begin 
	insert into inventario (idproducto, cantidad, fechamovimiento, tipomovimiento,comentario)
	values (new.idproducto, new.cantidad, now(), 'Salida', 'Venta de Cliente');
	return new;
end;
$$ language plpgsql;


create trigger trigger_registrar_inventario_insert
after insert on detallepedido
for each row 
execute function registrar_inventario_insert();



create or replace function registrar_inventario_delete()
returns trigger as $$
begin 
	insert into inventario (idproducto, cantidad, fechamovimiento, tipomovimiento,comentario)
	values (OLD.idproducto, OLD.cantidad, now(), 'Entrada', 'Devolucion de Producto');
	return OLD;
end;
$$ language plpgsql;



create trigger trigger_registrar_inventario_delete
after delete on detallepedido
for each row 
execute function registrar_inventario_delete();



select * from detallepedido d where idpedido =1

select * from inventario i ;

create or replace function registrar_inventario_update()
returns trigger  as $$
begin 
	if old.cantidad <> new.cantidad then
		insert into inventario (idproducto, cantidad, fechamovimiento, tipomovimiento,comentario)
		values (OLD.idproducto, OLD.cantidad, now(), 'Entrada', 
		'Cambio de Producto '||new.idproducto::varchar);
		insert into inventario (idproducto, cantidad, fechamovimiento, tipomovimiento,comentario)
		values (new.idproducto, new.cantidad, now(), 'Salida', 
		'Actualizcación de producto'||new.idproducto::varchar);
	end if;
	return new;
end;
$$ language plpgsql;


create trigger trigger_registrar_inventario_update
after update on detallepedido
for each row 
execute function  registrar_inventario_update();


-------------------------


create table system_log(
	log_id serial primary key,
	log_timestamp timestamp default current_timestamp,
	log_usuario varchar default current_user,
	log_level varchar(10) not null,
	log_message text not null
);


select * from system_log ;



create or replace function system_log_trigger()
returns trigger  as $$
begin 
	if(TG_OP='INSERT') then
		insert into system_log(log_level, log_message)
		values('ADD', 'Nuevo registro Insertado en la tabla '||TG_TABLE_NAME);
	end if;
	if(TG_OP='UPDATE') then
		insert into system_log(log_level,log_message)
		values('UPDATE','Registro Actualizado en la tabla '||TG_TABLE_NAME);
	end if;
	if(TG_OP='DELETE') then
		insert into system_log(log_level,log_message)
		values('DELETE','Registro Eliminado en la tabla '||TG_TABLE_NAME||old);
	end if;

	return new;
end;
$$ language plpgsql;

create trigger system_log_trigger
after insert or update or delete on oficina
for each row 
execute function system_log_trigger();










