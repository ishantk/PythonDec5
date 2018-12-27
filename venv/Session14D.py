import numpy as np
arr = np.genfromtxt("CityTemps.csv",delimiter=",")
print(arr)

print(arr[1][0])

np.savetxt("CityTemps1.csv", arr, delimiter=",")
print("==File Created==")

# Assignment
# Read File 1 create numpy array
# Flip Elements Horzontally and Vertically and save outputs in 2 different files
