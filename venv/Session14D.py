import numpy as np
arr = np.genfromtxt("CityTemps.csv",delimiter=",")
print(arr)

print(arr[1][0])

np.savetxt("CityTemps1.csv", arr, delimiter=",")
print("==File Created==")

# Assignment
# Read File 1 create numpy array
# Flip Elements Horzontally and Vertically and save outputs in 2 different files


# Create a numpy array with all 1's and 0's
# Extract data from Diagnols from up to down !!
# Convert to decimal and add them !!
# Convert to decimal yourself !!
