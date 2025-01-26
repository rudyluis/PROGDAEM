CREATE OR REPLACE FUNCTION meses_dif(
    fecha1 DATE,
    fecha2 DATE)
RETURNS INTEGER
AS $$
DECLARE
    v_meses_dif INTEGER;
BEGIN
    v_meses_dif := EXTRACT(YEAR FROM age(fecha2, fecha1)) * 12 + EXTRACT(MONTH FROM age(fecha2, fecha1));
    RETURN v_meses_dif;
END;
$$ LANGUAGE plpgsql;



SELECT age('2023-12-31'::date, '2020-01-01'::date) AS diferencia;

SELECT meses_dif('2000-01-01'::DATE, '2023-12-31'::DATE); -- Devuelve el número de meses entre 2000-01-01 y 2023-12-31
