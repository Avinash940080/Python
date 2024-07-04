from tkinter import *
from PIL import Image,ImageTk

# any variable u can give instead of root
root = Tk()


root.geometry("500x500")
#so it will have min size
root.minsize(400,400)
# it will have max size
root.maxsize(1000,1000)

#for jpg image
image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)
slabel = Label(image=photo)
slabel.pack()

#for png image
photo = PhotoImage(file="1.png")
slabel = Label(image=photo)
slabel.pack()

soumay = Label(text="This is label")
soumay.pack()
root.mainloop()

