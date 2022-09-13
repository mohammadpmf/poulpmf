from translator import Translator
from tkinter import *

def translate1():
    sample_text = Translator(t1.get("1.0", "end-1c"))
    sv_lbl.set(sample_text.translate_to_morse())
    
root = Tk()
t1 = Text(root, height=10)
btn = Button(root, text = 'Click to translate to morse', command = translate1)
sv_lbl = StringVar()
sv_lbl.set('')
lbl = Label(root, textvariable=sv_lbl)

t1.pack()
btn.pack()
lbl.pack()
mainloop()