from flask import Flask, render_template, escape, request
import base64
import numpy as np
from PIL import Image
import PIL.ImageOps  
import keras as kr
from keras.models import load_model # To save and load models
model = load_model('../test_model.h5')
import imageio
import cv2
from io import BytesIO

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

    img = Image.open(BytesIO(imgdata))
    #img = img.convert('L')
    #img = PIL.ImageOps.invert(img)
    img.save("image.png")

    # Open the image convert to bytes.
    # img = Image.open(BytesIO(imgdata))
    # # Save the image in bytes.
    # img = img.save("image.png")

    # inverted_image = PIL.ImageOps.invert(img)
    # inverted_image.save("image.png")

    # Use openCV to read in the image.
    gray = cv2.imread("image.png")
    # Grayscale the image.
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    # resize the images and invert it (black background)
    #gray = cv2.resize(255-gray, (28, 28))

    (thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # # save the processed images
    cv2.imwrite("image_Test.png", gray)

    #cv2.imshow('image', gray)

    # with open('testImage.png', 'wb+') as f:
    #     f.write(imgdata)

    # Read RGB image and convert to grayscale E.g single channel (L)
    # Using the Pillow (PIL) library which is a Python Imaging Library by Fredrik Lundh and Contributors.
    # https://pillow.readthedocs.io/en/stable/
    #img = Image.open('testImage.png').convert('L')
    #print(img)

    # The problem I initally had was that I was using a black pen in the HTML so when convert the 
    # image to greyscale there would be no distinct values (E.g All 0's) To solve this I have used a strong red pen which solves the problem.
    
    # reshape image data for use in neural network
    # Creates a two dimensional array of the 784 bytes in the image (28 x 28)
    #imgGray = ~np.array(img).reshape(1, 784).astype(np.uint8) / 255
    #img = np.ndarray.flatten(np.array(img).reshape(1, 784).astype(np.uint8) / 255.0)
    imgGray = np.ndarray.flatten(np.array(gray)).reshape(1, 784).astype("float32") / 255

    #grayArray = (np.array(grayImage).reshape(1, 28, 28, 1))
    
    #print(img)

    counter = 0

    #Print Contents
    for i in imgGray[0]:
        #print(i,end=" ")
        if i > 0:
           print(".",end="")
        else:
           print("0",end="")
        counter +=1

        if counter == 28:
            print("\n")
            counter = 0

    # Testing - print array of predicted result. £.g [[1.9111006e-02 1.0649475e-02 1.9441145e-02...]]
    # The highest value is the predicted result.
    print("\nResults:", model.predict(imgGray))

    # Return the largest value in the returned array as a String. 
    # From testing the model.predict it would return an array of possibilities. The highest value would be the right answer.
    # To get the largest value I looked up a numpy methods and found argmax() to achieve this.
    # https://kite.com/python/examples/5750/numpy-find-the-index-of-the-largest-element-of-an-array
    return str(model.predict(imgGray).argmax())

# I encountered the error below when trying to call model.predict()
# "Tensor Tensor("dense_3/Softmax:0", shape=(?, 10), dtype=float32) is not an element of this graph."
# From research it seems to be a common problem and one fix I found is to run the script through the main
# setting the the threaded attribute to false.
# https://github.com/jrosebr1/simple-keras-rest-api/issues/5
if __name__ == "__main__":
    app.run(debug = False, threaded = False)