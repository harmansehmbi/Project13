# tkinter to create GUI's
from tkinter import *

def onClick():
    print("Button Clicked")

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

window.mainloop() # Keeo on running the process/program.