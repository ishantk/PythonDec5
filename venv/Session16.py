import matplotlib.pyplot as plt

# X Coordinates are Indexes
# Y = f(X)
"""
Y = [5, 7, 9, 11, 13]
plt.plot(Y)
plt.show()
"""

X = list(range(10))
Y = [n**2 for n in X]

print(X)
print(Y)

# plt.plot(X, Y)

Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]


plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

plt.legend()

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")\

plt.title("Polymomial Graphs")

plt.grid(True)

# plt.savefig("Polynomial.png")

plt.xlim(0, 10)
plt.ylim(0, 1000)

plt.show()
