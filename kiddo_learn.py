import tkinter as tk
from modules.login import *
from modules.profiles import *

H1 = "Verdana 16 bold"
H2 = "Verdana 12 bold"
# MINI
MEDIUM = "400x400+500+250"
# LARGE

class LoginMenu(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.title("Kiddo Learn")
        self.geometry(MEDIUM)

        h1 = tk.Label(self, text="LOGIN", font=H1)
        h1.pack()

        container = tk.Frame(self)
        container.pack()

        self.message_var = tk.StringVar()
        message = tk.Label(container, textvariable=self.message_var)
        message.grid(row=2, column=0, columnspan=2)

        username = tk.Label(container, text="Username:")
        username.grid(row=0, column=0)

        password = tk.Label(container, text="Password:")
        password.grid(row=1, column=0)

        self.entry_username = tk.Entry(container)
        self.entry_username.grid(row=0, column=1)

        self.entry_password = tk.Entry(container, show="*")
        self.entry_password.grid(row=1, column=1)

        button_login = tk.Button(self, text="Login", command=self.check_login)
        button_login.pack()

        button_create = tk.Button(self, text="Create New Account", command=self.to_CreateAccountMenu)
        button_create.pack()

    def check_login(self):
        authorized = login(self.entry_username, self.entry_password)
        username = self.entry_username.get()

        if authorized:
            self.destroy()
            Application(username).mainloop()
        else:
            self.message_var.set("Invalid username and/or password")

    def to_CreateAccountMenu(self):
        self.destroy()
        CreateAccountMenu().mainloop()

class CreateAccountMenu(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.title("Kiddo Learn")
        self.geometry(MEDIUM)

        h1 = tk.Label(self, text="CREATE NEW ACCOUNT", font=H1)
        h1.pack()

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
        existing_accounts = check_file(accounts)

        if username != "" and password != "" and confirm != "":
            if confirm == password:
                create = True
            else:
                self.message_var.set("Please make sure your password is identical")
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

        for account in existing_accounts:
            if username == account["username"]:
                create = False
                self.message_var.set("Username has been taken.")
                break
            else:
                continue

        if create:
            f = format_txt(username)
            create_file(f)
            create_account(username, password)
            self.to_LoginMenu()

    def to_LoginMenu(self):
        self.destroy()
        LoginMenu().mainloop()

class Application(tk.Toplevel):
    def __init__(self, user):
        tk.Toplevel.__init__(self)
        self.title("Kiddo Learn")
        self.geometry(MEDIUM)
        self.user = user

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

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        h1 = tk.Label(self, text="Main Menu", font=H1)
        h1.pack()

        container = tk.Frame(self)
        container.pack(side="top", expand=True, fill="both")
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        self.info = ProfilesInfo(container, self.controller, self)
        self.info.grid(row=0, column=1)

        self.profiles = Profiles(container, self.controller, self)
        self.profiles.grid(row=0, column=0)

        buttons = tk.Frame(self)
        buttons.pack(side="top")

        button_lesson = tk.Button(buttons, text="Begin Lesson")
        button_lesson.pack(side="left")

        button_test = tk.Button(buttons, text="Test")
        button_test.pack(side="left")

class Profiles(tk.Frame):
    adding_profile = False

    def __init__(self, parent, app, main):
        tk.Frame.__init__(self, parent)
        self.user = app.user
        self.info = main.info

        h2 = tk.Label(self, text="Profiles", font=H2)
        h2.grid(row=0, column=0)

        button_add = tk.Button(self, text="Add Profile", command=self.add_profile)
        button_add.grid(row=0, column=1)

        self.update_profile()

    def add_profile(self):
        if Profiles.adding_profile == False:
            Profiles.adding_profile = True
            AddProfileMenu(self).mainloop()

    def update_profile(self):
        f = format_txt(self.user)

        try:
            profiles = check_file(f)
        except:
            create_file(f)
            profiles = check_file(f)

        row_count = 1
        for prof in profiles:
            name = prof["name"]
            age = prof["age"]

            Profile(self, name, self.info).grid(row=row_count, column=0, columnspan=2)
            row_count += 1


class AddProfileMenu(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.parent = parent

        self.protocol("WM_DELETE_WINDOW", self.cancel_profile)

        container = tk.Frame(self)
        container.pack(side="top", expand=True, fill="both")

        h2 = tk.Label(container, text="Add Profile", font=H2)
        h2.pack(side="top")

        entries = tk.Frame(container)
        entries.pack(side="top", expand=True, fill="both")

        name = tk.Label(entries, text="Name")
        name.grid(row=0, column=0)

        age = tk.Label(entries, text="Age")
        age.grid(row=1, column=0)

        gender = tk.Label(entries, text="Gender")
        gender.grid(row=2, column=0)

        self.entry_name = tk.Entry(entries)
        self.entry_name.grid(row=0, column=1)

        self.entry_age = tk.Entry(entries)
        self.entry_age.grid(row=1, column=1)

        self.gender_var = tk.StringVar()

        self.entry_gender = tk.Frame(entries)
        self.entry_gender.grid(row=2, column=1)

        self.entry_gender_m = tk.Radiobutton(self.entry_gender, text="Male", variable=self.gender_var, value="Male")
        self.entry_gender_m.pack(side="left")

        self.entry_gender_f = tk.Radiobutton(self.entry_gender, text="Female", variable=self.gender_var, value="Female")
        self.entry_gender_f.pack(side="left")

        buttons = tk.Frame(container)
        buttons.pack(side="top")

        button_confirm = tk.Button(buttons, text="Confirm", command=self.create_profile)
        button_confirm.pack(side="left")

        button_cancel = tk.Button(buttons, text="Cancel", command=self.cancel_profile)
        button_cancel.pack(side="left")

    def create_profile(self):
        f = format_txt(self.parent.user)
        try:
            profiles = check_file(f)
        except:
            create_file(f)
            profiles = check_file(f)

        prof = {"name": self.entry_name.get(),
                "age": self.entry_age.get(),
                "gender": self.gender_var.get(),
                "completed": "0",
                "points": "0",
                "grade": "~"
                }
        profiles.append(prof)

        with open(f, "w") as out_file:
            out_file.write("{}".format(profiles))

        self.parent.update_profile()
        Profiles.adding_profile = False
        self.destroy()

    def cancel_profile(self):
        Profiles.adding_profile = False
        self.destroy()

class ProfilesInfo(tk.Frame):
    def __init__(self, parent, app, main):
        tk.Frame.__init__(self, parent)
        self.user = app.user

        h2 = tk.Label(self, text="Info", font=H2)
        h2.grid(row=0, column=0, columnspan=2)

        self.info_list = ["Name", "Age", "Gender", "Lessons Completed", "Number Of Points", "Grade"]

        row_count = 1
        for info in self.info_list:
            tk.Label(self, text=info).grid(row=row_count, column=0, sticky="w")
            row_count += 1
            
        self.data = {}

    def display_values(self):
        row_count = 1
        for val in self.value_list:
            value_var = tk.StringVar()
            value_var.set(val)
            tk.Label(self, textvariable=value_var).grid(row=row_count, column=1)
            row_count += 1

class Profile(tk.Button):
    def __init__(self, parent, name, info):
        tk.Button.__init__(self, parent, text=name, command=self.update_info_data)
        self.user = parent.user
        self.name = name
        self.info = info

    def update_info_data(self):
        f = format_txt(self.user)
        try:
            profiles = check_file(f)
        except:
            create_file(f)
            profiles = check_file(f)

        for prof in profiles:
            if self.name == prof["name"]:
                self.info.data = prof
            else:
                continue

        self.info.display_values()

class Lesson(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        h1 = tk.Label(self, text="Lesson", font=H1)
        h1.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    try:
        check_file(r"data\accounts.txt")
        LoginMenu().mainloop()
    except:
        create_file(r"data\accounts.txt")
        CreateAccountMenu().mainloop()
