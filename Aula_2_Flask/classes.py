#E como se eu criasse um novo tipo de classe realmente, no qual posso acessar sub-classes dentro, com uma funcao pre pronta talvez e por ai vai
class Ponto:
    def __init__(self, x, y): #O 'self' se refere a propria varaivel utilizada na criacao da classe, ja 'x' e 'y' sao sub-classes dessa
        self.x = x
        self.y = y

pontin = Ponto(3, 7)
print(pontin.x)
print(pontin.y)
