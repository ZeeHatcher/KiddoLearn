import tkinter as tk

class App(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)

        quitbutton = tk.Button(self, text="Quit", command=self.close_app)
        quitbutton.pack()

    def close_app(self):
        self.destroy()
        Menu().mainloop()

class Menu(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)

        label = tk.Label(self, text="Main Menu")
        label.pack()

        quitbutton = tk.Button(self, text="Quit", command=self.close_app)
        quitbutton.pack()

    def close_app(self):
        self.destroy()
        App().mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    App().mainloop()
