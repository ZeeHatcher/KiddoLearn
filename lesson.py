import tkinter as tk
import math
from fileio import *

class Learn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.description = check_description(self.controller.lesson)
        self.index = 0
        self.current_item = self.controller.items[self.index]

        self.frame = tk.Frame(self)
        self.frame.pack(side="top", expand=True, fill="both")

        buttons = tk.Frame(self)
        buttons.pack(side="bottom", pady=10)

        self.button_prev = tk.Button(buttons, text="Previous", command=self.prev_item, bg=MISC, activebackground=MISC_D, state="disabled")
        self.button_prev.pack(side="left", padx=5)

        self.button_next = tk.Button(buttons, text="Next", command=self.next_item, bg=SUBMIT, activebackground=SUBMIT_D)
        self.button_next.pack(side="right", padx=5)

        if self.index == len(self.controller.items) - 1:
            self.button_next["state"] = "disabled"

        self.display_item()

    def prev_item(self):
        self.button_next["state"] = "normal"

        if self.index > 0:
            self.index -= 1

        if self.index == 0:
            self.button_prev["state"] = "disabled"

        self.display_item()

    def next_item(self):
        self.button_prev["state"] = "normal"

        if self.index < len(self.controller.items) - 1:
            self.index += 1

        if self.index == len(self.controller.items) - 1:
            self.button_next["state"] = "disabled"

        self.display_item()

    def display_item(self):
        for child in self.frame.winfo_children():
            child.destroy()

        self.current_item = self.controller.items[self.index]

        for item in self.description:
            if self.current_item == item["item"]:
                self.controller.lrn(self.frame, self, item["description"], item["examples"]).pack(side="top")

class LearnAlphabet(tk.Frame):
    def __init__(self, parent, controller, description, examples):
        tk.Frame.__init__(self, parent)

        desc = tk.Label(self, text=description, font=DESC)
        desc.pack(side="top")

        ex = tk.Label(self, text=examples)
        ex.pack(side="top")

class LearnNumbers(tk.Frame):
    def __init__(self, parent, controller, description, examples):
        tk.Frame.__init__(self, parent)
        self.num = int(controller.current_item)

        desc = tk.Label(self, text=description, font=DESC)
        desc.pack(side="top")

        circles = tk.Frame(self)
        circles.pack(side="top")

        for x in range(self.num):
            img = tk.PhotoImage(file=r"images\circle.gif")
            circle = tk.Label(circles, image=img)
            circle.image = img
            circle.pack(side="left")

        ex = tk.Label(self, text=examples)
        ex.pack(side="top")

class LearnFood(Learn):
    def __init__(self, parent, controller, description, examples):
        tk.Frame.__init__(self, parent)

        desc = tk.Label(self, text=description, font=DESC)
        desc.pack(side="top")

        items = tk.Frame(self)
        items.pack(side="top")

        for ex in examples:
            gif = format_gif("food", ex)

            img = tk.PhotoImage(file=gif)
            ex = tk.Label(items, image=img)
            ex.image = img
            ex.pack(side="left")

class LearnAnimals(tk.Frame):
    def __init__(self, parent, controller, description, examples):
        tk.Frame.__init__(self, parent)

        desc = tk.Label(self, text=description, font=DESC)
        desc.pack(side="top")

        gif = format_gif("animals", examples)

        img = tk.PhotoImage(file=gif)
        ex = tk.Label(self, image=img)
        ex.image = img
        ex.pack(side="top")

class LearnColors(tk.Frame):
    def __init__(self, parent, controller, description, examples):
        tk.Frame.__init__(self, parent)

        desc = tk.Label(self, text=description, font=DESC)
        desc.pack(side="top")

        gif = format_gif("colors", examples)

        img = tk.PhotoImage(file=gif)
        ex = tk.Label(self, image=img)
        ex.image = img
        ex.pack(side="top")

class LearnDaysMonths(tk.Frame):
    def __init__(self, parent, controller, description, examples):
        tk.Frame.__init__(self, parent)

        desc = tk.Label(self, text=description, font=DESC)
        desc.pack(side="top")

        items = tk.Frame(self)
        items.pack(side="top")

        for ex in examples:
            i = examples.index(ex)
            tk.Label(items, text=str(i+1)).grid(row=i, column=0, sticky="e")
            tk.Label(items, text=ex).grid(row=i, column=1, sticky="w")

class ExampleGIF(tk.Frame):
    def __init__(self, parent, controller, gif):
        tk.Frame.__init__(self, parent, controller)
        gif_file = format_gif(controller.controller.lesson, gif)

        gif_img = tk.PhotoImage(file=gif_file)
        img = tk.Label(self, image=gif_img)
        img.image = gif_img
        img.pack()
