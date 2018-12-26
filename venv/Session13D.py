import json

employees = {"eid":101, "ename":"John Watson", "age":30, "salary":50000}
print(employees)
print(type(employees))

jsonData = json.dumps(employees)
print(jsonData)
print(type(jsonData))

emps = json.loads(jsonData)
print(emps)
print(type(emps))

