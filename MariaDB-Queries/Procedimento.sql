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