# Function with inputs having default values

# def addNumbers(a=10, b): error
# def addNumbers(a, b=10): ok
def addNumbers(a=10, b=10):
    c = a+b
    print(c)

addNumbers()
addNumbers(11)
addNumbers(11,11)

def addNumbers1(a, b=12, c=30): # a : non default, b and c : default
    z = a+b+c
    print(z)

addNumbers1(10)