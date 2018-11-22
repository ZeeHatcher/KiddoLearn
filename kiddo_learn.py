import tkinter as tk
from fileio import *
from lesson import *
from exercise import *

# Constants for color, size, fonts, etc.
SUBMIT = "#81ff42"
SUBMIT_D = "#5fc12e"
MISC = "#c4faff"
MISC_D = "#99c5c9"
SPECIAL = "#fff189"
SPECIAL_D = "#d1c56e"
CANCEL = "#ff7663"
CANCEL_D= "#c65c4d"
H1 = "Verdana 16 bold"
H2 = "Verdana 12 bold"
# MINI
MEDIUM = "500x500+500+250"
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
        existing_accounts = check_file(accounts)

        username = self.entry_username.get()
        password = self.entry_password.get()

        for account in existing_accounts:
            if username == account["username"] and password == account["password"]:
                authorized = True
                break
            else:
                authorized = False
                continue

        if authorized:
            self.destroy()
            Application.user = username
            Application()
        else:
            self.message_var.set("Invalid username and/or password")

    def to_CreateAccountMenu(self):
        self.destroy()
        CreateAccountMenu()

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

            new_account = {"username": username, "password": password}
            existing_accounts = check_file(accounts)
            existing_accounts.append(new_account)

            with open(accounts, "w") as out_file:
                out_file.write("{}".format(existing_accounts))

            self.to_LoginMenu()

    def to_LoginMenu(self):
        self.destroy()
        LoginMenu()

class Application(tk.Toplevel):
    user = None
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Kiddo Learn")
        self.geometry(LARGE)
        self.resizable(False, False)

        self.active_frame = MainMenu(self)
        self.active_frame.place(x=0, y=50, relwidth=1, relheight=1)

        logo_img = tk.PhotoImage(file=r"images\kiddo_learn.gif")
        self.logo = tk.Label(self, image=logo_img)
        self.logo.image = logo_img
        self.logo.place(anchor="n", relx=0.5, y=25, relwidth=1)

class MainMenu(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4, relwidth=1)

        h1 = tk.Label(frame, text="Main Menu", font=H1)
        h1.pack(side="top", pady=10)

        content = tk.Frame(frame)
        content.pack(side="top", expand=True, fill="both", padx="50")
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)

        self.info = ProfilesInfo(content, self)
        self.info.grid(row=0, column=1, sticky="nsew", padx=10)

        self.profiles = Profiles(content, self)
        self.profiles.grid(row=0, column=0, sticky="nsew", padx=10)

        buttons = tk.Frame(frame)
        buttons.pack(side="top")

        self.button_lesson = tk.Button(buttons, text="Lesson", command=self.to_LessonMenu_Test, width=10, state="disabled", bg=MISC, activebackground=MISC_D)
        self.button_lesson.pack(side="left", padx=10)

        self.button_test = tk.Button(buttons, text="Test", command=self.to_LessonMenu_Exercise, width=10, state="disabled", bg=SPECIAL, activebackground=SPECIAL_D)
        self.button_test.pack(side="left", padx=10)

        self.button_logout = tk.Button(buttons, text="Logout", command=self.to_LoginMenu, width=10)
        self.button_logout.pack(side="left", padx=10)

    def to_LoginMenu(self):
        LessonMenu.profile = None
        Application.user = None
        self.controller.destroy()
        LoginMenu()

    def to_LessonMenu(self):
        self.controller.active_frame = LessonMenu(self.controller)
        self.controller.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.controller.logo.lift()
        self.destroy()

    def to_LessonMenu_Test(self):
        LessonMenu.test = False
        self.to_LessonMenu()

    def to_LessonMenu_Exercise(self):
        LessonMenu.test = True
        self.to_LessonMenu()

class Profiles(tk.Frame):
    adding_profile = False

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.profiles_list = []

        self.pack_propagate(False)
        self["height"] = 300

        h2 = tk.Label(self, text="Profiles", font=H2, pady=5)
        h2.pack(side="top")

        buttons = tk.Frame(self)
        buttons.pack(side="top", pady=5)

        self.button_add = tk.Button(buttons, text="Add Profile", command=self.add_profile, bg=SUBMIT, activebackground=SUBMIT_D, width=10)
        self.button_add.pack(side="left", padx=10)

        self.button_delete = tk.Button(buttons, text="Delete Profile", command=self.delete_profile, bg=CANCEL, activebackground=CANCEL_D, state="disabled", width=10)
        self.button_delete.pack(side="left", padx=10)

        self.profs = tk.Frame(self, relief="groove", borderwidth=1)
        self.profs.pack(side="top", pady=10, ipadx=5, ipady=5, fill="y")
        self.update_profiles()

    def add_profile(self):
        if Profiles.adding_profile == False:
            Profiles.adding_profile = True
            AddProfileMenu(self)

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

            p = Profile(self.profs, self, name)
            p.pack(side="top")
            self.profiles_list.append(p)

            row_count += 1

    def delete_profile(self):
        for prof in self.profiles_list:
            if prof.selected:
                i = self.profiles_list.index(prof)
                prof.destroy()
                self.profiles_list.pop(i)

                for var in self.controller.info.var_list:
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

                LessonMenu.profile = None

            else:
                continue

        self.button_delete["state"] = "disabled"
        self.controller.button_lesson["state"] = "disabled"
        self.controller.button_test["state"] = "disabled"

class Profile(tk.Button):
    def __init__(self, parent, controller, name):
        tk.Button.__init__(self, parent, text=name, command=self.select_profile)
        self.name = name
        self.controller = controller
        self.info = controller.controller.info
        self.selected = False
        self["width"] = 30
        self["borderwidth"] = 1
        self["bg"] = "white"

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

        for prof in self.controller.profiles_list:
            prof.selected = False
            prof["bg"] = "white"

        self.controller.controller.profiles.button_delete["state"] = "normal"
        self.controller.controller.button_lesson["state"] = "normal"
        self.controller.controller.button_test["state"] = "normal"

        self.selected = True
        self["bg"] = "#c4faff"

class ProfilesInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.pack_propagate(False)
        self["height"] = 300

        h2 = tk.Label(self, text="Info", font=H2, pady=5)
        h2.pack(side="top")

        self.infos = tk.Frame(self, relief="sunken", borderwidth=1, bg="white")
        self.infos.pack(side="top", fill="x", pady=5)
        self.infos.columnconfigure(0, weight=1)
        self.infos.columnconfigure(1, weight=1)

        self.info_list = ["Name", "Age", "Gender", "Lessons Completed", "Number Of Points", "Grade"]

        self.var_list = []
        for x in range(6):
            self.var_list.append(tk.StringVar())

        for info in self.info_list:
            i = self.info_list.index(info)
            tk.Label(self.infos, text=info, bg="white").grid(row=i, column=0, sticky="w")
            tk.Label(self.infos, textvariable=self.var_list[i], bg="white").grid(row=i, column=1, sticky="e")

class AddProfileMenu(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.controller = controller

        self.protocol("WM_DELETE_WINDOW", self.quit_profile)

        frame = tk.Frame(self)
        frame.pack(side="top", expand=True, fill="both")

        h2 = tk.Label(frame, text="Add Profile", font=H2)
        h2.pack(side="top")

        entries = tk.Frame(frame)
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

        buttons = tk.Frame(frame)
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
    profile = None
    test = False

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

        back = tk.Button(frame, text="Return To Main Menu", command=self.to_MainMenu, bg=CANCEL, activebackground=CANCEL_D)
        back.pack(side="top", pady=10)

        lessons_list = ["Alphabet", "Numbers", "Food", "Animals", "Colors","Days & Months"]

        for l in lessons_list:
            i = lessons_list.index(l)

            if i < len(lessons_list) / 2:
                LessonMenuButton(lessons, self, l).grid(row=0, column=i, pady=2, padx=2)
            else:
                LessonMenuButton(lessons, self, l).grid(row=1, column=int(i-(len(lessons_list) / 2)), pady=2, padx=2)

    def to_MainMenu(self):
        LessonMenu.profile = None
        LessonMenu.test = False
        self.controller.active_frame = MainMenu(self.controller)
        self.controller.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.controller.logo.lift()
        self.destroy()

class LessonMenuButton(tk.Button):
    def __init__(self, parent, controller, lesson):
        tk.Button.__init__(self, parent, text=lesson, command=self.check_mode)
        self.lesson = lesson
        self.parent = parent
        self.controller = controller
        self["width"] = 15
        self["height"] = int(self["width"] / 2)

    def check_mode(self):
        if LessonMenu.test:
            self.to_Exercise()
        else:
            self.to_SelectMenu()

    def to_SelectMenu(self):
        self.controller.active_frame = SelectMenu(self.controller.controller, self.lesson)
        self.controller.active_frame.place(relwidth=1, relheight=1)
        self.destroy()

    def to_Exercise(self):
        Exercise.lesson = self.lesson
        self.controller.active_frame = Exercise(self.controller.controller)
        self.controller.active_frame.place(relwidth=1, relheight=1)
        self.destroy()

class SelectMenu(tk.Frame):
    lesson_items = {"Alphabet": tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                    "Numbers": ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"),
                    "Food": ("Fruits", "Vegetables", "Meat", "Dairy", "Grains"),
                    "Animals": ("Dog", "Cat", "Cow", "Dolphin", "Lion", "Tiger", "Bear", "Monkey", "Horse", "Penguin"),
                    "Colors": ("Blue", "Red", "Purple", "Yellow", "Grey", "Orange", "Green", "White", "Black", "Brown"),
                    "Days & Months": ("Days", "Months")}

    def __init__(self, controller, lesson):
        tk.Frame.__init__(self, controller)
        self.items = SelectMenu.lesson_items[lesson]
        self.lesson = lesson
        self.controller = controller

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.5, relwidth=1)

        h2 = tk.Label(frame, text=lesson, font=H2)
        h2.pack(side="top", pady=5)

        buttons = tk.Frame(frame)
        buttons.pack(side="top", pady=5)

        controls = tk.Frame(frame)
        controls.pack(side="top", pady=10)

        self.begin = tk.Button(controls, text="Begin", command=self.begin_lesson, width=20, bg=SUBMIT, activebackground=SUBMIT_D, state="disabled")
        self.begin.pack(side="top", pady=2)

        back = tk.Button(controls, text="Return To Lesson Menu", command=self.back, width=20, bg=CANCEL, activebackground=CANCEL_D)
        back.pack(side="top", pady=2)

        self.lesson_select_buttons = []

        i = 0
        for r in range(int(math.ceil(len(self.items) / 5))):
            b_r = SelectMenuButtonRow(buttons, self, r)
            b_r.grid(row=r, column=0, padx=5, pady=2)

            for c in range(1, 6):
                try:
                    b = SelectMenuButton(buttons, self, self.items[i])
                    b.grid(row=r, column=c, padx=2, pady=2)
                    self.lesson_select_buttons.append(b)
                    i += 1
                except:
                    break

        self.button_select_all = tk.Button(buttons, text="Select All", command=self.select_all, width=20, bg=SPECIAL, activebackground=SPECIAL_D)
        self.button_select_all.grid(column=0, columnspan=6, pady=5)

    def begin_lesson(self):
        selected = []
        for button in self.lesson_select_buttons:
            if button.selected:
                # i = self.lesson_select_buttons.index(button)
                selected.append(button.item)
            else:
                continue

        Lesson.lesson = self.lesson
        self.controller.active_frame = Lesson(self.controller, selected)
        self.controller.active_frame.place(relwidth=1, relheight=1)
        self.destroy()

    def select_all(self):
        for button in self.lesson_select_buttons:
            if not button.selected:
                all_selected = False
                break
            else:
                all_selected = True

        for button in self.lesson_select_buttons:
            if all_selected:
                button.select_button()
            else:
                button.selected = False
                button.select_button()

        self.check_selected()

    def check_selected(self):
        for button in self.lesson_select_buttons:
            if button.selected:
                self.begin["state"] = "normal"
                break
            else:
                self.begin["state"] = "disabled"

    def back(self):
        Lesson.lesson = None
        Exercise.lesson = None
        self.controller.active_frame = LessonMenu(self.controller)
        self.controller.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.controller.logo.lift()
        self.destroy()

class SelectMenuButton(tk.Button):
    def __init__(self, parent, controller, item):
        tk.Button.__init__(self, parent, text=item, command=self.select_button)
        self.controller = controller
        self["width"] = 7
        self["height"] = int(self["width"] / 2)
        self.item = item

        self.selected = False

    def select_button(self):
        if self.selected:
            self.selected = False
            self["bg"] = "#f0f0f0"
        else:
            self.selected = True
            self["bg"] = "#c4faff"

        self.controller.check_selected()

class SelectMenuButtonRow(tk.Button):
    def __init__(self, parent, controller, row):
        tk.Button.__init__(self, parent, command=self.select_row)
        self.controller = controller
        self.row = row
        self["height"] = 3
        self["bg"] = SPECIAL
        self["activebackground"] = SPECIAL_D

    def select_row(self):
        row_start = self.row * 5

        for i in range(row_start, row_start + 5):
            try:
                button = self.controller.lesson_select_buttons[i]

                if not button.selected:
                    all_selected = False
                    break
                else:
                    all_selected = True

            except:
                break

        for i in range(row_start, row_start + 5):
            try:
                button = self.controller.lesson_select_buttons[i]

                if all_selected:
                    button.select_button()
                else:
                    button.selected = False
                    button.select_button()

            except:
                break

        self.controller.check_selected()

class Lesson(tk.Frame):
    lesson = None
    learn = {"Alphabet": LearnAlphabet, "Numbers": LearnNumbers, "Food": LearnFood, "Animals": LearnAnimals, "Colors": LearnColors, "Days & Months": LearnDaysMonths}
    def __init__(self, controller, items):
        tk.Frame.__init__(self, controller)
        self.controller = controller
        self.items = items
        self.lrn = self.learn[self.lesson]

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4, relwidth=1)

        Learn(frame, self).pack(side="top", expand=True, fill="both")

        back = tk.Button(frame, text="Return To Lesson Menu", command=self.back, bg=CANCEL, activebackground=CANCEL_D)
        back.pack(side="bottom")

    def back(self):
        Lesson.lesson = None
        self.controller.active_frame = LessonMenu(self.controller)
        self.controller.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.controller.logo.lift()
        self.destroy()

class Exercise(tk.Frame):
    lesson = None
    learn = {"Alphabet": ExAlphabet, "Numbers": ExNumbers, "Food": ExFood, "Animals": ExAnimals, "Colors": ExColors, "Days & Months": ExDaysMonths}
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller
        self.lrn = self.learn[self.lesson]

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4, relwidth=1)

        Ex(frame, self).pack(side="top", expand=True, fill="both")

        back = tk.Button(frame, text="Return To Lesson Menu", command=self.back, bg=CANCEL, activebackground=CANCEL_D)
        back.pack(side="bottom", pady=10)

    def back(self):
        Lesson.lesson = None
        self.controller.active_frame = LessonMenu(self.controller)
        self.controller.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.controller.logo.lift()
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    try:
        check_file(accounts)
        LoginMenu()
    except:
        create_file(accounts)
        CreateAccountMenu()

    root.mainloop()
