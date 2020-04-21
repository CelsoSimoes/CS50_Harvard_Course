UPDATE voos -- Atualiza a tabela voos
  SET duration = 430 --Colocando a duracao do voo em 430 mins
  WHERE orgin = 'New York' --Onde a origin contenha a varchar 'New York'
  AND destination = 'London'; --E o destina seja 'London'
