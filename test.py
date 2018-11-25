import tkinter as tk

results = [1, 2, 3, 4, 7, 7, 7, 4, 3, 1, 2]
class Graph(tk.Frame):
    def __init__(self, parent, profile, lesson):
        tk.Frame.__init__(self, parent)
        self.lesson = lesson
        min_x = 20
        max_x = (len(results) * 20) + min_x
        min_y = 450
        max_y = 50

        scrollbar = tk.Scrollbar(self, orient="horizontal")
        scrollbar.pack(side="bottom", fill="x")

        c = tk.Canvas(self, height=500, xscrollcommand=scrollbar.set, scrollregion=(0, 0, max_x+20, 0))
        c.pack(side="top")

        scrollbar.config(command=c.xview)

        c.create_line(min_x, min_y, max_x, min_y)
        c.create_line(min_x, min_y, min_x, max_y)

        for score in range(21):
            y = min_y - score * 20
            c.create_text(min_x-10, y, text=str(score))

        x1 = min_x
        y1 = min_y
        for i in range(len(results)):
            x2 = x1 + 20
            y2 = min_y - results[i] * 20

            c.create_line(x1, y1, x2, y2)
            c.create_oval(x2-3, y2-3, x2+3, y2+3, fill="black")
            c.create_text(x1, min_y+10, text=str(i))

            y1 = y2
            x1 += 20

if __name__ == "__main__":
    root = tk.Tk()
    Graph(root, "Jonathan", "Alphabet").pack()
    root.mainloop()
