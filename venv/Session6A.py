# Structure of an Object
# self -> Reference to Current Object (Object in Action)

# What so ever we write in class belongs to class
# It is Property of class
# What Object Has than ?? Only Data !!
class User:
    # Constructor : Gets executed when an Object is created in memory
    # Constructor with inputs
    def __init__(self, name, phone, email, adrs):
        print("Constructor Executed")
        self.name = name
        self.phone = phone
        self.email = email
        self.address = adrs

    # Method
    def showUserDetails(self):
        print("{} can be called at {}".format(self.name,self.phone))



u1 = User("Sia","+91 88888 77777","sia@example.com","Pristine Magnum")
u2 = User("Kim","+91 99999 77777","kim@example.com","Eastern Shores")

print(u1)
print(u2)

u1.age = 20

print(u1.__dict__)
print(u2.__dict__)

u1.showUserDetails() # Gets Translated to User.showUserDetails(u1)
u2.showUserDetails() # Gets Translated to User.showUserDetails(u2)

User.showUserDetails(u1)
User.showUserDetails(u2)

print(u1.__dict__)
print(u2.__dict__)

# Whats in the Class ??
print(User.__dict__)

print(u1.__sizeof__())
print(u2.__sizeof__())
