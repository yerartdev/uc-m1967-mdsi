--------------------------------------------------------------------------------
-- Alumno: Gerardo de Miguel González                                         --
--------------------------------------------------------------------------------
-- Práctica 2 (ejercicio de seguimiento)                                      --
-- Consultas sobre una base de datos                                          --
--------------------------------------------------------------------------------

-- 1. Mostrar los datos de los pedidos realizados entre octubre y noviembre de 2018 (0.5 ptos)

select * from pedidos p
  where (p.fechaHoraPedido >= '2018-10-01' and p.fechaHoraPedido <='2018-11-30')
  order by p.fechaHoraPedido;

-- 2. Devolver el id, nombre, apellido1, apellido2, fecha de alta y fecha de baja de todos los miembros del personal que no estén de baja, ordenados descendentemente por fecha de alta y ascendentemente por nombre (0.75 pto, 0.25 ptos adicionales si la consulta se realiza con el nombre y apellidos concatenados).

select p.idpersonal,
       p.nombre, p.apellido1, p.apellido2,
       p.fechaAlta, p. fechaBaja from personal p
where p.fechaBaja is null
order by p.fechaAlta desc;

select p.idpersonal, p.nombre,
       p.apellido1, p.apellido2,
       p.fechaAlta, p. fechaBaja from personal p
where p.fechaBaja is null
order by p.nombre;

--::GMG::No se prodece variación del resultado si se hace por las dos columnas ya que no hay ningún desempate que hacer por fecha de alta 

select p.idpersonal,
       p.nombre, p.apellido1, p.apellido2,
       p.fechaAlta, p. fechaBaja from personal p
where p.fechaBaja is null
order by p.fechaAlta desc, p.nombre;

--::GMG::Concatenando las partes del nombre

select p.idpersonal,
      (p.nombre || ' '  || p.apellido1 || ' ' ||p.apellido2) as nombre,
      p.fechaAlta, p. fechaBaja from personal p
where p.fechaBaja is null
order by p.fechaAlta desc, p.nombre;

-- 3. Retornar los datos de todos los clientes cuyo nombre de calle comience por G o J y que además tengan observaciones (1 pto).

--::GMG::Borrador
--       http://www.sqlitetutorial.net/sqlite-like/

select (c.nombre || ' '  || c.apellido1 || ' ' ||c.apellido2) as nombre, c.calle from clientes c 
where (c.calle like 'Calle G%' or c.calle like 'Calle J%');

-- 4. Devolver el id e importe de las pizzas junto con el id y descripción de todos sus ingredientes, siempre que el importe de estas pizzas sea mayor de 3 (1 pto).

-- 5. Mostrar los datos de todas las pizzas que no hayan sido nunca pedidas, ordenados por id ascendentemente (1 pto).

-- 6. Devolver los datos de las bases, junto con los datos de las pizzas en las que están presentes, incluyendo los datos de las bases que no están en ninguna pizza (0.5 ptos)

-- 7. Retornar los datos de los pedidos realizados por el cliente con id 1, junto con los datos de sus líneas y de las pizzas pedidas, siempre que el precio unitario en la línea sea menor que el importe base de la pizza. (1.5 ptos)

-- 8. Mostrar el id y nif de todos los usuarios, junto con el número total de pedidos realizados (0.75 pto, 0.25 ptos adicionales si sólo se devuelven los datos de los que hayan realizado más de un pedido).

-- 9. Sumar 0.5 al importe base de todas las pizzas que contengan el ingrediente con id 1 (0.75 pto).

-- 10. Eliminar las líneas de los pedidos anteriores a 2018 (0.75 pto).

-- 11. BONUS para el 10: Realizar una consulta que devuelva el número de pizzas totales pedidas por cada cliente. En la consulta deberán aparecer el id y nif de los clientes, además de su nombre y apellidos concatenados (1 pto).
