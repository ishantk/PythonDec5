# Function of Single Expression
def areaOfCircle(radius=2.2):
    area = 3.14 * radius * radius
    return area

result = areaOfCircle(3.3)
print("Area of Circle with radius 3.3 is",result)
print("Area of Circle with radius 4.4 is",areaOfCircle(4.4))
print("Area of Circle with radius  is",areaOfCircle())
print("Area of Circle with radius  is",areaOfCircle(radius=5.5))

print(areaOfCircle)

# Reference Copy
area = areaOfCircle

print(area)

print("Area of Circle with radius 7.7 is",area(7.7))

# Lambda : is a function like a regular function
#          but, it is a single expression function
#          lambda function has no name -> Anonymous Function

lm = lambda radius : 3.14 * radius * radius
print(lm(3.3))
print(lm(12))
