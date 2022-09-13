from tkinter import *
win=Tk()

win.title("poulstar")
win.geometry("240x260+600+260")
win.config(bg="#8d74a9")
win.resizable(1, 1)
# lbl1=Label(root,text="username:",bg="#8d74a9",fg="#da1704")
# e_username=Entry(root)

# lbl2=Label(root,text="password:",bg="#8d74a9")
# e_password=Entry(root)

# btn=Button(root,text="send")
# #================pack===========
# lbl1.pack(pady=10)
# e_username.pack()

# lbl2.pack(pady=10)
# e_password.pack(pady=10)

# btn.pack(pady=20)

btn1=Button(win,text="blue")
btn2=Button(win,text="red")
btn3=Button(win,text="yellow")
btn4=Button(win,text="gray")
btn5=Button(win,text="pink")
btn6=Button(win,text="orange")

#============pack==============
# btn1.pack(side='left', expand=1, fill='both', padx=60, pady=60)
# btn2.pack(side='left')
# btn3.pack(side='right')
# btn4.pack(side='bottom')
# btn5.pack(side='bottom')
# btn6.pack()

#============place==============
btn1.place(x=10,y=10, width=60, height=30)
btn2.place(x=90,y=10, width=60, height=30)
btn3.place(x=160,y=10, width=60, height=30)
btn4.place(x=10,y=60, width=60, height=30)
btn5.place(x=90,y=60, width=60, height=30)
btn6.place(x=160,y=60, width=60, height=30)

win.mainloop()