from tkinter import *

def equal():
    try:
        answear=eval(entry.get())
    except:
        answear="ERORR"
    clear()    
    entry.insert(0, answear)
    
def clear():
    entry.delete(0,END)

def add_n(n):
    entry.insert(END,n)

root = Tk()
root.geometry('600x400')

btn9 = Button(root,text=9, padx=15, pady=15,command=lambda:add_n(9))    
btn8 = Button(root,text=8, padx=15, pady=15,command=lambda:add_n(8))
btn7 = Button(root,text=7, padx=15, pady=15,command=lambda:add_n(7))
btn6 = Button(root,text=6, padx=15, pady=15,command=lambda:add_n(6))
btn5 = Button(root,text=5, padx=15, pady=15,command=lambda:add_n(5))
btn4 = Button(root,text=4, padx=15, pady=15,command=lambda:add_n(4))
btn3 = Button(root,text=3, padx=15, pady=15,command=lambda:add_n(3))
btn2 = Button(root,text=2, padx=15, pady=15,command=lambda:add_n(2))
btn1 = Button(root,text=1, padx=15, pady=15,command=lambda:add_n(1))
btn0 = Button(root, text='0', padx=15, pady=15,command=lambda:add_n(0))
btn000 = Button(root,text='000', padx=15, pady=15,command=lambda:add_n("000"))
btnm = Button(root,text='-', padx=15, pady=15,command=lambda:add_n("-"))
btnz = Button(root,text='*', padx=15, pady=15,command=lambda:add_n("*"))
btn = Button(root,text= '/', padx=15, pady=15,command=lambda:add_n("/"))
btns = Button(root,text='=', padx=15, pady=15,command=lambda:equal())
btnb = Button(root,text='+', padx=15, pady=15,command=lambda:add_n("+"))
btnc = Button(root,text='c', padx=15, pady=15,command=lambda:clear())
entry = Entry(root)

# ==========================
entry.grid(row=0, column=1, columnspan=5, sticky='nsew')
btnc.grid(row=1, column=5, sticky='nsew')
btnb.grid(row=1, column=4, rowspan=2, sticky='nsew')
btns.grid(row=4, column=4, columnspan=2, sticky='nsew')
btn9.grid(row=1, column=3, sticky='nsew')
btn8.grid(row=1, column=2, sticky='nsew')
btn7.grid(row=1, column=1, sticky='nsew')
btn.grid(row=2, column=5, sticky='nsew')
btnz.grid(row=3, column=5, sticky='nsew')
btn6.grid(row=2, column=3, sticky='nsew')
btn5.grid(row=2, column=2, sticky='nsew')
btn4.grid(row=2, column=1, sticky='nsew')
btnm.grid(row=3, column=4, sticky='nsew')
btn3.grid(row=3, column=3, sticky='nsew')
btn2.grid(row=3, column=2, sticky='nsew')
btn1.grid(row=3, column=1, sticky='nsew')
btn0.grid(row=4, column=1, sticky='nsew')
btn000.grid(row=4, column=2, columnspan=2, sticky='nsew')

mainloop()



