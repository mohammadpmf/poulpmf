from tkinter import *

class MyForm():
    def __init__(self, root, bg='white'):
        self.root = root
        self.lbl_frm = LabelFrame(root, bg=bg, text='info')
        self.lbl_name = Label(self.lbl_frm, text='Name: ')
        self.lbl_family = Label(self.lbl_frm, text='Family: ')
        self.e_name = Entry(self.lbl_frm)
        self.e_family = Entry(self.lbl_frm)
        self.btn_reset = Button(self.lbl_frm, text='reset', command=self.reset)
        self.lbl_name.grid(row=1, column=1)
        self.lbl_family.grid(row=2, column=1)
        self.e_name.grid(row=1, column=2)
        self.e_family.grid(row=2, column=2)
        self.btn_reset.grid(row=3, column=1)
    def pack(self):
        self.lbl_frm.pack()
    def place(self, x=0, y=0, width=0, height=0):
        self.lbl_frm.place(x=x, y=y, width=width, height=height)
    def grid(self):
        self.lbl_frm.grid()
    def reset(self):
        self.e_name.delete(0, END)
        self.e_family.delete(0, END)
        self.e_name.focus_set()
    

root = Tk()
root.geometry('600x600')
Button(root, text='OK').place(x=400, y=200, width=100, height=30)
myform1 = MyForm(root, bg='red')
myform1.place(x=2, y=155, width=250, height=150)
myform2 = MyForm(root)
myform2.place(x=2, y=5, width=250, height=150)
myform3 = MyForm(root)
myform3.place(x=2, y=305, width=250, height=150)
root.mainloop()