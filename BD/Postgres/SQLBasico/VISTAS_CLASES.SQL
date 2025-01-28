/*
Una vista en SQL es una tabla virtual que se crea a partir de una consulta. 
Aunque parece una tabla real, no almacena los datos directamente, sino que obtiene los datos dinámicamente 
a partir de las tablas subyacentes definidas en la consulta.

Características principales:
Tabla virtual: No ocupa espacio adicional en la base de datos, ya que no almacena los datos.
Consulta predefinida: Es una consulta que se guarda y puede ser reutilizada como si fuera una tabla.
Simplificación: Permite simplificar consultas complejas al encapsularlas dentro de una vista.
Seguridad: Puede restringir el acceso a datos sensibles mostrando solo las columnas o filas necesarias.

*/

CREATE OR REPLACE VIEW vista_pedidos_producto1 AS
SELECT
    p.idProducto,
    p.descripcion AS Producto,
    COUNT(dp.idPedido) AS TotalPedidos
FROM
    producto p
LEFT JOIN
    detallepedido dp ON p.idProducto = dp.idProducto
GROUP BY
    p.idProducto, p.descripcion
ORDER BY
    TotalPedidos DESC; 

SELECT * FROM vista_pedidos_producto1;


----TRIGGERS
/*

¿Qué es un Trigger en SQL?
Un trigger es un tipo especial de procedimiento almacenado que se ejecuta automáticamente 
en respuesta a ciertos eventos que ocurren en una tabla o vista. Estos eventos pueden ser:

INSERT: Cuando se inserta un nuevo registro.
UPDATE: Cuando se actualiza un registro existente.
DELETE: Cuando se elimina un registro.
Los triggers permiten definir lógica que se ejecuta automáticamente en la base de datos, 
lo que los hace útiles para mantener la integridad de los datos, auditar cambios y automatizar tareas.


*/
/*

Beneficios de los Triggers
Automatización de tareas repetitivas:

Realizan acciones automáticamente, como registros de auditoría o actualizaciones en tablas relacionadas.
Mantener la integridad referencial:

Garantizan que ciertas reglas o restricciones se cumplan en los datos.
Auditoría:

Permiten rastrear cambios en los datos (qué cambió, quién lo cambió, cuándo lo hizo).
Cálculos en tiempo real:

Pueden realizar actualizaciones automáticas de datos derivados.
Centralización de la lógica:

Reducen la necesidad de lógica repetitiva en el código de la aplicación, 
ya que la base de datos maneja las reglas.
Dificultades o desventajas de los Triggers
Rendimiento:

Los triggers se ejecutan automáticamente y pueden impactar negativamente en el rendimiento 
si realizan operaciones complejas o en grandes volúmenes de datos.
Dificultad para depurar:

La lógica de los triggers puede ser difícil de rastrear, especialmente si hay múltiples 
triggers asociados a una tabla.
Complejidad oculta:

Los triggers pueden introducir comportamientos no evidentes para los desarrolladores que trabajan en el sistema, lo que puede causar errores inesperados.
Impacto en la mantenibilidad:

Si no están documentados adecuadamente, pueden dificultar el mantenimiento de la
 base de datos y de las aplicaciones relacionadas.
Orden de ejecución:

En sistemas con varios triggers asociados a una misma tabla, controlar el orden de 
ejecución puede ser complicado.
Cuándo usar triggers
Para auditoría (registro de cambios en los datos).
Para mantener la integridad de los datos entre tablas relacionadas.
Para realizar cálculos automáticos basados en cambios en los datos.
Cuando las acciones automáticas deben ejecutarse independientemente del cliente 
o aplicación que acceda a la base de datos.

*/
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