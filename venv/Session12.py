from tkinter import *
import mysql.connector

# tkinter is a library which is used to create GUI's
# but python isnt meant to develop apps. Its major role lies in research !!

class Customer:

    # Constructor
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # Destructor
    def __del__(self):
        print("==Object Destroyed==")

def saveCustomerInDB(cRef):

    # Create SQL Query
    sql = "insert into Customer values(null, '{}', '{}', '{}')".format(cRef.name, cRef.phone, cRef.email)

    # Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="GW2018AI")

    # Execute SQL Query On Connection
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print("Customer", cRef.name, " Registered in Loyalty Program !!")


def onClick():
    # print("==Button Clicked==")
    # Extract Data from Entry which User will Enter
    name = entryName.get()
    phone = entryPhone.get()
    email = entryEmail.get()

    # We have saved the data in Object
    cRef = Customer(name, phone, email)
    print(cRef.__dict__)

    saveCustomerInDB(cRef)

# Window
window = Tk()

# Textual Information : Label
lblTitle = Label(window, text="Add Your Customer Details")
lblTitle.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()

window.mainloop()

"""
Assignment 1 :
Develop a Customer Loyalty Program Software !!
> Add Customer
> Update Customer
> De-Activate Customer
> View All Customers
    Activated and DeActivated
> Grant Reward Points | 10 percent points of shopping done 
> Redeem Reward Points   

Assignment 2 :
Order Management at Mc Donalds
 
"""