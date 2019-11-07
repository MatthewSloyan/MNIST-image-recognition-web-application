from flask import Flask, render_template, escape, request
import base64
import numpy as np
from PIL import Image
import keras as kr
from keras.models import load_model # To save and load models
model = load_model('../test_model.h5')

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
    # Get the base64 image from the request as JSON
    jsonData = request.get_json()

    # get the base64 binary out of the json data so it can be decoded. 'data' is the key for the JSON data.
    # base64 data follows this format "data:image/png;base64,iVBORw0KGgoA..."
    # so strip out from base64, onwards. 
    # https://www.w3schools.com/python/ref_string_split.asp
    base64_data = jsonData['data'].split('base64,')[1]

    # Using the base64 string decode and write to a png file in the root directory
    # I will later create dynamic file names so that multiple users could predict images at once.
    # wb+ creates the file from scratch
    # There's no need to close the writer as it's automatically done when exiting with statement.
    # Code adapted from and uses the imported base64 library: https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image
    imgdata = base64.b64decode(base64_data)
    with open('testImage.png', 'wb+') as f:
        f.write(imgdata)

    # Read RGB image and convert to grayscale E.g single channel (L)
    # Using the Pillow (PIL) library which is a Python Imaging Library by Fredrik Lundh and Contributors.
    # https://pillow.readthedocs.io/en/stable/
    img = Image.open('testImage.png').convert('L')
    #print(img)

    # The problem I initally had was that I was using a black pen in the HTML so when convert the 
    # image to greyscale there would be no distinct values (E.g All 0's) To solve this I have used a strong red pen which solves the problem.
    
    # reshape image data for use in neural network
    # Creates a two dimensional array of the 784 bytes in the image (28 x 28)
    img = ~np.array(img).reshape(1, 784).astype(np.uint8) / 255.0
    #print(img)

    # Testing - print array of predicted result. £.g [[1.9111006e-02 1.0649475e-02 1.9441145e-02...]]
    # The highest value is the predicted result.
    print("\nResults:", model.predict(img))

    # Return the largest value in the returned array as a String. 
    # From testing the model.predict it would return an array of possibilities. The highest value would be the right answer.
    # To get the largest value I looked up a numpy methods and found argmax() to achieve this.
    # https://kite.com/python/examples/5750/numpy-find-the-index-of-the-largest-element-of-an-array
    return str(model.predict(img).argmax())

# I encountered the error below when trying to call model.predict()
# "Tensor Tensor("dense_3/Softmax:0", shape=(?, 10), dtype=float32) is not an element of this graph."
# From research it seems to be a common problem and one fix I found is to run the script through the main
# setting the the threaded attribute to false.
# https://github.com/jrosebr1/simple-keras-rest-api/issues/5
if __name__ == "__main__":
    app.run(debug = False, threaded = False)