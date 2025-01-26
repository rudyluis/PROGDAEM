use cine;
/*10*/
select count(*)  as total_reservas_QR
from reserva r
inner join pago p on  r.IDReserva= p.IDreserva
inner join tipoPago tp on tp.IdPago= p.IdPago
inner join qr q on q.IDTipoPago= tp.IdTipoPago;
/*12*/

SELECT p.titulo,c.nombreClasificacion FROM pelicula p
JOIN clasificacion c ON p.IDClasificacion=c.IDClasificacion
WHERE c.nombreClasificacion like '%Mayores de 18 años%';

/*14*/
select titulo, max(duracion) as duracion from pelicula;
/*16*/

select p.titulo 
from pelicula p
inner join funcion f on f.IDPelicula=p.IDPelicula
left join sala s on s.IDFuncion = f.IDFuncion;
/*18*/
SELECT  concat(cliente.nombre,' ',cliente.apellidoPaterno,' ',cliente.apellidoMaterno) as nombre_cliente, 
COUNT(reserva.IDReserva) as NumeroDeReservas
FROM cliente
JOIN reserva on cliente.IDCliente = reserva.IDCliente
GROUP BY cliente.IDCliente;

/*20*/

select cli.nombre
from reserva r
join cliente  cli on r.IDCliente = cli.IDCliente 
inner join pago p on  r.IDReserva= p.IDreserva
inner join tipoPago tp on tp.IdPago= p.IdPago
inner join efectivo e on tp.IDTipoPago = e.IDTipoPago;

/*22*/
SELECT DISTINCT c.nombre, c.apellidoPaterno, c.apellidoMaterno
FROM cliente c
JOIN reserva r ON c.IDCliente = r.IDCliente
JOIN funcion f ON r.IDFuncion = f.IDFuncion
JOIN sala s ON f.IDFuncion = s.IDFuncion
WHERE s.tipoPantalla = '3D';

/*24*/
SELECT COUNT(*)  as numero_funciones 
FROM sala WHERE tipoPantalla = 'Plana'
group by tipoPantalla;

/*26*/

SELECT COUNT(*) AS asientos_ocupados_sala_2
FROM asiento
WHERE IDReserva IN (SELECT IDReserva FROM reserva WHERE IDFuncion = 4);



select count(*) as asientos_ocupados
from asiento a
inner join reserva r on a.IDReserva= r.IDReserva
inner join  funcion f on f.IDfuncion = r.IDFuncion
inner join sala s on f.IDFuncion=s.IDFuncion
where s.numeroSala=2 

