import tkinter as tk
def ok():
    if s.get() == 1:
        print("OK")
    else:
        print("Not ok")
root =tk.Tk()
s = tk.IntVar()
tk.Checkbutton(root, text="Delester", variable=s, command=ok).pack()
root.mainloop()
