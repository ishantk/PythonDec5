import numpy as np

# Read File and Create a numpy Array
arr = np.loadtxt("data.txt")
print(arr)
print(arr.shape)
print(arr.ndim)

# Write Data in File from numpy array

arr1 = np.arange(10, 200, 10)
print(arr1)
np.savetxt("data1.txt", arr1)
print("==File Created==")