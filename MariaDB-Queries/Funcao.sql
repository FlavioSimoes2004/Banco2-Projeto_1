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