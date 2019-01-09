def show():
    return "Hello"

# Reference Copy
s = show

print(s)
print(type(s))

print(s())
print(s())
print(s())

def showAgain():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
    yield "E"



# Reference Copy
sa = showAgain

print(sa)
print(type(sa))

gen = sa()
print(gen)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def dataGenerator():
    file = "CityTemps.csv"

    for row in open(file, "r"):
        # print(row)
        yield row

dg = dataGenerator()
print(next(dg))
print(next(dg))