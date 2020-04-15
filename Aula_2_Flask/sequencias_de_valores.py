nome = "Alice" #Podemos acessar carcter por caracter da palavra Alice
nome[0] #printa o 'A'
nome[-1] #printa o 'e'
#E por ai vai

#TUPLA
coordenada = (10.0, 20.0) #Essa é uma TUPLA em Python, que representa um conjunto de valores numa unica variavel
coordenada[0]
coordenada[1]

#LISTA
nomes = ["Alice", "Bob", "Charlie"] #posso colocar qualquer tipo de variavel nas listas tambem
nomes[0]#'Alice'
nomes[1] #'Bob'
nomes[2] #'Charlie'
nomes[3] #'Error index out of range'

#SET
s = set() #É uma colecao de itens no qual nenhum item aparece duas vezes, ou seja, não adiciona valores repetidos
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)

#DICIONARIOS
#Sao usados para mapear valores, de um para o outro. O que fica atras do ':' é a 'key'/chave, e o que vem depois é o 'value'/valor associado a chave
idades= {"Carlos": 27, "Joaquim": 21} #Cria o dicionario
idades["Joao"] = 32 #Adiciona outro item ao dicionario
idades["Carlos"] += 1 #Adiciona mais 1 a valor associado com aquela chave
# idades["Calors"] = idades["Carlos"] + 1 #é outra forma de escrever a linha de cima
print(idades)
