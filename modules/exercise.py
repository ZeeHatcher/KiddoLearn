import tkinter as tk
import random

numbers = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
           "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}

class Lessons(tk.Frame):
    def __init__(self, controller, lesson):
        tk.Frame.__init__(self, controller)

        self.question_list = list(lesson.keys())
        random.shuffle(self.question_list)

        Exercise(self, self.question_list[0], 1).place(relwidth=1, relheight=1)

class Exercise(tk.Frame):
    def __init__(self, controller, question, type):
        tk.Frame.__init__(self, controller)
        self.controller = controller
        self.question = question

        if type == 1:
            QuestionType1(self, self).pack(side="top")
        elif type == 2:
            QuestionType2(self, self).pack(side="top")

        self.answers = tk.Frame(self)
        self.answers.pack(side="top")

        unchosen = list(numbers.keys())
        col = [0, 1, 2, 3]
        c = random.choice(col)

        AnswerButton(self.answers, self, numbers[self.question]).grid(row=0, column=c, padx=2)

        unchosen.remove(self.question)
        col.remove(c)

        for ans in range(3):
            c = random.choice(col)
            chosen = random.choice(unchosen)

            AnswerButton(self.answers, self, numbers[chosen]).grid(row=0, column=c, padx=2)

            unchosen.remove(chosen)
            col.remove(c)

class QuestionType1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.q = tk.Label(self, text=controller.question)
        self.q.pack(side="top")

class QuestionType2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.q = tk.Label(self, text=controller.question)
        self.q.pack(side="top")

class AnswerButton(tk.Button):
    def __init__(self, parent, controller, item):
        tk.Button.__init__(self, parent, text=item, command=self.check_answer)
        self.item = item
        self.controller = controller
        self.lesson = self.controller.controller

    def check_answer(self):
        if self.item == numbers[self.controller.question]:
            self.controller.controller.question_list.remove(self.controller.question)
            self.controller.destroy()

            if len(self.lesson.question_list) != 0:
                random.shuffle(self.lesson.question_list)
                Exercise(self.lesson, self.lesson.question_list[0], 1).place(relwidth=1, relheight=1)
        else:
            self.controller.destroy()
            random.shuffle(self.lesson.question_list)
            Exercise(self.lesson, self.lesson.question_list[0], 1).place(relwidth=1, relheight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")

    Lessons(root, numbers).pack(side="top", expand=True, fill="both")

    root.mainloop()
