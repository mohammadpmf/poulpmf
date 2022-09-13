from tkinter import *

class MyForm():
    def __init__(self, root, *args, **kwargs):
        self.root = root
        self.lbl_frm = LabelFrame(root, *args, **kwargs)
        self.lbl_name = Label(self.lbl_frm, text='Name: ', *args, **kwargs)
        self.lbl_family = Label(self.lbl_frm, text='Family: ', *args, **kwargs)
        self.e_name = Entry(self.lbl_frm)
        self.e_family = Entry(self.lbl_frm)
        self.btn_reset = Button(self.lbl_frm, text='reset', command=self.reset, *args, *kwargs)
        self.lbl_name.grid(row=1, column=1)
        self.lbl_family.grid(row=2, column=1)
        self.e_name.grid(row=1, column=2)
        self.e_family.grid(row=2, column=2)
        self.btn_reset.grid(row=3, column=1)
    def pack(self, *args, **kwargs):
        self.lbl_frm.pack(*args, **kwargs)
    def place(self, *args, **kwargs):
        self.lbl_frm.place(*args, **kwargs)
    def grid(self, *args, **kwargs):
        self.lbl_frm.grid(*args, **kwargs)
    def reset(self):
        self.e_name.delete(0, END)
        self.e_family.delete(0, END)
        self.e_name.focus_set()


class Thermometer():
    def __init__(self, root, box_color=None, init_temp=25, *args, **kwargs):
        self.state      ='C'
        self.root       = root
        self.lbl_frm    = LabelFrame(self.root)
        self.lbl_box    = Label(self.lbl_frm, bg=box_color)
        self.lbl_name   = Label(self.lbl_frm, bg=box_color, text="C")
        self.lbl_100    = Label(self.lbl_frm, bg=box_color, text="100")
        self.lbl_80     = Label(self.lbl_frm, bg=box_color, text="80")
        self.lbl_60     = Label(self.lbl_frm, bg=box_color, text="60")
        self.lbl_40     = Label(self.lbl_frm, bg=box_color, text="40")
        self.lbl_20     = Label(self.lbl_frm, bg=box_color, text="20")
        self.lbl_0      = Label(self.lbl_frm, bg=box_color, text="0")
        self.lbl_color1 = Label(self.lbl_frm, bg='red')
        self.lbl_color2 = Label(self.lbl_frm, bg='dark red')
        self.lbl_color3 = Label(self.lbl_frm, bg='dark blue')
        self.spin_temp  = Spinbox(self.lbl_frm, from_=0, to=100, state='readonly',justify='center',command=self.change_temp)
        self.btn_change = Button(self.lbl_frm, text="F/C", command=self.change)
        self.lbl_box    .place(relx=0.18, rely=0,    relwidth=0.64, relheight=0.72)
        self.lbl_name   .place(relx=0.2,  rely=0,    relwidth=0.6,  relheight=0.1 )
        self.lbl_100    .place(relx=0.2,  rely=0.11, relwidth=0.2,  relheight=0.1 )
        self.lbl_80     .place(relx=0.6,  rely=0.21, relwidth=0.2,  relheight=0.1 )
        self.lbl_60     .place(relx=0.2,  rely=0.31, relwidth=0.2,  relheight=0.1 )
        self.lbl_40     .place(relx=0.6,  rely=0.41, relwidth=0.2,  relheight=0.1 )
        self.lbl_20     .place(relx=0.2,  rely=0.51, relwidth=0.2,  relheight=0.1 )
        self.lbl_0      .place(relx=0.6,  rely=0.61, relwidth=0.2,  relheight=0.1 )
        self.lbl_color1 .place(relx=0.41, rely=0.1,  relwidth=0.18, relheight=0.6 )
        self.lbl_color2 .place(relx=0.44, rely=0.1,  relwidth=0.12, relheight=0.6 )
        self.lbl_color3 .place(relx=0.48, rely=0.1,  relwidth=0.04, relheight=0.6 )
        self.spin_temp  .place(relx=0.3,  rely=0.83, relwidth=0.4,  relheight=0.12)
        self.btn_change .place(relx=0.05, rely=0.83, relwidth=0.2,  relheight=0.12)
        self.temp = init_temp
        self.spin_temp['state']='normal'
        self.spin_temp.delete(0, END)
        self.spin_temp.insert(0, init_temp)
        self.spin_temp['state']='readonly'
        self.change_temp()
    def place(self, *args, **kwargs):
        self.lbl_frm.place(*args, **kwargs)

    
    def change_temp(self):
        temp = int(self.spin_temp.get())
        if self.state == 'C':
            self.lbl_color3 .place(rely=0.7-((temp+1)*6/1013), relheight=((temp+1)*6/1013))
        elif self.state == 'F':
            t = (temp-32)*5/9
            self.lbl_color3 .place(rely=0.7-((t+1)*6/1013), relheight=((t+1)*6/1013))

    def change(self):
        if self.state == 'C':
            self.state = 'F'
            self.lbl_name['text'] = "°F "
            self.lbl_100['text'] = "212"
            self.lbl_80['text'] = "176"
            self.lbl_60['text'] = "140"
            self.lbl_40['text'] = "104"
            self.lbl_20['text'] = "68"
            self.lbl_0['text'] = "32"
            
            self.spin_temp['state']='normal'
            t = int(self.spin_temp.get())
            t = int(t*9/5)+32
            self.spin_temp.delete(0, END)
            self.spin_temp.insert(0, t)
            self.spin_temp.config(from_=32,to=212, state='readonly')
        elif self.state == 'F':
            self.state = 'C'
            self.lbl_name['text'] = "°C "
            self.lbl_100['text'] = "100"
            self.lbl_80['text'] = "80"
            self.lbl_60['text'] = "60"
            self.lbl_40['text'] = "40"
            self.lbl_20['text'] = "20"
            self.lbl_0['text'] = "0"
            t = int(self.spin_temp.get())
            t = int((t-32)*5/9)
            self.spin_temp.delete(0, END)
            self.spin_temp.insert(0, t)
            self.spin_temp.config(from_=0,to=100, state='readonly')
        self.change_temp()



# root = Tk()
# t1 = Thermometer(root, box_color='gray',init_temp=25)
# t1.place(relx=0, rely=0, relwidth=1, relheight=1)
# root.mainloop()

# root = Tk()
# root.geometry('600x600')
# Button(root, text='OK').place()
# myform1 = MyForm(root, bg='red')
# myform1.grid(row=1, column=1)
# myform2 = MyForm(root, fg='green', bg='light blue')
# myform2.grid()
# myform3 = MyForm(root, bg='cyan')
# myform3.grid(row=3, column=2, padx=10, sticky='news')
# root.mainloop()
