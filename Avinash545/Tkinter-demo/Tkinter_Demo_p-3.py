from tkinter import *

root = Tk()
root.geometry("500x500")

#creating frame
f1 = Frame(root,bg="grey", borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2 = Frame(root,borderwidth=9,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l = Label(f1,text="Project Tkinter- Pycharm",font="Helvetica",fg="red",bg="white")
l.pack()

l2 = Label(f2,text="Welcome to this ")
l2.pack(padx=10,pady=10)
root.mainloop()
