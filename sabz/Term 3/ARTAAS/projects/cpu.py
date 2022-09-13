import random
import tkinter
from tkinter import Label, PhotoImage, messagebox
from PIL import Image, ImageTk

root = tkinter.Tk()
xs = []
ys = []
roots = []
imgs = []
ls = []
for i in range(20):
    xs.append(random.randint(0,1080))
    ys.append(random.randint(0,720))
    roots.append(tkinter.Toplevel(root))
    roots[i].geometry(f'200x200+{xs[i]}+{ys[i]}')
    if i%4==0:
        roots[i].protocol("WM_DELETE_WINDOW", lambda: 0)
    imgs.append(Image.open('1.jpeg', 'r'))
    imgs[i] = imgs[i].resize((200, 200))
    imgs[i] = ImageTk.PhotoImage(imgs[i])
    ls.append(Label(roots[i], image=imgs[i]))
    ls[i].pack()
for b in range(22):
    messagebox.showerror('EROOR', "                       ERROR                     ")

root.withdraw()
root.mainloop() 


