CREATE DATABASE IF NOT EXISTS Restaurante;
USE Restaurante;

CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    sexo CHAR(1) CHECK (sexo IN ('m', 'f', 'o')),
    idade INTEGER NOT NULL,
    nascimento DATE NOT NULL,
    pontos INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS prato(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    valor DECIMAL(10, 3) NOT NULL,
    disponibilidade BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS fornecedor(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    estado_origem ENUM(
        'AC',
        'AL',
        'AP',
        'AM',
        'BA',
        'CE',
        'ES',
        'GO',
        'MA',
        'MT',
        'MS',
        'MG',
        'PA',
        'PB',
        'PE',
        'PR',
        'PI',
        'RJ',
        'RN',
        'RS',
        'RO',
        'RR',
        'SC',
        'SP',
        'SE',
        'TO'
    ) NOT NULL
);

CREATE TABLE IF NOT EXISTS ingredientes(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    data_fabricacao DATE NOT NULL,
    data_validade DATE NOT NULL,
    quantidade INTEGER NOT NULL,
    observacao VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS usos(
    id_prato INTEGER NOT NULL,
    id_ingrediente INTEGER NOT NULL,
    FOREIGN KEY (id_prato) REFERENCES prato (id) ON DELETE CASCADE,
    FOREIGN KEY (id_ingrediente) REFERENCES ingredientes (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS venda(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_cliente INTEGER NOT NULL,
    id_prato INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    dia DATE NOT NULL,
    hora TIME NOT NULL,
    valor DECIMAL(10, 3),
    FOREIGN KEY (id_cliente) REFERENCES cliente (id) ON DELETE CASCADE,
    FOREIGN KEY (id_prato) REFERENCES prato (id) ON DELETE CASCADE
);