import datetime #Biblioteca que checa a real data atual

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    agora = datetime.datetime.now() #Pegando a data atual
    novo_ano = agora.month == 1 and agora.day == 1 #Atribuindo a variavel novo_ano o primeiro da do ano
    novo_ano = True #Deixando como se fosse True mesmo
    return render_template("ano_novo.html", ano_nov = novo_ano)
