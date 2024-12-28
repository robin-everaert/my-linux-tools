#!/usr/bin/env python3
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button
import tkinter as tk
import os

# Create the main window
root = tk.Tk()
root.tk.call("tk", "scaling", 1.0)

# Initialize the style
style = Style(theme="darkly")

# Define a custom style with a bold font
style.configure(
    "Custom.TButton",
    font=("Sans-serif", 16, "bold"),
    background="#B80808",
    foreground="#ececec",
    borderwidth=0,  # Remove border
    relief="flat"   # Make the button flat
)
style.map(
    "Custom.TButton",
    background=[("active", "#FF5733")],  # Bright orange-red on hover
    foreground=[("active", "#FFFFFF")]  # Pure white text on hover
)

# Configure the main window
root.title("LaunchPad")
root.geometry("150x300")

# Function to open a folder
def open_folder(path):
    full_path = os.path.expanduser(path)  # Resolve ~ to an absolute path
    os.system(f'xdg-open "{full_path}"')  # Open the folder

# Function to create styled buttons
def create_button(parent, text, path):
    return Button(
        parent,
        text=text,
        width=12,
        style="Custom.TButton",  
        command=lambda: open_folder(path)
    )

# Add buttons
cur_button_frame = tk.Frame(root)
cur_button_frame.pack(pady=10)

btn1 = create_button(cur_button_frame, "DOWNLOAD", "~/Downloads")
btn2 = create_button(cur_button_frame, "SCREENSHOT", "~/Pictures/Screenshots")
btn3 = create_button(cur_button_frame, "GITHUB", "~/gitHub")

# Pack the buttons
buttons = [btn1, btn2, btn3]
for btn in buttons:
    btn.pack(side="top", pady=5)

# Launch the application
root.mainloop()
