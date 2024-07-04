from tkinter import *
def draw_rectangle(canvas, coordinates):
    canvas.create_rectangle(coordinates, fill="red")

window = Tk()
window.title("Canvas")
window.geometry("500x500")

mycan = Canvas(window, width=300, height=200, bg="blue",bd="12",relief="groove")
mycan.pack(pady=20)

x = (50, 50, 250, 200)

draw_rectangle(mycan, x)

window.mainloop()
