import matplotlib.pyplot as plt

X = list(range(6))

Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

# plt.plot(X, Y1, "y")
# plt.plot(X, Y2, "m")
# plt.plot(X, Y3, "b")

# plt.plot(X, Y1, "--")
# plt.plot(X, Y2, "-.")
# plt.plot(X, Y3, ":")

plt.plot(X, Y1, "o")
plt.plot(X, Y2, "^")
plt.plot(X, Y3, "D")

plt.show()

# Explore : https://seaborn.pydata.org/tutorial/relational.html