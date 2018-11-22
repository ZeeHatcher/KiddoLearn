import tkinter as tk
from fileio import *

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
