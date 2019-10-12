# Adapted from: https://docs.python.org/3/library/gzip.html

import gzip

# Open the MNIST dataset of 60000 training images.
with gzip.open('MNIST_Images/t10k-images-idx3-ubyte.gz', 'rb') as f:
    file_content = f.read()

print(type(file_content))

# Print out the first four bytes.
# b'\x00\x00\x08\x03' is the output which correlates with the MNIST website results.
print(file_content[0:4])

# Adapted from: https://stackoverflow.com/questions/51220161/how-to-convert-from-bytes-to-int
# Convert bytes to a 32 bit integer using big-endian and little-endian.
print(int.from_bytes(file_content[0:4], byteorder='big')) #2051
print(int.from_bytes(file_content[0:4], byteorder='little')) #50855936

