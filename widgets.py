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

        self.profs = tk.Frame(self, relief="groove", borderwidth=1, width=220, height=25)
        self.profs.pack(side="top", pady=10, ipadx=5, fill="y")
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
                profiles = check_file(f)

                for p in profiles:
                    if p["name"] == prof.name:
                        profiles.pop(profiles.index(p))

                with open(f, "w") as out_file:
                    for prof in profiles:
                        out_file.write("{}\n".format(prof))

                record_f = format_txt(self.user + "_records")
                records = check_file(record_f)

                delete_index = []
                for rec in records:
                    if rec["name"] == prof.name:
                        delete_index.append(records.index(rec))

                for i in range(len(delete_index)-1, -1, -1):
                    records.pop(delete_index[i])

                with open(record_f, "w") as out_file:
                    for rec in records:
                        out_file.write("{}\n".format(rec))

        self.button_delete["state"] = "disabled"
        self.controller.button_lesson["state"] = "disabled"
        self.controller.button_test["state"] = "disabled"
        self.controller.info.bt_stat["state"] = "disabled"

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
        lessons = list(lesson_items.keys())
        f = format_txt(self.user)
        try:
            profiles = check_file(f)
        except:
            create_file(f)
            profiles = check_file(f)

        for prof in profiles:
            if self.name == prof["name"]:
                self.info.profile = self.name
                self.info.var_list[0].set(prof["name"])
                self.info.var_list[1].set(prof["age"])
                self.info.var_list[2].set(prof["gender"])
                self.info.var_list[4].set(prof["grade"])

                completed = 0
                for ls in lessons:
                    if len(prof["items"][ls]) == len(lesson_items[ls]):
                        completed += 1

                self.info.var_list[3].set(str(completed) + "/6")

        for prof in self.controller.profiles_list:
            prof.selected = False
            prof["bg"] = "white"

        self.controller.controller.profiles.button_delete["state"] = "normal"
        self.controller.controller.button_lesson["state"] = "normal"
        self.controller.controller.button_test["state"] = "normal"
        self.controller.controller.info.bt_stat["state"] = "normal"

        self.selected = True
        self["bg"] = "#c4faff"

        self.controller.controller.set_profile(self.name)

class ProfilesInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.profile = None

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

        self.bt_stat = tk.Button(self, width=10, text="Statistics", bg=MISC, activebackground=MISC_D, state="disabled", command=lambda: Statistics(self, self.profile))
        self.bt_stat.pack(side="top", pady=10)

class AddProfileMenu(tk.Toplevel):
    adding_profile = False
    def __init__(self, controller, user):
        tk.Toplevel.__init__(self)
        self.controller = controller
        self.user = user
        self.geometry(MINI)

        self.protocol("WM_DELETE_WINDOW", self.quit_profile)

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.5)

        h2 = tk.Label(frame, text="Add Profile", font=H2)
        h2.pack(side="top", pady=10)

        entries = tk.Frame(frame)
        entries.pack(side="top", expand=True, fill="both")

        entries.columnconfigure(0, weight=1)
        entries.columnconfigure(1, weight=1)

        name = tk.Label(entries, text="Name: ")
        name.grid(row=0, column=0, sticky="e", padx=5)

        age = tk.Label(entries, text="Age: ")
        age.grid(row=1, column=0, sticky="e", padx=5)

        gender = tk.Label(entries, text="Gender: ")
        gender.grid(row=2, column=0, sticky="e", padx=5)

        self.entry_name = tk.Entry(entries)
        self.entry_name.grid(row=0, column=1, sticky="w", padx=5)

        self.entry_age = tk.Entry(entries)
        self.entry_age.grid(row=1, column=1, sticky="w", padx=5)

        self.gender_var = tk.StringVar()

        self.entry_gender = tk.Frame(entries)
        self.entry_gender.grid(row=2, column=1, sticky="w", padx=5)

        self.entry_gender_m = tk.Radiobutton(self.entry_gender, text="Male", variable=self.gender_var, value="Male")
        self.entry_gender_m.pack(side="left", padx=2)

        self.entry_gender_f = tk.Radiobutton(self.entry_gender, text="Female", variable=self.gender_var, value="Female")
        self.entry_gender_f.pack(side="left", padx=2)

        self.message_var = tk.StringVar()
        self.message = tk.Label(entries, textvariable=self.message_var)
        self.message.grid(row=3, column=0, columnspan=2)

        buttons = tk.Frame(frame)
        buttons.pack(side="top", pady=10)

        button_confirm = tk.Button(buttons, text="Confirm", command=self.check_profile, bg=SUBMIT, activebackground=SUBMIT_D)
        button_confirm.pack(side="left", padx=10)

        button_cancel = tk.Button(buttons, text="Cancel", command=self.quit_profile, bg=CANCEL, activebackground=CANCEL_D)
        button_cancel.pack(side="left", padx=10)

    def check_profile(self):
        if (self.entry_name.get() != "") and (self.entry_age.get() != "") and (self.gender_var.get() != ""):
            f = format_txt(self.user)
            try:
                profiles = check_file(f)
            except:
                create_file(f)
                profiles = check_file(f)

            prof = {"name": self.entry_name.get(),
                    "age": self.entry_age.get(),
                    "gender": self.gender_var.get(),
                    "grade": "~",
                    "items": {"Alphabet": [],
                              "Numbers": [],
                              "Food": [],
                              "Animals": [],
                              "Colors": [],
                              "Days & Months": []}
                    }

            with open(f, "a") as out_file:
                out_file.write("{}\n".format(prof))

            self.controller.update_profiles()
            self.controller.profiles_list[-1].select_profile()

            self.quit_profile()
        else:
            self.message_var.set("Please fill in the required information")

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

        f = format_txt(self.controller.controller.user)
        profiles = check_file(f)

        if not self.controller.test:
            for prof in profiles:
                if self.controller.profile == prof["name"] and len(prof["items"][self.lesson]) == len(lesson_items[self.lesson]):
                        self["bg"] = SUBMIT

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
            self["relief"] = "raised"
        else:
            self.selected = True
            self["relief"] = "sunken"

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

class Statistics(tk.Toplevel):
    def __init__(self, controller, profile):
        tk.Toplevel.__init__(self)
        self.controller = controller
        self.profile = profile

        self.geometry(MEDIUM)
        lessons_list = ["Alphabet", "Numbers", "Food", "Animals", "Colors","Days & Months"]

        buttons = tk.Frame(self)
        buttons.pack(side="top")

        self.bt_list = []
        for ls in lessons_list:
            i = lessons_list.index(ls)
            bt = StatisticsButton(buttons, self, ls)

            if i < len(lessons_list) / 2:
                bt.grid(row=0, column=i, pady=2, padx=2)
            else:
                bt.grid(row=1, column=int(i-(len(lessons_list) / 2)), padx=2)

            self.bt_list.append(bt)

class StatisticsButton(tk.Button):
    def __init__(self, parent, controller, ls):
        tk.Button.__init__(self, parent, text=ls, command=self.select_graph)
        self["width"] = 12
        self["bg"] = "white"
        self.controller = controller
        self.ls = ls
        self.selected = False

    def select_graph(self):
        for bt in self.controller.bt_list:
            bt.selected = False
            bt["bg"] = "white"

        self.selected = True
        self["bg"] = MISC

        try:
            self.controller.graph.destroy()
        except:
            pass

        self.controller.graph = Graph(self.controller, self.controller.profile, self.ls)
        self.controller.graph.pack(side="top", pady=10)

class Graph(tk.Frame):
    def __init__(self, controller, profile, lesson):
        tk.Frame.__init__(self, controller)
        self.user = controller.controller.controller.controller.user
        self.controller = controller
        self.profile = profile
        self.lesson = lesson

        records_f = format_txt(self.user + "_records")
        records = check_file(records_f)

        results = []
        for rec in records:
            if rec["name"] == self.profile and rec["lesson"] == self.lesson:
                results.append(rec["correct"])

        x_change = 25
        y_change = 15
        min_x = 50
        if (len(results) * x_change) < 400:
            max_x = 350
        else:
            max_x = (len(results) * x_change) + min_x

        min_y = 350
        max_y = 50

        scrollbar = tk.Scrollbar(self, orient="horizontal")
        scrollbar.pack(side="bottom", fill="x")

        c = tk.Canvas(self, height=400, xscrollcommand=scrollbar.set, scrollregion=(0, 0, max_x+20, 0))
        c.pack(side="top")

        scrollbar.config(command=c.xview)

        fail_y = min_y - 10 * y_change
        pass_y = min_y - 16 * y_change

        c.create_rectangle(min_x, min_y, max_x, fail_y, fill="#ffbcbc")
        c.create_rectangle(min_x, fail_y, max_x, pass_y, fill="#bcffc1")
        c.create_rectangle(min_x, pass_y, max_x, max_y, fill="#fffdbc")

        c.create_line(min_x, min_y, max_x, min_y)
        c.create_line(min_x, min_y, min_x, max_y)

        c.create_text(min_x, min_y+10, text="0")

        for score in range(21):
            y = min_y - score * y_change
            c.create_text(min_x-10, y, text=str(score))

        x1 = min_x
        y1 = min_y
        for i in range(len(results)):
            x2 = x1 + x_change
            y2 = min_y - results[i] * y_change

            c.create_line(x1, y1, x2, y2)
            c.create_oval(x2-3, y2-3, x2+3, y2+3, fill="black")
            c.create_text(x2, min_y+10, text=str(i+1))

            y1 = y2
            x1 += x_change
