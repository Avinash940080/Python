from tkinter import *
def draw_rectangle(canvas, coordinates, color):
    canvas.create_rectangle(coordinates, fill=color)

window = Tk()
window.title("Canvas")
window.geometry("500x500")

mycan = Canvas(window, width=300, height=200, bg="blue")
mycan.pack(pady=20)

x = (50, 50, 250, 200)
color = "black"

draw_rectangle(mycan, x, color)

window.mainloop()
