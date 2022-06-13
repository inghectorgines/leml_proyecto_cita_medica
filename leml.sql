CREATE DATABASE IF NOT EXISTS leml_cita_medica;
USE leml_cita_medica;

CREATE TABLE registro_doc(
    id INT(25) auto_increment NOT NULL,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    num_consultorio VARCHAR(100) NOT NULL,
    num_cedula VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_registro_doc PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE (email)  
)ENGINE=InnoDb;

CREATE TABLE registrar_consult(
    id INT(25) auto_increment NOT NULL,
    usuario_id INT(25) NOT NULL,
    num_consulta VARCHAR(255),
    user VARCHAR(255),
    apellidos VARCHAR(255),
    edad VARCHAR(255) NOT NULL,
    telefono VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_registrar_consult PRIMARY KEY (id),
    CONSTRAINT fk_consult_doc FOREIGN KEY (usuario_id) REFERENCES registro_doc(id)
)ENGINE=InnoDb;

