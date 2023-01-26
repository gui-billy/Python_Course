import tkinter as tk
from tkinter import ttk
import ccxt

def get_btc_price():
    # Initialize the Binance exchange object
    binance = ccxt.binance()
    # Get the ticker for the BTC/USDT symbol
    ticker = binance.fetch_ticker("BTC/USDT")
    # Return the last price
    return ticker["last"]

def on_close():
    # code to close the window
    root.destroy()

def on_minimize():
    # code to minimize the window
    root.iconify()

def on_maximize():
    # code to maximize the window
    root.state("normal")

root = tk.Tk()
root.title("Bitcoin Price")
root.geometry("400x200")

btc_price = get_btc_price()
price_label = ttk.Label(root, text=f"Bitcoin Price: ${btc_price}")
price_label.pack()



root.mainloop()
