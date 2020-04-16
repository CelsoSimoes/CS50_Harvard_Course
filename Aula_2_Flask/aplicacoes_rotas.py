from flask import Flask #Importacao padrao para executar um aplicacao web com Flask

app = Flask(__name__) #Cria a variavel que sera a raiz da aplicacao que estamos criando

@app.route("/") #Cria uma rota para minha aplicacao Web, no caso a rota principal so com o '/'
def index():
    return "Ola Mundo!!!"

#Rotas comuns com enderecos pre-setados
#Cria a segunda rota da minha aplicacao web, '/celso'
@app.route("/celso")
def celso():
    return "Ola Celso!"

#Terceira rota
@app.route("/maria")
def maria():
    return "Ola Mariaaaa!"

#Este e um exemplo de aplicacao web dinamica
#Estas linhas de codigo criam sites nao pre-setados, para qualquer nome que o usuario venha a digitar na barra de enderecos
@app.route("/<string:name>")
def ola(name):
    name = name.capitalize() #Ira tornar a primeira letra do nome maiuscula
    return f"Ola, {name}!"
