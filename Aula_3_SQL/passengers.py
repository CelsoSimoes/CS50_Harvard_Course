import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#Rodando multiplas queryes em um unico arquivo
def main():

    # Lista todos os voos.
    voos = db.execute("SELECT id, origin, destination, duration FROM voos").fetchall() #Seleciona todas as colunas da 'voos' e passa para a variavel voos do nosso arquivo python, como uma lista
    for voo in voos:
        print(f"Voo {voo.id}: {voo.origin} to {voo.destination}, {voo.duration} minutes.") #Para cada linha da minha lista printa os dados dessa linha

    # O usuario escolhe a id de um voo.
    voo_id = int(input("\nVoo ID: ")) #Pega a ID de um voo, dada pelo usuario, e salva essa id na variavel
    voo = db.execute("SELECT origin, destination, duration FROM voos WHERE id = :id", #:id representa um placeholder que sera substituido pelo valor da variavel
                        {"id": voo_id}).fetchone() # comando para atribuir valor ao placeholder no comando SQL

    # Se o voo nao for valido.
    if voo is None: #Se a consulta nao retorna nada:
        print("Error: Nao existe esse voo.")
        return #Retorna nada :)

    # Caso seja valido.
    passengers = db.execute("SELECT name FROM passengers WHERE voo_id = :voo_id", #Retorna os nomes dos passageiros que estavam naquele voo
                            {"voo_id": voo_id}).fetchall() # Comando... Diferente do de cima... **Duvida**
    print("\nPassengers:")
    for passenger in passengers: #Pra cada passageiro, printa o nome desse passageiro
        print(passenger.name)
    if len(passengers) == 0: #Se não houverem passageiros
        print("No passengers.")

if __name__ == "__main__":
    main()
