class Student:

    def __init__(self,roll,name,phone):
        self.roll = roll
        self.name = name
        self.phone = phone

    def studentToCSV(self):
        return "{},{},{}\n".format(self.roll,self.name,self.phone)

#Object Construction
s1 = Student(101,"John","+91 99999 88888")
s2 = Student(201,"Fionna","+91 88888 66666")

print(s1.__dict__)
print(s2.__dict__)
print(Student.__dict__)

# Objects are getting created in RAM !!
# RAM is volatile

file = open("/Users/ishantkumar/Downloads/studentsData.csv","a") # append mode
line = s1.studentToCSV()
file.write(line)
file.close()

# Assignment : Read CSV File and create Objects in Python
