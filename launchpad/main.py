#!/home/kibs/gitHub/my-linux-tools/launchpad/env/bin/python
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button
import tkinter as tk
import os

# Create the main window
root = tk.Tk()
root.title("")
root.tk.call("tk", "scaling", 1.0)
root.attributes("-topmost", True) # z-index

# Define the size of the window (code by chat GPT)
window_width = 160  
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

button_data = [
    ("ROOT", "/"),
    ("DOWNLOAD", "~/Downloads"),
    ("SCREENSHOT", "~/Pictures/Screenshots"),
    ("GITHUB", "~/"),
    ("NS CUR", "~/"),
    ("NS SERV 1", "~/"),
    ("NS SERV 2", "~/"),
    ("WIP", "~/"),
]

for text, path in button_data:
    btn = create_button(cur_button_frame, text, path)
    btn.pack(side="top", pady=5)

# Launch the application
root.mainloop()
