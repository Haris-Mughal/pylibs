from tkinter import *
from tkinter import ttk, simpledialog
import math

def calc(event):
    op = combo.get()
    n = simpledialog.askfloat("Input", "Enter number:")

    if op == "Square": result = n**2
    elif op == "Cube": result = n**3
    elif op == "Square Root": result = math.sqrt(n)

    print(result)

root = Tk()
combo = ttk.Combobox(root, values=["Square","Cube","Square Root"])
combo.pack()
combo.bind("<<ComboboxSelected>>", calc)
root.mainloop()
