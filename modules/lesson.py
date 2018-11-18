import tkinter as tk
from modules.fileio import *
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
DESC = "Verdana 20"
# MINI
MEDIUM = "400x400+500+250"
LARGE = "800x600+250+250"

class Learn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.index = 0

        self.frame = tk.Frame(self)
        self.frame.pack(side="top", pady=10)

        buttons = tk.Frame(self)
        buttons.pack(side="bottom", pady=10)

        self.button_prev = tk.Button(buttons, text="Previous", command=self.prev_item, bg=MISC, activebackground=MISC_D, state="disabled")
        self.button_prev.pack(side="left", padx=5)

        self.button_next = tk.Button(buttons, text="Next", command=self.next_item, bg=SUBMIT, activebackground=SUBMIT_D)
        self.button_next.pack(side="right", padx=5)

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

        descriptions = check_description(self.controller.lesson)
        current_item = self.controller.items[self.index]

        for item in descriptions:
            if current_item == item["item"]:
                desc = item["description"]
                ex = item["examples"]

                tk.Label(self.frame, text=desc, font=DESC).pack(side="top")

                if ".gif" in ex:
                    ExampleGIF(self.frame, self, ex).pack(side="top")
                else:
                    tk.Label(self.frame, text=ex).pack(side="top")


class ExampleGIF(tk.Frame):
    def __init__(self, parent, controller, gif):
        tk.Frame.__init__(self, parent, controller)
        gif_file = format_gif(controller.controller.lesson, gif)

        gif_img = tk.PhotoImage(file=gif_file)
        img = tk.Label(self, image=gif_img)
        img.image = gif_img
        img.pack()

class Exercise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
