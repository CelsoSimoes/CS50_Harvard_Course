from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cabecalho = "Ola Mundo Tche"
    return render_template("variavel.html", reader = cabecalho)
