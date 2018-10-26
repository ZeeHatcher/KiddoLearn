import tkinter as tk
from modules.login import *

HEADING = "Verdana 16 bold"
WINDOW_SIZE = "400x400+500+250"

class Application(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Kiddo Learn")
        self.geometry(WINDOW_SIZE)

        container = tk.Frame(self)
        container.pack(side="top", expand=True, fill="both")

        self.frames = {}

        for F in (MainMenu, Lesson):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame(MainMenu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class LoginMenu(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.title("Kiddo Learn")
        self.geometry(WINDOW_SIZE)

        heading = tk.Label(self, text="LOGIN", font=HEADING)
        heading.pack()

        container = tk.Frame(self)
        container.pack()

        self.message_var = tk.StringVar()
        message = tk.Label(container, textvariable=self.message_var)
        message.grid(row=3, column=1, columnspan=2)

        username = tk.Label(container, text="Username:")
        username.grid(row=1, column=1)

        password = tk.Label(container, text="Password:")
        password.grid(row=2, column=1)

        self.entry_username = tk.Entry(container)
        self.entry_username.grid(row=1, column=2)

        self.entry_password = tk.Entry(container, show="*")
        self.entry_password.grid(row=2, column=2)

        button_login = tk.Button(self, text="Login", command=self.check_login)
        button_login.pack()

        button_create = tk.Button(self, text="Create New Account", command=self.to_CreateAccountMenu)
        button_create.pack()

    def check_login(self):
        authorized = login(self.entry_username, self.entry_password)
        if authorized:
            self.destroy()
            Application().mainloop()
        else:
            self.message_var.set("Invalid username and/or password")

    def to_CreateAccountMenu(self):
        self.destroy()
        CreateAccountMenu().mainloop()

class CreateAccountMenu(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.title("Kiddo Learn")
        self.geometry(WINDOW_SIZE)

        heading = tk.Label(self, text="CREATE NEW ACCOUNT", font=HEADING)
        heading.pack()

        container = tk.Frame(self)
        container.pack()

        username = tk.Label(container, text="New Username:")
        username.grid(row=1, column=1)

        password = tk.Label(container, text="New Password:")
        password.grid(row=2, column=1)

        confirm = tk.Label(container, text="Confirm Password:")
        confirm.grid(row=3, column=1)

        self.message_var = tk.StringVar()
        message = tk.Label(container, textvariable=self.message_var)
        message.grid(row=5, column=1, columnspan=2)

        self.entry_username = tk.Entry(container)
        self.entry_username.grid(row=1, column=2)

        self.entry_password = tk.Entry(container, show="*")
        self.entry_password.grid(row=2, column=2)

        self.entry_confirm = tk.Entry(container, show="*")
        self.entry_confirm.grid(row=3, column=2)

        button_create = tk.Button(self, text="Create Account", command=self.check_create_account)
        button_create.pack()

        button_back = tk.Button(self, text="Back To Login Menu", command=self.to_LoginMenu)
        button_back.pack()

    def check_create_account(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm = self.entry_confirm.get()
        create = False
        existing_account_dict = check_file("account.txt")

        if username != "" and password != "" and confirm != "":
            if not(username in existing_account_dict["username"]):
                if confirm == password:
                    create = True
                else:
                    self.message_var.set("Please make sure your password is identical")
            else:
                self.message_var.set("Username has been taken.")
        else:
            self.message_var.set("Please fill in your username and password")

        for i in [username, password]:
            for letter in i:
                if letter == " ":
                    self.message_var.set("Please input a valid username and password")
                    create = False
                    break
                else:
                    continue

        if create:
            create_account(username, password)
            self.destroy()
            LoginMenu().mainloop()

    def to_LoginMenu(self):
        self.destroy()
        LoginMenu().mainloop()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        heading = tk.Label(self, text="Main Menu", font=HEADING)
        heading.pack()

class Lesson(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        heading = tk.Label(self, text="Lesson", font=HEADING)
        heading.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    LoginMenu().mainloop()
