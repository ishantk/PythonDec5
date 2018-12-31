import pandas as pd
import numpy as np

numbers = [10, 20, 30, 40, 50]
print(numbers)

print()

arr = np.arange(10, 21)
print(arr)

print()

# Passing List
s1 = pd.Series(numbers)

# Passing numpy array
s2 = pd.Series(arr)

print(s1)
print(s2)

# Passing Dictionary
ages = {"john": 30, "jennie": 28, "jim": 33, "jack": 40, "joe": 50, "john": 33}
s3 = pd.Series(ages)

print(s3)


print(s1[0])
print(s2[1])
print(s3["john"])

# Slicing on Series
print(s1[2:])
print(s3["jim":])

print(s1[:3])
print(s1[1:3])

