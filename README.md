# Emerging Technologies Project

Name: Matthew Sloyan
Student ID: G00348036

# Project statement
**Model:** Create, document, and train a model that recognises hand-written digits using the MNIST dataset. This should be done using the keras and jupyter Python.

**Application:** Create a web application that allows a user to draw a digit using their mouse or touchscreen device. The drawing should then be then be submitted for recognition to the model you have trained above. This should be done using the flask Python package.

# Platforms
Coded and tested on a Linux Ubuntu 18.04 LTS virtual machine using VMware.

# How to run
**Download**
* First, clone the repository using the following command `git clone https://github.com/MatthewSloyan/4th-Year-MNIST-Image-Recognition-Web-Application.git` 
* Traverse using the command line to the folder you have cloned using the cd command.

**Jupyter Notebook**
cd into "Jupyter Notebook" folder and run `jupyter lab` or `jupyter notebook`. This will load the notebook in your default web browser.

**Flask web application**
cd into "flaskWebApplication" folder and run `python flaskWebApp.py` or `jupyter notebook`. This will run the web app in development mode, and will be available here `http://127.0.0.1:5000/`.

# User Guide
Below you’ll find a basic guide to the user interface, in the “How it works” section is a description of how this works in the code behind.

* Go to `http://127.0.0.1:5000/` when application is running (More information on how to do this in the "How to run" section).
* Using the mouse or touch screen begin to draw a digit between 0-9.
* To erase your work, select the "Change Mode" button to swap to erase mode, and again to swap back to draw mode.
* To change pen size, move the slider until at a suitable size.
* When you are happy with your digit, select the "Predict" button and wait for predicition.

# How it works
### Training the model
More information on how the model is trained can be found in the Jupyter Notebook. (More information on how to do this in the "How to run" section).

#### Flask Web Application

# Project Plan
* Week 1 - Initial research and setup of project.
* Week 2 - Reading the MNIST datasets and displaying the results.
* Week 3 - Training the MNIST dataset using Jupyter.
* Week 4 - Development of Flask web application.	
* Week 5 - Testing of web application with model.
* Week 6 - Adding finishing touches, tidying up code, and adding extras.

# Research & Development Diary

#### Start of Semester to 06-10-19
Each week I watched the various videos posted on Moodle and read into more about each topic such as Collatz, simple linear regression, deep learning and Newton's method. I also researched online more about Jupyter notebooks to get a grasp of how they work as we hadn’t any experience with it. This has really helped me with this project and will be a valuable skill going forward in my career. 

#### Week of 06-10-19 to 13-10-19
To help with the project I researched more about the MNIST dataset with help from the sources on Moodle. From this I found out more about how it's compressed and the possible ways to read it. With help from the video on Moodle I began coding a basic C program that reads in the bytes for the uncompressed training dataset of images. The results correlated with the sample data on the MNIST website, so it was a success. I then went on to code a similar program in Python from what I had learn which allowed me to display the results visually using matplotlib. As it's been read in correctly, I can move onto training the dataset using Keras.

#### Week of 13-10-19 to 20-10-19
I wanted to learn more about how Keras works in the background and how neural networks work in general. An interesting link I found was in relation to the theory of neural networks and machine learning based off the MNIST dataset, it doesn't go into any details of how to code a solution but the insights and explanations where very useful for developing my own model. [(Neural networks and deep learning).](http://neuralnetworksanddeeplearning.com/chap1.html) To learn more about Keras I also looked up some of the possible activation functions (linear, relu and softmax), loss functions (categorical_crossentropy) and optimizers (adam) that could be used. An outline of how each of these works and why I chose them can be found in the Jupyter Notebook in this repository. 

With this knowledge I began to create a model using Keras, I used help from the official documentation and the videos on Moodle which gave me a good basis, but my own research really solidified how it all works. I set up the input layer with 784 inputs which is each pixel (28 x 28). I then set up the hidden layers and finally an output layer of 10 neurons which will represents the numbers 0-9. Using this model, I reshaped the training data into the a two-dimensional numpy array consisting of 784 indexes. With this the data could be fed in the neural network and trained. From basic tests the results were promising accuracy of 94% but I will try and improve this with time.

#### Week of 20-10-19 to 27-10-19
With the model trained and tested, I began to move the code to a Jupyter Notebook. I also did some extra research into how I could improve the training accuracy. By increasing the epochs and tweaking the model I got the accuracy to 96% which still can be improved. With time I will also add more to the notebook as I learn more. I also researched how the model could possibly be saved so that retraining won't be required every time it's run, this will be useful for the flask application. To achieve this, I found the load_model from the Keras documentation which saves a .h5 binary file.

#### Week of 27-10-19 to 3-11-19
The next step was to pull it all together and create the Flask web application for the project. To begin I researched how Flask works and what it does in the background. I then created a basic Flask web application with a basic home page. On this page is a small 28 x 28 canvas which the user can draw a little number. I am currently using this for testing purposes and will scale the image accordingly once I get it working correctly. 

Once I set up the canvas, I needed a way to send the drawing to the Flask server. To achieve this, I felt an asynchronous xhttp request using AJAX would work best as it would return the result and update the webpage when ready. [(xhttp)](https://www.w3schools.com/xml/ajax_xmlhttprequest_send.asp) I tried sending the data but I couldn't access it on the server, so I decided to parse it to a base64 binary string, wrap it in JSON, send this JSON to the server and then decode this string on the server into a local file. [(Base64).](https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image) The local file is then converted to a single channel image (Grayscale) or else it would contain 4 arrays (RGBA). This wouldn't work with my model. With it converted it is passed into the predict method and the index of the largest result is returned which is the predicted number. It currently only ever displays 5 so some testing and fixing will be required.

#### Week of 3-11-19 to 10-11-19
As I was at a good state and ahead of the project plan, I took a break on this to focus on some of the other projects.

#### Week of 10-11-19 to 17-11-19
I wanted to fix the fact that the predicting would always be 5 no matter what which isn't ideal. From testing I found that when converting to grayscale the digit would be very faint which I figured was the first problem. To fix this I changed the pen colour to red which is a stronger RGB value so when converting to grayscale (Single channel) it is not lost. This increased the prediction success rate but it still wasn't perfect unfortunately.

#### Week of 17-11-19 to 24-11-19
I went back to how the model was being trained to find a solution, from this I noticed that the model contained digits with solid black digits whereas my prediction was using grey images. From my experience as I graphic designer I knew that you could make colours solid black or white by increasing the threshold of the image. I researched online how to do this which converted all the pixels above 127 to solid black. [(PIL Threshold)](https://www.geeksforgeeks.org/python-pil-image-point-method/). With this in place the prediction worked perfectly and could predict all 9 numbers if drawn correctly. 

The next step was to allow the canvas to be larger as it was currently 28 x 28 pixels which is quite small. To achieve this, I looked up the PIL documentation and found the resize method. [(PIL Resize)](https://pillow.readthedocs.io/en/3.1.x/reference/Image.html). From testing all the resampling methods, I found ANTIALIAS to work best which smoothens the edges of images. Some of the other methods can be found below.

* NEAREST - use nearest neighbour.
* BILINEAR - linear interpolation.
* BICUBIC - cubic spline interpolation
* LANCZOS - a high-quality downsampling filter

From further testing I wanted to increase the accuracy of the neural network, I first found that not inverting the image produced a higher accuracy when training and increased the speed of each epoch by 1 second. With this I updated the flask web application to handle this and modified the code to just use PIL while doing all the processing in memory. This also alleviated the need to save the image locally and reopened it like before during testing, which increased the response time.

#### Week of 24-11-19 to 1-12-19
As I have the Jupyter Notebook, and Flask Application running and working correctly. This week was for tidying up code, adding styling and improving the user experience of the web application. 

I began with moving the javascript and css code to separate static files which cleaned up the html file. I also added styling to the buttons, sliders etc which drasically improved the user experience.

#### Final Week

## References 
All references are also in code in respective areas.

**Project Research**
* Neural networks & Deep learning: http://neuralnetworksanddeeplearning.com/chap1.html
* MNIST: http://yann.lecun.com/exdb/mnist/
* Big/Small Endian: https://en.wikipedia.org/wiki/Endianness

**Training the Model**
* Seeding: https://keras.io/getting-started/faq/#how-can-i-obtain-reproducible-results-using-keras-during-development
https://stackoverflow.com/questions/42022950/
https://www.tensorflow.org/api_docs/python/tf/set_random_seed
* gzip: https://docs.python.org/3/library/gzip.html
* Big/small Endian: https://stackoverflow.com/questions/51220161/how-to-convert-from-bytes-to-int
* Activation Functions (Softmax etc): https://missinglink.ai/guides/neural-network-concepts/7-types-neural-network-activation-functions-right/
* Loss Functions: http://keras.io/losses/
* Optimizers: https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/
* Sklearn Preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing
* Sklearn Decomposition: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
* Label Preprocessing: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html
* Save Model: https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model
* Graph Display: https://towardsdatascience.com/a-simple-2d-cnn-for-mnist-digit-recognition-a998dbc1e79a

**Flask Web App**
Frontend:
* Bootstrap: https://getbootstrap.com/docs/4.3/getting-started/introduction/
* OnClick: https://www.w3schools.com/jsref/event_onclick.asp
* Range Slider: https://www.w3schools.com/howto/howto_js_rangeslider.asp
* Drawing: https://www.html5canvastutorials.com/labs/html5-canvas-paint-application/
* Canvas to base64: https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
* xhttp: https://www.w3schools.com/xml/ajax_xmlhttprequest_send.asp
* Clear Canvas: https://stackoverflow.com/questions/2142535/how-to-clear-the-canvas-for-redrawing
* Check if blank: https://stackoverflow.com/questions/17386707/how-to-check-if-a-canvas-is-blank
* Styling: https://stackoverflow.com/questions/9067892/how-to-align-two-elements-on-the-same-line-without-changing-html
https://www.fabriziovanmarciano.com/button-styles/
https://www.w3schools.com/howto/howto_js_rangeslider.asp

Backend (Flask): 
* Flask: https://www.palletsprojects.com/p/flask/
* Threading issue: https://github.com/jrosebr1/simple-keras-rest-api/issues/5
* PIL: https://pillow.readthedocs.io/en/stable/
* Base64: https://www.w3schools.com/python/ref_string_split.asp
https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image
* Threshold using PIL: https://www.geeksforgeeks.org/python-pil-image-point-method/
* Resize using PIL: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
* Prediction value: https://kite.com/python/examples/5750/numpy-find-the-index-of-the-largest-element-of-an-array
