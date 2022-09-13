from tkinter import *
from tkinter.ttk import Combobox
def set_bg(event):
    root.configure(bg=combotext.get())
    l2.config(text=combotext.get(),bg=combotext.get())
root = Tk()
root.geometry("250x250")
root.title("change bg")

l1=Label(root,text="select your bg color",bg="pink")
l1.pack(side=TOP,fill='both')
combotext = StringVar()
combotext.set('Select')

box = Combobox(root, textvariable=combotext, state='readonly')
box.pack()
box['values'] = ("green",
                 "red",
                 "blue",
                 "yellow",
                 "deep pink",
                 'pink',
                 'gray')

l2=Label(root)
l2.place(x=100,y=100)
root.bind('<<ComboboxSelected>>', set_bg)

root.mainloop()