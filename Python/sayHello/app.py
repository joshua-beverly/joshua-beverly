### Run flask from terminal with: python3 -m flask run

from flask import Flask, render_template, request, flash

## Creates a class for the app
app = Flask(__name__)
#app.secret_key = "secretkey"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")