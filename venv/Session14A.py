import numpy as np

arr1 = np.arange(10, 51)
print(arr1)
print(type(arr1))

print()

arr2 = np.arange(10, 51, 3)
print(arr2)

print()

arr3 = np.zeros((3, 3))
print(arr3)

arr4 = np.linspace(0, 20, 6)
print(arr4)

numbers = [11, 22, 33, 44, 55]
arr5 = np.asarray(numbers)
print(arr5)

print()

arr6 = np.zeros(8)
print(arr6)
print(arr6.shape)

arr7 = arr6.reshape(2, 2, 2)
print(arr7)
print(arr7.shape)

arr8 = arr7.ravel()
print(arr8)