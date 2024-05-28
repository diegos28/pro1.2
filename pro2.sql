create database pro2;
use pro2;
CREATE TABLE usuario(
id int auto_increment,
nombre varchar(50) ,
contraseña varchar(50) ,
telefono int(11) ,
direcion varchar(50) ,
usuario varchar(50) ,
Rango varchar(50) ,
primary key (id)) ;

CREATE TABLE producto(
id int  auto_increment,
product varchar(50) ,
numero int(11) ,
Descripcion varchar(50) ,
Precio int(50),
Liga varchar(1000) ,
primary key (id));

CREATE TABLE compra(
id int not null auto_increment,
image varchar(1000) ,
title varchar(50) ,
price int(50) ,
amount varchar(50) ,
total_card varchar(50) ,
count_product int(11) ,
primary key (id));
INSERT INTO usuario (id, nombre, contraseña, telefono, direcion, usuario, Rango) VALUES (NULL, 'alejandro', 'alejandro', '451156', 'alejandro', 'alejandro', 'Administrador');