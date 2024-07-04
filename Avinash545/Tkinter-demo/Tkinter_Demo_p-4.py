from tkinter import *

root = Tk()
root.geometry("500x500")
def fun():
    print("Hello world")

frame = Frame(root,borderwidth=66,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="ne")
#creating a button
b1 = Button(frame,fg="red",text="Print now")
b1.pack(side=LEFT,padx=10,pady=10)

#creating a button
b2 = Button(frame,fg="red",text="Print now")
b2.pack(side=RIGHT,padx=15,pady=15)

#creating a button
b3 = Button(frame,fg="red",text="Print now",command=fun)
b3.pack(side=RIGHT,padx=20,pady=20)
root.mainloop()