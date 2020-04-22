import os #Importa a biblioteca de um sistema operacional

from sqlalchemy import create_engine #
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) #A engine é usada para gerenciar as conexoes com o bancos de dados. O "DATABASE_URL" especifica onde esta o meu banco de dados, no caso, este é um local host do computador do proprio usuario

db = scoped_session(sessionmaker(bind=engine)) #Cria uma sessao encapsulada que garante que diferentes usuarios interagindo com banco de dados sejam mantidos separadamente

#OBS: Precisarei realizar importacoes para trabalhar com o Porjeto 1
def main():
