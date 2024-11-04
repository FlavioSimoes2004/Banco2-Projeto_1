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

CREATE PROCEDURE IF NOT EXISTS Gastar_pontos()
BEGIN

END;