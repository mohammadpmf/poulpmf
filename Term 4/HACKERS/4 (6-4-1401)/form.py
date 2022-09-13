from tkinter import *

class MyForm:
    def save(self):
        open(self.entry_name.get(), 'w')

    def __init__(self, root):
        self.root = root
        self.lbl_name = Label(root, text='Name: ')
        self.entry_name = Entry(root)
        self.lbl_family = Label(root, text='Family: ')
        self.entry_family = Entry(root)
        self.btn_save = Button(root, text='Save', command=self.save)
        self.btn_reset = Button(root, text='Reset')
    
    def grid(self):
        self.lbl_name.grid(row=1, column=1)
        self.entry_name.grid(row=1, column=2)
        self.lbl_family.grid(row=2, column=1)
        self.entry_family.grid(row=2, column=2)
        self.btn_save.grid(row=3, column=1)
        self.btn_reset.grid(row=3, column=2)


