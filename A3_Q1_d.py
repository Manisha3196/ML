import numpy as np

# Defining the input array
A = np.array([[1, 2], [3, 4], [5, 6]])

# Reshaping the array to a 2x3 shape without changing its data
B = A.reshape((2, 3))

# Printing the original and reshaped arrays
print("Original array:\n", A)
print("Reshaped array:\n", B)
