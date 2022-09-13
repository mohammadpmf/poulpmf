from tkinter import *
# from PIL import Image, ImageTk

class MyForm:
    def save(self, event=''):
        name = self.entry_name.get()
        family = self.entry_family.get() 
        user = self.entry_user.get()
        password = self.entry_pass.get()
        file = open(name, 'w')
        file.write(name)
        file.write('\n')
        file.write(family)
        file.write('\n')
        file.write(user)
        file.write('\n')
        file.write(password)
        file.close()

    def reset(self):
        self.entry_name.delete(0, END)
        self.entry_family.delete(0, END)
        self.entry_user.delete(0, END)
        self.entry_pass.delete(0, END)
        self.entry_name.focus_set()

    def next(self, event):
        self.entry_family.focus_set()
    def next2(self, event):
        self.entry_user.focus_set()
    def next3(self, event):
        self.entry_pass.focus_set()

    def check(self):
        print(self.state.get())
        if self.state.get() == 1:
            self.entry_pass.config(show="")
        elif self.state.get() == 0:
            self.entry_pass.config(show="*")


    def __init__(self, root):
        self.root = root
        self.lbl_name = Label(root, text='Name: ')
        self.entry_name = Entry(root)
        self.entry_name.bind('<Return>', self.next)
        self.lbl_family = Label(root, text='Family: ')
        self.entry_family = Entry(root)
        self.entry_family.bind('<Return>', self.next2)
        self.lbl_user = Label(root, text='Username: ')
        self.entry_user = Entry(root)
        self.entry_user.bind('<Return>', self.next3)
        self.lbl_pass = Label(root, text='Password: ')
        self.entry_pass = Entry(root, show='*')
        self.entry_pass.bind('<Return>', self.save)
        # self.pictrue = Image.open("1.png", 'r')
        # self.pictrue = self.pictrue.resize((200, 100))
        # self.pictrue = ImageTk.PhotoImage(self.pictrue)
        # self.lbl_pic = Label(root, image=self.pictrue)
        self.state = IntVar()
        self.cb = Checkbutton(root, text='show password',
        variable=self.state, command=self.check)
        self.btn_save = Button(root, text='Save', command=self.save)
        self.btn_reset = Button(root, text='Reset', command=self.reset)
    
    def grid(self):
        self.lbl_name.grid(row=1, column=1, padx=5, pady=5)
        self.entry_name.grid(row=1, column=2, padx=5, pady=5)
        self.lbl_family.grid(row=2, column=1, padx=5, pady=5)
        self.entry_family.grid(row=2, column=2, padx=5, pady=5)
        self.lbl_user.grid(row=3, column=1, padx=5, pady=5)
        self.entry_user.grid(row=3, column=2, padx=5, pady=5)
        self.lbl_pass.grid(row=4, column=1, padx=5, pady=5)
        self.entry_pass.grid(row=4, column=2, padx=5, pady=5)
        # self.lbl_pic.grid(row=5, column=1, padx=5, pady=5)
        self.cb.grid(row=5, column=2, padx=5, pady=5)
        self.btn_save.grid(row=6, column=1, padx=5, pady=5)
        self.btn_reset.grid(row=6, column=2, padx=5, pady=5)


