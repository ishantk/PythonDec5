# Variable Arguments : Tuple (*args)
def addNumbers(*args):
    print(args)
    print(type(args))

    sum = 0
    for x in args:
        sum = sum + x

    print("sum is",sum)


addNumbers(10,20)
addNumbers(10,20,30,40,50)
addNumbers(10,20,30,40,50,60,70,80,90,100)

# Assignment : Develop Calculator App, which asks user what you wish to do
# PS: Use Functions

def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))

fun(a=10,b=20,c=30)





