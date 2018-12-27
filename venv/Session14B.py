import numpy as np

arr = np.arange(11, 99, 7)
print(arr)

# Access Element using index
print(arr[1])
print(arr[-1])

# Slicing
print(arr[3:])
print(arr[:5])

print(arr[3:5])

slices = slice(1, 10, 2)    # -> 1, 3, 5, 7, 9
print(arr[slices])


arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2D[0][1])

print(arr2D[0:2, 0:2])

print(arr2D.shape)
print(arr2D.ndim)
print(arr2D.itemsize)

