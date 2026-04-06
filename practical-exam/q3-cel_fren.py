from tkinter import *
from tkinter import ttk, simpledialog

def convert(event):
    op = combo.get()
    t = simpledialog.askfloat("Input", "Enter temperature:")

    if op == "C to F": result = (t*9/5)+32
    elif op == "F to C": result = (t-32)*5/9

    print(result)

root = Tk()
combo = ttk.Combobox(root, values=["C to F","F to C"])
combo.pack()
combo.bind("<<ComboboxSelected>>", convert)
root.mainloop()
