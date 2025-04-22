# used for numerical computations
# working with large arrays and matrices


# Install pandas pip install numpy

# Importing numpy library
import numpy as np

# Create a 1D array
arr_1 = np.array([10,11,12,13,14,15,16,17,18,19,20,
                  21,22,23,24,25,26,27,28,29,30,
                  31,32,33,34,35,36,37,38,39,40,
                  41,42,43,44,45,46,47,48,49,50])
print(arr_1)

# perform arithmetic operations

print("Maximum Value:", np.max(arr_1))

print("Minimum Value:", np.min(arr_1))
print("Array * 2:", arr_1 * 3)
