#### SCI-KIT ####

import numpy as np
from sklearn.linear_model import LinearRegression


regression = LinearRegression()

X = np.array([[1, 2, 3, 4, 5]])

Y = np.array([[2.8, 3.4, 4, 4.6, 5.2]])


reg = regression.fit(X, Y)
print(reg.score)
mse = reg.score(X, Y)
print(mse)