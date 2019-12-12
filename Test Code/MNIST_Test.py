# Imports
import gzip 
import numpy as np
import matplotlib.pyplot as plt

# Test code to learn more about the MNIST dataset, how it works etc.
# ======================

# Adapted from: https://docs.python.org/3/library/gzip.html
# Open the MNIST dataset of 10000 testing images.
with gzip.open('../Jupyter Notebook/MNIST_Images/t10k-images-idx3-ubyte.gz', 'rb') as f:
    file_content = f.read()

# Open the label dataset like before.
with gzip.open('../Jupyter Notebook/MNIST_Images/t10k-labels-idx1-ubyte.gz', 'rb') as f:
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