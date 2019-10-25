from flask import Flask, render_template, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route("/home")
def homePage():
    return render_template("home.html")