# https://keras.io/getting-started/faq/#how-can-i-obtain-reproducible-results-using-keras-during-development
# From our lecturer I found that it was best to seed the random weight generator to get reproducible results.
# As TensorFlow will automatically assign random weights on each run based on probibility.
# To achieve this I found documentation on the Keras website above, which I have adapted.
import numpy as np
import tensorflow as tf
import random as rn

# The below is necessary for starting Numpy and core Python generated random numbers in a well-defined initial state.
np.random.seed(42)
rn.seed(12345)

# Force TensorFlow to use single thread.
# Multiple threads are a potential source of non-reproducible results.
# For further details, see: https://stackoverflow.com/questions/42022950/
session_conf = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)

from keras import backend as K

# The below tf.set_random_seed() will make random number generation
# in the TensorFlow backend have a well-defined initial state.
# For further details, see: https://www.tensorflow.org/api_docs/python/tf/set_random_seed
tf.set_random_seed(1234)

sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)
K.set_session(sess)

# Additional Imports
import keras as kr
from keras.models import load_model
import sklearn.preprocessing as pre # For encoding categorical variables.
import gzip 
import matplotlib.pyplot as plt

# Test code to learn more about the MNIST dataset, how it works etc.
# ======================

# Adapted from: https://docs.python.org/3/library/gzip.html
# Open the MNIST dataset of 10000 testing images.
with gzip.open('MNIST_Images/t10k-images-idx3-ubyte.gz', 'rb') as f:
    file_content = f.read()

# Open the label dataset like before.
with gzip.open('MNIST_Images/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    labels = f.read()

# Get the label for a specific image (Expected result = 4)
print(int.from_bytes(labels[12:13], byteorder="big"))

# Print the file type of the dataset - bytes
print("File Type:", type(file_content))

# Print out the first four bytes.
# b'\x00\x00\x08\x03' is the output which correlates with the MNIST website results.
print(file_content[0:4])

# Adapted from: https://stackoverflow.com/questions/51220161/how-to-convert-from-bytes-to-int
# Convert bytes to a 32 bit integer using big-endian and little-endian.
print("Big-endian:", int.from_bytes(file_content[0:4], byteorder='big')) #2051
print("Little-endian:", int.from_bytes(file_content[0:4], byteorder='little')) #50855936

# Display a single image from the dataset
image = ~np.array(list(file_content[800:1584])).reshape(28,28).astype(np.uint8)

for x in image[0:28]:
    for y in image[0:28]:
        if y.any() > 127:
            print("0", end=" ")
        else: 
            print(".", end=" ")
    print()

# Display plot of image
plt.imshow(image, cmap='gray')
plt.show()

# Test code to train the model using a Keras neural network, this will be then later converted to a Jupyter Notebook.
# =========================

# Read in the training images (60000)
with gzip.open('MNIST_Images/train-images-idx3-ubyte.gz', 'rb') as f:
    train_img = f.read()

with gzip.open('MNIST_Images/train-labels-idx1-ubyte.gz', 'rb') as f:
    train_lbl = f.read()

# Start a neural network, building it by layers.
model = kr.models.Sequential()

# Add a hidden layer with 1000 neurons and an input layer with 784.
model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
model.add(kr.layers.Dense(units=400, activation='relu')) # relu = Rectified Linear Unit.
# Add a three neuron output layer.
model.add(kr.layers.Dense(units=10, activation='softmax'))

# Build the graph.
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Parse files into lists
# The bitwise operator ~ (tilde) is a complement operator. It takes one bit operand and returns its complement. If the operand is 1, it returns 0, and if it is 0, it returns 1
train_img = ~np.array(list(train_img[16:])).reshape(60000, 28, 28).astype(np.uint8) / 255.0
train_lbl =  np.array(list(train_lbl[ 8:])).astype(np.uint8)
inputs = train_img.reshape(60000, 784)

encoder = pre.LabelBinarizer()
encoder.fit(train_lbl)
outputs = encoder.transform(train_lbl)

print(train_lbl[0], outputs[0])

for i in range(10):
    print(i, encoder.transform([i]))

# https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model
# Rather than retraining the model again and again I wanted to be able to save and load it, so I researched and found a way to achieve this.
try:
    model = load_model('test_model.h5')
except:
    model.fit(inputs, outputs, epochs=2, batch_size=100)
    model.save('test_model.h5')

# Test code to test trained model above
# =========================

with gzip.open('MNIST_Images/t10k-images-idx3-ubyte.gz', 'rb') as f:
    test_img = f.read()

with gzip.open('MNIST_Images/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    test_lbl = f.read()

# Parse files into lists    
test_img = ~np.array(list(test_img[16:])).reshape(10000, 784).astype(np.uint8) / 255.0
test_lbl =  np.array(list(test_lbl[ 8:])).astype(np.uint8)

(encoder.inverse_transform(model.predict(test_img)) == test_lbl).sum()

# Predict image using model
model.predict(test_img[5:6])

plt.imshow(test_img[5].reshape(28, 28), cmap='gray')
plt.show()