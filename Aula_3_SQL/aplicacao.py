import os

#Usaremos todas as bibliotecas vistas ate agr em conjunto para conseguir rodar essa aplicacao
#Que utiliza de pyhton, html, css, sql, para exibir uma lista de voo, e adicionar um novo passageiro a essa Lista
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    voos = db.execute("SELECT * FROM voos").fetchall() #Pega a lista de voos
    return render_template("index.html", voos = voos)

@app.route("/book", methods=["POST"])
def book():
    #Agenda um voo

    name = request.form.get("name") #Seleciona o nome que o usuario digitou e guarda na variavel
    try:
        voo_id = int(request.form.get("voo_id"))
    except ValueError:
        return render_template("erro.html", message = "Numero de voo invalido.")

    # Tendo certeza de que o voo existe.
      if db.execute("SELECT * FROM voos WHERE id = :id", {"id": voo_id}).rowcount == 0: #Rowcount conta a quantidade de linhas que a query retorna
          return render_template("error.html", message="Nao ha voo com essa id.") #Caso tenha 0 linhas, cai nessa condicao
      db.execute("INSERT INTO passengers (name, voo_id) VALUES (:name, :voo_id)", #Depois de ter toda a certeza, que a id existe, que ela e um numero, e que temos uma pessoa, realizamos a query para inserir tal dado no banco de dados
              {"name": name, "voo_id": voo_id}) #É essecial usar a sintaxe desses placeholder ":voo_id", e o comando VALUES na query, pois dessa forma, o SQL tabalhara com tais informacoes sem problemas
      db.commit()
      return render_template("success.html")

@app.route("/voos")
  def voos():
      #Lista todos os voos
      voos = db.execute("SELECT * FROM voos").fetchall()
      return render_template("voos.html", voos=voos)

@app.route("/voos/<int:voo_id>")
  def voo(voo_id): #O parametro voo_id e passado pela url
      #Lista detalhes sobre cada voo

      # Condicional para garantir que o id existe.
      voo = db.execute("SELECT * FROM voos WHERE id = :id", {"id": voo_id}).fetchone()
      if voo is None:
          return render_template("error.html", message="Nao ha tal voo.")

      # Pega todos os passageiros se o voo existir.
      passengers = db.execute("SELECT name FROM passengers WHERE voo_id = :voo_id",
                              {"voo_id": voo_id}).fetchall()
      return render_template("voo.html", voo=voo, passengers=passengers)
