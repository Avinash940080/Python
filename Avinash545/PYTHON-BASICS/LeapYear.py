from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def is_leap_year():
    year = int(LeapYearEntry.get())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        messagebox.showinfo("OUTPUT","It is a Leap Year")
    else:
        messagebox.showinfo("OUTPUT","It is a Not an Leap Year")

window = Tk()
window.title("Leap Year")
blabel = Label(window)
blabel.grid()
frame  = Frame(window)
frame.place(x=600,y=100)

Leap_yearlabel = Label(frame, text="Enter an year ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
Leap_yearlabel.grid(row=0, column=0, padx=10, pady=5)  # Add padx and pady to create space

LeapYearEntry = Entry(frame, width=30)
LeapYearEntry.grid(row=0, column=1)

submit_button = Button(frame, text="Submit", command=is_leap_year)
submit_button.grid(row=1, column=1)

window.mainloop()



