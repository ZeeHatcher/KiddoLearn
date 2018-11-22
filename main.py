import tkinter as tk
from fileio import *
from lesson import *
from exercise import *
from widgets import *

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

        self.frames = (MainMenu, LessonMenu, SelectMenu, Lesson, Exercise)

        self.active_frame = self.frames[0](self)
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

        self.profiles = Profiles(content, self, Application.user)
        self.profiles.grid(row=0, column=0, sticky="nsew", padx=10)

        buttons = tk.Frame(frame)
        buttons.pack(side="top")

        self.button_lesson = tk.Button(buttons, text="Lesson", command=lambda: self.to_LessonMenu(0), width=10, state="disabled", bg=MISC, activebackground=MISC_D)
        self.button_lesson.pack(side="left", padx=10)

        self.button_test = tk.Button(buttons, text="Test", command=lambda: self.to_LessonMenu(1), width=10, state="disabled", bg=SPECIAL, activebackground=SPECIAL_D)
        self.button_test.pack(side="left", padx=10)

        self.button_logout = tk.Button(buttons, text="Logout", command=self.logout, width=10)
        self.button_logout.pack(side="left", padx=10)

    def logout(self):
        LessonMenu.profile = None
        Application.user = None
        self.controller.destroy()
        LoginMenu()

    def to_LessonMenu(self, mode):
        if mode == 0:
            LessonMenu.test = False
        else:
            LessonMenu.test = True

        self.controller.active_frame = LessonMenu(self.controller)
        self.controller.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.controller.logo.lift()
        self.destroy()

    def set_lesson(self, ls):
        LessonMenu.lesson = ls

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

    def to_Menu(self, menu, ls):
        if menu == 0:
            self.controller.active_frame = SelectMenu(self.controller, ls)

        elif menu == 1:
            Exercise.lesson = ls
            self.controller.active_frame = Exercise(self.controller)

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
