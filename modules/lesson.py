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
        tk.Frame(self, parent)

class Exercise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame(self, parent)
