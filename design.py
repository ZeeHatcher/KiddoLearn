import tkinter as tk

def button_design(button):
    button["relief"] = "raised"
    button["width"] = "10"

class MainApp(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        button = tk.Button(self, text="Login")
        button_design(button)
        button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    MainApp(root).pack(expand=True, fill="both")
    root.mainloop()
