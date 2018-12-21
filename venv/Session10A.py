file = open("/Users/ishantkumar/Downloads/data.xml","r")
data = file.readlines()
print(data)
print(type(data))
print(data[0])

for line in data:
    print(line)

# del data
file.close()