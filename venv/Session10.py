# File Handling !!
# Persistance : To Save data permanently

# open -> 1st input is file name
#      -> mode
# file = open("Query.py","r")
# file = open("/Users/ishantkumar/Downloads/mystudents.csv","r")
# file = open("/Users/ishantkumar/Downloads/data.xml","r")
# file = open("/Users/ishantkumar/Downloads/pic.jpg","r") err -> how to solve this error !!

file = open("/Users/ishantkumar/Downloads/mystudents.csv","r")
print(type(file))

"""
# Read the File
fileContents = file.read() # Read all the file contents
print(fileContents)

# Once file is read, it cannot be re-read
fileContents = file.read()
print(fileContents)
"""

"""
line = file.readline() # read line by line
print(line)

line = file.readline()
print(line)

line = file.readline()
print(line)

"""

data = file.read(15)
print(data)

# data = file.read()
# print(data)

line = file.readline()
print(line)

print("Is File Closed ?",file.closed)

file.close()

print("Is File Closed Now ?",file.closed)

# Assignment : Read a python file and find all the objects in it
#              Make a list of objects alongwith count

#              Read an Image File
#              1. Horizontal Flip
#              2. GreyScale