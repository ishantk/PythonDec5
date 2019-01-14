from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

# Software Engnrs
X1 = [1, 2, 3, 4, 5]                        # Exp
Y1 = [20000, 27000, 33000, 35000, 40000]    # Salaries

# Accountants
X2 = [1, 2, 3, 4, 5]                        # Exp
Y2 = [15000, 22000, 27000, 31000, 35000]    # Salaries


plt.scatter(X1, Y1, c='r', label="SE")
plt.scatter(X2, Y2, c='g', label="ACC")
plt.xlabel("X")
plt.xlabel("Y")
plt.legend(loc=1)
# plt.show()

# SVM in Action !!
# You can use even real data set like iris or any other !!
X, Y = make_blobs(n_samples=40, centers=2, random_state=20)
print(X)
print(Y)

clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, Y)

# Try to use this instead of DecisionTree
# clf.predict()