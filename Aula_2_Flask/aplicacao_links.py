from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("link1.html")

@app.route("/mais")
def mais():
    return render_template("link2.html")
