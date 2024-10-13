-- Inserindo dados na tabela cliente
INSERT INTO cliente (nome, sexo, idade, nascimento, pontos) VALUES
('Alice', 'f', 30, '1993-05-15', 100),
('Bruno', 'm', 25, '1998-02-20', 150),
('Carlos', 'm', 40, '1983-07-10', 200),
('Diana', 'f', 35, '1988-11-25', 250),
('Eduardo', 'm', 28, '1995-03-30', 80),
('Fernanda', 'f', 32, '1991-04-12', 120),
('Gustavo', 'm', 27, '1996-06-18', 90),
('Helena', 'f', 29, '1994-09-03', 110),
('Igor', 'm', 22, '2001-01-01', 70),
('Júlia', 'f', 26, '1997-08-08', 130);

-- Inserindo dados na tabela prato
INSERT INTO prato (nome, descricao, valor, disponibilidade) VALUES
('Pizza Margherita', 'Pizza clássica com molho de tomate e queijo.', 25.50, TRUE),
('Bife à Parmegiana', 'Bife empanado coberto com queijo e molho.', 45.00, TRUE),
('Sushi', 'Variados tipos de sushi com peixe fresco.', 60.00, TRUE),
('Salada Caesar', 'Salada com frango grelhado e molho Caesar.', 30.00, TRUE),
('Espaguete à Carbonara', 'Massa com molho cremoso de ovos e queijo.', 35.00, TRUE),
('Lasagna', 'Camadas de massa com carne e molho de tomate.', 40.00, TRUE),
('Tacos', 'Tacos recheados com carne e vegetais.', 20.00, TRUE),
('Burger', 'Hambúrguer com queijo, alface e tomate.', 28.00, TRUE),
('Feijoada', 'Prato típico brasileiro com feijão e carnes.', 50.00, TRUE),
('Brownie', 'Bolo de chocolate com nozes.', 15.00, TRUE);

-- Inserindo dados na tabela fornecedor
INSERT INTO fornecedor (nome, estado_origem) VALUES
('Fornecedor A', 'São Paulo'),
('Fornecedor B', 'Minas Gerais'),
('Fornecedor C', 'Rio de Janeiro'),
('Fornecedor D', 'Bahia'),
('Fornecedor E', 'Rio Grande do Sul'),
('Fornecedor F', 'Paraná'),
('Fornecedor G', 'Ceará'),
('Fornecedor H', 'Santa Catarina'),
('Fornecedor I', 'Pernambuco'),
('Fornecedor J', 'Espírito Santo');

-- Inserindo dados na tabela ingredientes
INSERT INTO ingredientes (nome, data_fabricacao, data_validade, quantidade, observacao) VALUES
('Farinha', '2024-01-10', '2025-01-10', 100, 'Usar para pães e massas.'),
('Queijo', '2024-02-15', '2024-07-15', 50, 'Queijo mussarela.'),
('Carne', '2024-03-01', '2024-05-01', 30, 'Carne bovina.'),
('Tomate', '2024-04-05', '2024-06-05', 80, 'Tomate fresco.'),
('Alface', '2024-04-10', '2024-05-10', 60, 'Alface crespa.'),
('Cebola', '2024-03-20', '2024-06-20', 70, 'Cebola roxa.'),
('Pimenta', '2024-04-15', '2024-07-15', 40, 'Pimenta dedo de moça.'),
('Ovo', '2024-03-15', '2024-06-15', 120, 'Ovos caipiras.'),
('Chocolate', '2024-02-20', '2025-02-20', 20, 'Chocolate meio amargo.'),
('Peixe', '2024-03-10', '2024-04-10', 25, 'Peixe fresco do dia.');

-- Inserindo dados na tabela usos
INSERT INTO usos (id_prato, id_ingrediente) VALUES
(1, 1),  -- Pizza Margherita usa Farinha
(1, 2),  -- Pizza Margherita usa Queijo
(2, 3),  -- Bife à Parmegiana usa Carne
(3, 9),  -- Sushi usa Peixe
(4, 5),  -- Salada Caesar usa Alface
(5, 1),  -- Espaguete à Carbonara usa Farinha (massa)
(6, 3),  -- Lasagna usa Carne
(7, 3),  -- Tacos usa Carne
(8, 1),  -- Burger usa Farinha (pão)
(9, 4);  -- Feijoada usa Tomate

-- Inserindo dados na tabela venda
INSERT INTO venda (id_cliente, id_prato, quantidade, dia, hora, valor) VALUES
(1, 1, 2, '2024-10-01', '12:00:00', 51.00),
(2, 3, 1, '2024-10-02', '19:00:00', 60.00),
(3, 2, 3, '2024-10-03', '20:30:00', 135.00),
(4, 4, 1, '2024-10-04', '13:00:00', 30.00),
(5, 5, 2, '2024-10-05', '18:00:00', 70.00),
(6, 6, 1, '2024-10-06', '21:00:00', 40.00),
(7, 7, 4, '2024-10-07', '12:00:00', 80.00),
(8, 8, 1, '2024-10-08', '14:00:00', 28.00),
(9, 9, 1, '2024-10-09', '11:00:00', 50.00),
(10, 10, 2, '2024-10-10', '15:00:00', 30.00);
