from tkinter import *
from tkinter import filedialog
from time import sleep
from PIL import Image, ImageTk

class Slider():
    def __init__(self, root, address1, address2, width, height):
        self.image_number = 1
        self.root = root
        self.width = width
        self.height = height
        self.frame = Frame(self.root, width=width, height=height+30)
        a = Image.open(address1)
        a = a.resize((width, height))
        self.img1 = ImageTk.PhotoImage(a)
        b = Image.open(address2)
        b = b.resize((width, height))
        self.img2 = ImageTk.PhotoImage(b)
        self.lbl_picture = Label(self.frame, image=self.img1)
        self.lbl_picture.place(x=0, y=0, width=width, height=height)
        self.btn = Button(self.frame, text="Next", command=self.next)
        self.btn.place(relx=0.4, relwidth=0.2, y=height)
    def next(self):
        self.btn.config(state='disable')
        for i in range(self.height, -1, -10):
            self.lbl_picture.place(y=self.height-i, height=i)
            sleep(0.01)
            self.lbl_picture.update()
        self.lbl_picture.place(y=0, width=0, height=self.height)
        if self.image_number == 1:
            self.lbl_picture.config(image=self.img2)
            self.image_number = 2
        else:
            self.lbl_picture.config(image=self.img1)
            self.image_number = 1
            
        for i in range(0, self.width, 10):
            self.lbl_picture.place(width=i)
            sleep(0.01)
            self.lbl_picture.update()
        self.btn.config(state='normal')
        

    def grid(self):
        self.frame.grid()

root = Tk()
address1 = filedialog.askopenfilename()
address2 = filedialog.askopenfilename()
s1 = Slider(root, address1, address2, 400, 400)
s1.grid()


root.mainloop()