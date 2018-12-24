import mysql.connector


# Passed Object as Reference
def saveStudentInDB(sRef):

    # Create SQL Query
    sql = "insert into Student values(null,'{}','{}')".format(sRef.name, sRef.address)

    # Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="GW2018AI")

    # Execute SQL Query On Connection
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(sRef.name,"Saved in DB !!")

def updateStudentInDB(sRef):

    # Create SQL Query
    sql = "update Student set name = '{}', address = '{}' where roll = {}".format(sRef.name, sRef.address, sRef.roll)

    # Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="GW2018AI")

    # Execute SQL Query On Connection
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(sRef.name,"Updated in DB !!")

def deleteStudentFromDB(roll):

    # Create SQL Query
    sql = " delete from Student where roll = {}".format(roll)

    # Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="GW2018AI")

    # Execute SQL Query On Connection
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(roll,"Deleted From DB !!")


def fetchStudentsFromDB():

    # Create SQL Query
    sql = "Select * from Student"

    # Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="GW2018AI")

    # Execute SQL Query On Connection
    cursor = con.cursor()
    cursor.execute(sql)

    # row = cursor.fetchone()
    # print(row)
    # row = cursor.fetchone()
    # print(row)
    # row = cursor.fetchone()
    # print(row)

    rows = cursor.fetchall()
    print(rows)

    for row in rows:
        print(row)


class Student:

    # Constructor
    # self is a reference variable which points to the current object
    def __init__(self, roll, name, adrs):
        self.roll = roll
        self.name = name
        self.address = adrs
        print("Object Created",id(self))

    # Destructor
    def __del__(self):
        print("Object Deleted",id(self))


# Object Construction Statement
# s1 is a reference variable

"""
s1 = Student(3, "Fionna Flynn", "Eastern Shores")
s2 = Student(0, "Sia", "Pristine Magnum")
print(s1.__dict__)
print(s2.__dict__)

print(s1.roll)
print(s1.name)
print(s1.address)


# del s1
# del s2

print(__name__)

# saveStudentInDB(s2)
# updateStudentInDB(s1)
# deleteStudentFromDB(3)

"""

fetchStudentsFromDB()

"""
    SQL:
    create table Student(
        roll integer primary key auto_increment,
        name varchar(256),
        address varchar(512)
    )
    
    # INSERT Data in TABLE
    insert into Student values(null,'John','Redwood Shores')
    insert into Student(roll,name,address) values(null,'John','Redwood Shores')
    
    # UPDATE
    update Student set name = 'John Watson', address = 'Pristine Magnum' where roll = 1
    
    # DELETE
    delete from Student where roll = 1
    
    # Retrieve or QUERY
    select * from Student
    select roll,name from Student
    select * from Student where roll > 5
    select * from Student where roll = 1
    
"""