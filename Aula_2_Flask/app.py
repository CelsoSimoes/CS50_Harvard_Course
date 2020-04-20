from flask import Flask, render_template, request, session
from flask_session.__init__ import Session #Necessario a instalacao do flask session: 'pip install flask_session'

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# notes = [] #Defino uma lista vazia que ira salvar minhas 'notas'. Essa e uma variavel global acessivel por toda a aplicacao, nao e o ideal

@app.route("/", methods=["GET", "POST"])
def notas():
    if session.get("notes") is None:
        session["notes"] = [] #Crio a lista de notas unica da minha sessao
    if request.method == "POST": #Se o metodo request for POST
        note = request.form.get("note") #Acessamos a variavel note
        session["notes"].append(note) #Acrescento uma nota a minha lista

    return render_template("notes.html", notes=session["notes"])
