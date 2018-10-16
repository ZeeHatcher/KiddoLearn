import tkinter as tk
from modules.login import *

HEADING = "Verdana 16 bold"

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Kiddo Learn")
        self.geometry("400x400")
        container = tk.Frame(self)
        container.pack(side="top", expand=True, fill="both")

        self.frames = {}

        for F in (LoginMenu, CreateAccountMenu, MainMenu):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame(LoginMenu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class LoginMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

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

        self.entry_password = tk.Entry(container)
        self.entry_password.grid(row=2, column=2)

        button_login = tk.Button(self, text="Login", command=self.check_login)
        button_login.pack()

        button_create = tk.Button(self, text="Create New Account", command=lambda : controller.show_frame(CreateAccountMenu))
        button_create.pack()

    def check_login(self):
        authorized = login(self.entry_username, self.entry_password)
        if authorized:
            self.controller.show_frame(MainMenu)
        else:
            self.message_var.set("Invalid username and/or password")


class CreateAccountMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

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

        self.entry_password = tk.Entry(container)
        self.entry_password.grid(row=2, column=2)

        self.entry_confirm = tk.Entry(container)
        self.entry_confirm.grid(row=3, column=2)

        button = tk.Button(self, text="Create Account", command=self.check_create_account)
        button.pack()

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
            self.controller.show_frame(LoginMenu)

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        heading = tk.Label(self, text="Main Menu", font=HEADING)
        heading.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
