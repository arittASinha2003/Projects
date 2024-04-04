import re
import tkinter as tk
from tkinter import messagebox

def password_strength():
    password = password_entry.get()
    with open('C:\\Users\\as200\\Desktop\\Programs\\Projects\\rockyou.txt', 'r', encoding='ISO-8859-1') as file:
        common_passwords = file.read().splitlines()

    # checking against common passwords
    if password in common_passwords:
        result = "Password is too common"
    # calculating the length
    elif len(password) < 8:
        result = "Password must be at least 8 characters long"
    # searching for digits
    elif re.search('[0-9]',password) is None:
        result = "Password must contain at least one number"
    # searching for uppercase
    elif re.search('[A-Z]',password) is None: 
        result = "Password must contain at least one uppercase letter"
    # searching for lowercase
    elif re.search('[a-z]',password) is None: 
        result = "Password must contain at least one lowercase letter"
    # searching for symbols
    elif re.search('[!@#$%^&*(),.?":{}|<>]',password) is None: 
        result = "Password must contain at least one special character"
    else:
        result = "Strong Password"

    messagebox.showinfo("Password Strength", result)

root = tk.Tk()
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root)
password_entry.pack()

check_button = tk.Button(root, text="Check Strength", command=password_strength)
check_button.pack()

root.mainloop()
