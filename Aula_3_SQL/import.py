import csv #Importa a biblioteca necessaria para fazer a leitura de arquivos '.csv' em Python
import os #Importa a biblioteca de um sistema operacional

from sqlalchemy import create_engine #
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) #A engine é usada para gerenciar as conexoes com o bancos de dados. O "DATABASE_URL" especifica onde esta o meu banco de dados, no caso, este é um local host do computador do proprio usuario

db = scoped_session(sessionmaker(bind=engine)) #Cria uma sessao encapsulada que garante que diferentes usuarios interagindo com banco de dados sejam mantidos separadamente

#OBS: Precisarei realizar importacoes para trabalhar com o Porjeto 1
def main():
  f = open("voos.csv") #Variavel que vai armazenar todo meu arquivo csv
  reader = csv.reader(f) #ferramenta para tonar legivel, ler o arquivo csv
  for origin, destination, duration in reader: # loop que dá a cada coluna um nome
      db.execute("INSERT INTO voos (origin, destination, duration) VALUES (:origin, :destination, :duration)", # em verde tenho os 'Placeholders' que uso logo abaixo para atribuir os valores das variavels na leitura do arquivo
                  {"origin": origin, "destination": destination, "duration": duration}) # Substitui os valores CSV para um SQL
      print(f"Added flight from {origin} to {destination} lasting {duration} minutes.") #Printando somente para saber o que esta acontecendo com o codigo
  db.commit() # "transactions are assumed, so close the transaction finished". Fecha a transacao feita, e comita as mudancas

if __name__ == "__main__":
    main()
