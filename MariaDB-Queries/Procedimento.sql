CREATE PROCEDURE IF NOT EXISTS Reajuste(IN percentual DOUBLE)
BEGIN
    UPDATE prato
    SET valor = valor + (valor * (percentual/100));
END;

DROP PROCEDURE IF EXISTS Sorteio;
DELIMITER //
CREATE PROCEDURE Sorteio()
BEGIN
    DECLARE random_id INT;
    
    SELECT id INTO random_id
    FROM cliente
    ORDER BY RAND()
    LIMIT 1;
    
    UPDATE cliente
    SET pontos = pontos + 100
    WHERE id = random_id;
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS Estatisticas;
DELIMITER //
CREATE PROCEDURE Estatisticas()
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

    DECLARE produto_mais_vendido INT;

    SELECT v.id_prato, SUM(v.valor * v.quantidade) AS maior_ganho
    INTO produto_mais_vendido, @maior_valor_ganho
    FROM venda v
    GROUP BY v.id_prato
    ORDER BY maior_ganho DESC
    LIMIT 1;

    SELECT p.nome AS prato, @maior_valor_ganho AS valor_ganho_total
    FROM prato p
    WHERE p.id = produto_mais_vendido;
        LIMIT 1;
    
    SELECT p.nome AS prato, @maior_valor_ganho AS valor_ganho_total
    FROM prato p
    WHERE p.id = produto_mais_vendido;

    SELECT DATE_FORMAT(v.dia, '%Y-%m') AS mes, SUM(v.valor * v.quantidade) AS ganho_mes
    FROM venda v
    WHERE v.id_prato = produto_mais_vendido
    GROUP BY mes
    ORDER BY ganho_mes DESC
    LIMIT 1;

    SELECT DATE_FORMAT(v.dia, '%Y-%m') AS mes, SUM(v.valor * v.quantidade) AS ganho_mes
    FROM venda v
    WHERE v.id_prato = produto_mais_vendido
    GROUP BY mes
    ORDER BY ganho_mes ASC
    LIMIT 1;
END//
DELIMITER ;
call Estatisticas();

CREATE PROCEDURE IF NOT EXISTS Gastar_pontos()
BEGIN

END;

DELIMITER $$

CREATE PROCEDURE comprar_prato_com_pontos(IN p_id_cliente INT, IN p_id_prato INT)
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

END$$

DELIMITER ;
