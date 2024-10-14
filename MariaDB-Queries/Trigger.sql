CREATE TRIGGER IF NOT EXISTS ganhar_ponto
AFTER INSERT ON venda
FOR EACH ROW
BEGIN
    UPDATE cliente
    SET pontos = pontos + Calculo(NEW.valor)
    WHERE NEW.id_cliente = id;
END;