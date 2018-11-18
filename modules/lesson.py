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

class Learn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        buttons = tk.Frame(self)
        buttons.pack(side="bottom", pady=10)

        self.button_prev = tk.Button(buttons, text="Previous", command=self.prev_item, bg=MISC, activebackground=MISC_D, state="disabled")
        self.button_prev.pack(side="left", padx=5)

        self.button_next = tk.Button(buttons, text="Next", command=self.next_item, bg=SUBMIT, activebackground=SUBMIT_D)
        self.button_next.pack(side="right", padx=5)

    def prev_item(self):
        self.button_next["state"] = "normal"
        i = self.controller.index

        if i > 0:
            i -= 1

        if i == 0:
            self.button_prev["state"] = "disabled"

    def next_item(self):
        self.button_prev["state"] = "normal"
        i = self.controller.index

        if i < len(self.controller.items):
            i += 1

        if i == len(self.controller.items):
            self.button_next["state"] = "disabled"

class Exercise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
