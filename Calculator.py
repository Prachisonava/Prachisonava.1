import tkinter as tk
from tkinter import ttk

def button_click(value):
    current = entry_var.get()
    entry_var.set(current + value)

def clear():

    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create entry widget
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    ttk.Button(root, text=button, command=lambda button=button: button_click(button)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create clear button
ttk.Button(root, text='C', command=clear).grid(row=row, column=0, columnspan=2, padx=5, pady=5)

# Create calculate button
ttk.Button(root, text='=', command=calculate).grid(row=row, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()