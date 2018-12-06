# Single Value Container

# Write Operation
a = 10
b = 10

# Update Operation
a = 111

c = a+b

# Read Operation
print("a is",a)
print("b is",b)
print("c is",c)

print(type(a))
print(type(b))
print(type(c))

d = 2.2
print("d is",d)
print(type(d))

e = 'A'
print("e is",e)
print(type(e))

# Memory | Hashing Algorithm

print(id(a))
print(id(e))

print(hex(id(a)))
print(hex(id(e)))

x = 10
y = 10
z = x  # Reference Copy
# x and y are reference variables !!

print("x is",x," and hex id of x is",hex(id(x)))
print("y is",y," and hex id of y is",hex(id(y)))
print("z is",z," and hex id of z is",hex(id(z)))

x = 111

print("x is",x," and hex id of x is",hex(id(x)))

# PS: In Python we have every storage container as reference type