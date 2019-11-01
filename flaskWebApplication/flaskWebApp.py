from flask import Flask, render_template, escape, request
import base64

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route("/home")
def homePage():
    return render_template("home.html")

@app.route("/predictImage", methods=['POST'])
def predictImage():
    # Get the base64 image from the request
    jsonData = request.get_json()

    # get the base64 binary out of the json data so it can be decoded.
    # base64 data follows this format "data:image/png;base64,iVBORw0KGgoA..."
    # so strip out from base64, onwards.
    base64_data = jsonData['data'].split('base64,')[1]

    print(base64_data)

    return render_template("home.html")