# Overriding
class Cab:
    def bookCab(self, source, destination):
        print("Cab Booked from",source,"to",destination)

class Uber(Cab):
    def bookCab(self, source, destination):
        print("Uber Cab Booked from",source,"to",destination)

class OLA(Cab):
    # def bookCab(self, source, destination, typeOfCab):
    #     print("OLA",typeOfCab," Cab Booked from",source,"to",destination)
    def bookCab(self, source, destination):
        print("OLA Cab Booked from",source,"to",destination)


# cRef = Cab()
# cRef.bookCab("MBD Mall","Pavilion Mall")

# uRef = Uber()
# uRef.bookCab("MBD Mall","Pavilion Mall")

# oRef = OLA()
# oRef.bookCab("MBD Mall","Pavilion Mall","Shared")

# Polymorphism : Run Time Polymorphism



cRef = Cab()
cRef.bookCab("MBD Mall","Pavilion Mall")

cRef = Uber()
cRef.bookCab("MBD Mall","Pavilion Mall")

cRef = OLA()
cRef.bookCab("MBD Mall","Pavilion Mall")