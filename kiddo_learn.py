import tkinter as tk
from modules.login import *
from modules.lesson import *

# Constants for color, size, fonts, etc.
SUBMIT = "#81ff42"
SUBMIT_D = "#5fc12e"
MISC = "#c4faff"
MISC_D = "#99c5c9"
CANCEL = "#ff7663"
CANCEL_D= "#c65c4d"
H1 = "Verdana 16 bold"
H2 = "Verdana 12 bold"
# MINI
MEDIUM = "400x400+500+250"
LARGE = "800x600+250+250"

class LoginMenu(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.title("Kiddo Learn")
        self.geometry(MEDIUM)
        self.resizable(False, False)

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4)

        logo_img = tk.PhotoImage(file=r"images\kiddo_learn.gif")
        logo = tk.Label(frame, image=logo_img)
        logo.image = logo_img
        logo.pack(side="top", pady=10)

        h1 = tk.Label(frame, text="LOGIN", font=H1)
        h1.pack(side="top", pady=10)

        entries = tk.Frame(frame)
        entries.pack(side="top")

        username = tk.Label(entries, text="Username:")
        username.grid(row=0, column=0, sticky="e", padx=5)

        password = tk.Label(entries, text="Password:")
        password.grid(row=1, column=0, sticky="e", padx=5)

        self.entry_username = tk.Entry(entries, width=20)
        self.entry_username.grid(row=0, column=1, sticky="w", padx=5)

        self.entry_password = tk.Entry(entries, show="*", width=20)
        self.entry_password.grid(row=1, column=1, sticky="w", padx=5)

        self.message_var = tk.StringVar()
        message = tk.Label(entries, textvariable=self.message_var)
        message.grid(row=2, column=0, columnspan=2, pady=10)

        button_login = tk.Button(frame, text="Login", command=self.check_login, bg=SUBMIT, activebackground=SUBMIT_D)
        button_login.pack(side="top", pady=2)

        button_create = tk.Button(frame, text="Create New Account", command=self.to_CreateAccountMenu, bg=MISC, activebackground=MISC_D)
        button_create.pack(side="top", pady=2)

    def check_login(self):
        authorized = login(self.entry_username, self.entry_password)
        username = self.entry_username.get()

        if authorized:
            self.destroy()
            Application.user = username
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
        self.geometry(MEDIUM)
        self.resizable(False, False)

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4)

        h1 = tk.Label(frame, text="CREATE NEW ACCOUNT", font=H1)
        h1.pack(side="top", pady=10)

        entries = tk.Frame(frame)
        entries.pack(side="top")

        username = tk.Label(entries, text="New Username:")
        username.grid(row=1, column=1, sticky="e", padx=5)

        password = tk.Label(entries, text="New Password:")
        password.grid(row=2, column=1, sticky="e", padx=5)

        confirm = tk.Label(entries, text="Confirm Password:")
        confirm.grid(row=3, column=1, sticky="e", padx=5)

        self.entry_username = tk.Entry(entries)
        self.entry_username.grid(row=1, column=2, sticky="w", padx=5)

        self.entry_password = tk.Entry(entries, show="*")
        self.entry_password.grid(row=2, column=2, sticky="w", padx=5)

        self.entry_confirm = tk.Entry(entries, show="*")
        self.entry_confirm.grid(row=3, column=2, sticky="w", padx=5)

        self.message_var = tk.StringVar()
        message = tk.Label(entries, textvariable=self.message_var)
        message.grid(row=4, column=1, columnspan=2, pady=10)

        button_create = tk.Button(frame, text="Confirm", command=self.check_create_account, bg=SUBMIT, activebackground=SUBMIT_D)
        button_create.pack(side="top", pady=2)

        button_back = tk.Button(frame, text="Cancel", command=self.to_LoginMenu, bg=CANCEL, activebackground=CANCEL_D)
        button_back.pack(side="top", pady=2)

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
                    self.message_var.set("Only lowercase/uppercase alphabets, numbers and symbols are allowed")
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
    user = ""
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Kiddo Learn")
        self.geometry(LARGE)
        self.resizable(False, False)

        self.active_frame = MainMenu(self)
        self.active_frame.place(x=0, y=0, relwidth=1, relheight=1)

class MainMenu(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4, relwidth=1)

        h1 = tk.Label(frame, text="Main Menu", font=H1)
        h1.pack(side="top", pady=10)

        content = tk.Frame(frame)
        content.pack(side="top", expand=True, fill="both")
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)

        self.info = ProfilesInfo(content, self)
        self.info.grid(row=0, column=1, sticky="nsew", padx=10)

        self.profiles = Profiles(content, self)
        self.profiles.grid(row=0, column=0, sticky="nsew", padx=10)

        buttons = tk.Frame(frame)
        buttons.pack(side="top")

        button_lesson = tk.Button(buttons, text="Begin Lesson", command=self.to_LessonMenu)
        button_lesson.pack(side="left")

        button_test = tk.Button(buttons, text="Test")
        button_test.pack(side="left")

        button_logout = tk.Button(buttons, text="Logout", command=self.to_LoginMenu)
        button_logout.pack(side="left")

    def to_LoginMenu(self):
        LessonMenu.profile = ""
        Application.user = ""
        self.controller.destroy()
        LoginMenu().mainloop()

    def to_LessonMenu(self):
        if LessonMenu.profile != "":
            self.controller.active_frame = LessonMenu(self.controller)
            self.controller.active_frame.place(x=0, y=0, relwidth=1, relheight=1)
            self.destroy()
        else:
            print("Please select a profile before proceeding.")

class Profiles(tk.Frame):
    adding_profile = False

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.profiles_list = []

        self.grid_propagate(False)
        self["height"] = 300

        h2 = tk.Label(self, text="Profiles", font=H2)
        h2.pack(side="top")

        button_add = tk.Button(self, text="Add Profile", command=self.add_profile)
        button_add.pack(side="bottom", pady=10)

        self.update_profiles()

    def add_profile(self):
        if Profiles.adding_profile == False:
            Profiles.adding_profile = True
            AddProfileMenu(self).mainloop()

    def update_profiles(self):
        for prof in self.profiles_list:
            prof.destroy()

        self.profiles_list = []

        f = format_txt(Application.user)

        try:
            profiles = check_file(f)
        except:
            create_file(f)
            profiles = check_file(f)

        row_count = 1
        for prof in profiles:
            name = prof["name"]
            age = prof["age"]

            p = Profile(self, name)
            p.pack(side="top")
            self.profiles_list.append(p)

            row_count += 1

class Profile(tk.Button):
    def __init__(self, parent, name):
        tk.Button.__init__(self, parent, text=name, command=self.select_profile)
        self.name = name
        self.parent = parent
        self.info = parent.controller.info
        self.selected = False
        self["width"] = 25

    def select_profile(self):
        LessonMenu.profile = self.name

        f = format_txt(Application.user)
        try:
            profiles = check_file(f)
        except:
            create_file(f)
            profiles = check_file(f)

        for prof in profiles:
            if self.name == prof["name"]:
                self.info.var_list[0].set(prof["name"])
                self.info.var_list[1].set(prof["age"])
                self.info.var_list[2].set(prof["gender"])
                self.info.var_list[3].set(prof["completed"])
                self.info.var_list[4].set(prof["points"])
                self.info.var_list[5].set(prof["grade"])
            else:
                continue

        for prof in self.parent.profiles_list:
            prof.selected = False
            prof["bg"] = "#f0f0f0"

        self.selected = True
        self["bg"] = "#c4faff"

class ProfilesInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self["height"] = 200

        self.pack_propagate(False)

        h2 = tk.Label(self, text="Info", font=H2)
        h2.pack(side="top")

        self.infos = tk.Frame(self)
        self.infos.pack(side="top", expand=True, fill="both")
        self.infos.columnconfigure(0, weight=1)
        self.infos.columnconfigure(1, weight=1)

        self.info_list = ["Name", "Age", "Gender", "Lessons Completed", "Number Of Points", "Grade"]

        self.var_list = []
        for x in range(6):
            self.var_list.append(tk.StringVar())

        for info in self.info_list:
            i = self.info_list.index(info)
            tk.Label(self.infos, text=info).grid(row=i, column=0, sticky="w")
            tk.Label(self.infos, textvariable=self.var_list[i]).grid(row=i, column=1, sticky="e")

        self.delete = tk.Button(self, text="Delete Profile", command=self.delete_profile)
        self.delete.pack(side="top")

    def delete_profile(self):
        for prof in self.controller.profiles.profiles_list:
            if prof.selected:
                i = self.controller.profiles.profiles_list.index(prof)
                prof.destroy()
                self.controller.profiles.profiles_list.pop(i)

                for var in self.var_list:
                    var.set("")

                f = format_txt(Application.user)
                try:
                    profiles = check_file(f)
                except:
                    create_file(f)
                    profiles = check_file(f)

                for p in profiles:
                    if prof.name == p["name"]:
                        profiles.pop(profiles.index(p))
                    else:
                        continue

                with open(f, "w") as out_file:
                    out_file.write("{}".format(profiles))

                LessonMenu.profile = ""
                
            else:
                continue
        
class AddProfileMenu(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.controller = controller

        self.protocol("WM_DELETE_WINDOW", self.quit_profile)

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

        self.message_var = tk.StringVar()
        self.message = tk.Label(entries, textvariable=self.message_var)
        self.message.grid(row=3, column=1)

        buttons = tk.Frame(container)
        buttons.pack(side="top")

        button_confirm = tk.Button(buttons, text="Confirm", command=self.check_profile)
        button_confirm.pack(side="left")

        button_cancel = tk.Button(buttons, text="Cancel", command=self.quit_profile)
        button_cancel.pack(side="left")

    def check_profile(self):
        if (self.entry_name.get() != "") and (self.entry_age.get() != "") and (self.gender_var.get() != ""):
            self.create_profile()
        else:
            self.message_var.set("Please fill in the required information")

    def create_profile(self):
        f = format_txt(Application.user)
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
                "grade": "~",
                "stage": {"alphabet": 0,
                          "numbers": 0,
                          "food": 0,
                          "animals": 0,
                          "colors": 0,
                          "days & months": 0
                          }
                }

        profiles.append(prof)

        with open(f, "w") as out_file:
            out_file.write("{}".format(profiles))

        self.controller.update_profiles()
        self.controller.profiles_list[-1].select_profile()
        self.quit_profile()

    def quit_profile(self):
        Profiles.adding_profile = False
        self.destroy()

class LessonMenu(tk.Frame):
    profile = ""
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller
        self.profile = ""

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4, relwidth=1)

        h1 = tk.Label(frame, text="Lessons", font=H1)
        h1.pack(side="top", pady=10)

        lessons = tk.Frame(frame)
        lessons.pack(side="top", pady=10)

        back = tk.Button(frame, text="Back To Main Menu", command=self.to_MainMenu)
        back.pack(side="top", pady=10)

        lessons_list = ["Alphabet", "Numbers", "Food", "Animals", "Colors","Days & Months"]

        for l in lessons_list:
            i = lessons_list.index(l)

            if i < len(lessons_list) / 2:
                LessonMenuButton(lessons, self, l).grid(row=0, column=i)
            else:
                LessonMenuButton(lessons, self, l).grid(row=1, column=int(i-(len(lessons_list) / 2)))

    def to_MainMenu(self):
        LessonMenu.profile = ""
        self.controller.active_frame = MainMenu(self.controller)
        self.controller.active_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    try:
        check_file(r"data\accounts.txt")
        LoginMenu().mainloop()
    except:
        create_file(r"data\accounts.txt")
        CreateAccountMenu().mainloop()
