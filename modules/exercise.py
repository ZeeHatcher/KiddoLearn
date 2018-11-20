import tkinter as tk
import random
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
        self.controller = controller
        self.q_count = 0
        self.correct_count = 0
        self.wrong_count = 0
        self.exercise = check_exercise(self.controller.lesson)

        self.frame = tk.Frame(self)
        self.frame.pack(side="top")

        self.random_question()

    def random_question(self):
        self.clear_frame()

        type = str(random.randrange(len(self.exercise)) + 1)

        for t in self.exercise:
            try:
                ques_ans = t[type]
            except:
                continue

        q_list = list(ques_ans.keys())
        a_list = list(ques_ans.values())

        q = random.choice(q_list)
        a = ques_ans[q]

        self.controller.lrn(self.frame, self, q, a, a_list).pack(side="top")

    def clear_frame(self):
        for child in self.frame.winfo_children():
            child.destroy()

    def to_Results(self):
        pass

class ExAlphabet(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.q = q
        self.a = a
        self.a_list = a_list

        question = tk.Label(self, text=q)
        question.pack(side="top")

        answers = tk.Frame(self)
        answers.pack(side="bottom")

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExNumbers(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.q = q
        self.a = a
        self.a_list = a_list

        question = tk.Label(self, text=q)
        question.pack(side="top")

        answers = tk.Frame(self)
        answers.pack(side="bottom")

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExFood(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.q = q
        self.a = a
        self.a_list = a_list

        question = tk.Label(self, text=q)
        question.pack(side="top")

        answers = tk.Frame(self)
        answers.pack(side="bottom")

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExAnimals(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.q = q
        self.a = a
        self.a_list = a_list

        question = tk.Label(self, text=q)
        question.pack(side="top")

        answers = tk.Frame(self)
        answers.pack(side="bottom")

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExColors(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.q = q
        self.a = a
        self.a_list = a_list

        question = tk.Label(self, text=q)
        question.pack(side="top")

        answers = tk.Frame(self)
        answers.pack(side="bottom")

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExDaysMonths(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.q = q
        self.a = a
        self.a_list = a_list

        question = tk.Label(self, text=q)
        question.pack(side="top")

        answers = tk.Frame(self)
        answers.pack(side="bottom")

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class QuestionGIF(tk.Frame):
    def __init__(self, parent, controller, gif):
        tk.Frame.__init__(self, parent, controller)
        gif_file = format_gif(controller.controller.lesson, gif)

        gif_img = tk.PhotoImage(file=gif_file)
        img = tk.Label(self, image=gif_img)
        img.image = gif_img
        img.pack()

class AnswerButton(tk.Button):
    def __init__(self, parent, controller, a):
        tk.Button.__init__(self, parent, text=a, command=self.test)
        self.a = a
        self.controller = controller

    def test(self):
        if self.a == self.controller.a:
            print("correct")
        else:
            print("wrong")

class Results(tk.Frame):
    def __init__(self, parent, controller, correct_count, wrong_count):
        tk.Frame.__init__(self, parent)
