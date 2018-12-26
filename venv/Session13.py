# Built In Modules of Python

import os

"""
path = os.getcwd()

print("CWD:", path)

os.chdir("/Users/ishantkumar/Downloads")

path = os.getcwd()
print("CWD Now is:", path)

# os.mkdir("/Users/ishantkumar/Downloads/PythonPrograms")
# print("==Directory Created==")

# os.rmdir("/Users/ishantkumar/Downloads/PythonPrograms")
"""

print(os.name)
print(os.getlogin())
print(os.getppid())

path = os.path.join("/Users/ishantkumar/Downloads","PythonPrograms")
print(path)

newPath = os.path.split(path)
print(newPath)

newPath = os.path.split(os.getcwd())
print(newPath)

print(os.path.exists("/Users/ishantkumar/Downloads/PythonPrograms"))
print(os.path.isdir("/Users/ishantkumar/Downloads/PythonPrograms"))
print(os.path.isfile("/Users/ishantkumar/Downloads/PythonPrograms"))

files = os.walk("/Users/ishantkumar/Downloads/LambdaExpressions")
allFiles = list(files)
print(type(files))
print(type(allFiles))

print("*****************")
for f in allFiles:
    print(f)

print("*****************")

# Assignment : Create a File Explorer App

