import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

table = pd.read_csv("AllCountries.csv")
# print(table)

# print(table.shape)
# print(table.dtypes)

# firstFive = table.head(5)
# print(firstFive)
# tail(5)

# Gives basic Analysis on Columns automatically !!
# Statistical Summary
# print(table.describe())

# Write a Program to find all countries with Land Area greater than 2000

table1 = table.loc[:, ["Country", "LandArea"]]
print(table1)

for row in table1.itertuples():
    if row[2] > 2000:
        print(row)

# Compare GDP of Top 10 Richest Countries

