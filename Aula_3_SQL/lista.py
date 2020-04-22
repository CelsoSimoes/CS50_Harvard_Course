import os #Importa a biblioteca de um sistema operacional

from sqlalchemy import create_engine #
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) #A engine é usada para gerenciar as conexoes com o bancos de dados. O "DATABASE_URL" especifica onde esta o meu banco de dados, no caso, este é um local host do computador do proprio usuario

db = scoped_session(sessionmaker(bind=engine)) #Cria uma sessao encapsulada que garante que diferentes usuarios interagindo com banco de dados sejam mantidos separadamente

def main():
    #Dentro do 'db.execute', eu posso especificar qualquer comando em SQL que eu queira usar
    voos = db.execute("SELECT origin, destination, duration FROM voos").fetchall() # O fetchall significa: Rode a query, e me retorne todos os resultados
    #Com isso eu obternho uma lista, gracas ao fetchall, com todos os voos da tabela voos
    for voo in voos:
        print(f"{voo.origin} to {voo.destination}, {voo.duration} minutes.") #Para cada voo, printa ass infor do voo

if __name__ == "__main__":
    main()
