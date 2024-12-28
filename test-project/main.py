#!/usr/bin/env python3
import tkinter as tk

# Create window
root = tk.Tk()
root.title("My Linux App")

# add text
label = tk.Label(root, text="Hello, Linux!")
label.pack(pady=20, padx=20)

# Launch app
root.mainloop()
