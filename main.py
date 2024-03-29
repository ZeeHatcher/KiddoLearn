import tkinter as tk
from fileio import *
from lesson import *
from exercise import *
from widgets import *

class Root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

    def change_window(self, old, new): # Change windows between LoginMenu, CreateAccountMenu and Application
        old.destroy()
        new(self)

class LoginMenu(tk.Toplevel):
    def __init__(self, root):
        tk.Toplevel.__init__(self)
        self.root = root

        self.protocol("WM_DELETE_WINDOW", self.root.destroy)

        # LoginMenu GUI
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

        button_create = tk.Button(frame, text="Create New Account", command=lambda: root.change_window(self, CreateAccountMenu), bg=MISC, activebackground=MISC_D)
        button_create.pack(side="top", pady=2)

    def check_login(self): # Checks existing accounts for a match
        existing_accounts = check_file(accounts)

        username = self.entry_username.get()
        password = self.entry_password.get()

        authorized = False

        for account in existing_accounts: # Loops through list of existing accounts
            if username == account["username"] and password == account["password"]:
                authorized = True
                break

        if authorized: # Process after checking
            self.destroy()
            Application.user = username
            Application(self.root)
        else:
            self.message_var.set("Invalid username and/or password")

class CreateAccountMenu(tk.Toplevel):
    def __init__(self, root):
        tk.Toplevel.__init__(self)
        self.root = root

        self.protocol("WM_DELETE_WINDOW", self.root.destroy)

        # CreateAccountMenu GUI
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

        button_back = tk.Button(frame, text="Cancel", command=lambda: root.change_window(self, LoginMenu), bg=CANCEL, activebackground=CANCEL_D)
        button_back.pack(side="top", pady=2)

    def check_create_account(self): # Checks existing accounts and input for conflicts
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm = self.entry_confirm.get()
        create = False
        existing_accounts = check_file(accounts)

        if username != "" and password != "" and confirm != "": # Prevents empty username and password
            if confirm == password: # Makes sure password is similar
                create = True
            else:
                self.message_var.set("Please make sure your password is identical")
        else:
            self.message_var.set("Please fill in your username and password")

        for i in [username, password]: # Prevents spaces in username and password
            for letter in i:
                if letter == " ":
                    self.message_var.set("Only lowercase/uppercase alphabets, numbers and symbols are allowed")
                    create = False
                    break

        for account in existing_accounts: # Checks existing accounts for identical username
            if username == account["username"]:
                create = False
                self.message_var.set("Username has been taken.")
                break

        if create: # Create and write to text file
            f = format_txt(username)
            create_file(f)

            new_account = {"username": username, "password": password}

            with open(accounts, "a") as out_file:
                out_file.write("{}\n".format(new_account))

            self.root.change_window(self, LoginMenu)

class Application(tk.Toplevel):
    user = None
    def __init__(self, root):
        tk.Toplevel.__init__(self)
        self.root = root
        self.title("Kiddo Learn")
        self.geometry(LARGE)
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.frames = (MainMenu, LessonMenu, SelectMenu, Lesson, Exercise)

        self.active_frame = self.frames[0](self)
        self.active_frame.place(x=0, y=50, relwidth=1, relheight=1)

        # Logo
        logo_img = tk.PhotoImage(file=r"images\kiddo_learn.gif")
        self.logo = tk.Label(self, image=logo_img)
        self.logo.image = logo_img
        self.logo.place(anchor="n", relx=0.5, y=25, relwidth=1)

    def back_MainMenu(self, old): # Function to return to MainMenu
        Lesson.lesson = None
        Exercise.lesson = None
        LessonMenu.profile = None
        LessonMenu.test = False
        self.active_frame = MainMenu(self)
        self.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.logo.lift()
        old.destroy()

class MainMenu(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller

        # MainMenu GUI
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

        self.button_logout = tk.Button(buttons, text="Logout", command=self.logout, width=10, bg=CANCEL, activebackground=CANCEL_D)
        self.button_logout.pack(side="left", padx=10)

    def logout(self): # Logout and go to LoginMenu
        LessonMenu.profile = None
        Application.user = None
        self.controller.root.change_window(self.controller, LoginMenu)

    def to_LessonMenu(self, mode): # Go to LessonMenu if button_lesson or button_test was pressed
        if mode == 0: # Checks if button_lesson or button_test was pressed
            LessonMenu.test = False
        else:
            LessonMenu.test = True

        # Creates LessonMenu and displays it
        self.controller.active_frame = LessonMenu(self.controller)
        self.controller.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.controller.logo.lift()
        self.destroy()

    def set_profile(self, prof): # Sets LessonMenu.profile to the name of the selected profile
        LessonMenu.profile = prof

class LessonMenu(tk.Frame):
    profile = None
    test = False

    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller

        # LessonMenu GUI
        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4, relwidth=1)

        h1 = tk.Label(frame, text="Lessons", font=H1)
        h1.pack(side="top", pady=10)

        lessons = tk.Frame(frame)
        lessons.pack(side="top", pady=10)

        back = tk.Button(frame, text="Return To Main Menu", command=lambda: controller.back_MainMenu(self), bg=CANCEL, activebackground=CANCEL_D)
        back.pack(side="top", pady=10)

        lessons_list = ["Alphabet", "Numbers", "Food", "Animals", "Colors","Days & Months"]

        for l in lessons_list: # Creates and displays LessonMenuButton in a 3x2 grid
            i = lessons_list.index(l)

            if i < len(lessons_list) / 2:
                bt = LessonMenuButton(lessons, self, l)
                bt.grid(row=0, column=i, pady=2, padx=2)
            else:
                bt = LessonMenuButton(lessons, self, l)
                bt.grid(row=1, column=int(i-(len(lessons_list) / 2)), pady=2, padx=2)

    def to_Menu(self, menu, ls): # Go to the appropriate frame based on if button_lesson or button_test was pressed
        if menu == 0:
            self.controller.active_frame = SelectMenu(self.controller, ls, LessonMenu.profile)

        elif menu == 1:
            Exercise.lesson = ls
            self.controller.active_frame = Exercise(self.controller, LessonMenu.profile)

        self.controller.active_frame.place(relwidth=1, relheight=1)
        self.destroy()

class SelectMenu(tk.Frame):
    def __init__(self, controller, lesson, profile):
        tk.Frame.__init__(self, controller)
        self.items = lesson_items[lesson]
        self.lesson = lesson
        self.controller = controller
        self.profile = profile

        # SelectMenu GUI
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
        for r in range(int(math.ceil(len(self.items) / 5))): # Creates and display SelectMenuButton and SelectMenuButtonRow
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

        f = format_txt(Application.user)
        profiles = check_file(f)

        for prof in profiles: # Checks existing profile for completed lesson items and colors them green
            if self.profile == prof["name"]:
                for i in prof["items"][self.lesson]:
                    bt = self.lesson_select_buttons[i]
                    bt["bg"] = SUBMIT

        self.button_select_all = tk.Button(buttons, text="Select All", command=self.select_all, width=20, bg=SPECIAL, activebackground=SPECIAL_D)
        self.button_select_all.grid(column=0, columnspan=6, pady=5)

    def begin_lesson(self): # Checks selected items and begins a lesson with the selected items
        selected = []
        for button in self.lesson_select_buttons: # Loops through list of buttons to see which one is selected
            if button.selected:
                selected.append(button.item)

        # Begins a lesson with the selected items
        Lesson.lesson = self.lesson
        self.controller.active_frame = Lesson(self.controller, selected, self.profile)
        self.controller.active_frame.place(relwidth=1, relheight=1)
        self.destroy()

    def select_all(self): # Quality-of-life function to select all buttons
        for button in self.lesson_select_buttons: # Checks if all the buttons have been selected or not
            if not button.selected:
                all_selected = False
                break
            else:
                all_selected = True

        for button in self.lesson_select_buttons: # Selects/Deselects the buttons
            if all_selected:
                button.select_button()
            else:
                button.selected = False
                button.select_button()

        self.check_selected()

    def check_selected(self): # Enables the Begin button only if at least one item is selected
        for button in self.lesson_select_buttons:
            if button.selected:
                self.begin["state"] = "normal"
                break
            else:
                self.begin["state"] = "disabled"

    def back(self): # Back to LessonMenu
        Lesson.lesson = None
        Exercise.lesson = None
        self.controller.active_frame = LessonMenu(self.controller)
        self.controller.active_frame.place(x=0, y=50, relwidth=1, relheight=1)
        self.controller.logo.lift()
        self.destroy()

if __name__ == "__main__": # Start of Program
    root = Root()
    root.withdraw()

    try: # Checks for accounts file
        check_file(accounts)
        LoginMenu(root)
    except:
        create_file(accounts)
        CreateAccountMenu(root)

    root.mainloop()
