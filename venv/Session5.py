# string is a built in type and will have various built in functions
# strings are IMMUTABLE
name1 = "John Watson"
print("name1 is",name1)
print(type(name1))
name2 = name1.upper()
print("name1 now is",name1)
print("name2 is",name2)

#del name1

str1 = "Hello World"
str2 = "Hello World"

# if str1 == str2:
if str1 is str2:
    print("Strings are Equal")
else:
    print("Strings are Not Equal")

names = "John, Jennie, Jim, Jack, Joe"
size = len(names)
print(size)
print(names[0])
print(names[size-1])

print(names[-3])
# print(names[28]) # Error at Runtime : IndexError

for i in range(-1, -(len(names)+1), -1):
    print (names[i], end='')

print()
newNames = names.split(",")
print(type(newNames))

for name in newNames:
    print(name.strip())

print("====Slicing====")

# names = "John, Jennie, Jim, Jack, Joe"
# Slicing
print(names[0:3])
print(names[3:6])
print(names[3:])
print(names[:5])

print(names[-4:])
print(names[:-3])

modifiedNames = names.replace('J','K')
print(names)
print(modifiedNames)

email = "john@example.com"
password = "john123"

fileName = "somesong.mp3"

if fileName.endswith(".mp3"):
    print("This is a Song !!")

# if fileName.startswith("...")

if email.__contains__("@") and email.__contains__(".com"):
    print("A Valid Email !!")

if len(password) > 6:
    print("Valid Password")

# s1 and s2 are reference variables
s1 = "Jennie"
s2 = "Jennie"

#....

s2 = "Jack"

print(hex(id(s1)))
print(hex(id(s2)))

# Explore Built In Functions
