import tkinter as tk
results = [2, 6, 5, 6, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14,15]

class Graph(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        min_x = 50
        max_x = (len(results) * 50) + min_x
        min_y = 450
        max_y = 50

        scrollbar = tk.Scrollbar(self, orient="horizontal")
        scrollbar.pack(side="bottom", fill="x")

        c = tk.Canvas(self, height=500, xscrollcommand=scrollbar.set, scrollregion=(0, 0, max_x, 0))
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
            x2 = x1 + 50
            y2 = min_y - results[i] * 20

            c.create_line(x1, y1, x2, y2)
            c.create_oval(x1-3, y1-3, x1+3, y1+3, fill="black")
            c.create_text(x1, min_y+10, text=str(i))

            y1 = y2
            x1 += 50

if __name__ == "__main__":
    root = tk.Tk()
    Graph(root).pack()
    root.mainloop()
