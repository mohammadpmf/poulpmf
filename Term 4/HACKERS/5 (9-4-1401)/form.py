from tkinter import *

class MyForm:
    def save(self, event=''):
        name = self.entry_name.get()
        family = self.entry_family.get() 
        file = open(name, 'w')
        file.write(name)
        file.write('\n')
        file.write(family)
        file.close()

    def reset(self):
        self.entry_name.delete(0, END)
        self.entry_family.delete(0, END)
        self.entry_name.focus_set()

    def next(self, event):
        self.entry_family.focus_set()

    def __init__(self, root):
        self.root = root
        self.lbl_name = Label(root, text='Name: ')
        self.entry_name = Entry(root)
        self.entry_name.bind('<Return>', self.next)
        self.lbl_family = Label(root, text='Family: ')
        self.entry_family = Entry(root)
        self.entry_family.bind('<Return>', self.save)
        self.btn_save = Button(root, text='Save', command=self.save)
        self.btn_reset = Button(root, text='Reset', command=self.reset)
    
    def grid(self):
        self.lbl_name.grid(row=1, column=1)
        self.entry_name.grid(row=1, column=2)
        self.lbl_family.grid(row=2, column=1)
        self.entry_family.grid(row=2, column=2)
        self.btn_save.grid(row=3, column=1, padx=5, pady=5)
        self.btn_reset.grid(row=3, column=2, padx=5, pady=5)


