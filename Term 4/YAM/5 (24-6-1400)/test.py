import tkinter
from tkinter.ttk import Button, Label

def ok():
    sss.set('ok')
root = tkinter.Tk()
sss = tkinter.StringVar()
label = Label(textvariable=sss)
sss.set('test')
btn = Button(text='ok', command=ok)
label.pack()
btn.pack()

tkinter.mainloop()