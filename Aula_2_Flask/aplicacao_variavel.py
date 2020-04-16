from flask import Flask, render_template

app = Flask(__name__)

#Com o arquivo HTML pre-pronto e tambem pre formatado para receber uma variavel 'x'(No nosso caso 'reader'), eu posso modificar oq será retornado
#para essa variavel do meu proprio arquivo python/Flask
@app.route("/")
def index():
    cabecalho = "Ola Mundo Tche"
    return render_template("variavel.html", reader = cabecalho)

@app.route("/tchau")
def tchau():
    cabecalho =  "Tchaau!"
    return render_template("variavel.html", reader = cabecalho)
    
