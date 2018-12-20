# object is a built in class
# it is parent to every class, either built in classes or user defined
# class Parent(object):
class Parent:
    def purchaseBike(self):
        print("Lets buy Bajaj Pulsar")


# Object Construction
pRef = Parent()
pRef.fname = "John"
pRef.lname = "Watson"

print(pRef.__dict__)
print(Parent.__dict__)
