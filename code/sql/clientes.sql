clientes.sql
DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes(
    id_cliente integer PRIMARY KEY AUTOINCREMENT,
    nombre varchar(50) NOT NULL,
    email varchar(50) NOT NULL
);

INSERT INTO clientes(nombre, email) VALUES('Fernando','fer@email.com');
INSERT INTO clientes(nombre, email) VALUES('Erick','erick@email.com');
INSERT INTO clientes(nombre, email) VALUES('Nataly','nat@email.com');

.headers ON

SELECT * FROM clientes;