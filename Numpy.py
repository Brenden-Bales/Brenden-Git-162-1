import numpy as np

# Generate a random 2-dimensional array with dimensions 5x5
array_2d = np.random.randint(0, 9, size=(5, 5), dtype=int)

# Print the entire array
print("Random 2D Array:")
print(array_2d)
print()

# Print the number from the 2nd row, 3rd column
print("Number from the 2nd row, 3rd column:", array_2d[1, 2])
print()

# Print the sum of all the elements
print("Sum of all elements:", np.sum(array_2d))
print()

# Print the mean of each row
print("Mean of each row in the array:")
print(np.mean(array_2d, axis=1))
print()

# Print the maximum value in each column of the array
print("Maximum value in each column of the array:")
print(np.max(array_2d, axis=0))
