from tkinter import *

def calculate():
    try:
        a = float(e1.get())
        b = float(e2.get())

        op = v.get()

        if op == 1:
            result = "Add = " + str(a + b)
        elif op == 2:
            result = "Sub = " + str(a - b)
        elif op == 3:
            result = "Mul = " + str(a * b)
        elif op == 4:
            result = "Div = " + (str(a / b) if b != 0 else "Error")
        elif op == 5:
            result = "Mod = " + str(a % b)
        else:
            result = "Select an option"

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

# Variable for radio buttons
v = IntVar()

# Radio Buttons
Radiobutton(root, text="Addition", variable=v, value=1).place(x=20, y=90)
Radiobutton(root, text="Subtraction", variable=v, value=2).place(x=20, y=115)
Radiobutton(root, text="Multiplication", variable=v, value=3).place(x=20, y=140)
Radiobutton(root, text="Division", variable=v, value=4).place(x=20, y=165)
Radiobutton(root, text="Modulus", variable=v, value=5).place(x=20, y=190)

# Button
Button(root, text="Calculate", command=calculate).place(x=100, y=230)

# Result Label
lbl = Label(root, text="")
lbl.place(x=20, y=270)

root.mainloop()