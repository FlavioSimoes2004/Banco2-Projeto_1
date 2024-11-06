CREATE VIEW IF NOT EXISTS average_gender_age AS
SELECT sexo, AVG(idade) 
FROM cliente 
GROUP BY sexo;

CREATE VIEW IF NOT EXISTS rush_time AS
SELECT HOUR(hora) AS hour_gap, SUM(valor) AS total_vendas
FROM venda
GROUP BY HOUR(hora)
ORDER BY total_vendas DESC;

CREATE VIEW IF NOT EXISTS dish_profit AS
SELECT (quantidade * valor)
FROM venda
GROUP BY id_prato;
