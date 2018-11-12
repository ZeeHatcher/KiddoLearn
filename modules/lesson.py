import tkinter as tk

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

dict_lesson = {"alphabet": tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
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
        self["width"] = 10
        self["height"] = int(self["width"] / 2)

    def to_Lesson(self):
        Lesson(self.controller.controller, self.lesson).place(relwidth=1, relheight=1)

class Lesson(tk.Frame):
    def __init__(self, parent, lesson):
        tk.Frame.__init__(self, parent)
        self.lesson = lesson

        h1 = tk.Label(self, text="Lesson")
        h1.pack(side="top")

        back = tk.Button(self, text="Return To Lesson Menu", command=self.back)
        back.pack(side="top")

        lesson_select = LessonSelect(self, dict_lesson[lesson])
        lesson_select.pack(side="top")

    def back(self):
        self.destroy()

class LessonSelect(tk.Frame):
    def __init__(self, parent, lesson):
        tk.Frame.__init__(self, parent)
        self.lesson = lesson

        self.container = tk.Frame(self)
        self.container.pack(side="top")

        self.begin = tk.Button(self, text="Begin Lesson", command=self.begin_lesson)
        self.begin.pack(side="top")

        self.lesson_select_buttons = []

        i = 0
        for r in range(int(len(self.lesson) / 5) + 1):
            for c in range(5):
                try:
                    b = LessonSelectButton(self.container, self.lesson[i])
                    b.grid(row=r, column=c, padx=2)
                    self.lesson_select_buttons.append(b)
                    i += 1
                except:
                    break

    def begin_lesson(self):
        selected = []
        for button in self.lesson_select_buttons:
            if button.selected:
                selected.append(button.item)
            else:
                continue

        print(selected)

class LessonSelectButton(tk.Button):
    def __init__(self, parent, item):
        tk.Button.__init__(self, parent, text=item, command=self.select_button)
        self["width"] = 5
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
