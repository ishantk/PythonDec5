class OLACab:
    def bookCab(self, source, destination):
        print("Cab Booked from",source,"to",destination)

class OLAMicro(OLACab):
    def bookCab(self, source, destination):
        print("OLA Micro Cab Booked from",source,"to",destination)

class OLAMini(OLACab):
    def bookCab(self, source, destination):
        print("OLA Mini Cab Booked from",source,"to",destination)

class OLAShared(OLACab):
    def bookCab(self, source, destination):
        print("OLA Shared Cab Booked from",source,"to",destination)

class OLABike(OLACab):
    def bookCab(self, source, destination):
        print("OLA Bike Booked from",source,"to",destination)

# Factory Design Pattern
class UI:

    def bookMeACab(self, typeOfCab):

        cab = None

        if typeOfCab == 1:
            cab = OLAMicro()
        elif typeOfCab == 2:
            cab = OLAMini()
        elif typeOfCab == 3:
            cab = OLAShared()
        else:
            cab = OLABike()

        return cab

ui = UI()
print("===============")
print("1. Micro Cab")
print("2. Mini Cab")
print("3. Shared Cab")
print("4. Bike")
print("===============")

source = input("Enter Your Source Location ")
dest = input("Enter Your Destination Location ")
typeOfCab = int(input("Please Enter Type of Cab "))

cRef = ui.bookMeACab(typeOfCab)
cRef.bookCab(source,dest)