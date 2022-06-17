import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Body Measurements")

# window size
window_width = 600
window_height = 400

# screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# screen center
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# root settings
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

ttk.Label(root, text='Weight in lbs').pack()
ttk.Entry(root).pack()

root.mainloop() # keep at end
