# tkinter to create GUI's
from tkinter import *

from Project12 import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def onClick():

    print("Button Clicked")

    cRef = Customer(None, None, None)

    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()

    cRef.showCustomerDetails()



    data = cRef.__dict__

    db.collection("Customer").document().set(data)

    print(">> ", cRef.name, "Saved in Firebase")


window = Tk()

lblTitle = Label(window, text="Add Customer Details")
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

window.mainloop() # Keep on running the program/process