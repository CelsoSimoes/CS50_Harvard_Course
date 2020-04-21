SELECT * FROM voos
WHERE origin IN ('New York', 'Lima');
--Seleciona todas as linhas no qual a coluna orgini possua as strings 'New York' ou 'Lima'

SELECT * FROM voos
WHERE origin LIKE '%a%';
--Esse %a% é parecido com um placeholder
-- Diz: Seleciona todas as linnhas da tabela voos no qual a string da coluna orgins tenha alguma letra 'a'
