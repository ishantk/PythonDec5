# Pass By Value Vs Pass by Reference
# Shallow and Deep Copy

def fun(a , b):

    print("a before is", a)
    print("b before is", b)

    # Update Operation of a and b
    a = 10
    b = 20

    print("a after is",a)
    print("b after is",b)

x = 100
y = 200

fun(x,y) # Value Copy

print("x is", x)
print("y is", y)

print("********")

def hello(numbers):
    print("==numbers Before==")
    for x in numbers:
        print(x)

    for x in range(0,len(numbers)):
        numbers[x] = numbers[x]*2

    print("==numbers After==")
    for x in numbers:
        print(x)

#       0  1  2  3   4
nums = [10,20,30,40,50]
hello(nums) # Reference Copy
print("nums[0] is:",nums[0])
print("*****nums*****")
for x in nums:
    print(x)
