# Emerging Technologies Project

Name: Matthew Sloyan
Student ID: G00348036

# Project statement
**Model:** Create, document, and train a model that recognises hand-written digits using the MNIST dataset. This should be done using the keras and jupyter Python.

**Application:** Create a web application that allows a user to draw a digit using their mouse or touchscreen device. The drawing should then be then be submitted for recognition to the model you have trained above. This should be done using the flask Python package.

# Platforms
Coded and tested on a Linux Ubuntu 18.04 LTS virtual machine using VMware.

# How to run
* First, clone the repository using the following command `git clone https://github.com/MatthewSloyan/4th-Year-MNIST-Image-Recognition-Web-Application.git` 
* Traverse using the command line to the folder you have cloned using the cd command.
* From the command line run the following command. `will be updated`

# User Guide
Below you’ll find a basic guide to the user interface, in the “How it works” section is a description of how this works in the code behind.

Will be updated.

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
I wanted to learn more about how Keras works in the background and how neural networks work in general. An interesting link I found was in relation to the theory of neural networks and machine learning based off the MNIST dataset, it doesn't go into any details of how to code a solution but the insights and explanations where very useful for developing my own model. [Neural networks and deep learning][1] To learn more about Keras I also looked up some of the possible activation functions (linear, relu and softmax), loss functions (categorical_crossentropy) and optimizers (adam) that could be used. An outline of how each of these works and why I chose them can be found in the Jupyter Notebook in this repository. 

With this knowledge I began to create a model using Keras, I used help from the official documentation and the videos on Moodle which gave me a good basis, but my own research really solidified how it all works. I set up the input layer with 784 inputs which is each pixel (28 x 28). I then set up the hidden layers and finally an output layer of 10 neurons which will represents the numbers 0-9. Using this model, I reshaped the training data into the a two-dimensional numpy array consisting of 784 indexes. With this the data could be fed in the neural network and trained. From basic tests the results were promising accuracy of 94% but I will try and improve this with time.

#### Week of 20-10-19 to 27-10-19
With the model trained and tested, I began to move the code to a Jupyter Notebook. I also did some extra research into how I could improve the training accuracy. By increasing the epochs and tweaking the model I got the accuracy to 96% which still can be improved. With time I will also add more to the notebook as I learn more. I also researched how the model could possibly be saved so that retraining won't be required every time it's run, this will be useful for the flask application. To achieve this, I found the load_model from the Keras documentation which saves a .h5 binary file.

#### Week of 27-10-19 to 3-11-19
The next step was to pull it all together and create the Flask web application for the project. To begin I researched how Flask works and what it does in the background. I then created a basic Flask web application with a basic home page. On this page is a small 28 x 28 canvas which the user can draw a little number. I am currently using this for testing purposes and will scale the image accordingly once I get it working correctly. 

Once I set up the canvas, I needed a way to send the drawing to the Flask server. To achieve this, I felt an asynchronous xhttp request using AJAX would work best as it would return the result and update the webpage when ready. I tried sending the data but I couldn't access it on the server, so I decided to parse it to a base64 binary string, wrap it in JSON, send this JSON to the server and then decode this string on the server into a local file. The local file is then converted to a single channel image (Grayscale) or else it would contain 4 arrays (RGBA). This wouldn't work with my model. With it converted it is passed into the predict method and the index of the largest result is returned which is the predicted number. It currently only ever displays 5 so some testing and fixing will be required.

## References 
* http://neuralnetworksanddeeplearning.com/chap1.html

[1]: http://neuralnetworksanddeeplearning.com/chap1.html
