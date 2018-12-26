print("App Started")

try:
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    num3 = num1/num2
# except ZeroDivisionError as z:
#     print("You are trying to divide by 0",z)
# except ValueError as vRef:
#     print("You are trying to enter an invalid number",vRef)
except Exception as e:
    print("OOPS!! Some Error:",e)
else:
    print("Number3 is:", num3)
finally:
    print("Executed For Sure !!")


print("App Finished")

# PS : In Python every error occur at run time and hence we call it run time error or Exception
# Q : How will we know about all the errors ?
# A : Whenever you face them !! Or you go to documentation !!
#     Exception is a built in class which is parent of all errors
