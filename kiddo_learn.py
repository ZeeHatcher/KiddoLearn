import tkinter as tk
from modules.login import *

# Main Window
root = tk.Tk()
root.title("Kiddo Learn")
root.geometry("500x500")
root["bg"] = "white"
def_bg = root.cget("bg")

# Login Menu
frame_loginmenu = tk.Frame(root, bg=def_bg)
frame_username = tk.Frame(frame_loginmenu, bg=def_bg)
frame_password = tk.Frame(frame_loginmenu, bg=def_bg)

label_title = tk.Label(frame_loginmenu, text="Kiddo Learn", fg="orange", bg=def_bg, font="Helvetica 25 bold")
label_username = tk.Label(frame_username, bg=def_bg, text="Username: ")
label_password = tk.Label(frame_password, bg=def_bg, text="Password:  ")

entry_username = tk.Entry(frame_username)
entry_password = tk.Entry(frame_password)

button_login = tk.Button(frame_loginmenu, text="Login", command=lambda : login(entry_username, entry_password, frame_mainmenu))
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

# Main Menu
frame_mainmenu = tk.Frame(root, bg=def_bg)
frame_profiles = tk.Frame(frame_mainmenu, bg=def_bg)
frame_info = tk.Frame(frame_mainmenu, bg=def_bg)

label_mainmenu = tk.Label(frame_mainmenu, bg=def_bg, text="Main Menu", font="Times 15 bold")
label_profiles = tk.Label(frame_profiles, bg=def_bg, text="Profiles", font="Times 10 bold")
label_info = tk.Label(frame_info, bg=def_bg, text="Information", font="Times 10 bold")

frame_mainmenu.place(relx=0.5, rely=0.5, anchor="center")
label_mainmenu.pack()
frame_profiles.pack()
label_profiles.pack()
frame_info.pack()
label_info.pack()



# mainloop
root.mainloop()
