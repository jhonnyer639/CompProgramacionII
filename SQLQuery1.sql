create database Datos;

use Datos;

create table Empleados(
	ID int IDENTITY(1,1) PRIMARY KEY,
	NumCedula varchar(12),
	Nombre varchar (40),
	Apellido varchar(40),
	FechaNac date,
	Correo varchar(40),
	Telefono varchar(15),
);

select * from Empleados