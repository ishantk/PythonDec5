#### SCI-KIT ####

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets

# data = datasets.load_boston()
# irisData = datasets.load_iris()


data = pd.read_csv("BostonHousing.csv")
print(data)

X = data.iloc[:,0:13]
Y = data["medv"]

print(X)
print(Y)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=5)

model = LinearRegression()
model.fit(x_train, y_train)

pred_y = model.predict(x_test)
print(pred_y)


# Plot the datasets on graph !!
