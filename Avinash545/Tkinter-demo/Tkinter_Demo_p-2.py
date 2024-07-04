from tkinter import *

root = Tk()

root.geometry("500x500")
root.title("My GUI WITH SOUMAY")

#Important Label Option -
'''
text - adds the text
bg - background
fg - foreground
font - sets the font
padx - x padding
pady - y padding
relief - border styling - SUNKEN,RAISED,GROOVE,RIDGE
'''

mytitle = Label(text = " MY FIRST TITLE\n Second line",bg="red",fg="white",padx=23,pady=24,
                font="comicsansms 9 bold",borderwidth=3,relief= SUNKEN
                )
mytitle.pack()

#Impostant pack options
#anchor = nw nw means north west
#side = top,bottom,left,right
#fill
#padx
#pady

mytitle.pack(side=BOTTOM,anchor="se",fill=X) # se means south east
#fill = X means it will horijantaly cover  fill= Y means verticaly


root.mainloop()
