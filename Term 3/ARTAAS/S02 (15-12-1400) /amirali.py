from tkinter import * 
root = Tk()

def save():
    pass

root.title(':D')
root.geometry('400x450')
root.config(bg='#1228B8')
root.resizable(0,0)
lbl1=Label(root,text='name:',bg='#1228B8',font=(30))
name=Entry(root)

lbl2=Label(root,text='family:',bg='#1228B8',font=(30))
family=Entry(root)

lbl3=Label(root,text='age:',bg='#1228B8',font=(30))
age=Entry(root)

lbl4=Label(root,text='username:',bg='#1228B8',font=(30))
username=Entry(root)

lbl5=Label(root,text='password:',bg='#1228B8',font=(30))
password=Entry(root)

btn_save=Button(root,text='Save', command=save)
btn_exit=Button(root, text='Exit', command=exit)
#=============================
lbl1.pack(pady=10)
name.pack()

lbl2.pack(pady=10)
family.pack()

lbl3.pack(pady=10)
age.pack()

lbl4.pack(pady=10)
username.pack()

lbl5.pack(pady=10)
password.pack()

btn_exit.pack(pady=10)
btn_save.pack(pady=10)


root.mainloop()