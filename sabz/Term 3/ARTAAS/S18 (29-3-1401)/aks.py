import tkinter as tk

root = tk.Tk()
root.geometry('300x300')
img = tk.PhotoImage(file='1.jpg')
label = tk.Label(root, image=img)
label.pack()

root.mainloop()