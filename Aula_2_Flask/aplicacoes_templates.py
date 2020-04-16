from flask import Flask, render_template #Usado para permitir o uso de templates na pasta que possui o mesmo nome

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") #Irá executar o arquivo HTML na rota defininda
