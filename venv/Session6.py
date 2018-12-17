# OOPS | Object Oriented Programming Structure
# Object and Class

"""
    Real World:
    Object is anything which you can see, touch, feel.
    eg: chair, table, dog, human, apple

    Class is a representation(drawing) how an object will look like

    Analogy to Objects in CS:
        eg: Geometry Box
            1. Homogeneous
            2. Hetrogeneous

    Computer Science:
    Object is a Storage Container | Its a Box
    Class is a representation(textual description) how an object will look like

    Amazon, Uber, Myntra
    User -> Registration/Login
        name
        phone
        email
        age
        gender
        address
        .
        ..
        ...

    Object and Dictionary are very much similar
    Dictionary is Key and Value
    Object is attribute and Value

    Identification of Object is done when we see lot of details getting associated with some single entity
"""

# Textual Representation how an Object will look like. We also say its Structure for an Object
# Whatever we are doing in class will have something to do with object
# class User:
#     pass

class User:

    # Constructor : Gets executed when an Object is created in memory
    def __init__(self):
        print("Constructor Executed")

# Object Construction Statement
# u1 is a reference Variable point to Object
u1 = User()  # User() -> Execution of Constructor
u2 = User()

u3 = u1      # Reference Copy

print(u1)
print(u2)

print(hex(id(u1)))
print(hex(id(u2)))

# Write Operation in Object
u1.name = "John"
u1.phone = "+91 99999 88888"
u3.email = "john@example.com"
u3.age = 30
u1.gender = "Male"
u3.address = "Redwood Shores"

u2.name = "Fionna"
u2.phone = "+91 99999 77777"
u2.email = "fionna@example.com"
u2.age = 32
u2.gender = "Female"
u2.address = "Country Homes"
u2.vehicle = 3

# Update Operation
u1.name = "John Watson"
u2.name = "Fionna Flynn"

u3.age = 45

# Delete Operation
# del u2.vehicle # Removing an Attribute
# del u2       # Removing an Entire Object

# Read Operation
print(u1.__dict__)
print(u2.__dict__)
print(u3.__dict__)

# Custom Read
print(u1.name," lives in ",u1.address)
print(u2.name," can be called on ",u2.phone)


print("{} lives in {}".format(u1.name,u1.address))
print("{} can be called on {}".format(u2.name,u2.phone))
