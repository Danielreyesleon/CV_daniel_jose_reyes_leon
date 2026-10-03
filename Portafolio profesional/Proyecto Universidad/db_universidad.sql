create database db_universidad;
go

use db_universidad;
go

create table carreras (
    carrera_id int primary key,
    nombre varchar(50) not null,
    esta_activa bit not null,
    facultad varchar(50) not null,
    duracion_anios int not null
);
go


create table estudiantes (
    estudiante_id int primary key,
    nombre_completo varchar(150) not null,
    fecha_nacimiento date not null,
    carrera_id int not null,
    email varchar(100) not null,
    telefono varchar(20) not null,
    esta_activo bit not null
);
go


create table cursos (
    curso_id int primary key,
    nombre varchar(50) not null,
    costo decimal(8,2) not null,
    creditos int not null,
    esta_activo bit not null
);
go


create table matriculas (
    matricula_id int primary key,
    fecha date not null,
    estudiante_id int not null,
    estado varchar(20) not null,
    monto_total decimal(8,2) not null
);
go


create table detalle_matricula (
    detalle_id int primary key,
    matricula_id int not null,
    curso_id int not null,
    nota decimal(4,2) not null
);
go 
insert into carreras (carrera_id, nombre, facultad, duracion_anios, esta_activa) values
(46, 'Ingenieria en Telecomunicaciones', 'Ingenieria', 5, 1),
(47, 'Administracion Bancaria', 'Ciencias Economicas', 4, 1),
(48, 'Diseno Web', 'Diseno', 4, 1),
(49, 'Derecho Comercial', 'Derecho', 5, 1),
(50, 'Psicologia Clinica', 'Ciencias Sociales', 5, 1),
(51, 'Contabilidad Financiera', 'Ciencias Economicas', 4, 1),
(52, 'Ingenieria Energetica', 'Ingenieria', 5, 1),
(53, 'Marketing Politico', 'Ciencias Economicas', 4, 1),
(54, 'Arquitectura Digital', 'Arquitectura', 5, 0),
(55, 'Medicina Forense', 'Medicina', 6, 1),
(56, 'Ingenieria Hidraulica', 'Ingenieria', 5, 1),
(57, 'Gastronomia Creativa', 'Gastronomia', 3, 1),
(58, 'Periodismo Investigativo', 'Comunicacion', 4, 1),
(59, 'Ingenieria Textil', 'Ingenieria', 5, 1),
(60, 'Traduccion Empresarial', 'Idiomas', 4, 1),
(61, 'Ingenieria Naval', 'Ingenieria', 5, 1),
(62, 'Administracion Logistica', 'Ciencias Economicas', 4, 1),
(63, 'Diseno Publicitario', 'Diseno', 4, 1),
(64, 'Derecho Laboral', 'Derecho', 5, 1),
(65, 'Psicologia Social', 'Ciencias Sociales', 5, 1),
(66, 'Contabilidad de Costos', 'Ciencias Economicas', 4, 1),
(67, 'Ingenieria Acustica', 'Ingenieria', 5, 1),
(68, 'Marketing Internacional', 'Ciencias Economicas', 4, 1),
(69, 'Arquitectura Modular', 'Arquitectura', 5, 0),
(70, 'Medicina Deportiva', 'Medicina', 6, 1),
(71, 'Ingenieria de Software', 'Ingenieria', 5, 1),
(72, 'Gastronomia Molecular', 'Gastronomia', 3, 1),
(73, 'Periodismo Multimedia', 'Comunicacion', 4, 1),
(74, 'Ingenieria Optica', 'Ingenieria', 5, 1),
(75, 'Traduccion Legal', 'Idiomas', 4, 1);
 
insert into estudiantes (estudiante_id, nombre_completo, fecha_nacimiento, email, telefono, carrera_id, esta_activo) values
(155, 'Mario Alberto Castillo', '2001-01-11', 'mario.castillo@estudiantes.uni.edu', '8214-1409', 46, 1),
(156, 'Laura Cristina Jimenez', '2002-02-22', 'laura.jimenez@estudiantes.uni.edu', '8381-5012', 47, 1),
(157, 'Jose Manuel Rojas', '1999-03-15', 'jose.rojas@estudiantes.uni.edu', '6242-2679', 48, 1),
(158, 'Andrea Sofia Solis', '2003-04-19', 'andrea.solis@estudiantes.uni.edu', '8858-9935', 49, 1),
(159, 'Carlos Eduardo Brenes', '2000-05-25', 'carlos.brenes@estudiantes.uni.edu', '6704-7912', 50, 1),
(160, 'Valeria Fernanda Soto', '2001-06-30', 'valeria.soto@estudiantes.uni.edu', '6130-2535', 51, 1),
(161, 'Miguel Angel Vargas', '2002-07-14', 'miguel.vargas@estudiantes.uni.edu', '6338-9279', 52, 1),
(162, 'Rosa Elena Mora', '2003-08-21', 'rosa.mora@estudiantes.uni.edu', '8127-4257', 53, 1),
(163, 'Daniel Tomas Araya', '1998-09-10', 'daniel.araya@estudiantes.uni.edu', '8765-9928', 54, 0),
(164, 'Lucia Maria Porras', '2000-10-05', 'lucia.porras@estudiantes.uni.edu', '7325-8359', 55, 1),
(165, 'Samuel Andres Chavarria', '2001-11-12', 'samuel.chavarria@estudiantes.uni.edu', '8384-1106', 56, 1),
(166, 'Nicole Alexandra Ruiz', '2002-12-01', 'nicole.ruiz@estudiantes.uni.edu', '6814-7924', 57, 1),
(167, 'Diego Tomas Villalta', '1999-01-18', 'diego.villalta@estudiantes.uni.edu', '7384-3547', 58, 1),
(168, 'Fiorella Jazmin Campos', '2003-02-27', 'fiorella.campos@estudiantes.uni.edu', '6881-6514', 59, 1),
(169, 'Luis Miguel Arguedas', '1998-03-14', 'luis.arguedas@estudiantes.uni.edu', '6194-7224', 60, 1),
(170, 'Carolina Maria Soto', '2001-04-22', 'carolina.soto@estudiantes.uni.edu', '6467-6635', 61, 1),
(171, 'Jorge Andres Rojas', '2002-05-09', 'jorge.rojas@estudiantes.uni.edu', '8370-1711', 62, 1),
(172, 'Daniela Sofia Campos', '2003-06-17', 'daniela.campos@estudiantes.uni.edu', '8570-9785', 63, 1),
(173, 'Miguel Angel Solano', '2000-07-28', 'miguel.solano@estudiantes.uni.edu', '6487-2291', 64, 1),
(174, 'Rosa Elena Pineda', '2001-08-03', 'rosa.pineda@estudiantes.uni.edu', '8400-6925', 65, 1),
(175, 'Mario Alejandro Ruiz', '2002-09-27', 'mario.ruiz@estudiantes.uni.edu', '8296-2139', 66, 1),
(176, 'Andrea Lucia Mora', '2003-10-16', 'andrea.mora@estudiantes.uni.edu', '6777-4733', 67, 1),
(177, 'Jose Manuel Araya', '1998-11-30', 'jose.araya@estudiantes.uni.edu', '7181-4814', 68, 1),
(178, 'Lucia Fernanda Porras', '2000-12-25', 'lucia.porras@estudiantes.uni.edu', '6489-5554', 69, 0),
(179, 'Carlos Eduardo Solis', '2001-01-18', 'carlos.solis@estudiantes.uni.edu', '7750-6977', 70, 1),
(180, 'Valeria Cristina Rojas', '2002-02-07', 'valeria.rojas@estudiantes.uni.edu', '6479-6820', 71, 1),
(181, 'Diego Tomas Brenes', '1999-03-12', 'diego.brenes@estudiantes.uni.edu', '6786-5374', 72, 1),
(182, 'Nicole Alexandra Vargas', '2003-04-01', 'nicole.vargas@estudiantes.uni.edu', '8799-2169', 73, 1),
(183, 'Samuel Andres Chacon', '2000-05-02', 'samuel.chacon@estudiantes.uni.edu', '8750-3803', 74, 1),
(184, 'Luis Alberto Jimenez', '2001-06-11', 'luis.jimenez@estudiantes.uni.edu', '8846-5010', 75, 1);
 
insert into cursos (curso_id, nombre, costo, creditos, esta_activo) values
(252, 'Telecomunicaciones I', 1600.00, 3, 1),
(253, 'Gestion Bancaria', 1500.00, 4, 1),
(254, 'Diseno Web Moderno', 1400.00, 4, 1),
(255, 'Derecho Mercantil', 1700.00, 4, 1),
(256, 'Psicologia de la Personalidad', 1300.00, 5, 1),
(257, 'Contabilidad Avanzada', 1550.00, 5, 1),
(258, 'Energia Renovable', 1650.00, 5, 1),
(259, 'Marketing Electoral', 1450.00, 3, 1),
(260, 'Modelado Arquitectonico', 1800.00, 5, 1),
(261, 'Medicina Legal', 1600.00, 4, 1),
(262, 'Hidraulica Aplicada', 1750.00, 3, 1),
(263, 'Cocina Creativa', 1900.00, 3, 1),
(264, 'Investigacion Periodistica', 1200.00, 3, 1),
(265, 'Textiles Industriales', 2000.00, 4, 1),
(266, 'Traduccion Profesional', 1500.00, 4, 1),
(267, 'Navegacion Maritima', 1600.00, 4, 1),
(268, 'Logistica Empresarial', 1500.00, 3, 1),
(269, 'Diseno Publicitario Digital', 1400.00, 3, 1),
(270, 'Derecho Laboral Aplicado', 1700.00, 5, 1),
(271, 'Psicologia Social Avanzada', 1300.00, 5, 1),
(272, 'Costos Industriales', 1550.00, 4, 1),
(273, 'Acustica Aplicada', 1650.00, 3, 1),
(274, 'Marketing Global', 1450.00, 5, 1),
(275, 'Arquitectura Modular Avanzada', 1800.00, 4, 1),
(276, 'Medicina Deportiva Aplicada', 1600.00, 4, 1),
(277, 'Ingenieria de Software I', 1750.00, 5, 1),
(278, 'Gastronomia Molecular Avanzada', 1900.00, 4, 1),
(279, 'Periodismo Multimedia I', 1200.00, 3, 1),
(280, 'Optica Aplicada', 2000.00, 4, 1),
(281, 'Traduccion Legal Profesional', 1500.00, 3, 1);
 
insert into matriculas (matricula_id, fecha, estudiante_id, estado, monto_total) values
(1052, '2026-02-18', 155, 'Activa', 3250.00),
(1053, '2026-02-18', 156, 'Activa', 1500.00),
(1054, '2026-02-19', 157, 'Pendiente de pago', 1400.00),
(1055, '2026-02-19', 158, 'Pendiente de pago', 1700.00),
(1056, '2026-02-20', 159, 'Activa', 1300.00),
(1057, '2026-02-20', 160, 'Activa', 1550.00),
(1058, '2026-02-21', 161, 'Activa', 1650.00),
(1059, '2026-02-21', 162, 'Pendiente de pago', 1450.00),
(1060, '2026-02-22', 163, 'Cancelada', 1800.00),
(1061, '2026-02-22', 164, 'Activa', 1600.00),
(1062, '2026-02-23', 165, 'Activa', 1750.00),
(1063, '2026-02-23', 166, 'Activa', 1900.00),
(1064, '2026-02-24', 167, 'Activa', 1200.00),
(1065, '2026-02-24', 168, 'Activa', 2000.00),
(1066, '2026-02-25', 169, 'Pendiente de pago', 1500.00),
(1067, '2026-02-25', 170, 'Activa', 1600.00),
(1068, '2026-02-26', 171, 'Pendiente de pago', 1500.00),
(1069, '2026-02-26', 172, 'Pendiente de pago', 1400.00),
(1070, '2026-02-27', 173, 'Pendiente de pago', 1700.00),
(1071, '2026-02-27', 174, 'Activa', 1300.00),
(1072, '2026-02-28', 175, 'Activa', 1550.00),
(1073, '2026-02-28', 176, 'Activa', 1650.00),
(1074, '2026-03-01', 177, 'Activa', 1450.00),
(1075, '2026-03-01', 178, 'Cancelada', 1800.00),
(1076, '2026-03-02', 179, 'Activa', 1600.00),
(1077, '2026-03-02', 180, 'Activa', 1750.00),
(1078, '2026-03-03', 181, 'Activa', 1900.00),
(1079, '2026-03-03', 182, 'Pendiente de pago', 1200.00),
(1080, '2026-03-04', 183, 'Activa', 2000.00),
(1081, '2026-03-04', 184, 'Pendiente de pago', 1500.00);
 
insert into detalle_matricula (detalle_id, matricula_id, curso_id, nota) values
(63, 1052, 252, 70.10),
(64, 1052, 258, 91.66),
(65, 1053, 253, 91.59),
(66, 1054, 254, 99.16),
(67, 1055, 255, 92.86),
(68, 1056, 256, 85.23),
(69, 1057, 257, 73.19),
(70, 1058, 258, 88.76),
(71, 1059, 259, 95.25),
(72, 1060, 260, 85.23),
(73, 1061, 261, 75.97),
(74, 1062, 262, 81.22),
(75, 1063, 263, 74.85),
(76, 1064, 264, 98.60),
(77, 1065, 265, 97.67),
(78, 1066, 266, 97.55),
(79, 1067, 267, 87.97),
(80, 1068, 268, 84.66),
(81, 1069, 269, 73.36),
(82, 1070, 270, 80.89),
(83, 1071, 271, 99.56),
(84, 1072, 272, 94.20),
(85, 1073, 273, 77.18),
(86, 1074, 274, 77.23),
(87, 1075, 275, 87.02),
(88, 1076, 276, 72.36),
(89, 1077, 277, 91.96),
(90, 1078, 278, 94.48),
(91, 1079, 279, 99.34),
(92, 1080, 280, 85.98),
(93, 1081, 281, 73.77);



-- select todos los estudiantes
select *
from estudiantes;
go

-- carreras que se encuentran ativas

select *
from carreras
where esta_activa = 1;
go

--order by consulta
select nombre_completo
from estudiantes
order by nombre_completo;
go


-- top siendo aplicado en consulta

select top 5 *
from cursos;
go

-- ejecusion de consulta like

select * 
from estudiantes
where nombre_completo like 'C%';
go

-- consulta con between integrado

select * 
from cursos
where costo between 1400 and 1700;
go

-- consulat con in integrafo en ella

select *
from carreras
where carrera_id in (1,5,22);
go

-- consulta de usando not
select * 
from carreras
where not esta_activa = 1;
go

-- consulta aplicccando is null

select *
from estudiantes
where carrera_id is null;
go

-- consulta con is not null
select *
from estudiantes
where carrera_id is not null
go

-- uso de consulta con and

select *
from cursos
where costo > 1500
and costo <1800;
go

--consulta or

select *
from carreras
where nombre = 'Ciberseguridad'
or nombre = 'Psicologia';
go

--consulta gropu by 

select  carrera_id, count(*) as cantidad_estudiantes
from estudiantes
group by carrera_id;
go

-- ejcutando having
select carrera_id , count(*) as cantidad
from estudiantes
group by carrera_id
having count(*) > 1;
go

-- constulta count
select count(*) as total_estudiantes
from estudiantes;
go

-- consulta con sum / suma
select sum(costo) as costo_total
from cursos;
go

-- consulta utilizando AVG / promedio

select avg(costo) as promedio_costo
from cursos;
go

-- consulta con min /minimo
select min(costo) ascosto_minimo
from cursos;
go

-- consulat de max / maximo

select max(costo) as costo_maximo
from cursos;
go

-- consulta inner join

select
e.nombre_completo,
c.nombre as carrera
from estudiantes e
inner join carreras c
on e.carrera_id =c.carrera_id;
go

-- consulta left join
select
e.nombre_completo,
m.matricula_id
from estudiantes e
left join matriculas m
on e.estudiante_id = m.estudiante_id;
go

-- consulat right join

select
e.nombre_completo,
m.matricula_id
from estudiantes e
right join matriculas m
on e.estudiante_id = m.matricula_id;
go

-- subconsultas
select *
from cursos
where costo >
(
select AVG(costo)
from cursos
);
go

-- views 
create view vista_estudiantes_carreras
as
select
e.nombre_completo,
c.nombre as carrera
from estudiantes e
inner join carreras c
on e.carrera_id = c.carrera_id;
go

select *
from vista_estudiantes_carreras;
go

-- view 2

create view vista_cursos_caros
as
select
nombre,
costo
from cursos
where costo > 1700;
go

select * 
from vista_cursos_caros;
go

-- view 3

create  view vista_matriculas
as
select
m.matricula_id,
m.fecha,
e.nombre_completo
from matriculas m
inner join estudiantes e
on m.estudiante_id = e.estudiante_id;
go

select *
from vista_matriculas;
go

-- view 4
create view vista_carreras_activas
as
select
carrera_id,
nombre
from carreras
where esta_activa = 1;
go

select *
from vista_estudiantes_carreras;
go

-- view 5
create view vista_detalles_cursos
as
select
dm.matricula_id,
c.nombre as curso,
c.costo
from detalle_matricula dm
inner join cursos c
on dm.curso_id =c.curso_id;
go

select *
from vista_detalles_cursos;
go

-- view 6

create view vista_estudiantes_ciberseguridad
as
select
e.nombre_completo,
c.nombre as carrera
from estudiantes e
inner join carreras c
on e.carrera_id = c.carrera_id
where c.nombre = 'Ciberseguridad';
go

select *
from vista_estudiantes_ciberseguridad;
go