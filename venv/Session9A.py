# Overriding
class Parent:
    def purchaseBike(self):
        print("Lets buy Bajaj Pulsar")

class Child(Parent):
    def purchaseBike(self):
        print("Lets buy Royal Enfield")

print(Child.__dict__)

ch = Child()
print(ch.__dict__)
print(ch)

ch.purchaseBike()