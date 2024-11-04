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

CREATE PROCEDURE IF NOT EXISTS Estatisticas()
BEGIN

END;

DROP PROCEDURE IF EXISTS PratMaisVend;
DELIMITER //
CREATE PROCEDURE PratMaisVend()
BEGIN
	SELECT  p.nome AS prato, sum(v.valor * v.quantidade) AS maior_ganho
    FROM venda v
    JOIN prato p ON v.id_prato = p.id
    GROUP BY v.id_prato
    ORDER BY maior_ganho DESC
	LIMIT 1;
END//
DELIMITER ;

CREATE PROCEDURE IF NOT EXISTS Gastar_pontos()
BEGIN

END;