--1. Calcula la fecha del primer y último pago realizado por cada uno de los clientes. 
El listado deberá mostrar el nombre y los apellidos de cada cliente.

SELECT 
  c.nombreCliente, 
  c.nombreContacto, 
  c.apellidoContacto, 
  MIN(p.fechaPago) AS primerPago, 
  MAX(p.fechaPago) AS ultimoPago
FROM cliente c
JOIN pago p ON c.IDCliente = p.IDCliente
GROUP BY c.IDCliente;



----2. Devuelve un listado de los 20 productos más vendidos y el número total de unidades q
ue se han vendido de cada uno. 
El listado deberá estar ordenado por el número total de unidades vendidas.

SELECT 
  pr.nombre, 
  SUM(dp.cantidad) AS totalUnidadesVendidas
FROM producto pr
JOIN detallePedido dp ON pr.IDProducto = dp.IDProducto
GROUP BY pr.IDProducto
ORDER BY totalUnidadesVendidas DESC
LIMIT 20;


---3. La facturación que ha tenido la empresa en toda la historia, 
indicando la base imponible, el IVA y el total facturado.

SELECT 
  SUM(dp.cantidad * dp.precioUnidad) AS baseImponible,
  SUM(dp.cantidad * dp.precioUnidad) * 0.21 AS IVA,
  SUM(dp.cantidad * dp.precioUnidad) * 1.21 AS totalFacturado
FROM detallePedido dp;


---4. Lista las ventas totales de los productos que hayan facturado más de 3000 dólares. Se mostrará el nombre, unidades vendidas, total facturado y total facturado con impuestos (13% IVA).

SELECT 
  pr.nombre, 
  SUM(dp.cantidad) AS unidadesVendidas, 
  SUM(dp.cantidad * dp.precioUnidad) AS totalFacturado,
  SUM(dp.cantidad * dp.precioUnidad) * 1.13 AS totalConImpuestos
FROM producto pr
JOIN detallePedido dp ON pr.IDProducto = dp.IDProducto
GROUP BY pr.IDProducto
HAVING SUM(dp.cantidad * dp.precioUnidad) > 3000;


--SUBCONSULTAS
--5.	Devuelve el nombre del cliente con mayor límite de crédito.
SELECT nombreCliente
FROM cliente
WHERE limite_credito = (SELECT MAX(limite_credito) FROM cliente);

--6.	Devuelve el nombre del producto del que se han vendido más unidades. (Tenga en cuenta que tendrá que calcular cuál es el número total de unidades que se han vendido de cada producto a partir de los datos de la tabla detalle_pedido)
SELECT pr.nombre
FROM producto pr
JOIN detallePedido dp ON pr.IDProducto = dp.IDProducto
GROUP BY pr.IDProducto
ORDER BY SUM(dp.cantidad) DESC
LIMIT 1;

--7.	Devuelve el producto que más unidades tiene en stock.
SELECT nombre
FROM producto
ORDER BY cantidadStock DESC
LIMIT 1;


--Subconsultas con ALL 
--8.	Devuelve el nombre del cliente con mayor límite de crédito.

SELECT nombreCliente
FROM cliente
WHERE limite_credito = ALL (SELECT MAX(limite_credito) FROM cliente);


--Subconsultas con IN y NOT IN
--9.	Devuelve el nombre, apellido1 y cargo de los empleados que no representen a ningún cliente.

SELECT nombre, apellido1, puesto
FROM empleado
WHERE IDEmpleado NOT IN (SELECT IDcodigoEmpleadoVentas FROM cliente);


--10.	Devuelve un listado de los productos que nunca han aparecido en un pedido.

SELECT nombre
FROM producto
WHERE IDProducto NOT IN (SELECT DISTINCT IDProducto FROM detallePedido);


--11.	Devuelve el nombre, apellidos, puesto y teléfono de la oficina de aquellos empleados que no sean representante de ventas de ningún cliente.

SELECT e.nombre, e.apellido1, e.puesto, e.extension, o.ciudad
FROM empleado e
JOIN oficina o ON e.IDOficina = o.IDOficina
WHERE e.IDEmpleado NOT IN (SELECT IDcodigoEmpleadoVentas FROM cliente);

--12.	Devuelve un listado con los clientes que han realizado algún pedido pero no han realizado ningún pago.

SELECT c.nombreCliente
FROM cliente c
JOIN pedido p ON c.IDCliente = p.IDCliente
LEFT JOIN pago pa ON c.IDCliente = pa.IDCliente
WHERE pa.IDPago IS NULL;


---Subconsultas con EXISTS y NOT EXISTS
--13.	Devuelve un listado que muestre solamente los clientes que no han realizado ningún pago.

SELECT nombreCliente
FROM cliente c
WHERE NOT EXISTS (SELECT 1 FROM pago p WHERE c.IDCliente = p.IDCliente);


--14.	Devuelve un listado de los productos que nunca han aparecido en un pedido.

SELECT nombre
FROM producto pr
WHERE NOT EXISTS (SELECT 1 FROM detallePedido dp WHERE pr.IDProducto = dp.IDProducto);


--Consultas de LEFT JOIN
--15.	Devuelve un listado con los nombres de los clientes y el total pagado por cada uno de ellos. Tenga en cuenta que pueden existir clientes que no han realizado ningún pago.


SELECT c.nombreCliente, COALESCE(SUM(p.total), 0) AS totalPagado
FROM cliente c
LEFT JOIN pago p ON c.IDCliente = p.IDCliente
GROUP BY c.IDCliente;


---16.	Devuelve el nombre, apellidos, puesto y teléfono de la oficina de aquellos empleados que no sean representante de ventas de ningún cliente.

SELECT e.nombre, e.apellido1, e.puesto, e.extension, o.ciudad
FROM empleado e
JOIN oficina o ON e.IDOficina = o.IDOficina
WHERE e.IDEmpleado NOT IN (SELECT IDcodigoEmpleadoVentas FROM cliente);


--17.	Devuelve un listado indicando todas las ciudades donde hay oficinas y el número de empleados que tiene.

SELECT o.ciudad, COUNT(e.IDEmpleado) AS numeroEmpleados
FROM oficina o
LEFT JOIN empleado e ON o.IDOficina = e.IDOficina
GROUP BY o.ciudad;


