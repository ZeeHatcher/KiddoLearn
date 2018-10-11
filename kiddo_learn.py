import tkinter as tk
from modules.login import *

# Main Window
root = tk.Tk()
root.title("Kiddo Learn")
root.geometry("500x500")
root["bg"] = "white"
def_bg = root.cget("bg")

# Login Mene
frame_loginmenu = tk.Frame(root, bg=def_bg)
frame_username = tk.Frame(frame_loginmenu, bg=def_bg)
frame_password = tk.Frame(frame_loginmenu, bg=def_bg)

label_title = tk.Label(frame_loginmenu, text="Kiddo Learn", fg="orange", bg=def_bg, font="Helvetica 25 bold")
label_username = tk.Label(frame_username, bg=def_bg, text="Username: ")
label_password = tk.Label(frame_password, bg=def_bg, text="Password:  ")

entry_username = tk.Entry(frame_username)
entry_password = tk.Entry(frame_password)

button_login = tk.Button(frame_loginmenu, text="Login", command=lambda : login(entry_username, entry_password))
button_createaccount = tk.Button(frame_loginmenu, text="Create New Account", command="")

frame_loginmenu.place(relx=0.5, rely=0.4, anchor="center")

label_title.pack()

frame_username.pack(pady=5)
label_username.pack(side="left")
entry_username.pack(side="right")

frame_password.pack(pady=5)
label_password.pack(side="left")
entry_password.pack(side="right")

button_login.pack()
button_createaccount.pack(pady=5)

# mainloop
root.mainloop()
