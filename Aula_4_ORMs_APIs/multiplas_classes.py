class Flight:

      counter = 1 #Contador que iremos utilizar para atribuir a cada novo voo criado, uma id unica

      def __init__(self, origin, destination, duration):

          #O id não chega a ser passado por parametro, pois é algo que o usuario nao precisa conhecer realemte
          # Faz o rastreio do numero da id.
          self.id = Flight.counter
          Flight.counter += 1 #Utilizando 'Flight.id', e nao 'self.id', nos estamos implementando a soma dentro da propria classe em si, e nao do novo objeto 'x' criado

          #Rastreia os passageiros daquele voo, com uma lista
          self.passengers = [] #= a uma lista vazia

          self.origin = origin
          self.destination = destination
          self.duration = duration

      def print_info(self):
          print(f"A origem é: {self.origin}")
          print(f"O destino é: {self.destination}")
          print(f"A duracao e de: {self.duration} minutos")

          print("Passageiros: ")
          for passenger in self.passengers:
              print (f"{passenger.name}")

      def atraso(self, tempo):
          self.duration += tempo

    #self é um objeto de Flight, e p aqui, é um objetp de Passenger
      def add_passanger(self, p):
          self.passengers.append(p) #Lembrando que toda lista em pyhton possui o metodo appende e ele adiciona mais um item a lista
          p.flight_id = self.id #Adiciona uma id especifica a id de voo do passageiro


class Passenger:

    def __init__(self, name):
        self.name = name

def main():
    #Inicializa o voo
    voo_1 = Flight(origin = "Contagem", destination="Jundiai", duration=34)

    #Cria dois passageiros
    Joao = Passenger("Joao")
    Matilda = Passenger("Matilda")

    #Adiciona Dois passageiros ao voo
    voo_1.add_passanger(Joao)
    voo_1.add_passanger(Matilda)

    #Printa as informacoes do voo
    voo_1.print_info()

if __name__ == "__main__":
    main()
