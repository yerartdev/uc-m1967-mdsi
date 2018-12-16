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

--::GMG::No se produce variación del resultado si se hace por las dos columnas ya que no hay ningún desempate que hacer por fecha de alta 

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

--::GMG:: http://www.sqlitetutorial.net/sqlite-like/

select (c.nombre || ' '  || c.apellido1 || ' ' ||c.apellido2) as nombre, 
        c.calle, c.observaciones from clientes c 
where (c.calle like 'Calle G%' or c.calle like 'Calle J%') and
      (c.observaciones is not null);

-- 4. Devolver el id e importe de las pizzas junto con el id y descripción de todos sus ingredientes, siempre que el importe de estas pizzas sea mayor de 3 (1 pto).

-- ::GMG:: Borradores

-- Para seleccionar los ingredientes y su descripción

select distinct ip.idingrediente, i.descripcion 
  from ingredientedepizza ip join ingredientes i 
  on ip.idingrediente = i.idingrediente;

-- Para seleccionar importe e ingredientes (id)

select i.idpizza, i.idingrediente, p.importeBase 
  from ingredientedepizza i join pizzas p 
  on i.idpizza = p.idpizza 
where (p.importeBase > 3) 
order by i.idpizza;

-- ::GMG:: Consulta final

select p.idpizza as pizza, 
       i.idingrediente, i.descripcion as ingrediente, 
       p.importeBase as importe from Pizzas p  
join  (
       IngredienteDepizza ip join Ingredientes i 
       on ip.idingrediente = i.idingrediente
      ) on p.idpizza = ip.idpizza 
where p.importeBase > 3;

-- 5. Mostrar los datos de todas las pizzas que no hayan sido nunca pedidas, ordenados por id ascendentemente (1 pto).

--::GMG:: Borradores

-- Intervienen Pizzas, Bases, IngredienteDePizzas, Ingredientes

-- Datos de todas la Pizzas con sus bases e ingredientes

select p.idpizza as pizza, 
       b.descripcion as base, 
       i.descripcion as ingrediente, 
       p.importeBase as importe 
from (Pizzas p join Bases b on p.idbase = b.idbase) join 
     (IngredienteDepizza ip join Ingredientes i 
      on ip.idingrediente = i.idingrediente) 
on p.idpizza = ip.idpizza;

-- Pizzas que se han pedido de LineasPedidos

select distinct lp.idpizza from lineaspedidos lp;

--::GMG:: Consulta final

select p.idpizza as pizza,
       b.descripcion as base,
       i.descripcion as ingrediente,
       p.importeBase as importe
from (Pizzas p join Bases b on p.idbase = b.idbase) join
     (IngredienteDepizza ip join Ingredientes i
      on ip.idingrediente = i.idingrediente)
on p.idpizza = ip.idpizza
where p.idpizza not in (
    select distinct lp.idpizza from lineaspedidos lp)
order by p.idpizza asc;

-- 6. Devolver los datos de las bases, junto con los datos de las pizzas en las que están presentes, incluyendo los datos de las bases que no están en ninguna pizza (0.5 ptos)

select b.idbase, b.descripcion as base, 
       p.idpizza as pizza, p.importeBase as importe 
from Bases b left join Pizzas p 
on b.idbase = p.idbase;

-- 7. Retornar los datos de los pedidos realizados por el cliente con id 1, junto con los datos de sus líneas y de las pizzas pedidas, siempre que el precio unitario en la línea sea menor que el importe base de la pizza. (1.5 ptos)

--::GMG:: Borradores

-- Datos de los pedidos realizados por el cliente 1 (LineasPedidos, Pedidos)

select lp.idpedido, lp.idpizza, lp.cantidad, lp.precioUnidad, lp.descuento
from LineasPedidos lp join Pedidos p on lp.idpedido = p.idpedido
where p.idcliente = 1;

-- Bases, Pizzas e importe base

select b.idbase, b.descripcion as base, 
       p.idpizza as pizza, p.importeBase as importe 
from Bases b join Pizzas p on b.idbase = p.idbase;

--::GMG::Consulta final

select lp.idpedido as pedido, lp.cantidad, lp.precioUnidad, lp.descuento, 
       p.idpizza as pizza, p.idbase as base, p.importeBase as importe 
from (LineasPedidos lp join Pedidos p on lp.idpedido = p.idpedido) 
     join Pizzas p on lp.idpizza = p.idpizza 
where p.idcliente = 1 and lp.precioUnidad < p.importeBase;

-- 8. Mostrar el id y nif de todos los usuarios, junto con el número total de pedidos realizados (0.75 pto, 0.25 ptos adicionales si sólo se devuelven los datos de los que hayan realizado más de un pedido).

--::GMG:: Borradores

-- id y nif de todos los clientes

select c.idcliente, c.nif from clientes c;

-- con sus líneas de pedidos

select c.idcliente, c.nif, 
       p.idpedido, lp.idlinea 
from (clientes c join pedidos p on c.idcliente = p.idcliente) 
     join lineaspedidos lp 
     on lp.idpedido = p.idpedido;

-- con el número de (líneas de) pedidos por cliente

select c.idcliente, c.nif, count(lp.idlinea) as pedidos 
from (clientes c join pedidos p on c.idcliente = p.idcliente) 
     join lineaspedidos lp 
     on lp.idpedido = p.idpedido 
group by c.idcliente, c.nif;

-- ::GMG::Consulta final

select c.idcliente, c.nif, count(lp.idlinea) as pedidos 
from (clientes c join pedidos p on c.idcliente = p.idcliente) 
     join lineaspedidos lp on lp.idpedido = p.idpedido 
group by c.idcliente, c.nif 
having pedidos > 1;

-- 9. Sumar 0.5 al importe base de todas las pizzas que contengan el ingrediente con id 1 (0.75 pto).

-- 10. Eliminar las líneas de los pedidos anteriores a 2018 (0.75 pto).

-- 11. BONUS para el 10: Realizar una consulta que devuelva el número de pizzas totales pedidas por cada cliente. En la consulta deberán aparecer el id y nif de los clientes, además de su nombre y apellidos concatenados (1 pto).
