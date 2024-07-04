import tkinter as tk
from tkinter import messagebox

def fact():
    num = int(AEntry.get())
    ans = 1
    if num < 0:
        messagebox.showerror("Error", "Factorial is not defined for negative numbers.")
    elif num == 0:
        messagebox.showinfo("Factorial", f"Factorial of {num} is 1")
    else:
        for i in range(1, num + 1):
            ans *= i
        messagebox.showinfo("Factorial", f"Factorial of {num} is {ans}")

window = tk.Tk()
window.title("Factorial of Number")
window.geometry('340x440')
window.configure(bg='#333333')

frame = tk.Frame(window)
frame.grid()

A = tk.Label(frame, text="Enter a number: ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
A.grid(row=0, column=0, padx=10, pady=5)

AEntry = tk.Entry(frame, width=30)
AEntry.grid(row=0, column=1)

submit_button = tk.Button(frame, text="Submit", command=fact)
submit_button.grid(row=1, column=1)

window.mainloop()
