import numpy as np
random_vector = np.random.randint(low=1, high=21, size=15)
array_3x5 = random_vector.reshape(3, 5)
print(array_3x5)
print(array_3x5.shape)
array_3x5[np.arange(3), array_3x5.argmax(axis=1)] = 0
print(array_3x5)
