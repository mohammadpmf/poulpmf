from tkinter import*
from tkinter import filedialog
from time import sleep
from PIL import Image,ImageTk
class Slider():
    def __init__(self,root,address1,address2,width,height):
        self.root=root
        self.width=width
        self.height=height
        self.frm=Frame(self.root,width=width,height=height+50)
        a=Image.open(address1)
        a=a.resize((width,height))
        self.img1=ImageTk.PhotoImage(a)
        b=Image.open(address2)
        b=b.resize((width,height))
        self.img2=ImageTk.PhotoImage(b)
        self.l_pic=Label(self.frm,image=self.img1)
        self.l_pic.place(x=0,y=0,width=width,height=height)
        self.btn=Button(self.frm,text="Next",command=self.next)
        self.btn.place(x=10,y=height+5)
    def next(self):
        self.btn["state"]="disable"
        for i in range(self.height,-1,-10):
            self.l_pic.place(y=self.height-i,height=i)
            sleep(0.01)
            self.l_pic.update()
        self.l_pic.place(y=0,height=self.height)
        self.l_pic.config(image=self.img2)
        for i in range(0,self.width,10):
            self.l_pic.place(width=i)
            sleep(0.01)
            self.l_pic.update()
        self.btn["state"]="normal"
            
    def grid(self):
        self.frm.grid()
root=Tk()
address1=filedialog.askopenfilename()
address2=filedialog.askopenfilename()
s1=Slider(root,address1,address2,400,400).grid()

root.mainloop()