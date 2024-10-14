CREATE PROCEDURE IF NOT EXISTS ganhar_ponto(IN valor DECIMAL(10, 3), OUT pontos INTEGER)
BEGIN
    SET pontos = 0;
    WHILE valor >= 10 DO
        SET valor = valor - 10;
        SET pontos = pontos + 1;
    END WHILE;
END;

CREATE TRIGGER IF NOT EXISTS ganhar_ponto
AFTER INSERT ON venda
FOR EACH ROW
BEGIN
    DECLARE points INTEGER;

    CALL ganhar_ponto(NEW.valor, points);

    UPDATE cliente
    SET pontos = pontos + points
    WHERE NEW.id_cliente = id;
END;