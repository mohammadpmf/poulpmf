from tkinter import *

root = Tk()
root.geometry('800x600')
btn0 = Button(root, text=0)
btn1 = Button(root, text=1)
btn2 = Button(root, text=2)
btn3 = Button(root, text=3)
btn4 = Button(root, text=4)
btn5 = Button(root, text=5)
btn6 = Button(root, text=6)
btn7 = Button(root, text=7)
btn8 = Button(root, text=8)
btn9 = Button(root, text=9)
btn0.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
btn1.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.25)
btn2.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.25)
btn3.place(relx=0, rely=0.25, relwidth=0.25, relheight=0.25)
btn4.place(relx=0.25, rely=0.25, relwidth=0.25, relheight=0.25)
btn5.place(relx=0.5, rely=0.25, relwidth=0.25, relheight=0.25)
btn6.place(relx=0, rely=0.5, relwidth=0.25, relheight=0.25)
btn7.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.25)
btn8.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.25)
btn9.place(relx=0.25, rely=0.75, relwidth=0.5, relheight=0.25)


root.mainloop()