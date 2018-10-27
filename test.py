import tkinter as tk
root = tk.Tk()

test_list = []
for x in range(5):
    test_list.append(tk.StringVar())

print(test_list)

root.mainloop
