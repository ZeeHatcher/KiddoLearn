import tkinter as tk
import math

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

lesson_items = {"alphabet": tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
               "numbers": tuple("0123456789"),
               "food": ("Noodle", "Rice", "Chicken", "Fish", "Vegetable", "Fruit"),
               "animals": ("Dog", "Cat", "Tiger", "Bird", "Fish", "Butterfly"),
               "colors": ("Blue", "Red", "Yellow", "Purple", "Black", "White"),
               "days & months": ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
               }

class LessonMenuButton(tk.Button):
    def __init__(self, parent, controller, lesson):
        tk.Button.__init__(self, parent, text=lesson, command=self.to_Lesson)
        self.lesson = lesson.lower()
        self.parent = parent
        self.controller = controller
        self["width"] = 15
        self["height"] = int(self["width"] / 2)

    def to_Lesson(self):
        Lesson.lesson = self.lesson
        Lesson(self.controller.controller).place(relwidth=1, relheight=1)

class Lesson(tk.Frame):
    lesson = None
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)

        h1 = tk.Label(self, text="Lesson", font=H1)
        h1.pack(side="top")

        lesson_select = LessonSelectItem(self, lesson_items[Lesson.lesson])
        lesson_select.pack(side="top")

    def back(self):
        self.destroy()

class LessonSelectItem(tk.Frame):
    def __init__(self, controller, lesson):
        tk.Frame.__init__(self, controller)
        self.lesson = lesson

        self.container = tk.Frame(self)
        self.container.pack(side="top")

        self.button_select_all = tk.Button(self, text="Select All", command=self.select_all)
        self.button_select_all.pack(side="top")

        self.begin = tk.Button(self, text="Begin Lesson", command=self.begin_lesson)
        self.begin.pack(side="top")

        back = tk.Button(self, text="Return To Lesson Menu", command=controller.back)
        back.pack(side="top")

        self.lesson_select_buttons = []

        i = 0
        for r in range(int(math.ceil(len(self.lesson) / 5))):
            b_r = LessonSelectItemRowButton(self.container, self, r)
            b_r.grid(row=r, column=0, padx=5, pady=2)

            for c in range(1, 6):
                try:
                    b = LessonSelectItemButton(self.container, self, self.lesson[i])
                    b.grid(row=r, column=c, padx=2, pady=2)
                    self.lesson_select_buttons.append(b)
                    i += 1
                except:
                    break

    def begin_lesson(self):
        selected = []
        for button in self.lesson_select_buttons:
            if button.selected:
                i = self.lesson_select_buttons.index(button)
                selected.append(i)
            else:
                continue

        print(selected)

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

class LessonSelectItemButton(tk.Button):
    def __init__(self, parent, controller, item):
        tk.Button.__init__(self, parent, text=item, command=self.select_button)
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

class LessonSelectItemRowButton(tk.Button):
    def __init__(self, parent, controller, row):
        tk.Button.__init__(self, parent, command=self.select_row)
        self.controller = controller
        self.row = row
        self["height"] = 3

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
