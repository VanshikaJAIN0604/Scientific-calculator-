import tkinter as tk
from math import sin, cos, tan, sqrt, log, exp, radians, factorial

root = tk.Tk()
root.title("Scientific Calculator")

display = tk.Entry(root, font=("Arial", 16), width=25, borderwidth=5, relief="ridge")
display.grid(row=0, column=0, columnspan=5)

def click(key):
    display.insert(tk.END, key)

def clear():
    display.delete(0, tk.END)

def evaluate():
    try:
        expression = display.get()
        
        result = eval(expression, {"__builtins__": None}, {
            "sin": sin, "cos": cos, "tan": tan, "sqrt": sqrt, "log": log, "exp": exp, 
            "factorial": factorial, "radians": radians
        })
        clear()
        display.insert(tk.END, str(result))
    except Exception as e:
        clear()
        display.insert(tk.END, "Error")

buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '(',
    '1', '2', '3', '-', ')',
    '0', '.', '=', '+', 'sqrt',
    'sin', 'cos', 'tan', 'log', 'exp',
    'factorial', 'radians'
]
row = 1
col = 0
for button in buttons:
    action = lambda x=button: click(x) if x not in ['=', 'C', 'sqrt', 'sin', 'cos', 'tan', 'log', 'exp', 'factorial', 'radians'] else None
    if button == "=":
        tk.Button(root, text=button, width=5, height=2, command=evaluate).grid(row=row, column=col)
    elif button == "C":
        tk.Button(root, text=button, width=5, height=2, command=clear).grid(row=row, column=col)
    elif button in ["sqrt", "sin", "cos", "tan", "log", "exp", "factorial", "radians"]:
        tk.Button(root, text=button, width=5, height=2, command=lambda b=button: click(b + '(')).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, height=2, command=action).grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()