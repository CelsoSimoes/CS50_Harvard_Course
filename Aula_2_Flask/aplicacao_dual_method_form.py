from flask import Flask, render_template, request #Request e utilizado para representar qualquer requisicao que meu usuario tenha feito

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("forms.html")

@app.route("/ola", methods=["GET", "POST"]) #Agora temos tanto o post quanto o get, e para cada caso trataremos de forma diferente no nosso if/else
def ola():
    if request.method == "GET":
        return "Por favor envie o Formulario!"
    else:
        name = request.form.get("name") #Isso fara com que obtenhamos o nome do formulario que o usuario escreveu, e não da url em si como fora feito antes
        return render_template("ola.html", name=name)
