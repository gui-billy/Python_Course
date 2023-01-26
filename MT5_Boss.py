import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import filedialog

def open_mt5():
    # code to open the MetaTrader 5 terminal
    subprocess.Popen("C:\\Program Files\\MetaTrader 5 Terminal\\terminal64.exe")

def change_icon():
    # code to change the icon of the window
    icon_path = filedialog.askopenfilename(title = "Select Icon", filetypes = (("ico files", "*.ico"), ("all files", "*.*")))
    root.iconbitmap(icon_path)

root = tk.Tk()
root.title("Open MT5")
root.geometry("400x200")

open_mt5_button = ttk.Button(root, text="Open MT5", command=open_mt5)
open_mt5_button.pack()

change_icon_button = ttk.Button(root, text="Change Icon", command=change_icon)
change_icon_button.pack()

root.mainloop()