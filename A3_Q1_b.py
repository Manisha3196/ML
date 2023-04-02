import numpy as np

# Defining the input matrix
A = np.array([[3, -2], [1, 0]])

# Computing the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Printing the results
print("Eigenvalues: ", eigenvalues)
print("Right eigenvectors:\n", eigenvectors)
