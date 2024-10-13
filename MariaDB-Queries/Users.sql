CREATE USER 'Administrador'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON Restaurante.* TO 'Administrador'@'localhost';

CREATE USER 'Gerente'@'localhost' IDENTIFIED BY '1234';

CREATE USER 'Funcionario'@'localhost' IDENTIFIED BY '1234';
GRANT SELECT ON Restaurante.venda TO 'Funcionario'@'localhost';