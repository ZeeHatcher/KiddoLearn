import tkinter as tk
from fileio import *

class Profiles(tk.Frame):
    def __init__(self, parent, controller, user):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user = user

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
        if AddProfileMenu.adding_profile == False:
            AddProfileMenu.adding_profile = True
            AddProfileMenu(self, self.user)

    def update_profiles(self):
        for prof in self.profiles_list:
            prof.destroy()

        self.profiles_list = []

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

            p = Profile(self.profs, self, self.user, name)
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

                f = format_txt(self.user)
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
                    for prof in profiles:
                        out_file.write("{}\n".format(prof))

            else:
                continue

        self.button_delete["state"] = "disabled"
        self.controller.button_lesson["state"] = "disabled"
        self.controller.button_test["state"] = "disabled"

class Profile(tk.Button):
    def __init__(self, parent, controller, user, name):
        tk.Button.__init__(self, parent, text=name, command=self.select_profile)
        self.user = user
        self.name = name
        self.controller = controller
        self.info = controller.controller.info
        self.selected = False
        self["width"] = 30
        self["borderwidth"] = 1
        self["bg"] = "white"

    def select_profile(self):
        f = format_txt(self.user)
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
                self.info.var_list[4].set(prof["grade"])
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

        self.info_list = ["Name", "Age", "Gender", "Lessons Completed", "Grade"]

        self.var_list = []
        for x in range(6):
            self.var_list.append(tk.StringVar())

        for info in self.info_list:
            i = self.info_list.index(info)
            tk.Label(self.infos, text=info, bg="white").grid(row=i, column=0, sticky="w")
            tk.Label(self.infos, textvariable=self.var_list[i], bg="white").grid(row=i, column=1, sticky="e")

class AddProfileMenu(tk.Toplevel):
    adding_profile = False
    def __init__(self, controller, user):
        tk.Toplevel.__init__(self)
        self.controller = controller
        self.user = user

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
        f = format_txt(self.user)
        try:
            profiles = check_file(f)
        except:
            create_file(f)
            profiles = check_file(f)

        prof = {"name": self.entry_name.get(),
                "age": self.entry_age.get(),
                "gender": self.gender_var.get(),
                "completed": "0",
                "grade": "~",
                }

        with open(f, "a") as out_file:
            out_file.write("{}\n".format(prof))

        self.controller.update_profiles()
        self.controller.profiles_list[-1].select_profile()
        self.quit_profile()

    def quit_profile(self):
        AddProfileMenu.adding_profile = False
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
        if self.controller.test:
            self.controller.to_Menu(1, self.lesson)
        else:
            self.controller.to_Menu(0, self.lesson)

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
