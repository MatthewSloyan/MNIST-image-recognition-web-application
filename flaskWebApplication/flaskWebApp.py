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

    #print(base64_data)

    # Using the base64 string decode and write to a png file in the root directory
    # I will later create dynamic file names so that multiple users could predict images at once.
    # wb+ creates the file from scratch
    # There's no need to close the writer as it's automatically done when exiting with statement.
    # Code adapted from: https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image
    imgdata = base64.b64decode(base64_data)
    with open('testImage.png', 'wb+') as f:
        f.write(imgdata)

    return render_template("home.html")