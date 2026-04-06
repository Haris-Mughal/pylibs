from tkinter import *
from tkinter import ttk, simpledialog

def check(event):
    n = int(simpledialog.askstring("Input","Enter number:"))
    print("Even" if n%2==0 else "Odd")

root = Tk()
combo = ttk.Combobox(root, values=["Check Even/Odd"])
combo.pack()
combo.bind("<<ComboboxSelected>>", check)
root.mainloop()
