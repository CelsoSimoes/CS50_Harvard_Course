CREATE TABLE voos (
  id SERIAL PRIMARY KEY, -- Serial do voo que ira acrescentar 1 automaticamente a cada novo voo. Como cada voo e unico, essa é tambem a chave primaria
  origin VARCHAR NOT NULL, -- Coluna não pode ser nulo, e é uma varchar/string
  destination VARCHAR NOT NULL, --texto
  duration INTEGER NOT NULL -- Todo voo precisa ter uma duracao. Esta em inteiros
);

CREATE TABLE passengers ( --Tabela usada para exemplificar a relacao de chave estrangeira no SQL
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    voos_id INTEGER REFERENCES voos --Chave estrangeira que sera mapeada para o id de 'voos' por default
);
