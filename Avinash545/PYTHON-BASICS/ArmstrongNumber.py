from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def Armstrong_Num():
    num =int(numEntry.get())
    temp = num
    sum = 0
    while num!=0:
        rem = num%10
        sum = (sum+(rem*rem*rem))
        num//=10

    if temp == sum:
        messagebox.showinfo("ARMSTRONG-NUM"," It is an armstrong no")
    else:
        messagebox.showinfo("ARMSTRONG NUM"," It is not armstrong no")

window = Tk()
window.title("ARMSTRONG-NUMBER")
blabel = Label(window)
blabel.grid()
frame = Frame(window)
frame.place(x=600,y=100)

num = Label(frame, text="Enter  the number : ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
num.grid(row=0, column=0, padx=10, pady=5)  # Add padx and pady to create space

numEntry = Entry(frame, width=30)
numEntry.grid(row=0, column=1)


submit_button = Button(frame, text="Submit", command=Armstrong_Num)
submit_button.grid(row=1, column=1)

window.mainloop()



