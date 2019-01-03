import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("FullData.csv")
# print(df)
print(df.head(5))
# print(df.tail(5))

"""
plt.figure(figsize=(30, 20))
# plt.savefig("Analysis1.png")
sns.countplot(y=df.Nationality, palette="Set2")
plt.show()
"""
# plt.figure(figsize=(15, 10))
# sns.countplot(x="Age", data=df)
# plt.show()

# Try to find a GoalKeeper who is strong enough to stop the shots

# print()

# print(df["GK_Handling"])
# print(df.GK_Handling)

# Lets take some weights
w1 = 0.5
w2 = 1
w3 = 1.5
w4 = 2
w5 = 3

df["GK_Shot_Stopper"] = (w1*df.GK_Positioning + w2*df.GK_Diving + w3*df.GK_Kicking + w4*df.GK_Handling + w5*df.GK_Reflexes)

print(df["GK_Shot_Stopper"])

sortedDF = df.sort_values("GK_Shot_Stopper")

print(sortedDF)

top5 = sortedDF.tail(5)

print(top5)

X = np.array(list(top5["Name"]))
Y = np.array(list(top5["GK_Shot_Stopper"]))

sns.barplot(X, Y, palette="colorblind")
plt.ylabel("Shot Stopper Score")

plt.show()

