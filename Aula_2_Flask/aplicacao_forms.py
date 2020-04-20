from flask import Flask, render_template, request #Request e utilizado para representar qualquer requisicao que meu usuario tenha feito

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("forms.html")

@app.route("/ola", methods=["POST"]) #O que o methods nesse trecho faz, é aceitar somente a requisicao http por post e nao por get que é como se acessassemos a pagina diretamente sem enviar nd, logo se tentando ir direto para o ola.html sem enviar/postar nada, receberemos um erro chamado 'method not allowed'
def ola():
    name = request.form.get("name") #Isso fara com que obtenhamos o nome do formulario que o usuario escreveu, e não da url em si como fora feito antes
    return render_template("ola.html", name=name)
