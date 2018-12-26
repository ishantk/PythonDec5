# User Defined Exception
class BankingExcpetion(Exception):
    pass


print("Banking Started")

accBalance = 10000
attempts = 0

def withdraw(amount):

    global accBalance
    global attempts

    accBalance = accBalance - amount
    if accBalance < 2000:
        accBalance = accBalance + amount
        print("Balance is LOW:", accBalance)
        attempts = attempts + 1
    else:
        print(amount, " Withdrawn !! New Balance is:", accBalance)

    if attempts == 3:
        # raise Exception("Invalid Attempts")
        raise BankingExcpetion("Invalid Attempts")

try:
    for i in range(1,60):
        withdraw(3000)
except Exception as e:
    print("Sorry!! Invalid Attempts !!", e)


print("Banking Finished")