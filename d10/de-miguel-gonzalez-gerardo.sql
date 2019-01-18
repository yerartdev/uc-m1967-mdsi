
---------------------------------------------------------------------------------------------------------
-- Entregable Práctica final SQLite
-- 
-- Master en Data Science 
-- M1967 - Modelos de Datos y Sistemas de Informacion 2018-2019
-- Gerardo de Miguel González
-----------------------------------------------------------------------------------------------------------


-- 1. Crea una nueva tabla para almacenar las temporadas de las series. La primary key ha de ser el par de campos “idSerie, numTemporada”. (2 ptos)

-- ::GMG::Sigo la nomencaltura de la bbdd del nombre de las tablas
--        y snakeCase del nombre de las columnas
-- ::nota::el tipo Booleano lo pongo como int (0,1)
-- https://www.sqlite.org/datatype3.html

create table TEMPORADAS
(
	idSerie int,
	numTemporada int,
	fechaEstreno date not null,
	fechaRegistro date not null,
	disponible int not null,
	foreign key (idSerie) references SERIES(idSerie)
	primary key (idSerie, numTemporada)
	CHECK (fechaRegistro > fechaEstreno)
	CHECK (disponible IN (0,1))
);

-- 2.	Añadir una nueva columna a la tabla "generos" para almacenar un campo denominado "descripcion" (0.25 ptos).

-- ::GMG:: Uso la manera canónica con alter table
-- https://www.sqlite.org/lang_altertable.html

alter table GENEROS add descripcion char(256);

-- 3.	Crea un índice sobre el par de campos “titulo” y “anyoFin” de las series (0.25 ptos)

-- ::GMG:: Uso la forma canónica con create index
-- https://www.sqlite.org/lang_createindex.html
-- ::nota::la columna anyoFin puede contener NULL según el schema de SERIES
--         y contiene un gran número de ellos (7 de 12) lo cual NO ES BUENO
--         para un índice ... según:
-- https://www.tutorialspoint.com/sqlite/sqlite_indexes.htm

create index titulo_anyoFin_index on SERIES (titulo, anyoFin);

-- 4.	Mostrar el “idserie”, “titulo”, “titulo original” y “sinopsis” de todas las series, ordenadas por título descendentemente (0.5 ptos)

select s.idSerie, s.titulo, s.tituloOriginal, s.sinopsis 
from SERIES s 
order by s.titulo desc;

-- 5.	Retornar los datos de los usuarios franceses o noruegos (0.5 ptos)

select * 
from USUARIOS
where (pais='Francia' or pais='Noruega');

-- 6.	Mostrar los datos de los actores junto con los datos de las series en las que actúan (0.75 ptos)

-- ::GMG:: Aquí intervienen tres tablas REPARTO, SERIES y ACTORES

select a.nombreArtistico as Actor, r.personaje as Personaje, 
       s.titulo as Serie 
from REPARTO r 
join SERIES s on r.idSerie = s.idSerie 
join ACTORES a on r.idActor = a.idActor;

-- 7.	Mostrar los datos de los usuarios que no hayan realizado nunca ninguna valoración (0.75 ptos)

-- ::GMG::Lo hago con una subconsulta que devuelve los usuarios que HAN hecho
--        valoraciones

select (nombreUsuario || ' ' || apellido1) as Usuario 
from usuarios
where idUsuario not in 
(select idUsuario from valoraciones);

-- 8.	Mostrar los datos de los usuarios junto con los datos de su profesión, incluyendo las profesiones que no estén asignadas a ningún usuario (0.75 ptos)

-- ::GMG::Si quiero que se muestren las profesiones no asignadas tengo que
--        heacer un left join
-- http://www.firebirdfaq.org/faq93/

select p.profesion as profesion, 
       (u.nombreUsuario || ' ' || u.apellido1) as usuario
from PROFESIONES p
left join USUARIOS u;

-- 9.	Retornar los datos de las series que estén en idioma español, y cuyo título comience por E o G (1 pto)

select s.titulo, s.anyoEstreno as estreno, g.genero, i.idioma 
from SERIES s
join GENEROS g on s.idGenero = g.idGenero
join IDIOMAS i on s.idIdioma = i.idIdioma
where (s.titulo like 'E%' or s.titulo like 'G%') and 
      i.idioma='Español';

-- 10.	Retornar los “idserie”, “titulo” y “sinopsis” de todas las series junto con la puntuación media, mínima y máxima de sus valoraciones (1 pto)

select s.idSerie as Id, s.titulo, s.sinopsis,
       avg (v.puntuacion) as pMed, min(v.puntuacion) as pMin, 
       max(v.puntuacion) as pMax
from SERIES s
join VALORACIONES v on s.idSerie = v.idSerie
group by s.idSerie;

-- 11.	Actualiza al valor 'Sin sinopsis' la sinopsis de todas las series cuya sinopsis sea nula y cuyo idioma sea el inglés (1 pto)

-- ::GMG::Uso una selección para obtener el id del idioma Inglés

update SERIES set sinopsis='sin sinopsis' 
where sinopsis is null and 
      idIdioma in 
      (select i.idIdioma from IDIOMAS i where i.idioma like 'Inglés'); 

-- ::nota::Comprobación

select s.idSerie as Id, s.titulo, s.sinopsis, i.idioma
from SERIES s
join IDIOMAS i on s.idIdioma =  i.idIdioma
group by s.idSerie;

-- 12.	Utilizando funciones ventana, muestra los datos de las valoraciones junto al nombre y apellidos (concatenados) de los usuarios que las realizan, y en la misma fila, el valor medio de las puntuaciones realizadas por el usuario (1.25 ptos)

select v.idValoracion as id, (u.nombre || " " || u.apellido1) as usuario,
       s.titulo as serie, v.puntuacion as valoracion,
       avg(v.puntuacion) over (partition by u.idUsuario) as usuaio_media
from VALORACIONES v 
join USUARIOS u on v.idUsuario = u.idUsuario
join SERIES s on v.idSerie = s.idSerie;


