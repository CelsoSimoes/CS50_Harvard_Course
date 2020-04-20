from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config= ["SESSION_PERMANENT"] = False
app.config= ["SESSION_TYPE"] = "filesystem"
Session(app)

notes = [] #Defino uma lista vazia que ira salvar minhas 'notas'

@app.route("/", methods=["GET", "POST"])
def index():
#    if session.get("notes") is None:
    #    session["notes"] = []
    if request.method == "POST": #Se o metodo request for POST
        note = request.form.get("note") #Acessamos a variavel note
        notes.append(note) #Acrescento uma nota ao 'notes'

    return render_template("index.html", notes=notes)
