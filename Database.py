import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='administrador',
    password='1234'
)

cursor = connection.cursor()
database_name = 'Restaurante'

create_tables_query = '''
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
'''

insert_into_tables = '''
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
('Julia', 'f', 26, '1997-08-08', 130);

INSERT INTO prato (nome, descricao, valor, disponibilidade) VALUES
('Pizza Margherita', 'Pizza classica com molho de tomate e queijo.', 25.50, TRUE),
('Bife a Parmegiana', 'Bife empanado coberto com queijo e molho.', 45.00, TRUE),
('Sushi', 'Variados tipos de sushi com peixe fresco.', 60.00, TRUE),
('Salada Caesar', 'Salada com frango grelhado e molho Caesar.', 30.00, TRUE),
('Espaguete a Carbonara', 'Massa com molho cremoso de ovos e queijo.', 35.00, TRUE),
('Lasagna', 'Camadas de massa com carne e molho de tomate.', 40.00, TRUE),
('Tacos', 'Tacos recheados com carne e vegetais.', 20.00, TRUE),
('Burger', 'Hamburguer com queijo, alface e tomate.', 28.00, TRUE),
('Feijoada', 'Prato tipico brasileiro com feijao e carnes.', 50.00, TRUE),
('Brownie', 'Bolo de chocolate com nozes.', 15.00, TRUE);

INSERT INTO fornecedor (nome, estado_origem) VALUES
('Fornecedor A', 'SP'),
('Fornecedor B', 'MG'),
('Fornecedor C', 'RJ'),
('Fornecedor D', 'BA'),
('Fornecedor E', 'RS'),
('Fornecedor F', 'PA'),
('Fornecedor G', 'CE'),
('Fornecedor H', 'SC'),
('Fornecedor I', 'PE'),
('Fornecedor J', 'ES');

INSERT INTO ingredientes (nome, data_fabricacao, data_validade, quantidade, observacao) VALUES
('Farinha', '2024-01-10', '2025-01-10', 100, 'Usar para paes e massas.'),
('Queijo', '2024-02-15', '2024-07-15', 50, 'Queijo mussarela.'),
('Carne', '2024-03-01', '2024-05-01', 30, 'Carne bovina.'),
('Tomate', '2024-04-05', '2024-06-05', 80, 'Tomate fresco.'),
('Alface', '2024-04-10', '2024-05-10', 60, 'Alface crespa.'),
('Cebola', '2024-03-20', '2024-06-20', 70, 'Cebola roxa.'),
('Pimenta', '2024-04-15', '2024-07-15', 40, 'Pimenta dedo de moça.'),
('Ovo', '2024-03-15', '2024-06-15', 120, 'Ovos caipiras.'),
('Chocolate', '2024-02-20', '2025-02-20', 20, 'Chocolate meio amargo.'),
('Peixe', '2024-03-10', '2024-04-10', 25, 'Peixe fresco do dia.');

INSERT INTO usos (id_prato, id_ingrediente) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 9),
(4, 5),
(5, 1),
(6, 3),
(7, 3),
(8, 1),
(9, 4);

INSERT INTO venda (id_cliente, id_prato, quantidade, dia, hora, valor) VALUES
(1, 1, 10, '2024-10-01', '12:00:00', 51.00),
(2, 3, 10, '2024-10-02', '19:00:00', 60.00),
(3, 2, 10, '2024-10-03', '20:30:00', 135.00),
(4, 4, 10, '2024-10-04', '13:00:00', 30.00),
(5, 5, 10, '2024-10-05', '18:00:00', 70.00),
(6, 6, 10, '2024-10-06', '21:00:00', 40.00),
(7, 7, 10, '2024-10-07', '12:00:00', 80.00),
(8, 8, 10, '2024-10-08', '14:00:00', 28.00),
(9, 9, 1, '2024-10-09', '11:00:00', 50.00),
(9, 9, 3, '2024-11-10', '11:00:00', 50.00),
(9, 9, 4, '2024-12-11', '11:00:00', 50.00),
(10, 10, 10, '2024-10-10', '15:00:00', 30.00);
'''

create_users_query = '''
CREATE USER IF NOT EXISTS 'Administrador'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON Restaurante.* TO 'Administrador'@'localhost';

CREATE USER IF NOT EXISTS 'Gerente'@'localhost' IDENTIFIED BY '1234';
GRANT SELECT, UPDATE, DELETE ON Restaurante.* TO 'Gerente'@'localhost';
FLUSH PRIVILEGES;

CREATE USER IF NOT EXISTS 'Funcionario'@'localhost' IDENTIFIED BY '1234';
GRANT INSERT, SELECT ON Restaurante.venda TO 'Funcionario'@'localhost';

FLUSH PRIVILEGES;
'''

create_function_query = '''
CREATE FUNCTION IF NOT EXISTS Calculo(IN valor DECIMAL(10, 3))
RETURNS INTEGER
BEGIN
    DECLARE pontos INTEGER;
    SET pontos = 0;

    WHILE valor >= 10 DO
        SET valor = valor - 10;
        SET pontos = pontos + 1;
    END WHILE;

    RETURN pontos;
END;
'''

create_views_query = ['''
CREATE VIEW IF NOT EXISTS average_gender_age AS
SELECT sexo, AVG(idade) 
FROM cliente 
GROUP BY sexo;
''',
'''
CREATE VIEW IF NOT EXISTS rush_time AS
SELECT HOUR(hora) AS hour_gap, SUM(valor) AS total_vendas
FROM venda
GROUP BY HOUR(hora)
ORDER BY total_vendas DESC;
'''
]

create_procedures_query = ['''
CREATE PROCEDURE IF NOT EXISTS Reajuste(IN percentual DOUBLE)
BEGIN
    UPDATE prato
    SET valor = valor + (valor * (percentual/100));
END;
''',
'''
CREATE PROCEDURE IF NOT EXISTS Sorteio()
BEGIN
    DECLARE random_id INT;
    
    SELECT id INTO random_id
    FROM cliente
    ORDER BY RAND()
    LIMIT 1;
    
    UPDATE cliente
    SET pontos = pontos + 100
    WHERE id = random_id;
END;
'''
,
    '''                           
CREATE PROCEDURE IF NOT EXISTS Estatisticas()
BEGIN
    SELECT  p.nome AS prato, sum(v.valor * v.quantidade) AS maior_ganho
    FROM venda v
    JOIN prato p ON v.id_prato = p.id
    GROUP BY v.id_prato
    ORDER BY maior_ganho DESC
	LIMIT 1;
    
    SELECT  p.nome AS prato, sum(v.valor * v.quantidade) AS menor_ganho
    FROM venda v
    JOIN prato p ON v.id_prato = p.id
    GROUP BY v.id_prato
    ORDER BY menor_ganho ASC
	LIMIT 1;
                           
    SELECT p.nome, SUM(v.valor) AS valor_total
    FROM venda v
    INNER JOIN prato p ON v.id_prato = p.id
    GROUP BY p.id
    ORDER BY valor_total ASC
    LIMIT 1;
                           
    SET @produto_menos_vendido = (
    SELECT p.id
    FROM venda v
    INNER JOIN prato p ON v.id_prato = p.id
    GROUP BY p.id
    ORDER BY SUM(v.valor) ASC
    LIMIT 1
    );
                           
    SELECT 
    MONTH(v.dia) AS mes,
    COUNT(*) AS quantidade_vendas
    FROM venda v
    WHERE v.id_prato = @produto_menos_vendido
    GROUP BY MONTH(v.dia)
    ORDER BY quantidade_vendas DESC, MONTH(v.dia) ASC;
END;
''',
'''
CREATE PROCEDURE IF NOT EXISTS comprar_prato_com_pontos(IN p_id_cliente INT, IN p_id_prato INT)
BEGIN
    DECLARE pontos_cliente INT;
    DECLARE valor_prato DECIMAL(10, 3);
    DECLARE pontos_necessarios INT;
    DECLARE pontos_extra INT DEFAULT 0;
    DECLARE novo_saldo_pontos INT;

    SELECT pontos INTO pontos_cliente
    FROM cliente
    WHERE id = p_id_cliente;

    IF pontos_cliente <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cliente não tem pontos suficientes.';
    END IF;

    SELECT valor INTO valor_prato
    FROM prato
    WHERE id = p_id_prato;

    SET pontos_necessarios = FLOOR(valor_prato);

    IF valor_prato > pontos_necessarios THEN
        SET pontos_extra = 1;
    END IF;

    IF pontos_cliente < (pontos_necessarios + pontos_extra) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Pontos insuficientes para comprar o prato.';
    END IF;

    SET novo_saldo_pontos = pontos_cliente - (pontos_necessarios + pontos_extra);

    UPDATE cliente
    SET pontos = novo_saldo_pontos
    WHERE id = p_id_cliente;

    INSERT INTO venda (id_cliente, id_prato, quantidade, dia, hora, valor)
    VALUES (p_id_cliente, p_id_prato, 1, CURDATE(), CURTIME(), valor_prato);

    SELECT 'Compra realizada com sucesso!';

END;
'''
]

create_triggers_query = ['''
CREATE TRIGGER IF NOT EXISTS ganhar_ponto
AFTER INSERT ON venda
FOR EACH ROW
BEGIN
    UPDATE cliente
    SET pontos = pontos + Calculo(NEW.valor)
    WHERE NEW.id_cliente = id;
END;
''',
'''
CREATE TRIGGER IF NOT EXISTS comida_vencida
AFTER UPDATE ON ingredientes
FOR EACH ROW
BEGIN
    IF NEW.data_validade < CURDATE() THEN
        UPDATE prato
        SET disponibilidade = FALSE
        WHERE id IN (
            SELECT id_prato
            FROM usos
            WHERE id_ingrediente = NEW.id
        );
    END IF;
END;
''',
'''
CREATE TRIGGER IF NOT EXISTS trigger_reduz_ingrediente_apos_venda
AFTER INSERT ON venda
FOR EACH ROW
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE ingrediente_id INT;
    DECLARE cursor_ingredientes CURSOR FOR 
        SELECT id_ingrediente FROM usos WHERE id_prato = NEW.id_prato;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cursor_ingredientes;
    
    read_loop: LOOP
        FETCH cursor_ingredientes INTO ingrediente_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        UPDATE ingredientes
        SET quantidade = quantidade - 1
        WHERE id = ingrediente_id;
    END LOOP;
    
    CLOSE cursor_ingredientes;
END;
''',
'''
CREATE TRIGGER verificar_disponibilidade
BEFORE INSERT ON venda
FOR EACH ROW
BEGIN
    DECLARE prato_disponivel BOOLEAN;

    SELECT disponibilidade INTO prato_disponivel
    FROM prato
    WHERE id = NEW.id_prato;

    IF prato_disponivel = FALSE THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O prato selecionado está indisponível';
    END IF;
END;
'''
]

setMesMenor = """
                    SET @produto_menos_vendido = (
                    SELECT p.id
                    FROM venda v
                    INNER JOIN prato p ON v.id_prato = p.id
                    GROUP BY p.id
                    ORDER BY SUM(v.valor) ASC
                    LIMIT 1
                    );
"""
mesMenor = """
                    SELECT
                    MONTH(dia) AS mes,
                    YEAR(dia) AS ano,
                    SUM(quantidade) AS total_vendido
                    FROM venda
                    WHERE id_prato = (
                    SELECT id_prato
                    FROM venda
                    GROUP BY id_prato
                    ORDER BY SUM(quantidade) ASC
                    LIMIT 1
                    )
                    GROUP BY YEAR(dia), MONTH(dia)
                    ORDER BY total_vendido ASC
                    LIMIT 1;
"""
mesMaior = """
                    SELECT
                    MONTH(dia) AS mes,
                    YEAR(dia) AS ano,
                    SUM(quantidade) AS total_vendido
                    FROM venda
                    WHERE id_prato = (
                    SELECT id_prato
                    FROM venda
                    GROUP BY id_prato
                    ORDER BY SUM(quantidade) ASC
                    LIMIT 1
                    )
                    GROUP BY YEAR(dia), MONTH(dia)
                    ORDER BY total_vendido DESC
                    LIMIT 1;
"""

queries = [
    create_tables_query,
    create_users_query,
    insert_into_tables
]

def drop_db():
    cursor.execute(f'DROP DATABASE IF EXISTS {database_name}')

def create_db():
    drop_db()
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
    cursor.execute(f'USE {database_name}')
    for query in queries:
        query = query.replace('\n', '')
        query = query.split(';')
        query.pop()

        for q in query:
            cursor.execute(q)

    cursor.execute(create_function_query)
    for query in create_procedures_query:
        cursor.execute(query)
    for query in create_views_query:
        cursor.execute(query)
    for query in create_triggers_query:
        cursor.execute(query)

if __name__ == "__main__":
    create_db()

    choice = None
    while(1):
        choice = int(input('[0] END\n[1] INSERT\n[2] DROP DATABASE\n[3] RECREATE DATABASE\n[4] VER PRODUTO MENOS VENDIDO\n[5] MES DE MENOR VENDA DO PRODUTO MENOS VENDIDO\n[6] MES DE MAIOR VENDA DO PRODUTO MENOS VENDIDO\n[7] COMPRAR PRATO COM PONTOS\nCHOOSE: '))
        while choice < 0 or choice > 7:
            choice = int(input('Invalid choice, choose again: '))
        
        if choice == 0:
            break
        elif choice == 1:
            choice = int(input('[0] CLIENTE\n[1] PRATO\n[2] FORNECEDOR\n[3] ingredientes\n[4] USOS\n[5] VENDA\nINSERT ON: '))
            while choice < 0 or choice > 5:
                choice = int(input('Invalid choice, choose again: '))

            if choice == 0: # insert cliente
                nome = input('NOME: ')
                sexo = input('SEXO [\'m\' or \'f\' or \'o\']: ')
                idade = input('IDADE: ')
                nascimento = input('DATA NASCIMENTO: ')
                pontos = input('PONTOS: ')
                cursor.execute(f'INSERT INTO cliente (nome, sexo, idade, nascimento, pontos) VALUES (\'{nome}\', \'{sexo}\', \'{idade}\', \'{nascimento}\', \'{pontos}\');')
            elif choice == 1: # insert prato
                nome = input('NOME: ')
                descricao = input('DESCRICAO: ')
                valor = input('VALOR: ')
                disponibilidade = input('DISPONIVEL [0 - nao | 1 - sim]? ')
                cursor.execute(f'INSERT INTO prato (nome, descricao, valor, disponibilidade) VALUES (\'{nome}\', \'{descricao}\', \'{valor}\', \'{disponibilidade}\');')
            elif choice == 2: # insert fornecedor
                nome = input('NOME: ')
                estado_origem = input('ESTADO (sigla maiusculo): ')
                cursor.execute(f'INSERT INTO fornecedor (nome, estado_origem) VALUES (\'{nome}\', \'{estado_origem}\');')
            elif choice == 3: # insert ingredientes
                nome = input('NOME: ')
                fabricacao = input('DATA FABRICACAO: ')
                validade = input('DATA VALIDADE: ')
                quant = input('QUANTIDADE: ')
                obs = input('OBSERVACAO: ')
                cursor.execute(f'INSERT INTO ingredientes (nome, data_fabricacao, data_validade, quantidade, observacao) VALUES (\'{nome}\', \'{fabricacao}\', \'{validade}\', \'{quant}\', \'{obs}\');')
            elif choice == 4: # insert usos
                prato = input('ID PRATO: ')
                ingrediente = input('ID INGREDIENTE: ')
                cursor.execute(f'INSERT INTO usos (id_prato, id_ingrediente) VALUES (\'{prato}\', \'{ingrediente}\');')
            else: # insert venda
                cliente = input('ID CLIENTE: ')
                prato = input('ID PRATO: ')
                quant = input('QUANTIDADE: ')
                dia = input('DIA: ')
                hora = input('HORA: ')
                valor = input('VALOR: ')
                cursor.execute(f'INSERT INTO venda (id_cliente, id_prato, quantidade, dia, hora, valor) VALUES (\'{cliente}\', \'{prato}\', \'{quant}\', \'{dia}\', \'{hora}\', \'{valor}\');')
            connection.commit() # use when insert, update or delete
        elif choice == 2:
            drop_db()
        elif choice == 3: # choice == 3
            create_db()
        elif choice == 4:
            cursor.execute(valorGanhoProdutoMenosVendido)
            for i in cursor:
                print(i)
        elif choice == 5:
            cursor.execute(setMesMenor)
            cursor.execute(mesMenor)
            for i in cursor:
                print(i)
        elif choice == 6:
            cursor.execute(mesMaior)
            print(*cursor)
        elif choice == 7:
            client_id = input("Digite o id do cliente: ")
            dish_id = input("Digite o id do prato: ")
            try:
                cursor.execute(f'CALL comprar_prato_com_pontos({client_id}, {dish_id});')
                print(cursor.fetchone())
            except:
                print('Pontos insuficientes!')
#create_db()
