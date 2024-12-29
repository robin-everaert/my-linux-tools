#!/home/kibs/gitHub/my-linux-tools/controldesk/env/bin/python
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button
from tkinter import font

import tkinter as tk
import psutil
import threading
import time

# -------------
# Create the main window
# -------------
root = tk.Tk()
root.title("Surveillance Réseau")
root.tk.call("tk", "scaling", 1)
root.attributes("-topmost", True)  # z-index

# -------------
# Define the size of the window
# -------------
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

# -------------
# Initialize the style (ttk library)
# -------------
style = Style(theme="darkly")
# Créer une police par défaut
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Ubuntu", size=14)  # Police et taille
root.option_add("*Font", default_font)

style.configure(
    "Custom.TButton",
    font=("Segoe UI", 16, "bold"),
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


# -------------
# NETWORK
# -------------
def convert_to_mbps(bytes_per_sec):
    return (bytes_per_sec * 8) / 1_000_000  # Convert bytes/sec to Mbps

def monitor_network(sent_label, recv_label):

    old_value = psutil.net_io_counters()
    while True:
        time.sleep(1)  # 1sc
        new_value = psutil.net_io_counters()
        
        # Difference between sent and recieve
        bytes_sent = new_value.bytes_sent - old_value.bytes_sent
        bytes_recv = new_value.bytes_recv - old_value.bytes_recv
        
        # Mbps conversion
        sent_mbps = convert_to_mbps(bytes_sent)
        recv_mbps = convert_to_mbps(bytes_recv)
           
        # Labels update
        sent_label.config(text=f"Upload : {sent_mbps:.2f} Mbps")
        recv_label.config(text=f"Download : {recv_mbps:.2f} Mbps")
        old_value = new_value

# Add labels
sent_label = tk.Label(root)
recv_label = tk.Label(root)

# Positioning labels
sent_label.pack(pady=2, padx=(1, 0), anchor="w")
recv_label.pack(pady=2, padx=(1, 0), anchor="w")

# Starting network observer in new thread
thread = threading.Thread(target=monitor_network, args=(sent_label, recv_label))
thread.daemon = True  
thread.start()

# -------------
# NETWORK
# -------------







# -------------
# Launch the application
# -------------
root.mainloop()
