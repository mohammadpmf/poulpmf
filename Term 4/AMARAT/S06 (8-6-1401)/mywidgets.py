from tkinter import *

class MyForm():
    def __init__(self, root, *args, **kwargs):
        self.root = root
        self.lbl_frm = LabelFrame(root, *args, **kwargs)
        self.lbl_name = Label(self.lbl_frm, text='Name: ', *args, **kwargs)
        self.lbl_family = Label(self.lbl_frm, text='Family: ', *args, **kwargs)
        self.e_name = Entry(self.lbl_frm)
        self.e_family = Entry(self.lbl_frm)
        self.btn_reset = Button(self.lbl_frm, text='reset', command=self.reset, *args, **kwargs)
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
    def __init__(self, root, *args, **kwargs):
        self.root = root
        self.lbl_frm = LabelFrame(self.root, text="Thermometer")
        self.spin_temp = Spinbox(self.lbl_frm, from_=0, to=100, state='readonly')
    def grid(self, *args, **kwargs):
        pass

root = Tk()
t1 = Thermometer(root)
t1.grid(row=1, column=1)
root.mainloop()

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