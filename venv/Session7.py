
# Anything which we write in class belongs to class
# Anything which we write in class's method with self belongs to object
# Every method in class shall contain 1st input as self
class Counter:

    myCount = 1

    def __init__(self):
        self.count = 1

    def incrementCount(self):
        self.count = self.count + 1
        Counter.myCount = Counter.myCount + 1

    def showCount(self):
        # yourCount = 100 | Property of showCount method
        print("count is",self.count)
        # print("yourCount is", yourCount)
        print("myCount is", Counter.myCount) # Property of class can be accessed by method with class name

# Object Construction Statement
c1 = Counter()
c2 = Counter()
c3 = c1     # Reference Copy

c1.incrementCount() # 2  -> Statement will be translated into such statement: Counter.incrementCount(c1)
c2.incrementCount() # 2
c3.incrementCount() # 3
c3.incrementCount() # 4
c1.incrementCount() # 5
c2.incrementCount() # 3

Counter.incrementCount(c1)

                #      A    B   C    D
c1.showCount()  #      8    8   9    6
c2.showCount()  #                    3
c3.showCount()  #                    6

# OOPS
