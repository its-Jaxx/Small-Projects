import pyautogui as pui
import time

try:
    import tkinter as tk
    from tkinter import scrolledtext
except ImportError:
    import subprocess
    subprocess.run(['pip', 'install', 'tk'])
    import tkinter as tk
    from tkinter import scrolledtext

bound_key = 'F10'
bind_key = f'<{bound_key}>'
coordinates_list = []

def update_position_label():
    mouse_position = pui.position()
    position_label.config(text=f"Mouse Position: {mouse_position}")
    root.after(10, update_position_label)

def save_coordinate(event):
    if event.keysym == bound_key:
        coordinates_list.append(pui.position())
        update_coordinates_label()

def update_coordinates_label():
    coordinates_text.config(state=tk.NORMAL)
    coordinates_text.delete('1.0', tk.END)
    for i, coord in enumerate(coordinates_list, start=1):
        coordinates_text.insert(tk.END, f"Position {i}: {coord}\n")
    coordinates_text.config(state=tk.DISABLED)
    coordinates_text.yview_moveto(1.0)
    root.update_idletasks()

root = tk.Tk()
root.title("Mouse Position Tracker")

initial_width = 400
root.geometry(f"{initial_width}x200")

position_label = tk.Label(root, text="Mouse Position: ")
position_label.pack(pady=10)

instruction_label = tk.Label(root, text=f"Press {bound_key} to save the coordinate")
instruction_label.pack(pady=5)

coordinates_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
coordinates_text.pack(pady=10)

root.bind(bind_key, save_coordinate)

update_position_label()

root.mainloop()
