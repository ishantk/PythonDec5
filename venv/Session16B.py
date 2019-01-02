import numpy as np
import matplotlib.pyplot as plt

A = [1, 2, 3]
B = [10, 20, 30]

# plt.bar(A, B)
# plt.show()

sales = {"2015": 50, "2016": 120, "2017": 30, "2018": 90}
# plt.bar(0, sales["2015"])
# plt.bar(1, sales["2016"])
# plt.bar(2, sales["2017"])
# plt.bar(3, sales["2018"])

# Iterating in a Dictionary
for i, key in enumerate(sales):
    # print(i, key)
    plt.bar(i, sales[key])

X = np.arange(len(sales))
print(X)

plt.xticks(X, sales.keys())

plt.show()
