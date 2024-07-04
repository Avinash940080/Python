from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def prime_no():
    num = int(numEntry.get())
    flag = False
    if num <= 1:
        messagebox.showinfo("PRIME-NUMBER CHECKER"," It is not prime nor composite")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        messagebox.showinfo("PRIME-NUMBER CHECKER"," It is not prime number")
    else:
        messagebox.showinfo("PRIME-NUMBER CHECKER"," It is an prime number")


window = Tk()
window.title("PRIME-NUMBER")
blabel = Label(window)
blabel.grid()
frame = Frame(window)
frame.place(x=600,y=100)

num = Label(frame, text="Enter  the number : ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
num.grid(row=0, column=0, padx=10, pady=5)  # Add padx and pady to create space

numEntry = Entry(frame, width=30)
numEntry.grid(row=0, column=1)


submit_button = Button(frame, text="Submit", command=prime_no)
submit_button.grid(row=1, column=1)

window.mainloop()



