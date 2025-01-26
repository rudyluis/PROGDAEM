--1
CREATE OR REPLACE FUNCTION listar_sucursal_pelicula(p_titulo VARCHAR)
RETURNS TABLE(nombre_pelicula VARCHAR, sucursal VARCHAR) AS $$
BEGIN
  IF p_titulo IS NULL THEN
    RETURN QUERY 
    SELECT pelicula.titulo, sucursal.direccion
    FROM pelicula
    INNER JOIN sucursalpelicula ON pelicula.IDPelicula = sucursalpelicula.IDPelicula
    INNER JOIN sucursal ON sucursalpelicula.IDSucursal = sucursal.IDSucursal;
  ELSE
    RETURN QUERY 
    SELECT pelicula.titulo, sucursal.direccion
    FROM pelicula
    INNER JOIN sucursalpelicula ON pelicula.IDPelicula = sucursalpelicula.IDPelicula
    INNER JOIN sucursal ON sucursalpelicula.IDSucursal = sucursal.IDSucursal
    WHERE pelicula.titulo = p_titulo;
  END IF;
END; $$ 
LANGUAGE 'plpgsql';

SELECT * FROM listar_sucursal_pelicula(NULL);


--2
CREATE OR REPLACE FUNCTION buscar_generos_pelicula(p_titulo VARCHAR)
RETURNS TABLE(nombre_pelicula VARCHAR, genero VARCHAR) AS $$
BEGIN
  IF p_titulo IS NULL THEN
    RETURN QUERY 
    SELECT pelicula.titulo, genero.nombreGenero
    FROM pelicula
    INNER JOIN generoPelicula ON pelicula.IDPelicula = generoPelicula.IDPelicula
    INNER JOIN genero ON generoPelicula.IDGenero = genero.IDGenero;
  ELSE
    RETURN QUERY 
    SELECT pelicula.titulo, genero.nombreGenero
    FROM pelicula
    INNER JOIN generoPelicula ON pelicula.IDPelicula = generoPelicula.IDPelicula
    INNER JOIN genero ON generoPelicula.IDGenero = genero.IDGenero
    WHERE pelicula.titulo = p_titulo;
  END IF;
END; $$ 
LANGUAGE 'plpgsql';

SELECT * FROM buscar_generos_pelicula(NULL); 
SELECT * FROM buscar_generos_pelicula('La Aventura Épica');

--3
--4