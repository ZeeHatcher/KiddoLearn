import tkinter as tk
from modules.fileio import *

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

class Ex(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class ExAlphabet(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class ExNumbers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class ExFood(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class ExAnimals(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class ExColors(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class ExDaysMonths(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class QuestionGIF(tk.Frame):
    def __init__(self, parent, controller, gif):
        tk.Frame.__init__(self, parent, controller)
        gif_file = format_gif(controller.controller.lesson, gif)

        gif_img = tk.PhotoImage(file=gif_file)
        img = tk.Label(self, image=gif_img)
        img.image = gif_img
        img.pack()

class AnswerButton(tk.Button):
    def __init__(self, parent, controller):
        tk.Button(self, parent)
