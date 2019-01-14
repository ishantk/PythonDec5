import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB

# Feature List
X = np.array([[100, 70], [120, 80], [130, 90], [150, 100], [800, 700], [1000, 900], [1200, 1100], [1500, 1400]])
# Label List
Y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

labels = ["Bike", "Car"]
model = GaussianNB()
# model = BernoulliNB()
# model = MultinomialNB()

model.fit(X, Y)

toBePredicted = [1117,750]

lbl = model.predict([toBePredicted])
print(labels[lbl[0]])