# tkinter to create GUI's
from tkinter import *

window = Tk()

lblTitle = Label(window, text="Add Customer Details")
lblTitle.pack()


lblName = Label(window, text="Enter Customer Name")
lblName.pack()

window.mainloop() # Keeo on running the process/program.