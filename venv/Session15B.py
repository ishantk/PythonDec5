import numpy as np
import pandas as pd

arr = np.arange(1, 21)
emp = {"eid": 101, "name": "john", "salary": 30000}

employees = [{"eid": 101, "name": "john", "salary": 30000},
             {"eid": 201, "name": "jennie", "salary": 40000},
             {"eid": 301, "name": "jim", "salary": 50000, "address":"Redwood Shores"}]

# print(employees)

# Construct DataFrame
# df1 = pd.DataFrame([arr, ])
# df2 = pd.DataFrame([emp, ])

# print(df1)
# print(df2)

table = pd.DataFrame(employees)
print(table)
print(type(table))

print(table["eid"])
print(table["eid"][2])
