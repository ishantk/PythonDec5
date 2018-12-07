"""num1 = int(input("Enter Number1"))
num2 = int(input("Enter Number2"))
# Arithmetic : +, -, *, /, %
num3 = num1 % num2
print(num3)
"""
age = 2
gender = "M"

# Conditional : >, <, >=, <= == !=
print(age>18)

# Logical : and or not
print(age>18 and gender=="M")

num1 = 8                # 1 0 0 0
num2 = 10               # 1 0 1 0

# Bitwise Operators
num3 = num1 & num2      # 1 0 0 0
num4 = num1 | num2      # 1 0 1 0
num5 = num1 ^ num2      # 0 0 1 0

print(num3)             # 8
print(num4)             # 10
print(num5)             # 10

# Shift Operators
# num6 = num1 >> 2          # 1 0 0 0 >> 2 -> 0 0 1 0
# print("num6 is:",num6)    # 0 0 1 0

num6 = 11 >> 3
print("num6 is:",num6)    # 1


num7 = 8 << 3
print("num7 is:",num7)    # 1 0 0 0 << 3  1 0 0 0 0 0 0

# Explore : odd numbers and negative numbers !!

x = 5
y = 3

# z = x/y
z = x//y
print("z is ",z)

johnsAge = 30
siasAge = 12

print(johnsAge is siasAge)
print(johnsAge is not siasAge)

# num = 12345
# result = 1+2+3+4+5
# 12345 => 1+2+3+4+5 = 15