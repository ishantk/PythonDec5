# Relationships in Objects :
    # HAS-A Relation
    # 1 to 1
    # 1 to many
    # many to many


class Address:

    def __init__(self, adrsLine, city, state, zipCode):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def showAddress(self):
        print("====Address Details====")
        print("Address Line\t",self.adrsLine)
        print("City\t\t\t", self.city)
        print("State\t\t\t", self.state)
        print("Zip Code\t\t", self.zipCode)
        print("=======================")

class Customer:

    # def __init__(self, name="NA", phone="NA", email="NA", address=None): # 1 to 1
    def __init__(self, name="NA", phone="NA", email="NA", addresses=None): # 1 to many
        print("Customer Object Constructed")
        self.name = name
        self.phone = phone
        self.email = email
        # self.address = address
        self.addresses = addresses

    def showCustomerDetails(self):
        print("====Customer Details====")
        print("Name\t\t\t", self.name)
        print("Phone\t\t\t", self.phone)
        print("Email\t\t\t", self.email)
        print("=======================")

        # self.address.showAddress() # 1 to 1
        for adrs in self.addresses:  # 1 to many
            adrs.showAddress()

a1 = Address("Pristine Mangum", "Bengaluru", "Karnataka", 520001)
# print(a1.__dict__)
# a1.showAddress()

a2 = Address("Country Homes", "Ludhiana", "Punjab", 141002)

addresses =[a1, a2]

# c1 = Customer("John", "+91 99999 88888", "john@example.com", a1)
c1 = Customer("John", "+91 99999 88888", "john@example.com", addresses)

# c2 = Customer()
# c2.age = 120
# c2.gender = "Male"
#
# print(c1.__dict__)
# print(c2.__dict__)
#
# c1.address.showAddress()

c1.showCustomerDetails()

# Assignment:  Explore Uber or OLA and create 1 to 1 and 1 to many relations