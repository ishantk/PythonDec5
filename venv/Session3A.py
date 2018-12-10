#Function : Block of Statements which gets executed in a sequence
#           Function can be executed again and again
# 1. Definition
# 2. Inputs
# 3. Acknowledgement
# Syntax: def nameOfFun(inputs):
#               ....
#               return -> to acknowledge if we want

def addNumbers():
    a = 10
    b = 20
    c = a+b
    print(c)

# Overwriting the definition of previous addNumbers
def addNumbers():
    a = 100
    b = 200
    c = a+b
    print(c)

# Overwriting the definition of previous addNumbers and this time we are giving inputs
def addNumbers(x, y):
    a = x
    b = y
    c = a+b
    print(c)


addNumbers(10,20)
addNumbers(11,13)
addNumbers(14,17)
addNumbers(12,12)
addNumbers(10,10)

print(type(addNumbers))
print(hex(id(addNumbers)))
print(addNumbers)

hello = addNumbers # Reference Copy
print("**************")
print(hello)
print(addNumbers)
print("**************")

hello(100,111)

def areaOfCircle(radius):
    a = 3.14 * radius * radius
    return a # Acknowledgement

result = areaOfCircle(2.2)
print(result)
print(areaOfCircle(3.75))

area = areaOfCircle
print(area(3.33))
