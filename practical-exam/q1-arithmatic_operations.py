from tkinter import *
from tkinter import ttk, simpledialog


def calculate(event):
    op = combo.get()
    a = simpledialog.askfloat("Input", "Enter first number:")
    b = simpledialog.askfloat("Input", "Enter second number:")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b if b != 0 else "Error"

    print("Result:", result)


root = Tk()
combo = ttk.Combobox(root, values=["+", "-", "*", "/"])
combo.pack()
combo.bind("<<ComboboxSelected>>", calculate)
root.mainloop()
