# Decision Flow

a = 1000
b = 200
c = 30

# Regular if/else
if a>b:
    print("a is greatest")
else:
    print("b is greatest")

# Nested if/else
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else:
        print("c is greatest")

if a>b and a>c:
    print("a is greatest")

isInternetConnected = True
isGPSConnected = False

if isInternetConnected:
    if isGPSConnected:
        print("You can browse Google Maps")
    else:
        print("Please Connect GPS and Try Again !!")
else:
    print("Please Connect Internet and Try Again !!")

if isInternetConnected and isGPSConnected:
    print("You can browse Google Maps")
else:
    print("Please check Internet or GPS and Try Again !!")

# Ladder if/else
uberGo = 1
uberX = 2
uberMoto = 3

print("Press 1 to book UberGo")
print("Press 2 to book UberX")
print("Press 3 to book UberMoto")

userChoice = int(input("Make Your Choice"))

if userChoice == uberGo:
    print("UberGo Booked !! Arriving Soon !!")
elif userChoice == uberX:
    print("UberX Booked !! Arriving Soon !!")
elif userChoice == uberMoto:
    print("UberMoto Booked !! Arriving Soon !!")
else:
    print("Please Make a Valid Selection !!")

internetTech = 2 # Assuming 2G
print("Speed should be greater than 4 mbps") if internetTech >=2 else print("Please upgrade your data plan")

# compare 5 numbers :  if few numbers are same than what will happen !!
# 121, 1441