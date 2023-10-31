import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "You have successfully logged in!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
window = tk.Tk()
window.title("Login Form")

# Create username label and entry
label_username = tk.Label(window, text="Username:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# Create password label and entry
label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create login button
btn_login = tk.Button(window, text="Login", command=validate_login)
btn_login.pack()

# Start the main loop
window.mainloop()