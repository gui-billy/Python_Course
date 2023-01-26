import tkinter as tk
from tkinter import messagebox

def check_cpf():
    cpf = entry.get()
    if len(cpf) != 11:
        messagebox.showerror("Error", "CPF must have 11 digits.")
        return
    if not cpf.isdigit():
        messagebox.showerror("Error", "CPF can only contain numbers.")
        return
    if cpf == "00000000000" or cpf == "11111111111" or cpf == "22222222222" or cpf == "33333333333" or cpf == "44444444444" or cpf == "55555555555" or cpf == "66666666666" or cpf == "77777777777" or cpf == "88888888888" or cpf == "99999999999":
        messagebox.showerror("Error", "Invalid CPF.")
        return
    else:
        # Calculating 1st digit
        first_digit = 0
        for i in range(9):
            first_digit += int(cpf[i]) * (10 - i)
        first_digit = ((first_digit*10) % 11)
        if first_digit > 9:
            first_digit = 0
        # Calculating 2nd digit
        second_digit = 0
        for i in range(10):
            if i<9:
                second_digit += int(cpf[i]) * (11 - i)       
            else:
                second_digit += int(first_digit) * (11 - i)
        second_digit = ((second_digit*10) % 11)
        if second_digit > 9:
            second_digit = 0
        # Checking if both digits match
        if int(cpf[-2]) != first_digit or int(cpf[-1]) != second_digit:
            messagebox.showerror("Error", "Invalid CPF.")
            return
        messagebox.showinfo("Success", "CPF is valid.")

root = tk.Tk()
root.title("CPF Validator")
root.geometry("400x200")
root.bind('<Return>', check_cpf)

label = tk.Label(root, text="Enter CPF:")
label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_cpf)
check_button.pack()

root.mainloop()

