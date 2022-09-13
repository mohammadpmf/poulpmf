from tkinter import *
class Thermometer:
    def __init__(self, root, color1='red', color2='light gray', dama=100):
        self.root = root
        self.dama = dama
        self.frame = LabelFrame(self.root, text='Thermometer', bg=color2, width=100, height=200)
        self.temp = Label(self.frame, width=1, bg=color1)
        self.spin = Spinbox(self.frame, from_=0, to=100, width=5
        , justify='center', command=self.change)
        self.spin.delete(0, END)
        self.spin.insert(0, self.dama)
        self.spin.config(state='readonly')
        self.bgcolor = StringVar(self.frame)
        self.bgcolor.set("alaki")
        self.r1 = Radiobutton(self.frame, highlightthickness=0, bg=color2, text='red', value='red', variable=self.bgcolor, command=self.change_color)
        self.r2 = Radiobutton(self.frame, highlightthickness=0, bg=color2, text='blue', value='blue', variable=self.bgcolor, command=self.change_color)

    def change_color(self):
        self.frame.config(bg=self.bgcolor.get())

    def change(self):
        t = int(self.spin.get())
        self.temp.place(x=40, y=105-t, height=t, width=10)


    def grid(self, row=1, column=1):
        self.temp.place(x=40, y=105-self.dama, height=self.dama, width=10)
        self.spin.place(x=10, y=110, height=20, width=75)
        self.r1.place(x=5, y=135)
        self.r2.place(x=5, y=155)
        # self.frame.place(x=5, y=0, width=100, height=155)
        self.frame.grid(row=row, column=column)