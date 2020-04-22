SELECT * FROM voos
WHERE origin IN ('New York', 'Lima');
--Seleciona todas as linhas no qual a coluna orgini possua as strings 'New York' ou 'Lima'

SELECT * FROM voos
WHERE origin LIKE '%a%';
--Esse %a% é parecido com um placeholder
-- Diz: Seleciona todas as linnhas da tabela voos no qual a string da coluna orgins tenha alguma letra 'a'

SELECT origin, COUNT(*) FROM flights GROUP BY origin;
--Seleciona a coluna origens da tabela de voos, agrupando as linhas pelo lugar de origem, e contando as linhas repetidas

SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;
--Seleciona os lugares de origem dos voos que aparecem pelo menos 2 ou mais vezes na origem


--Selects utilizando Juncao
SELECT origin, destination, name FROM voos JOIN passengers ON passengers.voos_id = voos.id;
--Seleciona as colunas de origem, destino e nome, da juncao das tabelasde voos e passageiros

SELECT origin, destination, name FROM voos JOIN passengers ON passengers.voos_id = voos.id WHERE name = 'Alice'
--Seleciona as colunas de origem, destino e nome, da juncao das tabelasde voos e passageiros, onde o nome da passageira no caso é Alice

SELECT * FROM flights WHERE id IN
  (SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1);
--Retorna as informacoes dos voos que possuem mais de 1 passageiro.Isso e Nesting/Aninhanmento em SQL.
