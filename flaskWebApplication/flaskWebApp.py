from flask import Flask, render_template, escape, request
import base64
import numpy as np
import matplotlib.image as mplimg
import matplotlib.pyplot as plt
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

    # Read RGB image 
    img = mplimg.imread('testImage.png')

    # Testing
    #image = ~np.array(list(img[0:784])).reshape(28,28).astype(np.uint8)
    #img = ~np.array(img).reshape(4, 784).astype(np.uint8) / 255.0

    test_imgs = ~np.array(list(img[:])).reshape(4, 784).astype(np.uint8) / 255.0
    #print(test_imgs[0:1])

    # Prediction always returns 5 for some reason, need to fix.
    print("\nResults:", model.predict(test_imgs[0:1]))
    print("\nResults:", model.predict(test_imgs[1:2]))
    print("\nResults:", model.predict(test_imgs[2:3]))
    print("\nResults:", model.predict(test_imgs[3:4]))

    return str(model.predict(test_imgs[0:1]).argmax())

# I encountered the error below when trying to call model.predict()
# "Tensor Tensor("dense_3/Softmax:0", shape=(?, 10), dtype=float32) is not an element of this graph."
# From research it seems to be a common problem and one fix I found is to run the script through the main
# setting the the threaded attribute to false.
# https://github.com/jrosebr1/simple-keras-rest-api/issues/5
if __name__ == "__main__":
    app.run(debug = False, threaded = False)