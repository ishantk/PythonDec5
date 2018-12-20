lm1 = lambda x : x*x

def square(x):
    return x*x

L1 = [10, 11, 34, 57, 13, 97, 54]
# result = map(lm1,L1)
result = map(square,L1)
print(result)
print(type(result))
print(list(result))

lm2 = lambda n : n%2 == 0
L2 = [10, 20, 30, 40, 50, 11, 13, 15, 17, 19]
result = map(lm2,L2)
print(result)
print(type(result))
print(list(result))

result = filter(lm2,L2)
print(result)
print(type(result))
print(list(result))

X = [10, 20, 30, 40, 50]
Y = [11, 22, 33, 44, 55]

lm3 = lambda P, Q : P + Q
result = map(lm3,X,Y)
print(list(result))

punjabPopulation = [12345, 34567, 12347, 6543, 8976]

# sum = 0
# for x in punjabPopulation:
#     sum = sum + x
# print("Population is ",sum)

lm4 = lambda x,y : x+y
from functools import reduce
result = reduce(lm4,punjabPopulation)
print(result)

employees = [ {"eid":101,"name":"John"}, {"eid":201,"name":"Jennie"}, {"eid":301,"name":"Fionna"} ]
lm5 = lambda emps : emps["eid"]
result = map(lm5,employees)
print(list(result))
