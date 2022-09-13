from tkinter import *

class Thermometer:
    def __init__(self, root, color1='red', color2='light gray', dama=100):
        self.root = root
        self.dama = dama
        self.frame = LabelFrame(self.root, text='Thermometer', bg=color2)
        self.temp = Label(self.frame, width=1, bg=color1)
        self.spin = Spinbox(self.frame, from_=0, to=100, width=5
        , justify='center', command=self.change)
        self.spin.delete(0, END)
        self.spin.insert(0, self.dama)
        self.spin.config(state='readonly')
    def change(self):
        t = int(self.spin.get())
        self.temp.place(x=40, y=105-t, height=t, width=10)


    def grid(self, row=1, column=1):
        self.temp.place(x=40, y=105-self.dama, height=self.dama, width=10)
        self.spin.place(x=10, y=110, height=20, width=75)
        self.frame.place(x=5, y=0, width=100, height=155)

root = Tk()
root.geometry('600x400')
dama1 = Thermometer(root, 'gold', '#c97b06', 20)
dama2 = Thermometer(root, 'silver', 'green', 60)
dama1.grid(row=1, column=1)
dama2.grid(row=2, column=1)

root.mainloop()