# Adapted from: https://docs.python.org/3/library/gzip.html

import keras as kr
import sklearn.preprocessing as pre # For encoding categorical variables.
import gzip
import numpy as np
import matplotlib.pyplot as plt

# Test code to learn more about the MNIST dataset, how it works etc.
# ======================

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

# Test code to train neural network, this will be then later converted to a Jupyter Notebook.
# =========================

# Start a neural network, building it by layers.
model = kr.models.Sequential()

# Add a hidden layer with 1000 neurons and an input layer with 784.
model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
model.add(kr.layers.Dense(units=400, activation='relu')) # relu = Rectified Linear Unit.
# Add a three neuron output layer.
model.add(kr.layers.Dense(units=10, activation='softmax'))

# Build the graph.
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

with gzip.open('MNIST_Images/train-images-idx3-ubyte.gz', 'rb') as f:
    train_img = f.read()

with gzip.open('MNIST_Images/train-labels-idx1-ubyte.gz', 'rb') as f:
    train_lbl = f.read()

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

model.fit(inputs, outputs, epochs=2, batch_size=100)


