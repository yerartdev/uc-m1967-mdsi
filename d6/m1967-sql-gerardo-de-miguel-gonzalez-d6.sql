---------------------------------------------------------------------------------------------------------
-- Entregable Práctica 1: Creación/modificación de tablas e inserción de datos
-- 
-- Máster en Data Science 
-- M1967 - Modelos de Datos y Sistemas de Información 2018-2019
-- Gerardo de Miguel González
---------------------------------------------------------------------------------------------------------

-- 1. Crear la tabla Director, siguiendo la descripción dada (3 puntos)

create table Director(
	iddirector integer not null unique, -- ::GMG::http://www.sqlitetutorial.net/sqlite-primary-key/
	dni char not null unique,           -- ::GMG::http://www.sqlitetutorial.net/sqlite-unique-constraint/
	nombre char not null,
	apellido1 char not null,
	apellido2 char null,
	fechaNacimiento date not null,
	fechaRegistro date not null,
	fechaDeceso date null,
	enActivo boolean not null,          -- ::GMG:: https://stackoverflow.com/questions/843780/store-boolean-value-in-sqlite
           CHECK (fechaRegistro > fechaNacimiento),
           CHECK (fechaDeceso > fechaNacimiento),
           CHECK (enActivo IN (0,1)),
	primary key(iddirector)
);

-- 2. Crear la tabla Película, siguiendo la descripción dada (3 puntos)

create table Pelicula (
	idpelicula integer not null unique,
	titulo char not null unique,
	fechaEstreno date not null,
	duracionMin real not null,
	genero char not null,
	iddirector integer not null,
           CHECK (idpelicula > 0),
           CHECK (duracionMin > 0),
           CHECK (genero IN ('terror','scifi','aventura')),
	foreign key (iddirector) references Director(iddirector),
	primary key (idpelicula)
);

-- 3. Insertar al menos 3 filas válidas en la tabla Director, y otras 3 filas válidas en la tabla Película (1 punto)

-- ::GMG:: Tabla Director
insert into Director 
	(iddirector, dni, nombre, apellido1, apellido2, fechaNacimiento, fechaRegistro, fechaDeceso, enActivo) 
	values 
	(1, '92371662X', 'John', 'Ford', null,'1894-02-01','1928-01-01','1973-08-31',0);
insert into Director 
	(iddirector, dni, nombre, apellido1, apellido2, fechaNacimiento, fechaRegistro, fechaDeceso, enActivo) 
	values 
	(2, '52167251B', 'José Luís', 'García', 'Muñoz','1944-01-20','1977-01-01',null,1);
insert into Director 
	(iddirector, dni, nombre, apellido1, apellido2, fechaNacimiento, fechaRegistro, fechaDeceso, enActivo) 
	values 
	(3, '52991633Z', 'Steven', 'Allen', 'Spielberg','1946-31-18','1975-01-01',null,1);

-- ::GMG:: Tabla Película

insert into Pelicula 
	(idpelicula, titulo, fechaEstreno, duracionMin, genero, iddirector) 
	values
	(1,'Jaws','1975-06-20',124,'terror',3);

insert into Pelicula 
	(idpelicula, titulo, fechaEstreno, duracionMin, genero, iddirector) 
	values
	(2,'A.I. Artificial Intelligence,','2001-06-29',146,'scifi',3);

insert into Pelicula 
	(idpelicula, titulo, fechaEstreno, duracionMin, genero, iddirector) 
	values
	(3,'Volver a Empezar','1982-03-01',87,'aventura',2);

-- 4. Añadir a la tabla Película una nueva columna que almacene la recaudación, que no pueda tomar un valor negativo, que no pueda ser nula, y que por defecto su valor sea 0 (1 punto)

alter table Pelicula 
	add recaudacion real NOT NULL CHECK (recaudacion >= 0) DEFAULT 0;

-- 5. ¿Se te ocurre un método mejor para almacenar los géneros de las películas Por ejemplo, ¿qué pasaría si quisiésemos ampliar los géneros posibles y añadir uno nuevo? Impleméntalo (1 punto)

-- ::GMG:: La solución es crear una nueva tabla con los géneros

create table Genero (
	idgenero integer not null primary key,
	txtgenero char not null);

insert into Genero (idgenero, txtgenero) 
	values (1,'terror'), (2,'scifi'), (3,'aventura'), (4,'drama'),(5,'comedia');

-- ::GMG:: También tenemos que modificar el modelo de datos de la tabla Película
--         Opto por rehacer por completo la tabla y las inserciones

drop table Pelicula;

create table Pelicula (
	idpelicula integer not null unique,
	titulo char not null unique,
	fechaEstreno date not null,
	duracionMin real not null,
	idgenero integer not null,
	iddirector integer not null, 
	recaudacion real NOT NULL default 0,
           CHECK (recaudacion >= 0),
           CHECK (idpelicula > 0),
           CHECK (duracionMin > 0),
foreign key (iddirector) references Director(iddirector),
foreign key (idgenero) references Genero(idgenero),
primary key (idpelicula)
);

insert into Pelicula 
	(idpelicula, titulo, fechaEstreno, duracionMin, idgenero, iddirector,recaudacion) 
	values
	(1,'Jaws','1975-06-20',124,1,3,470.7);

insert into Pelicula 
	(idpelicula, titulo, fechaEstreno, duracionMin, idgenero, iddirector,recaudacion) 
	values
	(2,'A.I. Artificial Intelligence,','2001-06-29',146,2,3,235.9);

insert into Pelicula 
	(idpelicula, titulo, fechaEstreno, duracionMin, idgenero, iddirector,recaudacion) 
	values
	(3,'Volver a Empezar','1982-03-01',87,4,2,1.292);


-- 6. Imaginemos que, además, queremos almacenar los datos de los actores que participan en las películas, sabiendo que un actor puede participar en varias películas, y una película tiene varios actores. Implementa una solución a este problema.

-- ::GMG:: Primero creamos una tabla Actor

create table Actor (
	idactor integer not null unique, 
	dni char not null unique,           
	nombre char not null,
	apellido1 char not null,
	apellido2 char null,
	fechaNacimiento date not null,
	fechaRegistro date not null,
	fechaDeceso date null,
	enActivo boolean not null,          
           CHECK (fechaRegistro > fechaNacimiento),
           CHECK (fechaDeceso > fechaNacimiento),
           CHECK (enActivo IN (0,1)),
	primary key(idactor)
);

-- ::GMG:: Metemos unos actores de las películas que hemos elegido

insert into Actor
	(idactor, dni, nombre, apellido1, apellido2, fechaNacimiento,fechaRegistro, fechaDeceso, enActivo) 
	values
	(1,'63007838M','Haley',' Joel','Osment','1988-04-10','1999-01-01',null,1),
	(2,'91614160P','Jude','Law',null,'1972-12-29','1999-02-01',null,1),
	(3,'97589106Z','Richard','Dreyfuss',null,'1947-10-29','1973-01-01',null,1),
	(4,'34228258A','Antonio','Ferrandis','Monrabal','1921-02-28','1975-01-01','2000-10-16',0),    
	(5,'06349393J','Encarna','Paso',null,'1931-03-25','1981-01-01',null,1),
	(6,'08479503R','Roy','Scheider',null,'1932-11-10','1975-03-01','2008-02-10',0);
    
-- ::GMG:: El hecho de que una película tiene varios actores y los actores pueden participar en varias películas
--         lo podemos implementar con una tabla Reparto en el que se ponga Pelicula, y Actor con referencias a 
--         ambas tablas. 

create table Reparto (
	idpelicula int NOT NULL,
	idactor int NOT NULL,
	FOREIGN KEY (idpelicula) REFERENCES Pelicula(idpelicula),
	FOREIGN KEY (idactor) REFERENCES Actor(idactor),
	PRIMARY KEY (idpelicula,idactor)
);

-- ::GMG:: Insertamos el reparto de las películas que hemos elegido

insert into Reparto (idpelicula,idactor) 
	values (2,1),(2,2),(1,3),(3,4),(3,5),(1,6);
