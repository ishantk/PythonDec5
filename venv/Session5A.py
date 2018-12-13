# List of Strings : homogeneous
# MUTABLE
names = ["John","Jennie","Jim","Jack","Joe"]

# List of Numbers : homogeneous
numbers = [10, 20, 30, 40, 50]

# List hetrogeneous
myList = [10, 2.2, "Hello", "Hi"]

print(len(names))
print(len(numbers))
print(len(myList))

print(names[0])
print(numbers[1])
print(myList[2])

# names = ["John","Jennie","Jim","Jack","Joe"]
print(names[2:])
print(names[2:4])

print(names[:-2])
print(names[-2:])
print(names[-4:-2])

for name in names:
    print(name)

names.append("Sia")
names.append("Kim")
names.append("Fionna")

print(names)

names.remove("Sia")

print(names)

# names.clear()
# print(names)

newNames = ["George","Harry","Bob"]

names.extend(newNames)  #-> append data of list in a list
# names.append(newNames) -> creates list in a list

print(names)
print(newNames)

# List
punjabStatePopulation = [1234, 3456, 6789, 1245, 6789]
gujratStatePopulation = [4567, 7653, 8987, 4567, 3322]

# List of Lists
indiaPopulation = [[1234, 3456, 6789, 1245, 6789],[4567, 7653, 8987, 4567, 3322]]

# Which state is more populated ?

#List : stores elements using indexing(0 to n-1) Technique
ages1 = [10, 10, 12, 13, 21, 54, 21, 12]
print(ages1)
print(type(ages1))

#Set : stores elements using hashing(hashCode) Technique
ages2 = {10, 10, 12, 13, 21, 54, 21, 12}
print(ages2)
print(type(ages2))


#Tuple : stores elements using indexing(0 to n-1) Technique | IMMUTABLE
ages3 = (10, 10, 12, 13, 21, 54, 21, 12)
print(ages3)
print(type(ages3))


ages1.append(88)
ages2.add(77)

print(ages1)
print(ages2)

for x in ages3:
    print(x,end='*')

print()
print("----")
print()
for i in range(0,len(ages3)):
    print(ages3[i],end='-')