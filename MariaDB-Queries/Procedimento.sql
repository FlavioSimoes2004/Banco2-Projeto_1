CREATE PROCEDURE IF NOT EXISTS Reajuste(IN percentual DOUBLE)
BEGIN
    UPDATE prato
    SET valor = valor + (valor * (percentual/100));
END;

DELIMITER #
CREATE PROCEDURE IF NOT EXISTS Sorteio()
BEGIN
    UPDATE cliente
    SET pontos = pontos + 100
    WHERE id = (
        SELECT id
        FROM cliente
        ORDER BY rand() 
        LIMIT 1
    );
END #
DELIMITER;

CREATE PROCEDURE IF NOT EXISTS Estatisticas()
BEGIN

END;

CREATE PROCEDURE IF NOT EXISTS Gastar_pontos()
BEGIN

END;