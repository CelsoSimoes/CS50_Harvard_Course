INSERT INTO voos -- Insere dentro da tabelas voos
  (orign, destination, duration) --Nas colunas citadas
  VALUES ('New York', 'London', 415) -- As seguintes informacoes
INSERT INTO voos (origin, destination, duration) VALUES ('Shanghai', 'Paris', 760);
INSERT INTO voos (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO voos (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO voos (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO voos (origin, destination, duration) VALUES ('Lima', 'New York', 455);
-- Acaba por o comando de insercao ficar bem repetitivo.
-- Existe uma forma de otimizar isso? **Procurar depois**
-- Resposta: Sim existe; basta usar um arquivo no formato '.csv' que posso colocar somente a informação/dados realemte uteis de forma compacta
-- que o programa ira ler esses arquivos, e posso fazer um insert do arquivo todo no geral

INSERT INTO passengers (name, voos_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, voos_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, voos_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, voos_id) VALUES ('Dave', 2);
INSERT INTO passengers (name, voos_id) VALUES ('Erin', 4);
INSERT INTO passengers (name, voos_id) VALUES ('Frank', 6);
INSERT INTO passengers (name, voos_id) VALUES ('Grace', 6);
--Inserindo valores na tabela de passageiros
