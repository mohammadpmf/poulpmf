from tkinter import *
from PIL import Image, ImageTk
from time import sleep
class Slider():
    def __init__(self, root, address=None, address2=None):
        self.root = root
        self.address=address
        self.address2=address2
        self.toggle = 'right'
        self.btn=Button(self.root, text='Change', command=self.change)
        self.frm = Frame(self.root, bg='cyan')
        self.img = Image.open(self.address)
        self.img = self.img.resize((400,400))
        self.img = ImageTk.PhotoImage(self.img)
        self.img2 = Image.open(self.address2)
        self.img2 = self.img2.resize((400,400))
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.lbl = Label(self.root, image=self.img)
        self.btn.place(relx=0.4, relwidth=0.2, relheight=0.1, rely=0.85)
        self.lbl.place(x=500, width=400, height=400, rely=0.1)
    def grid(self, args, *kwargs):
        self.frm.grid(*args, **kwargs)
    def change(self):
        self.btn['state']='disable'
        if self.toggle=='right':
            for i in range(400, 0, -10):
                self.lbl.place(width=i)
                self.lbl.update()
                sleep(0.01)
            self.lbl['image'] = self.img2
            for i in range(1, 401, 10):
                self.lbl.place(x=500-i, width=i)
                self.lbl.update()
                sleep(0.01)
            self.toggle='left'
        elif self.toggle=='left':
            for i in range(400, 0, -10):
                self.lbl.place(x=500-i, width=i)
                self.lbl.update()
                sleep(0.01)
            self.lbl['image'] = self.img
            for i in range(1, 401, 10):
                self.lbl.place(width=i)
                self.lbl.update()
                sleep(0.01)
            self.toggle='right'
        self.btn['state']='normal'
        

    
root = Tk()
root.geometry('1000x600+500+200')
aks = Slider(root, address="1.jpg", address2='2.jpg')
aks.grid()
root.mainloop()
