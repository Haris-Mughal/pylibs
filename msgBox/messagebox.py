from tkinter import *
from tkinter import messagebox

def show():
    result = ""

    if v1.get(): result += "Reading "
    if v2.get(): result += "Gaming "
    if v3.get(): result += "Traveling "
    if v4.get(): result += "Sports "
    if v5.get(): result += "Music "

    messagebox.showinfo("Selected", result)

root = Tk()
root.geometry("250x200")

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()

Checkbutton(root, text="Reading", variable=v1).place(x=20, y=20)
Checkbutton(root, text="Gaming", variable=v2).place(x=20, y=45)
Checkbutton(root, text="Traveling", variable=v3).place(x=20, y=70)
Checkbutton(root, text="Sports", variable=v4).place(x=20, y=95)
Checkbutton(root, text="Music", variable=v5).place(x=20, y=120)

Button(root, text="Show", command=show).place(x=80, y=150)

root.mainloop()