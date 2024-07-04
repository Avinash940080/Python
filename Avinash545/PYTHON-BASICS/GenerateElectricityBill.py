from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def calculate_bill():
    units =float(unitEntry.get())
    rate_per_unit = 5.0
    fixed_charge = 10.0
    total_cost = (units * rate_per_unit) + fixed_charge
    messagebox.showinfo("TOTAL COST  : ", f" ({total_cost})")


window = Tk()
window.title("GENERATE ELECTRICITY BILL")
blabel = Label(window)
blabel.grid()
frame = Frame(window)
frame.place(x=600,y=100)

unit = Label(frame, text="Enter  the number of units consumed: ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
unit.grid(row=0, column=0, padx=10, pady=5)  # Add padx and pady to create space

unitEntry = Entry(frame, width=30)
unitEntry.grid(row=0, column=1)


submit_button = Button(frame, text="Submit", command=calculate_bill)
submit_button.grid(row=2, column=1)

window.mainloop()


