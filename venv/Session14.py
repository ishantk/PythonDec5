# Importing numpy library
import numpy as np

# List
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(type(numbers))

print()

# arr1 = np.array([10, 20, 30, 40, 50])
arr1 = np.array({10, 20, 30, 40, 50, 30, 10})
print(arr1)
print(type(arr1))  # -> ndarray which stands for n dimensional array

print()

arr2 = np.array((10, 20, 30, 40, 50))
print(arr2)
print(type(arr2))

print()

arr3 = np.array(numbers)
print(arr3)
print(type(arr3))

employees = {"eid": 101, "name": "John", "age": 30}
arr4 = np.array(employees)
print(arr4)
print(type(arr4))

print()

# 2-D Array -> 3 Rows and 3 Cols
arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# arr5 = np.array([[1, 2, 3, 1], [4, 5, 6], [7, 8, 9]])
print(arr5)
print(arr5.shape)
print(type(arr5))

# 3-D Array
arr6 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr6)
print(type(arr6))
print(arr6.shape)
