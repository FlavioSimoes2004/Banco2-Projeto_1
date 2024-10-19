CREATE TRIGGER IF NOT EXISTS ganhar_ponto
AFTER INSERT ON venda
FOR EACH ROW
BEGIN
    UPDATE cliente
    SET pontos = pontos + Calculo(NEW.valor)
    WHERE NEW.id_cliente = id;
END;

DELIMITER #
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
END #
DELIMITER ;