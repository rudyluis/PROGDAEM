------- PARA TRIGGERS
---- INVENTARIO

CREATE TABLE inventario (
    IDInventario SERIAL PRIMARY KEY,
    IDProducto INTEGER NOT NULL,
    fechaMovimiento DATE NOT NULL,
    tipoMovimiento VARCHAR(20) NOT NULL, -- Por ejemplo: 'Entrada' o 'Salida'
    cantidad INTEGER NOT NULL,
    comentario TEXT,
    FOREIGN KEY (IDProducto) REFERENCES producto (IDProducto)
);

CREATE OR REPLACE FUNCTION actualizar_stock()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.tipoMovimiento = 'Entrada' THEN
        UPDATE producto
        SET cantidadStock = cantidadStock + NEW.cantidad
        WHERE IDProducto = NEW.IDProducto;
    ELSIF NEW.tipoMovimiento = 'Salida' THEN
        UPDATE producto
        SET cantidadStock = cantidadStock - NEW.cantidad
        WHERE IDProducto = NEW.IDProducto;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_actualizar_stock
AFTER INSERT ON inventario
FOR EACH ROW
EXECUTE FUNCTION actualizar_stock();



----- modificamos agregando un mensaje

CREATE OR REPLACE FUNCTION actualizar_stock()
RETURNS TRIGGER AS $$
DECLARE
    stock_actual INTEGER;
BEGIN
    IF NEW.tipoMovimiento = 'Entrada' THEN
        UPDATE producto
        SET cantidadStock = cantidadStock + NEW.cantidad
        WHERE IDProducto = NEW.IDProducto;
    ELSIF NEW.tipoMovimiento = 'Salida' THEN
        SELECT cantidadStock INTO stock_actual
        FROM producto
        WHERE IDProducto = NEW.IDProducto;

        IF stock_actual - NEW.cantidad < 0 THEN
            RAISE EXCEPTION 'No hay suficiente stock para el producto ID %', NEW.IDProducto;
        ELSE
            UPDATE producto
            SET cantidadStock = cantidadStock - NEW.cantidad
            WHERE IDProducto = NEW.IDProducto;
        END IF;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_actualizar_stock
AFTER INSERT ON inventario
FOR EACH ROW
EXECUTE FUNCTION actualizar_stock();


------------------ para detalle pedidio


-- Trigger para inserciones en detallePedido
CREATE OR REPLACE FUNCTION registrar_inventario_insert()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO inventario (idproducto, cantidad, fechamovimiento, tipomovimiento,comentario)
    VALUES (NEW.IDProducto, NEW.cantidad, NOW(), 'Salida','Venta Productos');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_registrar_inventario_insert
AFTER INSERT ON detallePedido
FOR EACH ROW
EXECUTE FUNCTION registrar_inventario_insert();

-- Trigger para actualizaciones en detallePedido
CREATE OR REPLACE FUNCTION registrar_inventario_update()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.cantidad <> NEW.cantidad then
    	INSERT INTO inventario (idproducto, cantidad, fechamovimiento, tipomovimiento,comentario)
        VALUES (NEW.IDProducto, OLD.cantidad, NOW(), 'Entrada','Cambio de Producto'||NEW.IDProducto::varchar);
        INSERT INTO inventario (idproducto, cantidad, fechamovimiento, tipomovimiento,comentario)
        VALUES (NEW.IDProducto, NEW.cantidad, NOW(), 'Salida','Cambio de Producto'||NEW.IDProducto::varchar);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_registrar_inventario_update
AFTER UPDATE ON detallePedido
FOR EACH ROW
EXECUTE FUNCTION registrar_inventario_update();

-- Trigger para eliminaciones en detallePedido
CREATE OR REPLACE FUNCTION registrar_inventario_delete()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO inventario (idproducto, cantidad, fechamovimiento, tipomovimiento,comentario)
     VALUES (OLD.IDProducto, OLD.cantidad, NOW(), 'Entrada','Devolucion de  Producto'||OLD.IDProducto::varchar);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_registrar_inventario_delete
AFTER DELETE ON detallePedido
FOR EACH ROW
EXECUTE FUNCTION registrar_inventario_delete();







