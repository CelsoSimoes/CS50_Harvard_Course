from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("link1_heranca.html")

@app.route("/mais")
def mais():
    return render_template("link2_heranca.html")
