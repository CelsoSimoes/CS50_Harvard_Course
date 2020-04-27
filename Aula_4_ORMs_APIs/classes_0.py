class Voo:
    def __init__(self, origin, destination, duration): #O __init__ é utilizadopara fazer a criação inicial da classe Vôo. Por padrão o 'self' costuma sempre ser o primeiro argumento de inicializacão (parametros), de uma classe
        self.origin = origin #E o self, se refere ao objeto no qual estamos trabalhando
        self.destination = destination
        self.duration = duration
#A forma como iremos definir tal classe na chamada, veremos ainda. Preciso passar o parametro 'self' na chamada ou nao?
# Resposta: nós nao precisamos passar o self na chamada.

#Definindo funcoes dentro da classe:
#Funcao que nao recebe parametros, e simplesmente printa todas as informcoes contidas no objeto 'voo'
    def print_info(self):
        print(f"A origem é: {self.origin}")
        print(f"O destino é: {self.destination}")
        print(f"A duracao e de: {self.duration} minutos")

#Funcao que recebe parametros, que ira receber o tempo de atraso de um voo, e somar a sua duracao
    def atraso(self, tempo):
        self.duration += tempo

def main():

    #Criando um objeto Voo:
    v = Voo(origin = "Contagem", destination="Belo Horizonte", duration= 45)
    v.print_info() #Chamando o metodo com parametro vazio

    #Somando +10 a duracao
    v.duration += 10

    #Acessando e printando cada variavel do meu voo:
    print(v.origin)
    print(v.destination)
    print(v.duration)

    v2 = Voo("Pernambuco", "Londrina", 97)
    v2.atraso(25) #Acrescetando um atraso de 25 minutos no voo v2, aumentando assim sua duracao
    v2.print_info() #Chamando o metodo com parametro vazio

#O que esse statment diz é: Se eu estiver rodando esse arquivo em paticular (classes_o.py), o que eu deveria fazer é:
if __name__ == "__main__":
    main()
#...Rodar a funcao 'main'
