import numpy as np

# Defining the input array
A = np.array([[0, 1, 2], [3, 4, 5]])

# Computing the sum of the diagonal elements
diag_sum = np.trace(A)

# Printing the result
print("Sum of diagonal elements:", diag_sum)