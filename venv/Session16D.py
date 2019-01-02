import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(100)
Y = np.random.randn(100)

X1 = np.random.randn(100)
Y1 = np.random.randn(100)

plt.scatter(X, Y)
plt.scatter(X1, Y1)


plt.show()