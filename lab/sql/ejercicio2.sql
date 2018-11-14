---------------------------------------------------------------------------------------------------------
-- Resolución del Ejercicio 2 - Tema 1
-- 
-- Máster en Data Science 
-- M1967 - Modelos de Datos y Sistemas de Información 2018-2019
-- Gerardo de Miguel González
-----------------------------------------------------------------------------------------------------------


-- Tabla para profesor para hacer referencia desde la tabla PlanEstudios
CREATE TABLE Profesor(
	idprofesor int PRIMARY KEY,
	dni char not null UNIQUE,
	nombre char not null,
	apellido1 char not null,
	apellido2 char null,
	tipoprofesor char not null,
	email char not null UNIQUE,
	fechaNacimiento date not null,
	fechaAlta date not null,
           CHECK (fechaAlta>fechaNacimiento),
           CHECK (email LIKE ('%@%')),
           CHECK (tipoprofesor IN ('Ayudante','AyudanteDoctor','Catedrático','Titular','ContratadoDoctor'))
);

CREATE TABLE Areas(
    idarea int primary key,
    area char not null unique
);

-- 1. Tabla para almacenar los planes de estudio
CREATE TABLE PlanEstudios(
    idplan int primary key,
    nombre char not null unique,
    creditos int not null,
    idarea int not null,
    fechaAlta date not null,
    fechaBaja date null,
    idprofesor int not null,
    check(creditos>=60 and creditos<=120),
    check(fechaAlta<fechaBaja),
    -- check (area in ('Ciencias','Humanidades', 'CienciasSociales', 'Ingenieria', 'CienciasSalud')),
   foreign key (idarea) references Areas (idarea),
   foreign key (idprofesor) references Profesor(idprofesor)
);

