import pandas as pd

s1 = pd.Series([10000, 20000, 30000], index=["John", "Jim", "Jack"])
print(s1)

print()

s2 = pd.Series([13000, 25000, 38000, 40000], index=["John", "Jim", "Jack", "Joe"])
print(s2)

print()

s3 = pd.Series([15000, 27000, 40000, 45000], index=["John", "Jim", "Jack", "Joe"])
print(s3)

print()

# DataFrame Construction using Series

table = pd.DataFrame({"2016": s1, "2017": s2})
print(table)

print()

# Adding Series in DataFrame dynamically
table["2018"] = s3
print(table)

print()

# Read Series(Column) from DataFrame
print(table["2017"])

# Delete a Column
# del table["2017"]
# table.pop("2017")
# print(table)

# Work on Rows !!
rows = pd.DataFrame([[30000, 40000], [50000, 60000]], columns=["2014", "2015"])

table = table.append(rows, sort=True)

print(table)

table = table.drop("Joe")
print(table)

print()

print(table.loc["John"])
print(table.iloc[1])

