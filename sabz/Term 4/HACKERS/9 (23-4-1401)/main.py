from tkinter import *

class Thermometer:
    def __init__(self, root, color1='red', color2='light gray'):
        self.root = root
        self.frame = LabelFrame(self.root, text='Thermometer', bg=color2)
        self.temp = Label(self.frame, width=1, bg=color1)
        self.spin = Spinbox(self.frame, from_=0, to=100, width=5
        , justify='center', state='readonly')
    
    def grid(self, row=1, column=1):
        self.temp.place(x=40, y=5, height=100, width=10)
        self.spin.place(x=10, y=110, height=20, width=75)
        self.frame.place(x=5, y=0, width=100, height=155)

root = Tk()
root.geometry('600x400')
dama1 = Thermometer(root)
dama1.grid(row=1, column=1)

root.mainloop()