create or replace function buscar_pelicula(nombre varchar)
returns varchar as $$
declare contador int :=1; 
declare query varchar;  
begin 
 loop 
	 query= 'Select p.titulo from pelicula p inner join sucursalpelicula sp on p.idpelicula= sp.idpelicula 
              where titulo = nombre'
	 
	 if 

 end loop;
 
end
$$ language plpgsql;


SELECT buscar_pelicula('Comedia Loca');





create or replace function CRUD_insert( crud_ind varchar, cd_fecha date , cd_hora time , cd_precio numeric(18,8), cd_disponibilidad bool, cd_idpelicula int)
)
returns varchar as $$
declare 
p_mensaje varchar ;
begin 
 if crud_ind 'Insert' then
  Insert into Funcion(fecha, hora, precio, disponibilidad, idpelicula)
   BEGIN
        INSERT INTO funcion (crud_ind, fecha, hora, precio, disponibilidad, idpelicula)
        VALUES ( cd_fecha, cd_hora, cd_precio, cd_disponibilidad, cd_idpelicula);

        SET @idFuncion = SCOPE_IDENTITY();
    END

  values(
 
 
end; 

$$ language plpgsql;

CREATE PROCEDURE InsertarFuncion (
    IN p_crud_ind VARCHAR(10),
    IN p_fecha DATE,
    IN p_hora TIME,
    IN p_precio NUMERIC(18, 8),
    IN p_disponibilidad BOOLEAN,
    IN p_idpelicula INT
)
BEGIN
    INSERT INTO funcion (crud_ind, fecha, hora, precio, disponibilidad, idpelicula)
    VALUES (p_crud_ind, p_fecha, p_hora, p_precio, p_disponibilidad, p_idpelicula);
END //

DELIMITER ;

-- Función para leer datos de la tabla "funcion"
CREATE PROCEDURE LeerFunciones ()
BEGIN
    SELECT * FROM funcion;
end;
$$ language plpgsql;


-- Función para actualizar datos en la tabla "funcion"


CREATE PROCEDURE ActualizarFuncion (
    IN p_id INT,
    IN p_crud_ind VARCHAR(10),
    IN p_fecha DATE,
    IN p_hora TIME,
    IN p_precio NUMERIC(18, 8),
    IN p_disponibilidad BOOLEAN,
    IN p_idpelicula INT
)
BEGIN
    UPDATE funcion
    SET
        crud_ind = p_crud_ind,
        fecha = p_fecha,
        hora = p_hora,
        precio = p_precio,
        disponibilidad = p_disponibilidad,
        idpelicula = p_idpelicula
    WHERE
        id = p_id;
end;
$$ language plpgsql;





CREATE PROCEDURE BorrarFuncion (IN p_id INT)
BEGIN
    DELETE FROM funcion WHERE id = p_id;
end; 
$$ language plpgsql;