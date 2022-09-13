from tkinter import *

class Thermometer:
    def __init__(self, root, color1='red', color2='light gray', dama=100, bg1='purple', bg2='pink'):
        self.root = root
        self.dama = dama
        self.frame = LabelFrame(self.root, text='Thermometer', bg=color2,width=100,height=210)
        self.temp = Label(self.frame, width=1, bg=color1)
        self.spin = Spinbox(self.frame, from_=0, to=100, width=5
        , justify='center', command=self.change)
        self.spin.delete(0, END)
        self.spin.insert(0, self.dama)
        self.spin.config(state='readonly')
        self.rcolor = StringVar()
        self.rcolor.set('yechizi')
        self.bg1 = bg1
        self.bg2 = bg2
        self.r1 = Radiobutton(self.frame,text=self.bg1,value=self.bg1,highlightthickness=0,bg=color2,variable=self.rcolor,command=self.change_color)
        self.r2 = Radiobutton(self.frame,text=self.bg2,value=self.bg2,highlightthickness=0,bg=color2,variable=self.rcolor,command=self.change_color)

    def change_color(self):
        color2 = self.rcolor.get()
        self.frame.config(bg=color2)
        self.r1.config(bg=color2)
        self.r2.config(bg=color2)

    def change(self):
        t = int(self.spin.get())
        self.temp.place(x=40, y=105-t, height=t, width=10)


    def grid(self, row=1, column=1):
        self.temp.place(x=40, y=105-self.dama, height=self.dama, width=10)
        self.spin.place(x=10, y=110, height=20, width=75)
        self.r1.place(x=10,y=140)
        self.r2.place(x=10,y=160)
        #self.frame.place(x=5, y=0, width=100, height=155)
        self.frame.grid(row=row,column=column)
        

root = Tk()
root.geometry('600x400')
dama1 = Thermometer(root, 'red', 'green', 20, bg1='cyan', bg2='orange')
dama2 = Thermometer(root, 'gold', '#c97b06', 20, bg1='green', bg2='tomato')
dama1.grid(row=1, column=1)
dama2.grid(row=2, column=1)



root.mainloop()