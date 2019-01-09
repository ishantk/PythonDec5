"""
    Regression

    Independent
    X = [1,2,3,4,5]

    Dependent
    Y = [2,4,5,4,5]

        X   Y   X-MX    Y-MY    sq(X-MX)    (X-MX)(Y-MY)
        ------------------------------------------------
        1   2   -2      -2      4           4
        2   4   -1      0       1           0
        3   5    0      1       0           0
        4   4    1      0       1           0
        5   5    2      1       4           2
        ------------------------------------------------
Mean    3   4
Slope of a Line : Y = b0 + b1X
We need to find b0 (Interceptor) and b1 (Slope)
b1 = Sum[(X-MX)(Y-MY)] / Sum[sq(X-MX)]
b1 = 6/10
b1 = 0.6

Y = b0 + 0.6X

We need to find b0 now !! Put Mean of X and Y in equation of line
4 = b0 + 3 * 0.6
b0 = 2.2

Equation of Line : Will be used for Prediction
Y = 2.2 + 0.6X

We can use above equation to predict. But before we do that we must check for errors !!

        X   Y   Y'  X-MX    Y-MY    Y'-MY   sq(Y'-MY)
        ------------------------------------------------
        1   2   2.8    -2     -2    -1.2    1.44
        2   4   3.4    -1      0    -0.6    0.36
        3   5   4       0      1       0       0
        4   4   4.6     1      0     0.6    0.36
        5   5   5.2     2      1     1.2    1.44
        ------------------------------------------------
Mean    3   4


Mean Square Error | MSE  = sum(sq(Y'-MY)) /  sum((X-MX)(Y-MY))
                    MSE = 3.6/6 = 0.6

                    MSE between 0 and 1 is accepted !!

                 => Y = 2.2 + 0.6X this fits in for predictions


"""

import matplotlib.pyplot as plt
from scipy import stats

X = [1,2,3,4,5]
Y = [2,4,5,4,5]

data = stats.linregress(X, Y)

b0 = data[1]
b1 = data[0]

Y1 = []
for x in X:
    y = b0 + b1*x
    Y1.append(y)

print(Y1)

plt.xlabel("Independent")
plt.ylabel("Dependent")

plt.grid(True)
# plt.plot(X, Y, "ro")
plt.plot(X, Y, "o", X, Y1)

plt.show()

