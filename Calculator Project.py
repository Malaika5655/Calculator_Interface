# Python Development Internship Projects
# Project 1: Calculator with GUI (Dark Theme)

import tkinter as tk
from tkinter import messagebox

# Dark theme colors
BG_COLOR = '#2c2f33'
BTN_COLOR = '#7289da'
TEXT_COLOR = '#ffffff'

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Dark Mode Calculator")
        root.configure(bg=BG_COLOR)

        self.entry = tk.Entry(root, width=25, font=('Arial', 18), bd=5, relief='sunken', bg=BG_COLOR, fg=TEXT_COLOR)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.click(x)
            tk.Button(root, text=text, width=5, height=2, command=action, bg=BTN_COLOR, fg=TEXT_COLOR, font=('Arial', 14)).grid(row=row, column=col, padx=5, pady=5)

    def click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.entry.insert(tk.END, text)

# Run calculator
if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
