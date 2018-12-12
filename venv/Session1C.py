# Multi Value Container
a = 10
print("a is",a," and type of a is",type(a))

print("************")

# TUPLE
# Homogeneous
a = 10, 20, 30, 40, 50
print("a is",a," and type of a is",type(a))

# Hetrogeneous
b = 10, 'A', 2.2, "Wow"
print("b is",b," and type of b is",type(b))

# LIST
c = [10,20,30,40,50]
print("c is",c," and type of c is",type(c))

c = [10, 'A', 2.2, "Wow"]
print("c is",c," and type of c is",type(c))


d = (10,20,30,40,50)
print("d is",d," and type of d is",type(d))

d = (10, 'A', 2.2, "Wow")
print("d is",d," and type of d is",type(d))

# SET
e = {10,20,30,40,50}
print("e is",e," and type of e is",type(e))

e = {10, 'A', 2.2, "Wow"}
print("e is",e," and type of e is",type(e))

print("**********")

# DICTIONARY
students = {101:"John",201:"Jennie",301:"Jack",401:"Jim",501:"Joe"}
print(students)
print(type(students))
print(students[101])
