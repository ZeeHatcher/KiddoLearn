import tkinter as tk
from modules.login import *

# Main Window
root = tk.Tk()
root.title("Kiddo Learn")
root.geometry("500x500")
root["bg"] = "white"
def_bg = root.cget("bg")

container = tk.Frame(root, bg=def_bg, padx=100, pady=100)
container.pack(fill="both", expand=True)

# Login Menu
lg = tk.Frame(container, bg=def_bg)
lg_form_fr = tk.Frame(lg, bg=def_bg)

lg_title_lb = tk.Label(lg, text="Kiddo Learn", fg="orange", bg=def_bg, font="Helvetica 25 bold")
lg_username_lb = tk.Label(lg_form_fr, bg=def_bg, text="Username: ")
lg_password_lb = tk.Label(lg_form_fr, bg=def_bg, text="Password:  ")

lg_username_ent = tk.Entry(lg_form_fr)
lg_password_ent = tk.Entry(lg_form_fr)

lg_login_bt = tk.Button(lg, text="Login", command=lambda : login(lg_username_ent, lg_password_ent, main))
lg_create_bt = tk.Button(lg, text="Create New Account", command=lambda : (lg.pack_forget(), display_crtacc()))

def display_lg() :
    lg.pack(fill="both", expand=True)

    lg_title_lb.pack()

    lg_form_fr.pack(pady=5)

    lg_username_lb.grid(row=1, column=1)
    lg_username_ent.grid(row=1, column=2)

    lg_password_lb.grid(row=2, column=1)
    lg_password_ent.grid(row=2, column=2)

    lg_login_bt.pack()
    lg_create_bt.pack(pady=5)

# Create Account Menu
crtacc = tk.Frame(container, bg=def_bg)
crtacc_form_fr = tk.Frame(crtacc, bg=def_bg)

crtacc_title_lb = tk.Label(crtacc, text="Create New Account", bg=def_bg, font="Helvetica 15 bold")
crtacc_username_lb = tk.Label(crtacc_form_fr, bg=def_bg, text="Username: ")
crtacc_password_lb = tk.Label(crtacc_form_fr, bg=def_bg, text="Password:  ")
crtacc_confirm_lb = tk.Label(crtacc_form_fr, bg=def_bg, text="Confirm Password:  ")

crtacc_username_ent = tk.Entry(crtacc_form_fr)
crtacc_password_ent = tk.Entry(crtacc_form_fr)
crtacc_confirm_ent = tk.Entry(crtacc_form_fr)

crtacc_create_bt = tk.Button(crtacc, text="Confirm", command=lambda : (crtacc.pack_forget(), display_lg()))

def display_crtacc() :
    crtacc.pack(fill="both", expand=True)

    crtacc_title_lb.pack(fill="both")

    crtacc_form_fr.pack(pady=5)

    crtacc_username_lb.grid(row=1, column=1, sticky="e")
    crtacc_username_ent.grid(row=1, column=2, sticky="w")

    crtacc_password_lb.grid(row=2, column=1, sticky="e")
    crtacc_password_ent.grid(row=2, column=2, sticky="w")

    crtacc_confirm_lb.grid(row=3, column=1, sticky="e")
    crtacc_confirm_ent.grid(row=3, column=2, sticky="w")

    crtacc_create_bt.pack(pady=5)

# Main Menu
main = tk.Frame(container, bg=def_bg)
main_profiles_fr = tk.Frame(main, bg=def_bg)
main_info_fr = tk.Frame(main, bg=def_bg)

main_title_lb = tk.Label(main, bg=def_bg, text="Main Menu", font="Times 15 bold")
main_profiles_lb = tk.Label(main_profiles_fr, bg=def_bg, text="Profiles", font="Times 10 bold")
main_info_lb = tk.Label(main_info_fr, bg=def_bg, text="Information", font="Times 10 bold")

def display_main() :
    main.place(relx=0.5, rely=0.5, anchor="center")
    main_title_lb.pack()
    main_profiles_fr.pack()
    main_profiles_lb.pack()
    main_info_fr.pack()
    main_info_lb.pack()

# mainloop
display_lg()

root.mainloop()
