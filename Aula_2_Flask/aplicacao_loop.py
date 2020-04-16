from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nomes = ["Celso", "Ana", "Joao"]
    return render_template("loops_jinja.html", nomes = nomes)
