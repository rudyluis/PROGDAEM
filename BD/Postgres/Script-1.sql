create or replace function mostrar_hola_mundo_v2()
returns text as $$
begin 
	raise notice 'Bases de Datos II';
	raise notice 'Hola Mundo';
	RETURN 'Hola mundo todo bien';
end;
$$ language plpgsql;


select * from mostrar_hola_mundo_v2(); 

create or replace procedure  mostrar_hola_mundo_proc()
as $$
begin 
	raise notice 'Bases de Datos II';
	raise notice 'Hola Mundo';
end;
$$ language plpgsql;

call mostrar_hola_mundo_proc(); 


------------------------------------------

create or replace  function suma_numeros(a int ,b int )
returns int as $$
declare 
	resultado int;
begin
	resultado:=a+b;
 	return resultado;
end;
$$ language plpgsql;


select suma_numeros(4,5);


select mostrar_mensaje('hola que tal';)


create or replace function mostrar_mensaje(mensaje text)
returns text as $$
declare 
	x int;
begin
	x:=5;
	return 'Hola '||mensaje||x::text||' años';
end;
$$ language plpgsql;
 
select mostrar_mensaje('Valeria');


-----------------------
create or replace function comparar_valores(a int ,b int)
returns text as $$
begin
	if(a>b) then
		return 'el mayor es: '||a;
	else
		return 'el mayor es: '||b;
	end if;
end;
$$ language plpgsql;

select comparar_valores(3,4);

create or replace function comparar_numeros_3(a int, b int, c int)
returns text as $$
begin
	if (a > b and a > c)then --- comparadores no hace falta el doble igual y el distinto es asi != o <> ---
		return 'El mayor es '||a;
	elseif (b > a and b > c) then
		return 'El mayor es '||b;
	else
		return 'El mayor es '||c;
	end if;
end;
$$ language plpgsql;
 
select comparar_numeros_3(100,2999,3);


create or replace  function  mostrar_numeros_hasta_n(n int)
returns void as $$
declare 
	contador int :=1;
begin
	loop
		exit when contador>n;
		raise notice 'Numero: %',contador;
		contador:=contador+1;
	end loop;
	
end
$$ language plpgsql;

select mostrar_numeros_hasta_n(10);

------------------------------------
create or replace  function  factorial(n int)
returns int as $$
declare
	i int :=1;
	resultado int:=1;
begin 
	while i<=n loop
		resultado:=resultado*i;
		i:=i+1;
		raise notice 'la variable i--->%, resultado--->%',i,resultado;
	end loop;
	return resultado;
end;
$$ language plpgsql;

select factorial(5);


------------------------------
create or replace  function  mostrar_numeros_hasta_n_forv2(n int)
returns setof int as $$
declare 
	contador int :=1;
begin
	for contador in 1..n loop
		---raise notice 'Numero: %', contador;
		return next contador;
	end loop;
	
	
end
$$ language plpgsql;


select mostrar_numeros_hasta_n_forv2(6);



create or replace function es_primo( numero int)
returns boolean as $$
declare
     sw int :=0;
begin
	if numero <=1 then
		return false;
	end if;

	for contador in 1..numero loop
		if numero % contador =0 then
			sw:=sw+1;
		end if;
	end loop;

if sw=2 then
		return true;
	else
		return false;
	end if;
end;
$$ language plpgsql;


select es_primo(19);



---------------------

create or replace function fibonacci(n int)
returns setof int as $$
declare
	f1 INT :=0;
	f2 INT :=1;
	nextF INT;
begin		
	return next f1;
	return next f2;
	FOR i in 3..n loop
		nextF:= f1+f2;
		return next nextF;
		f1=f2;
		f2=nextF;
	end loop;
	return;
end;
$$ language plpgsql;
 
select fibonacci(25);


create or replace function suma_pares (n int)
returns int as $$
declare
	contador int:=1;
	primos int:=0;
begin
	for contador in 1..n loop
		if MOD(contador,2)=0 then
			primos=primos+contador;
		end if;
	end loop;
return primos;
end;
$$ language plpgsql;
 
select suma_pares (8);
