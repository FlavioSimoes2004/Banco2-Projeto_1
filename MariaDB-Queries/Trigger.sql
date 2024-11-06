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

DELIMITER //
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
END//

DELIMITER ;