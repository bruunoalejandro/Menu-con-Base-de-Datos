create database base_registro;
use base_registro;

create table Personas
(
Rut int primary KEY,
Nombre Varchar(50),
Direccion Varchar(50),
Correo Varchar(50),
Estado_Civil Varchar(50)
)