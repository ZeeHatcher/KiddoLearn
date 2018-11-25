import tkinter as tk
import random
from fileio import *

class Exercise(tk.Frame):
    lesson = None
    def __init__(self, controller, profile):
        tk.Frame.__init__(self, controller)
        self.learn = {"Alphabet": ExAlphabet,
                      "Numbers": ExNumbers,
                      "Food": ExFood,
                      "Animals": ExAnimals,
                      "Colors": ExColors,
                      "Days & Months": ExDaysMonths}

        self.controller = controller
        self.lrn = self.learn[self.lesson]
        self.profile = profile

        frame = tk.Frame(self)
        frame.place(anchor="center", relx=0.5, rely=0.4, relwidth=1)

        self.end = tk.Button(frame, text="Return To Main Menu", command=lambda: controller.back_MainMenu(self), bg=CANCEL, activebackground=CANCEL_D)
        self.end.pack(side="bottom", pady=10)

        Ex(frame, self).pack(side="top", expand=True, fill="both")

class Ex(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q_count = 1
        self.correct_count = 0
        self.wrong_count = 0
        self.exercise = check_exercise(self.controller.lesson)

        self.frame = tk.Frame(self)
        self.frame.pack(side="top")

        self.random_question()

    def random_question(self): # Randomly chooses a question and displays it
        self.clear_frame()

        self.type = str(random.randrange(len(self.exercise)) + 1)

        for t in self.exercise:
            try:
                ques_ans = t[self.type]
            except:
                continue

        q_list = list(ques_ans.keys())
        a_list = list(ques_ans.values())

        q = random.choice(q_list)
        a = ques_ans[q]

        self.controller.lrn(self.frame, self, q, a, a_list).pack(side="top")

    def clear_frame(self): # Clear finished exercises for new ones
        for child in self.frame.winfo_children():
            child.destroy()

# Ex for different lessons
# Shows questions and answer buttons
# Answer buttons will have random items except the correct answer, and placed randomly
class ExAlphabet(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q = q
        self.a = a
        self.a_list = a_list

        question = tk.Label(self, text=q, font=DESC)
        question.pack(side="top", pady=5)

        answers = tk.Frame(self)
        answers.pack(side="bottom", pady=5)

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        # Correct answer
        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col, padx=5)

        self.a_list.remove(self.a)
        col_list.remove(col)

        # Wrong answers
        if self.controller.type == "3":
            for ans in a_list:
                if ans != self.a:
                    wrong_a = ans
                    break

            col = random.choice(col_list)

            wrong_ans = AnswerButton(answers, self, wrong_a)
            wrong_ans.grid(row=0, column=col, padx=5)

            col_list.remove(col)

        else:
            for i in range(3):
                try:
                    wrong_a = random.choice(self.a_list)
                    col = random.choice(col_list)

                    wrong_ans = AnswerButton(answers, self, wrong_a)
                    wrong_ans.grid(row=0, column=col, padx=5)

                    self.a_list.remove(wrong_a)
                    col_list.remove(col)

                except:
                    continue

class ExNumbers(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q = q
        self.a = a
        self.a_list = a_list

        if self.controller.type == "3":
            QuestionCircles(self, q).pack(side="top")
        else:
            question = tk.Label(self, text=q, font=DESC)
            question.pack(side="top", pady=5)

        answers = tk.Frame(self)
        answers.pack(side="bottom", pady=5)

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col, padx=5)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col, padx=5)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExFood(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q = q
        self.a = a
        self.a_list = a_list

        QuestionGIF(self, q).pack(side="top", pady=5)

        answers = tk.Frame(self)
        answers.pack(side="bottom", pady=5)

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col, padx=5)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col, padx=5)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExAnimals(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q = q
        self.a = a
        self.a_list = a_list

        QuestionGIF(self, q).pack(side="top", pady=5)

        answers = tk.Frame(self)
        answers.pack(side="bottom", pady=5)

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col, padx=5)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col, padx=5)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExColors(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q = q
        self.a = a
        self.a_list = a_list

        QuestionGIF(self, q).pack(side="top", pady=5)

        answers = tk.Frame(self)
        answers.pack(side="bottom", pady=5)

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col, padx=5)

        self.a_list.remove(self.a)
        col_list.remove(col)

        for i in range(3):
            try:
                wrong_a = random.choice(self.a_list)
                col = random.choice(col_list)

                wrong_ans = AnswerButton(answers, self, wrong_a)
                wrong_ans.grid(row=0, column=col, padx=5)

                self.a_list.remove(wrong_a)
                col_list.remove(col)

            except:
                continue

class ExDaysMonths(tk.Frame):
    def __init__(self, parent, controller, q, a, a_list):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q = q
        self.a = a
        self.a_list = a_list

        question = tk.Label(self, text=q, font=DESC)
        question.pack(side="top", pady=5)

        answers = tk.Frame(self)
        answers.pack(side="bottom", pady=5)

        col_list = [0, 1, 2, 3]
        col = random.choice(col_list)

        correct_ans = AnswerButton(answers, self, a)
        correct_ans.grid(row=0, column=col, padx=5)

        self.a_list.remove(self.a)
        col_list.remove(col)

        if self.controller.type == "1":
            for ans in a_list:
                if ans != self.a:
                    wrong_a = ans
                    break

            col = random.choice(col_list)

            wrong_ans = AnswerButton(answers, self, wrong_a)
            wrong_ans.grid(row=0, column=col, padx=5)

            col_list.remove(col)

        else:
            for i in range(3):
                try:
                    wrong_a = random.choice(self.a_list)
                    col = random.choice(col_list)

                    wrong_ans = AnswerButton(answers, self, wrong_a)
                    wrong_ans.grid(row=0, column=col, padx=5)

                    self.a_list.remove(wrong_a)
                    col_list.remove(col)

                except:
                    continue

class QuestionGIF(tk.Frame): # GIFs for certain questions
    def __init__(self, controller, gif):
        tk.Frame.__init__(self, controller)
        gif_file = format_gif(controller.controller.controller.lesson, gif)

        gif_img = tk.PhotoImage(file=gif_file)
        img = tk.Label(self, image=gif_img)
        img.image = gif_img
        img.pack()

class QuestionCircles(tk.Frame): # Circles for ExNumber
    def __init__(self, controller, num):
        tk.Frame.__init__(self, controller)

        for x in range(num):
            img = tk.PhotoImage(file=r"images\circle.gif")
            circle = tk.Label(self, image=img)
            circle.image = img
            circle.pack(side="left")

class AnswerButton(tk.Button):
    def __init__(self, parent, controller, a):
        tk.Button.__init__(self, parent, text=a, command=self.ans)
        self.a = a
        self.controller = controller
        self.ex = controller.controller

        self["width"] = 10
        self["height"] = int(self["width"] / 4)

    def ans(self):
        if self.a == self.controller.a:
            self.ex.correct_count += 1
        else:
            self.ex.wrong_count += 1

        if self.ex.q_count < 20:
            self.ex.q_count += 1
            self.ex.random_question()
        else:
            self.ex.clear_frame()
            Results(self.ex.frame, self.ex, self.ex.correct_count, self.ex.wrong_count).pack(side="top")

class Results(tk.Frame):
    def __init__(self, parent, controller, correct_count, wrong_count):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.correct_count = correct_count
        self.wrong_count = wrong_count

        self.total = correct_count + wrong_count

        # Results GUI
        h2 = tk.Label(self, text="Results", font=H2)
        h2.pack(side="top", pady=5)

        details = tk.Frame(self)
        details.pack(side="top", pady=5)

        q = tk.Label(details, text="Number of Questions")
        q.grid(row=0, column=0, sticky="w", padx=5, pady=2)

        num_q = tk.Label(details, text=str(self.total))
        num_q.grid(row=0, column=1, sticky="e", padx=5, pady=2)

        c = tk.Label(details, text="Correct Answers")
        c.grid(row=1, column=0, sticky="w", padx=5, pady=2)

        num_c = tk.Label(details, text=str(correct_count))
        num_c.grid(row=1, column=1, sticky="e", padx=5, pady=2)

        w = tk.Label(details, text="Wrong Answers")
        w.grid(row=2, column=0, sticky="w", padx=5, pady=2)

        num_w = tk.Label(details, text=str(wrong_count))
        num_w.grid(row=2, column=1, sticky="e", padx=5, pady=2)

        self.controller.controller.end.config(text="End Lesson", bg=SPECIAL, activebackground=SPECIAL_D, command=self.save_results)

    def save_results(self): # Saves the current exercise results into *_records.txt file
        user = self.controller.controller.controller.user
        profile = self.controller.controller.profile
        lesson = self.controller.controller.lesson

        record_f = user + "_records"
        f = format_txt(record_f)
        try:
            records = check_file(f)
        except:
            create_file(f)
            records = check_file(f)

        res = {"name": profile, "lesson": lesson, "correct": self.correct_count}

        records.append(res)

        with open(f, "w") as out_file:
            for record in records:
                out_file.write("{}\n".format(record))

        self.controller.controller.controller.back_MainMenu(self.controller.controller)
