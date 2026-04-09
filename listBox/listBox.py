from tkinter import *


def calculate():
    try:
        a = float(e1.get())
        b = float(e2.get())

        selected = lb.curselection()  # get selected index

        if not selected:
            lbl.config(text="Select an option")
            return

        op = selected[0]

        if op == 0:
            result = "Add = " + str(a + b)
        elif op == 1:
            result = "Sub = " + str(a - b)
        elif op == 2:
            result = "Mul = " + str(a * b)
        elif op == 3:
            result = "Div = " + (str(a / b) if b != 0 else "Error")
        elif op == 4:
            result = "Mod = " + str(a % b)

        lbl.config(text=result)

    except:
        lbl.config(text="Invalid Input")


root = Tk()
root.geometry("300x400")

# Textboxes
Label(root, text="Enter First Number").place(x=20, y=20)
e1 = Entry(root)
e1.place(x=150, y=20)

Label(root, text="Enter Second Number").place(x=20, y=50)
e2 = Entry(root)
e2.place(x=150, y=50)

# Listbox
lb = Listbox(root, height=5)
lb.insert(0, "Addition")
lb.insert(1, "Subtraction")
lb.insert(2, "Multiplication")
lb.insert(3, "Division")
lb.insert(4, "Modulus")
lb.place(x=20, y=90)

# Button
Button(root, text="Calculate", command=calculate).place(x=100, y=200)

# Result Label
lbl = Label(root, text="")
lbl.place(x=20, y=250)

root.mainloop()