/*1*/
use jardineria;
select o.codigoOficina, o.ciudad from oficina o;
/*2*/
select ciudad,telefono from oficina where pais='España';

/*3*/

SELECT nombre || ' ' || apellido1 || ' ' || apellido2 AS nombre, email 
FROM empleado 
WHERE IDEmpleadoJefe = 7;


/*4*/
SELECT nombre || ' ' || apellido1 || ' ' || apellido2 AS nombre, email 
from empleado 
where IDEmpleadoJefe is null;

/*5*/

select concat(nombre,' ',apellido1,' ',apellido2) as nombre  from empleado where puesto <>'Representante Ventas';

/*6*/
select distinct estado from pedido;

/*7*/
SELECT DISTINCT IDCliente 
FROM pago 
WHERE fechaPago BETWEEN '2008-01-01' AND '2008-12-31';

/*select distinct IDcliente from pago where Year(fechaPago)=2008;
select distinct IDcliente from pago where date_format(fechaPago,'%Y')=2008;  --- 
select distinct IDcliente from pago where fechaPago>='2008-01-01' and fechaPago<='2008-12-31';
SELECT DISTINCT c.codigoCliente
FROM cliente c
JOIN pago p ON c.IDCliente = p.IDCliente
WHERE YEAR(p.fechaPago) = 2008;*/

/*8*/
select codigoPedido, IDCliente, fechaEsperada, fechaEntrega from pedido
where estado='Entregado' and fechaEntrega>fechaEsperada;

/*9*/
/*
select codigoPedido, IDCliente, fechaEsperada, fechaEntrega  
from pedido  where adddate(fechaEntrega,2)<=fechaEsperada;
*/

SELECT codigoPedido, IDCliente, fechaEsperada, fechaEntrega  
FROM pedido  
WHERE fechaEntrega + INTERVAL '2 days' <= fechaEsperada;


select codigoPedido, IDCliente, fechaEsperada, fechaEntrega  
from pedido  where datediff(fechaEsperada,fechaEntrega)>=2;

select codigoPedido, IDCliente, fechaEsperada, fechaEntrega  
from pedido  where fechaEntrega + interval 2 DAY <= fechaEsperada;

/*10*/
SELECT codigoPedido, IDCliente, fechaEsperada, fechaEntrega
FROM pedido
WHERE estado = 'Rechazado' AND YEAR(fechaEntrega) = 2009;

/*11*/
/*
select IDPedido,estado from pedido where month(fechaEntrega)="01" and estado="Entregado";
*/

SELECT IDPedido, estado 
FROM pedido 
WHERE fechaEntrega BETWEEN '2009-01-01' AND '2009-01-31' 
AND estado = 'Entregado';

/*12*/



SELECT * 
FROM pago 
WHERE fechaPago BETWEEN '2008-01-01' AND '2008-12-31' 
AND formaPago = 'PayPal'
ORDER BY total DESC;


/*13*/
select p.* from producto p
inner join gamaProducto g on g.IDGamaProducto= p.IDGamaProducto
where g.gama='Ornamentales' and  p.cantidadStock>100
order by precioVenta;

/*opcion B*/
SELECT p.IDProducto, p.nombre, p.cantidadStock, p.precioVenta
FROM producto p
INNER JOIN gamaProducto g ON g.IDGamaProducto = p.IDGamaProducto
WHERE g.gama = 'Ornamentales' AND p.cantidadStock > 100
ORDER BY p.precioVenta;

/*SEGUNDA PARTE*/
/*1*/
select c.nombreContacto as cliente , e.Nombre as rep_ventas
from cliente c 
inner join empleado e on c.IDcodigoEmpleadoVentas=e.IDEmpleado;

/*2*/
select c.nombreContacto as cliente , e.Nombre as rep_ventas
from cliente c 
inner join empleado e on c.IDcodigoEmpleadoVentas=e.IDEmpleado
inner join pago p on c.IDCliente= p.IDCliente;

/*3*/
select c.nombreContacto as cliente , e.Nombre as rep_ventas
from cliente c 
inner join empleado e on c.IDcodigoEmpleadoVentas=e.IDEmpleado
where c.IDCliente not in(select Distinct p.IDCliente from pago p);

/*4*/
select c.nombreContacto as cliente , e.Nombre as rep_ventas, o.ciudad
from cliente c 
inner join empleado e on c.IDcodigoEmpleadoVentas=e.IDEmpleado
inner join pago p on c.IDCliente= p.IDCliente
inner join oficina o on o.IDOficina=e.IDOficina;

/*5*/

select c.nombreContacto as cliente , e.Nombre as rep_ventas, o.ciudad
from cliente c 
inner join empleado e on c.IDcodigoEmpleadoVentas=e.IDEmpleado
inner join oficina o on o.IDOficina=e.IDOficina
where c.IDCliente not in(select Distinct p.IDCliente from pago p);


/*6*/
select distinct o.lineaDireccion1 from oficina o
inner join empleado e on e.IDOficina=o.IDOficina
inner join cliente c on c.IDcodigoEmpleadoVentas=e.IDEmpleado
where c.ciudad='FuenLabrada' ;

/*9*/
select distinct c.nombreCliente, g.gama
from cliente c
inner join pedido p on c.IDCliente=p.IDCliente
inner join detallePedido dp on p.IDPedido= dp.IDPedido
inner join producto pr on pr.IDProducto=dp.IDProducto
inner join gamaProducto g on g.IDGamaProducto=pr.IDGamaProducto;
















 


