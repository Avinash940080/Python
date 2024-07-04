from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def even_odd():
    num =int(numEntry.get())
    if num % 2 == 0:
        messagebox.showinfo("EVEN-ODD CHECKER"," It is even number")
    else:
        messagebox.showinfo("EVEN-ODD CHECKER"," It is odd number")

window = Tk()
window.title("EVEN - ODD CHECKER")
blabel = Label(window)
blabel.grid()
frame = Frame(window)
frame.place(x=600,y=100)

num = Label(frame, text="Enter  the number : ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
num.grid(row=0, column=0, padx=10, pady=5)  # Add padx and pady to create space

numEntry = Entry(frame, width=30)
numEntry.grid(row=0, column=1)


submit_button = Button(frame, text="Submit", command=even_odd)
submit_button.grid(row=1, column=1)

window.mainloop()


