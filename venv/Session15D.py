import pandas as pd

table = pd.read_csv("CityTemps.csv")
print(table)
print(type(table))

print()
print(table["Year"])

print()
print(table.iloc[1])

print(table.iloc[:5])

# table = pd.read_excel()
# table = pd.read_json()


# Download Data Sets from Kaggle or github and read them using Pandas !!