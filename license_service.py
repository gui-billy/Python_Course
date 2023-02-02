import tkinter as tk
from tkinter import PhotoImage
import csv
from xmlrpc.server import SimpleXMLRPCServer


root = tk.Tk()
root.title("Example GUI")
root.geometry("400x400")

icon = PhotoImage(file="C:\\Users\\guilh\\iCloudDrive\\Logo - Algotrade\\Logo_Algotrade.png")
root.iconphoto(False, icon)

file_path = "C:\\Users\\guilh\\iCloudDrive\\Acesso_Clientes\\acesso.csv"

data = []
with open(file_path, newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    header_label = tk.Label(root, text="Headers: " + " ".join(headers))
    header_label.pack()

    for row in reader:
        data.append(row)
        row_label = tk.Label(root, text="Row: " + " ".join(row))
        row_label.pack()

def get_data():
    return data

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(get_data, "get_data")

root.mainloop()
server.serve_forever()
