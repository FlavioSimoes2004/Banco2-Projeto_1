CREATE VIEW IF NOT EXISTS average_gender_age AS
SELECT sexo, AVG(idade) FROM cliente GROUP BY sexo;