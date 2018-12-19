class Student:
    def __init__(self, roll, name, age):
        self.roll = roll  # public
        self._name = name # protected
        self.__age = age  # private

    def showStudentDetails(self):
        if self._name is "Fionna":
            print("Hello Fionna")
        else:
            print("Sorry !!")

    # def _sayHello(self):
    def __sayHello(self):
        print("Hello",self._name," your age is:",self.__age)

s1 = Student(101,"Fionna",30)
print(s1.roll)
print(s1._name)     # we are just giving a warning not ot access it !!
# print(s1.__age)   # error

print(s1.__dict__)
print(s1._Student__age)

s1._name = "John"
print(Student.__dict__)
s1.showStudentDetails()
# s1._sayHello()
s1._Student__sayHello()