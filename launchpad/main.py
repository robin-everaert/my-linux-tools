#!/usr/bin/env python3
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button
import tkinter as tk
import os

# Create the main window
root = tk.Tk()
root.tk.call("tk", "scaling", 1.0)
root.title("")
root.attributes("-topmost", True) # z-index

# Define the size of the window (code by chat GPT)
window_width = 150  
window_height = 280 
root.update_idletasks()  
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_offset = screen_width - window_width  
y_offset = screen_height - window_height  
if window_height > screen_height:
    window_height = screen_height
if window_width > screen_width:
    window_width = screen_width
root.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")

# Initialize the style (ttk library)
style = Style(theme="darkly")
style.configure(
    "Custom.TButton",
    font=("Sans-serif", 16, "bold"),
    background="#B80808",
    foreground="#ececec",
    borderwidth=0, 
    relief="flat"
)
style.map( # Hover
    "Custom.TButton",
    background=[("active", "#FF5733")],  
    foreground=[("active", "#FFFFFF")]  
)

# Function to open folder 
def open_folder(path):
    full_path = os.path.expanduser(path)  
    os.system(f'xdg-open "{full_path}"') 

# Function to create styled buttons function
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
btn4 = create_button(cur_button_frame, "NS CUR", "~/work/nutrisolution/current")
btn5 = create_button(cur_button_frame, "NS SERV 1", "~/work/nutrisolution/servers/server_1/www")
btn6 = create_button(cur_button_frame, "NS SERV 2", "~/work/nutrisolution/servers/server_2/www")
btn7 = create_button(cur_button_frame, "WIP", "~/work/wip")

# Pack the buttons
buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7]
for btn in buttons:
    btn.pack(side="top", pady=5)

# Launch the application
root.mainloop()
