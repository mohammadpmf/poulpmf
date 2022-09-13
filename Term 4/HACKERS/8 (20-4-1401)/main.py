from tkinter import *

def change_color():
    if color.get()==1:
        root.config(bg='red')
    elif color.get()==2:
        root.config(bg='blue')
    elif color.get()==3:
        root.config(bg='purple')
    elif color.get()==4:
        root.config(bg='cyan')

root = Tk()
root.geometry('300x200')
frame1 = Frame(root)
color = IntVar()
cb_red = Radiobutton(frame1, text='Red', variable=color, value=1, command=change_color)
cb_blue = Radiobutton(frame1, text='Blue', variable=color, value=2, command=change_color)
cb_purple = Radiobutton(frame1, text='Blue', variable=color, value=3, command=change_color)
cb_cyan = Radiobutton(frame1, text='Blue', variable=color, value=4, command=change_color)
cb_red.grid(row=1, column=1)
cb_blue.grid(row=1, column=2)
cb_purple.grid(row=1, column=3)
cb_cyan.grid(row=1, column=4)
frame1.grid(row=1, column=1)
root.mainloop()